from main.views import *
from django.urls import path

urlpatterns = [
    path('ls/',parsf),
    path('',main_view),
    path('category/<slug:slug>', page_view, name='category_detail'),
    path('category/<str:name>/<slug:slug>',item_view, name='item-detail'),
]