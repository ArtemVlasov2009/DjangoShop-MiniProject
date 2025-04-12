from django.shortcuts import render
# from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Product

# class MainPageView(View):
#     def get(self, request):
#         return render(request, "shop_app/main.html")

class MainPageView(TemplateView):
    '''
        Клас-відображення, що відповідає за відображення головної сторінки

        MainPageView успадковується від TemplateView - класу, що використовується при відображенні статичних сторінок
    '''

    # Шлял до HTML-шаблону, який треба відобразити
    template_name = 'shop_app/main.html'
    

class ProductListView(ListView):
    '''
        Клас-відображення, що відповідає за відображення сторінки зі списком продуктів

        ProductListView успадковується від ListView - класу, що використовується коли відобразити сторінку зі списком об'єктів моделі
    '''

    # Моедель, з якої будемо брати список усіх об'єктів
    model = Product
    # Вказуємо ім'я для списку з об'єктами моделі
    context_object_name = 'product_list'