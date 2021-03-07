from main.models import Item, RootCategory, Category
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import F
def sales_view(request):
    products_list = Item.objects.filter(pricecheanges__old_price__gt=F('pricecheanges__price')).distinct().order_by("?")
    category = {"name": 'Скидки недели'}
    paginator = Paginator(products_list, 200)

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'main-page.html',
                  {'products': products, "categories": RootCategory.objects.all(), 'category': category})


def main_view(request):
    products_list = Item.objects.filter(popular=True)
    category = {"name": 'Полярные товары'}
    paginator = Paginator(products_list, 25)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'main-page.html', {'products': products, "categories": RootCategory.objects.all(), 'category': category})


def page_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products_list = category.get_products.order_by('id')
    paginator = Paginator(products_list, 25)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'main-page.html', {'products': products, "categories": RootCategory.objects.all(), 'category': category})


def item_view(request, name, slug):
    products = Item.objects.get(slug=slug)
    return render(request, 'item-page.html', {'products': products, "categories": RootCategory.objects.all()})
