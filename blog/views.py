from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .form import CommentForm
from .form import SubscriberForm



def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def about(request):
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:about')  # reload page after subscribing
    else:
        form = SubscriberForm()
    return render(request, 'blog/about.html', {'form': form})


def contact(request):
    return render(request, 'blog/contact.html')



def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    recent_posts = Post.objects.exclude(pk=pk).order_by('-id')[:5]

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'blog/detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
        'recent_posts': recent_posts
    })

