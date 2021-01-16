import os

from celery import Celery
from celery.schedules import crontab
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PriceStatistics.settings')

app = Celery('PriceStatistics')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# Other Celery settings
app.conf.beat_schedule = {
    'task-number-one': {
        'task': 'main.tasks.task_number_one',
        'schedule': crontab(),
    },
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')




#celery -A shopProject worker -l info -P eventlet