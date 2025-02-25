
from django.shortcuts import render
from django.views.generic import TemplateView
from goods.models import Categories


# def index(request):
#     return render(request,'main/index.html')

class IndexView(TemplateView):
# Create your views here.
    template_name = 'main/index.html'

    
    