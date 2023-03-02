    # Choose query via variable

    # 31/07/2019

# try function syntaxe

def gSearch(chosenEntity, NbPages):

    from lib.google_search_results import GoogleSearchResults
    #from google_search_results import GoogleSearchResults
    #from google-search-results import GoogleSearchResults


    #from serpapi import GoogleSearch

    # get query from airtables and send to serp_api_key

    #from selenium import webdriver
    #from selenium.webdriver.common.by import By
    #from selenium.webdriver.support.ui import WebDriverWait
    #from selenium.webdriver.support import expected_conditions as EC
    #from selenium.common.exceptions import TimeoutException, NoSuchElementException
    #from selenium.webdriver.common.keys import Keys
    #from parsel import Selector
    #from time import sleep
    import requests, json
    import time
    import psutil
    import re
    import datetime


    # build query for google

    search_query_content = chosenEntity

    nbPages = NbPages



    # ---------------------------- Send query to SERPAPI

    params = {
        "engine": "google",
        "q": search_query_content,
        "location": "Ile-de-France, France",
        "google_domain": "google.fr",
        "gl": "fr",
        "hl": "fr",
        "start": "0", # changed to from 1 to 0 21/03
        "num": nbPages,
        "serp_api_key": "f417f9663423a0dd56863c429ae6032e50897ca366ef58a54becd55ab19428b3"

    }

    client = GoogleSearchResults(params)
    response_data = client.get_json()

    #print("Gsearch() : ")
    #print(response_data)

    return  response_data