# Build Cand object, add to Strapi, return ID
from datetime import *
from time import *
from addStrapi import *
from GetYrsExp import *
from prepareDate import *

def buildCandidate(pqResult, liUrl, stageTerms):

    print("buildCandidate) Running")
    
    new_candidate = {}
    currJtitle = ""
    currFirm = ""

    for i in pqResult:
        #if "full_name" in i:
            #print(testDate[i])

    # get all candidate data

        if i == "full_name":
            # print("print full name $$$$$$$$$$$$$$$$$$$$$$$$$ ",pqResult[i])
            new_candidate["name"] = pqResult[i]
            # print("1) candidate data is ", new_candidate["name"] )
        else:
            # continue
            print("no full_name")
            # new_candidate["name"] = new_candidate["name"] + " null"

        if i == "first_name":
            # print(pqResult[i])
            new_candidate["firstname"] = pqResult[i]
            # print("2) candidate firstname is ", new_candidate["firstname"])

        if i == "last_name":
            # print(pqResult[i])
            new_candidate["surname"] = pqResult[i]
            # print("3) candidate surname is ", new_candidate["surname"])

        if i == "city":
            # print(pqResult[i])
            new_candidate["location"] = pqResult[i]
            currLocation = new_candidate["location"]
            # print("4) candidate location is ", new_candidate["location"])

        if i == "occupation":
            # print(pqResult[i])
            new_candidate["job_title"] = pqResult[i]
            currJtitle = pqResult[i]
            
            # print("4) candidate jobtitle is ", new_candidate["job_title"])
        else:
            new_candidate["job_title"] = "Current jobtitle not set"

        if i == "headline":
            # print(pqResult[i])
            new_candidate["notes"] = pqResult[i]
            # print("4) candidate notes is ", new_candidate["notes"])
        else:
            print("no notes")
            new_candidate["job_title"] = "Current jobtitle not set"
            #new_candidate["job_title"] = pqResult[i]
            #new_candidate["notes"] = new_candidate["notes"] + " null"

    try:
        if new_candidate["notes"]:
            print("notes is set")
    except:
        print("set notes to null")
        new_candidate["notes"] = "null"

    try:
        if new_candidate["name"]:
            print("full name is set")
    except:
        print("set name to null")
        new_candidate["name"] = "null"

    # set candidate url

    # liUrl

    new_candidate["li_url"] = liUrl

    # set date added, convert to string

    today = date.today()

    today = str(today)

    print("buildCandidate) Today's date:", today)

    new_candidate["date_added"] = today

    # set current company
    try :
        if pqResult["experiences"][0]["company"]:

            new_candidate["company"] = pqResult["experiences"][0]["company"]
            currFirm = pqResult["experiences"][0]["company"]

        else:
            new_candidate["company"] = "unknown"
    except:
        new_candidate["company"] = "unknown"

    # 1) Add generic profile type "all", 2) put experiences -> title in here

    try:
        if pqResult["experiences"][0]["title"]:
            new_candidate["profile_type"] = "all, " + pqResult["experiences"][0]["title"]
    # last chance to set jobtitle if experience contains at job title
            new_candidate["job_title"] = pqResult["experiences"][0]["title"]
            currJtitle = pqResult["experiences"][0]["title"]
            

        else:
            new_candidate["profile_type"] = "all, "
    except:
        new_candidate["profile_type"] = "all, "

    # try to calculate time in post
    try:
        if isinstance(pqResult["experiences"][0]["ends_at"], dict) and isinstance(pqResult["experiences"][0]["starts_at"], dict):

            print("end date is set")
            print(pqResult["experiences"][0]["ends_at"])
            duration = prepareDate(pqResult["experiences"][0]["starts_at"], pqResult["experiences"][0]["ends_at"])
            
            print("buildCandidate) returnned from prepareDate (time in post): ", duration)
            
            new_candidate["time_in_post"] = duration

        elif isinstance(pqResult["experiences"][0]["ends_at"], dict):
            print("buildCandidate) only have ends_at")
            duration = 0
            new_candidate["time_in_post"] = duration
# what if no end date?

        elif isinstance(pqResult["experiences"][0]["starts_at"], dict):
            print("only have starts_at")
            duration = 0
            new_candidate["time_in_post"] = duration

        else:

            print("one or other is not set")
        # just use current date?
            duration = 0
            new_candidate["time_in_post"] = duration
    except:
        duration = 0
        new_candidate["time_in_post"] = duration


    # Get nb of years worked
    try:
        nbYrsExp = GetYrsExp(pqResult, stageTerms)
        print("buildCandidate) returnned from GetYrsExp (yrs exp): ", nbYrsExp)
        
    except:
        nbYrsExp = 0
        new_candidate["years_exp"] = nbYrsExp

    # calculate time in post
    # time_in_post

    # Add initial search excluder (json field)

    jsonPlug = {"searches": ["auto"]}
    new_candidate["json"] = jsonPlug

    # Add internal search json field

    searchJson = {"searchjson": [0]}
    new_candidate["internalsearchjson"] = searchJson

    # Add optimisestatus = "TO DO"

    new_candidate["optimisestatus"] = "TO DO"

    # print all data for new candidate
    print("final candidate object @@@@@@@@@@@@@ ", new_candidate)


    # ADD TO STRAPI HERE
    #sUrl = "https://strapi-1oni.onrender.com/candidates"
    sUrl = "candidates"

    testAdd = addStrapiApi(sUrl, new_candidate)

    # print("test data returned from Strapi: Add candidate ------- ", testAdd)
    print("00000000000000 - returned cand ID - ", testAdd["id"])
    # return testAdd
    return testAdd["id"], currJtitle, currFirm, currLocation, nbYrsExp
