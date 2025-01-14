from unicodedata import category
from django.shortcuts import render
from goods.models import Categories


def index(request):
    categories = Categories.objects.all()
    context = {
        'categories':categories
    }
    return render(request,'main/index.html', context)


def about(request):
    return render(request,'main/index.html')

# Create your views here.
