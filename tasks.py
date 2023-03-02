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
def runFullSearch(id):
    print("run_FullSearch task is running")

    # 1) receive id of search triggered in frontend

        # could just ID of search sent

    testUrl = "control-panels"
    query = "?_where[id]="
    searchVal = id

    # strapiApi(airUrl, queryString, search_val)
    goQuery = strapiApi(testUrl, query, searchVal)

    logger.info(f'Live search {goQuery}')

    print(goQuery)

    # 2) get all patterns




    return "running: " + goQuery


