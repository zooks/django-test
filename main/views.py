from django.shortcuts import render
from main.models import *
from django.http import Http404 # HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
# from django.core.context_processors import csrf
# from django.views.decorators.csrf import csrf_exempt
from datetime import *
import random
import string


# Create your views here.

def home(request):
    # goods = []
    # for item in range(0,3):
    #     goods.append(item)
    # goods = Item.objects.all() # все объекты класса Item

    categories = Category.objects.all()  # передаем alias, выводим все категории

    context = {
        'title': 'Hello World!',
        'site_name': 'Лучший шмот',
        'categories': categories,

    }
    return render(request, 'main-page.html', context)

def item(request, alias):
    try:
        article = Item.objects.get(alias=alias)  # передаем alias
    except:
        raise Http404('Объект не найден')

    context = {
        'article': article,

    }
    return render(request, 'article.html', context)

def get_category(request, alias):
    try:
        category = Category.objects.get(alias=alias)  # передаем alias
        goods = Item.objects.filter(category=category) # вывод товаров данной категории
    except:
        raise Http404('Объект не найден')

    context = {
        'goods': goods,
        'category': category,

    }
    return render(request, 'category.html', context)