from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{'title': "About us", 'url_name': 'about'},
        {'title': "Contacts", 'url_name': 'contact'},
        {'title': "Add page", 'url_name': 'add_page'},
        {'title': "LogIn", 'url_name': 'login'}
]

def index(request):
    posts = Cars.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Main page',
        'cat_selected': 0,
    }
    return render(request, 'cars/index.html', context=context )

def about(request):
    return render(request, 'cars/about.html', {'title': 'About page'})

def contact(request):
    return render(request, 'cars/contact.html', {'title': 'Contacts'} )

def addpage(request):
    return HttpResponse('Add page')

def login(request):
    return render(request, 'cars/login.html', {'title': 'LogIn'} )

def show_post(request, post_id):
    return HttpResponse(f"Article Display с id = {post_id}")

def show_category(request, cat_id):
    posts = Cars.objects.filter(cat_id=cat_id)
    if len(posts) == 0:
        raise Http404()

def pageNotFound(request, exeption):
    return HttpResponseNotFound('Page Not Found')
