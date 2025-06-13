from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from . models import Product, Category
from django.contrib.auth import get_user_model

User = get_user_model()

def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'Base.html')

def categories(request: HttpRequest) -> HttpResponse:
    try:
        categories = Category.objects.all()
    except Exception as e:
        categories = []
        print(f"Error: {e}")

    return render(request, 'categories.html', {'categories': categories})

def contact(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact.html')