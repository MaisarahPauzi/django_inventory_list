from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from inventory.models import Laptop, Desktop, Mobile


def index(request):

    return render(request, 'index.html')

def display_Laptop(request):
    items = Laptop.objects.all()
    context = {
        'items': items,
        'header': 'Laptops',
    }
    return render(request, 'index.html', context)


def display_Desktop(request):
    items = Desktop.objects.all()
    context = {
        'items': items,
        'header': 'Desktops',
    }
    return render(request, 'index.html', context)


def display_Mobile(request):
    items = Mobile.objects.all()
    context = {
        'items': items,
        'header': 'Mobiles',
    }
    return render(request, 'index.html', context)
