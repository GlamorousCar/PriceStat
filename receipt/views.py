from django.shortcuts import render
from main.models import Item
from django.db.models import Q
# Create your views here.

def receipt(request):
    a = Item.objects.filter(name__search='Молоко')
    return render(request, 'untitled.html', {'items': a} )