    # Choose query via variable
import sys
import requests, json
global tokenid
tokenid = "N{t[4AJHBa6]T@#$22"

    # 31/07/2019

# try function syntaxe
# function requires a search name, url, query, search tab & search value

# addProxy

def addStrapiApi(strapiUrl, payload):


    print("addStrapiApi is running")

    #payload = ""
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


    # make request
    response = requests.request("POST", strapiUrl, data=json.dumps(payload), headers=headers)
    response_data = response.json()
    return response_data

def addProxy(strapiUrl, payload):

    #print("addProxy is running")
    #print("addProxy) url: ",  strapiUrl)

    #payload = ""
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
        'X-Api-Key': "asoidewfoef"
        }


    # make request
    response = requests.request("POST", strapiUrl, data=json.dumps(payload), headers=headers)

    #print("addProxy) returned data BEFORE json: ",  response)

    response_data = response.json()

    #print("addProxy) returned data: ",  response_data)

    return response_data
