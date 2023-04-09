def getProfileProxyCurl(liUrl):

    import requests

    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'

    # api_key = 'e20779ac-51b4-4173-b119-31acd61b51c8'

    # check that URL finishes with a "/"

    nb = liUrl.count('/')
    #print(nb)

    if nb ==4 or nb <4:
        #print("less than 4")
        b = "/".join(liUrl.split("/")[:5])
        b = b + "/"
        #print(b)
    
    else:
        #print("five or more /")
        b = "/".join(liUrl.split("/")[:5])
        b = b + "/"
        #print(b)
    #b = b + "/"
    #print(b)    

    # check URL sent to proxycurl

    #print("getProfileProxyCurl) URL to fetch ------------------ ", liUrl)
    #print(b)

    # https://www.linkedin.com/in/karinedisdiermikus/
    # https://fr.linkedin.com/in/karinedisdiermikus/en = no
    # https://fr.linkedin.com/in/karinedisdiermikus/ = ok

    # test
    #liUrl = "https://fr.linkedin.com/in/karinedisdiermikus/en/"

    api_key = 'eddb274d-e91f-45f6-9c52-2fe17de2b98a'

    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {

        #'url': 'https://www.linkedin.com/in/in%C3%A8s-touati-40b250150/',
        'url': b,

    }
    #response = requests.get(api_endpoint,
    #                        params=params,
    #                        headers=header_dic)

    response = requests.request("GET", api_endpoint, params=params, headers=header_dic)
    # WORKS, put result data into json

    import json

    # print result
    #print("getProfileProxyCurl), print response ------------------ : ", response.content)
    #print("getProfileProxyCurl), print response CODE ------------------ : ", response.content.code)

    # try to access full response object
            # response.status_code

    # will do json conversion in main scrip
    # y = response.json()

    return response