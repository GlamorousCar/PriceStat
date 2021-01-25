import requests
import json
import time
import math
from main.models import Item,PriceCheanges,Category,RootCategory
import datetime

categories = 'https://shop.lenta.com/api/v8/shops/11/categories'
g = json.loads(requests.get(categories).text)

site = 'https://shop.lenta.com'

def categories_get():
    categories_list = []
    for i in g['data']['list']:
        l = i['child_categories']
        if not RootCategory.objects.filter(name=i['name']).exists():
            try:
                r = RootCategory(name=i['name'], slug=i['id'])
                r.save()
            except:
                print('eror')
        else:
            r = RootCategory.objects.get(name = i['name'])
        for j in l:
            if not Category.objects.filter(name=j['name']).exists():
                v = Category(name=j['name'],slug=j['id'],root_category=r)
                v.save()
            categories_id = j['id']
            categories_list.append(categories_id)
    return categories_list

startd_time = time.time()

main = []
COUNT = 0
def product_get(id):
    url = f'{site}/api/v8/shops/11/categories/{id}/products?sort=popularity&sort_order=desc'
    d = json.loads(requests.get(url).text)['data']['total']
    chech = math.ceil(d / 30)
    list_k = []
    global COUNT
    for step in range(chech):
        url = f'{site}/api/v8/shops/11/categories/{id}/products?sort=popularity&sort_order=desc&offset={step * 30}'
        n = json.loads(requests.get(url).text)
        for k in n['data']['list']:
            name = k['name']
            weight = k['item_weight']
            description = k['info']
            bigImage = k['image']['biggest']
            largeImage = k['image']['large']
            mediumImage = k['image']['medium']
            smallImage = k['image']['small']
            category = Category.objects.get(name=k['category'])
            composition = k['composition']
            slug = k['id'] + '-' + k['parameterize']
            display_weight = k['display_weight']
            if k['sale'] == False:
                old_price = k['price']
            else:
                old_price = k['old_price']
            price = k['price']
            r = Item(name=name,weight=weight,description=description,biggest=bigImage,large=largeImage,medium=mediumImage,small=smallImage,category= category, composition= composition,slug=slug,display_weight=display_weight)
            if Item.objects.filter(name = name).exists():
                try:
                    t = PriceCheanges(price=price, old_price = old_price, item=Item.objects.get(name =k['name']) , date= datetime.date.today())
                    t.save()
                except Exception as e:
                    print(e)

            else:
                try:
                    r.save()
                    t = PriceCheanges(price=price, old_price = old_price, item=r, date= datetime.date.today())
                    t.save()
                except Exception as e:
                    print(e)

            list_k.append(k['model_id'])
    return list_k

