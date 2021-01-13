from lentaparse.celery import app
import time
from .parse import product_get
from celery.utils.log import get_task_logger
from django.core.mail import send_mail
logger = get_task_logger(__name__)
@app.task()
def task_number_one():
    f = [196]
    email = send_mail("Новый заказ",
                      "Заказ",
                      "prynikvany@gmail.com", ['Dr.JohnYu@yandex.ru'])
    print('ifjks')
    # Do another thing...