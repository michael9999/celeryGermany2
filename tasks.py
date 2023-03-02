import os
from celery import Celery
from celery.utils.log import get_task_logger
from searchStrapiApi import strapiApi

app = Celery('tasks', broker=os.getenv("CELERY_BROKER_URL", "127.0.0.1"))
logger = get_task_logger(__name__)


@app.task
def add(x, y):
    logger.info(f'Adding {x} + {y}')
    return x + y

# run_FullSearch.delay(searchpapi)

@app.task
def runFullSearch(name):
    print("run_FullSearch task is running")

    # 1) Get "Live" search

    testUrl = "control-panels"
    query = "?_where[action]="
    searchVal = "Live"

    goQuery = strapiApi(testUrl, query, searchVal)

    logger.info(f'Live search {goQuery}')

    print(goQuery)

    return "running: " + goQuery


