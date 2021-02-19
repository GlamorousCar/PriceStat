from PriceStatistics.celery import app
import time
from .parse import product_get
from .parse import categories_get
from celery.utils.log import get_task_logger
from django.core.mail import send_mail
logger = get_task_logger(__name__)
@app.task()
def task_number_one():
    for i in categories_get():
        product_get(i)