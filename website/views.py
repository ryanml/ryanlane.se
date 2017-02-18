from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse as response

def home(request):
    page_title = "ryanlane.se"
    template = loader.get_template('website/home.html')
    context = { 'page_title': page_title }
    return response(template.render(context, request))

