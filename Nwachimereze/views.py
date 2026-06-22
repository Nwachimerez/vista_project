from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {"posts": posts})