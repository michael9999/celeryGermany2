from getCandidatesStrapiApi import *
from extractKeyData import *
from updateStrapi import *

def createCandOptSearch(candidateid):

    #getCandidatesStrapiApi(airUrl):

    candidateid = str(candidateid)
    targeturl = "https://strapi-1oni.onrender.com/candidates/" + candidateid

# get details of candidate to optimise (search)

    getDataToOptim = getCandidatesStrapiApi(targeturl)

    print("createCandOptSearch) Test cand data returned: ", getDataToOptim)

    print("createCandOptSearch) check we have ID: ", getDataToOptim["id"])
    # for i in getDataToOptim:

    # optimisedData = extractKeyData(i)

    optimisedData = extractKeyData(getDataToOptim)

        # update candidate here
        # test I have candid
    print("$$$$$$$$$$$$$$$ curr cand ID is: ", getDataToOptim["id"])

    # strapId = str(i["id"])

    strapId = str(getDataToOptim["id"])

    strapiUrl = "https://strapi-1oni.onrender.com/candidates/"

# add generic internalsearchjson

    genericintsearch = {"internalsearchjson": ["0"]}


# build a json for generic job in joblist field

    genericJob = {"jobs": [0]}


# update candidate field "optimisedsearch" = optimisedData, "optimisestatus" = "DONE"

    #payload = {"optimisedsearch":optimisedData, "optimisestatus": "DONE", "joblist":genericJob}

    payload = {"optimisedsearch":optimisedData, "optimisestatus": "DONE", "joblist":genericJob, "internalsearchjson":genericintsearch }

    update = updateStrapiApi_PC(strapiUrl, candidateid, payload)

    # updateStrapiApi_PC(airUrl, candId, payload)


    print("createCandOptSearch) data returned from update: ", update)

    return optimisedData