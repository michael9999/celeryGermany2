import os
from celery import Celery
from celery.utils.log import get_task_logger
from searchStrapiApi import strapiApi
from getControlPanel import * 
from getAllAttributes import *
from process_listsStrapi import *
from processSearchStrapiLatest import *

# Original
# app = Celery('tasks', broker=os.getenv("CELERY_BROKER_URL", "127.0.0.1"))

# trial 

app = Celery('tasks', broker=os.getenv("CELERY_BROKER_URL", "redis://localhost:6379")) # works 

# end trial


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

    testUrl = "control-panels"
    query = "?_where[id]="
    searchVal = id

    # get search clicked on 
    goQuery = strapiApi(testUrl, query, searchVal)

    print('Log info: Live search', goQuery)
    

    #print(goQuery)

    # 2) get search details (ex. list of firms)

    search_var_list_names, firm_list_names, nbPages, varPts, firmPts, languagePts, MinPoints, searchName, idNb, jobtitle_list_names, jobID, jobPts, locPts = getControlPanelDataStrapi(searchVal)

    # 3) build patterns

    searchTerm = getSearchVariablesStrapi(search_var_list_names[0])
    firmList = getFirmsStrapi(firm_list_names)
    searchTarget = getSearchTargetsStrapi()
    location = getLocationStrapi()
    language = getLanguagesStrapi()
    exclusions = getExclusionTermsStrapi() # not used at the moment

    # get exclusion terms for auto checking of variables, exclude stage, work experience etc...
    stageExclude = "excludestage"
    stageTerms = getSearchVariablesStrapi(stageExclude)

    # this only used once proxycurl has scraped the profile
    jobtitles = getJobTitlesStrapi(jobtitle_list_names)
    print("tasks.py) **************** Do we have jobtitles : ", jobtitles)

    # get live search patterns

    testUrl = "search-configs"
    query = "?_where[status]="
    searchVal = "Live"
    pattern1 = strapiApi(testUrl, query, searchVal)

    # put patterns in list

    patternList = []

    for x in pattern1:
    #someList.append(pattern1[x]["pattern"])

        patternList.append(x["pattern"])  
        logger.info(f'Log info: Live search {patternList}')

    # 3. Builds search queries for serpapi

    test = process_listsStrapi(patternList, firmList, searchTarget, searchTerm, location, language)


    # 4. Do Google search

    flattened = []
    for sublist in test:
        for val in sublist:
            flattened.append(val)
            
    #print(flattened)

    newTest = processSearchGo(flattened, nbPages, varPts, firmPts, languagePts, MinPoints, searchName, searchTerm, firm_list_names, language, idNb, jobtitles, stageTerms, jobID, jobPts, locPts)

    logger.info(f'Log info: processSearchGo {newTest}')

    return "running1: " + " - "


