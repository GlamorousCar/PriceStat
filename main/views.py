from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from main.models import Item,RootCategory,Category
# Create your views here.
from main.parse import product_get,categories_get
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
# Create your views here.
def parsf(request):
    #categories_get()
    f = [19]
    for i in f:
        product_get(i)
    return render(request, 'index.html')

def main_view(request):
    category={ "name" : 'Полярные товары'}
    products_list = Item.objects.filter(category_id=19)
    paginator = Paginator(products_list, 25)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        products = paginator.page(paginator.num_pages)
    return render(request, 'main-page.html', {'products': products, "categories": RootCategory.objects.all(),'category':category})
def page_view(request,slug):
    category = get_object_or_404(Category, slug=slug)
    products_list = category.get_products.order_by('id')
    paginator = Paginator(products_list, 25)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        products = paginator.page(paginator.num_pages)
    return render(request, 'main-page.html', {'products': products,"categories": RootCategory.objects.all(),'category':category})

def item_view(request, name, slug):
    products = Item.objects.get(slug=slug)

#TODO context processor
    return render(request, 'item-page.html', {'products': products,"categories": RootCategory.objects.all()})

