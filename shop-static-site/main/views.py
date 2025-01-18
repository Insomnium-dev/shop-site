from unicodedata import category
from django.shortcuts import render
from goods.models import Categories


def index(request):
    return render(request,'main/index.html')


def about(request):
    return render(request,'main/index.html')

# Create your views here.
