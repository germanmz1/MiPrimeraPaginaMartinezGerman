from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, PostForm
from .models import Post


def inicio(request):
    posts = Post.objects.all()
    return render(request, 'base.html', {'posts': posts})


def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PostForm()

    return render(request, 'crear_post.html', {'form': form})


def buscar_post(request):
    resultado = None

    if request.GET.get('titulo'):
        resultado = Post.objects.filter(
            titulo__icontains=request.GET.get('titulo')
        )

    return render(request, 'buscar.html', {'resultado': resultado})