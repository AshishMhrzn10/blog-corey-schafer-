from django.shortcuts import render
from .models import Post
# Create your views here.
def home(request):
    post = Post.objects.all()
    context = {
        'posts':post
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')