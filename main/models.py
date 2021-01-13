from django.db import models

# Create your models here.
from django.urls import reverse
# Create your models here.
from django.db import models


class RootCategory(models.Model):
    DEFAULT_PK = 1
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'


class Category(models.Model):
    DEFAULT_PK = 1
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)
    root_category = models.ForeignKey(RootCategory,on_delete=models.CASCADE,verbose_name='Родительская категория',default=RootCategory.DEFAULT_PK)

    def __str__(self):
        return self.name

    @property
    def get_products(self):
        return Item.objects.filter(category__name=self.name)

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Подкатегории'
        verbose_name = 'Подкатегория'


# Create your models here.
class Item(models.Model):
    name = models.TextField(max_length=512,db_index=True)
    biggest = models.TextField(default='no-image.png')
    large = models.TextField(default='no-image.png')
    medium = models.TextField(default='no-image.png')
    small = models.TextField(default='no-image.png')
    weight = models.IntegerField()
    slug = models.SlugField(default='slug',unique=True,max_length=256)
    description = models.TextField()
    composition = models.TextField(default='Состав')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=Category.DEFAULT_PK)

    def price(self):
        return PriceCheanges.objects.select_related('item').filter(item=self)


    def get_absolute_url(self):
        return f'/category/{self.category}'+'/'+f'{self.slug}'



class PriceCheanges(models.Model):


    date = models.DateTimeField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    old_price = models.DecimalField(default=100.00,max_digits=9, decimal_places=2, verbose_name='Цена')
    price = models.DecimalField(default=100.00,max_digits=9, decimal_places=2, verbose_name='Цена по скидке')

    def __str__(self):
        return str(self.price)