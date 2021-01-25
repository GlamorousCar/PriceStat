from django.contrib import admin

# Register your models here.
# Register your models here.
from django.contrib import admin

# Register your models here.
from main.models import Item, PriceCheanges,RootCategory,Category
class RootCategoryAdmin(admin.ModelAdmin):
    fields = ['name','slug']
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name','slug','root_category']

admin.site.register(Category, CategoryAdmin)
admin.site.register(RootCategory, RootCategoryAdmin)
class PriceCheangesInline(admin.TabularInline):
    model = PriceCheanges
    fields = ['date','price','old_price']


    raw_id_fields = ['item']

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name','weight', 'description')
    search_fields = ['name']
    inlines = [PriceCheangesInline]


admin.site.register(Item, ItemAdmin)


