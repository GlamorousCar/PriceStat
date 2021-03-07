import requests
import json
import math
import datetime
from main.models import Item, PriceCheanges, Category, RootCategory
from PriceStatistics.settings import logger

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
            except Exception as e:
                logger.debug(e)
        else:
            r = RootCategory.objects.get(name=i['name'])
        for j in l:
            if not Category.objects.filter(name=j['name']).exists():
                v = Category(name=j['name'], slug=j['id'], root_category=r)
                v.save()
            categories_id = j['id']
            categories_list.append(categories_id)
    return categories_list


main = []
COUNT = 0


def product_get(id):
    url = f'{site}/api/v8/shops/11/categories/{id}/products?sort=popularity&sort_order=desc'
    d = json.loads(requests.get(url).text)['data']['total']
    chech = math.ceil(d / 30)
    list_k = []
    today = datetime.datetime.today()
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
            slug = str(k['id']) + '-' + k['parameterize']
            display_weight = k['display_weight']
            if len(bigImage) < 2:
                bigImage, largeImage, mediumImage, smallImage = ['/static/assets/img/no-image.png'] * 4

            if not k['sale']:
                old_price = k['price']
            else:
                old_price = k['old_price']
            price = k['price']
            if old_price is None:
                old_price = price
            r = Item(name=name, weight=weight, description=description, biggest=bigImage, large=largeImage,
                     medium=mediumImage, small=smallImage, category=category, composition=composition, slug=slug,
                     display_weight=display_weight)
            if Item.objects.filter(name=name).exists():
                try:
                    if len(PriceCheanges.objects.filter(item=Item.objects.get(name=k['name'])).filter(date=today)) < 1:
                        t = PriceCheanges(price=price, old_price=old_price, item=Item.objects.get(name=k['name']),
                                          date=today)
                        t.save()
                except Exception as e:
                    logger.debug(str(e))
                    logger.debug(k)

            else:
                try:
                    r.save()
                    if len(PriceCheanges.objects.filter(item=Item.objects.get(name=k['name'])).filter(date=today)) < 1:
                        t = PriceCheanges(price=price, old_price=old_price, item=r, date=today)
                        t.save()
                except Exception as e:
                    logger.debug(str(e))
                    logger.debug(k)

            list_k.append(k['model_id'])
    return list_k
