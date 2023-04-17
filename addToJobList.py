from addStrapi import *
from searchStrapiApi import *
from updateStrapi import *

def addToJobList(cand, searchID, jobID, finalPoints, candName):

    print("addToJobList) Running")

    print("addToJobList) CAND ID : ", cand)

    print("addToJobList) Search ID : ", searchID)

    print("addToJobList) Job ID : ", jobID)

    print("addToJobList) Score : ", finalPoints)

    print("addToJobList) Cand name : ", candName)

    # get current job name 

    testUrl = "jobs"
    query = "?_where[id]="
    searchVal = jobID

    print("addToJobList) job id sent to strapi: ", searchVal)

    # get search clicked on 
    goQuery = strapiApi(testUrl, query, searchVal)

    print("should contain the correct job: ", goQuery)
    print(goQuery)

    jobName = goQuery[0]["job_title"]

    print("addToJobList) job name : ", jobName)

    # build new job structure for joblist json field
    # "Accountant(Lux)-138"

    finJobName = jobName + "-" + jobID
    

    # add new application to "applications" table

    # convert cand nb to string for api
    cand = str(cand)

    new_application = {}
    new_application["status"] = "Send LI queued"
    new_application["job"] = jobID
    new_application["candidate_name"] = candName
    new_application["candid"] = cand

    sUrl = "applications/"

    testAdd = addStrapiApi(sUrl, new_application)

    print(testAdd)
    appID = testAdd["id"]

    # update candidate object, add score, new application, new job (to json and shared fields)

    # new_jobs = {"jobs": [jobID]}

    new_jobs = {"jobs": [finJobName]}

    payload = {"joblist": new_jobs, "internal_points":finalPoints, 
    "applications":[appID], "jobs":[jobID]}

    sUrl = "candidates/"
    #cand = "712"

    finalCandData = updateStrapiApi_PC(sUrl, cand, payload)
    print(finalCandData)

    # complete

