import os
from celery import Celery
from celery.utils.log import get_task_logger
from searchStrapiApi import strapiApi
from getControlPanel import * 

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

    # get search clicked on 
    goQuery = strapiApi(testUrl, query, searchVal)

    logger.info(f'Live search {goQuery}')
    logger.info(f'Is this working?')

    print(goQuery)

    # 2) get all patterns

    search_var_list_names, firm_list_names, nbPages, varPts, firmPts, languagePts, MinPoints, searchName, idNb = getControlPanelDataStrapi(searchVal)

    logger.info(f'Live search {search_var_list_names}')

    # getConfigStrapi = get live pattern


    return "running: " + goQuery + " - " + search_var_list_names


