from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def main(request):
    return render(request, 'posts/main.html')

def new(request):
    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'posts/new.html', context)

def create(request):
    if (request.method == 'POST'):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('main')
