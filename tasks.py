import os
from celery import Celery
from celery.utils.log import get_task_logger

app = Celery('tasks', broker=os.getenv("CELERY_BROKER_URL", "127.0.0.1"))
logger = get_task_logger(__name__)


@app.task
def add(x, y):
    logger.info(f'Adding {x} + {y}')
    return x + y


@app.task
def run_FullSearch(name):
    print("run_FullSearch task is running")
    return "running: " + name 
