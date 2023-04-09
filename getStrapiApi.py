import settings
import sys
import requests, json

#def getStrapiApi(airUrl, strapiSearchName):
def getStrapiApi(airUrl):    

    settings.init()
    #print(settings.currStrapiUrl)
    rootUrl = settings.currStrapiUrl
    tokenid = settings.tokenid

    #tokenid = "N{t[4AJHBa6]T@#$22"

    #newSentence = name + " " + "Welcome"
    ## # print("(addStrapiApi) check payload : ")
    ## print(payload)
    ## print("(addStrapiApi) check URL: ")
    ## print(airUrl)

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

    # possible solution

    #resp= requests.get("https://stackoverflow.com/")
    #resp_dict = json.loads(resp.text)
    ## print(resp_dict)
    
    finalUrl = rootUrl
    # finalUrl = airUrl + strapiSearchName

    finalUrl = finalUrl + airUrl

    #print("getStrapiApi) this should be the final url: ", finalUrl)
    # make request
    # response = requests.request("POST", airUrl, data=json.dumps(payload), headers=headers)
    #response = requests.request("GET", airUrl, data=json.dumps(payload), headers=headers)
    # response = requests.request("GET", airUrl, headers=headers)
    response = requests.request("GET", finalUrl, headers=headers)

    response_data = response.json()
    ## print("(addStrapiApi) # printing response")
    ## print(response_data)
    return response_data