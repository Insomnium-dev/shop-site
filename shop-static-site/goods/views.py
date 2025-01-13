from django.shortcuts import render

# Create your views here.

def catalog(request):
    context = {
        'title': "Home - Каталог",
        'goods': [
        {'image': 'assets/img/goods/zinc.jpg',
         'name': 'Цинк',
         'price': 50.00},

        {'image': 'assets/img/goods/med.jpg',
         'name': 'Медь',
         'price': 150.00},

        {'image': 'assets/img/goods/alum.jpg',
         'name': 'Алюминий',
         'price': 70.00},

        {'image': 'assets/img/goods/nihrom.jpg',
         'name': 'Нихром',
         'price': 300.00},

        {'image': 'assets/img/goods/bronza.jpg',
         'name': 'Бронза',
         'price': 130.00},

        {'image': 'assets/img/goods/latun.jpg',
         'name': 'Латунь',
         'price': 150.00},
         
        {'image': 'assets/img/goods/fehral.jpg',
         'name': 'Фехраль',
         'price': 475.00},

        {'image': 'assets/img/goods/babbit.jpeg',
         'name': 'Баббит',
         'price': 275.00},
        ]
    }
    return render(request, 'goods/catalog.html', context)

def product(request):
    return render(request, 'goods/product.html')