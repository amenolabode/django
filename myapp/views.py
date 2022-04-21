from turtle import title
from django.http import HttpResponse
from django.shortcuts import render
from myapp.forms import PostForm
from myapp.models import Post

# Create your views here.
def show_posts(request ):
    posts = Post.objects.all()
    return render(request, "posts_list.html", {"posts_list": posts})

def create_new_post(request):
    if request.metod == 'POST':
        form = PostForm(request.POST)
        if form.is_valid:
            title = form.cleaned_data['title']
            request.POST.get('title')
        
    post = Post.objects.create(
        title = "My post title",
        body = "My new post body",
        # photo_url = "www.one.com"
    )
    post.save()
    return HttpResponse("<h2> Post created </h2>")

def login(request):
    return render(request, "login.html")