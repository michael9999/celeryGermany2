# Choose query via variable
import sys
import requests, json
import settings

#global tokenid
#tokenid = "N{t[4AJHBa6]T@#$22"


    # 31/07/2019

# try function syntaxe
# function requires a search name, url, query, search tab & search value

def strapiApi(airUrl, queryString, search_val):


    settings.init()
    #print(settings.currStrapiUrl)
    rootUrl = settings.currStrapiUrl
    tokenid = settings.tokenid

    # strapiApi(testUrl, query, searchVal)
    #newSentence = name + " " + "Welcome"

    #return newSentencekeydbaVNmwfCSbGwj
    #finalCount = 3
    #keydbaVNmwfCSbGwj

    # This works - https://strapi-public-test.herokuapp.com/control-panels?_where[action]=Live

    payload = ""
    headers = {
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.11.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "9f1d3e25-d22f-451b-a14b-7869dd209ed0,e16f5a95-6b2f-4469-99db-b93f697f8081",
        'cookie': "brw=brwis9EIw0YrCsUjG",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache",
        'token': tokenid
        }

    # convert id to string

    search_val = str(search_val)

    #print("this is what we are searching for: " + search_val)
    
    # build query string


    # rootUrl = "https://strapi-1oni.onrender.com/"

    finalairUrl = rootUrl + airUrl + queryString + search_val

    #print("Final STRAPI URL: ", finalairUrl)


    # make request
    #response = requests.request("GET", airUrl, data=payload, headers=headers, params=queryString)
    response = requests.request("GET", finalairUrl, headers=headers)
    response_data = response.json()
    #print("PRINTING RESPONSE DATA: ", response_data)

    return response_data