from website.models import Post
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse as response

def home(request):
    page_title = "ryanlane.se"
    template = loader.get_template('website/home.html')
    context = { 'page_title': page_title }
    return response(template.render(context, request))

def blog(request):
    page_title = "Recent Posts"
    posts = Post.objects.all()
    template = loader.get_template('website/blog.html')
    context = {
        'page_title': page_title,
        'posts': posts
    }
    return response(template.render(context, request))

