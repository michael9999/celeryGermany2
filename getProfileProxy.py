def getProfileProxyCurl(liUrl):

    import requests

    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'

    # api_key = 'e20779ac-51b4-4173-b119-31acd61b51c8'

    api_key = 'eddb274d-e91f-45f6-9c52-2fe17de2b98a'

    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {

        #'url': 'https://www.linkedin.com/in/in%C3%A8s-touati-40b250150/',
        'url': liUrl,

    }
    #response = requests.get(api_endpoint,
    #                        params=params,
    #                        headers=header_dic)

    response = requests.request("GET", api_endpoint, params=params, headers=header_dic)
    # WORKS, put result data into json

    import json

    # print result
    print("getProfileProxyCurl), print response : ", response)

    # will do json conversion in main scrip
    # y = response.json()

    return response