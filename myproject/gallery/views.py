from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Post
from .forms import UploadForm

class PostListView(ListView):
    model = Post
    template_name = 'gallery/index.html'
    context_object_name = 'posts'

def image_upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery:success')
    else:
        form = UploadForm()
    return render(request, 'gallery/upload.html', {'form' : form})


def success(request):
    return render(request, 'gallery/success.html', {})