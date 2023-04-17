from updateStrapi import *
from searchStrapiApi import *
import sys
import requests, json
#global tokenid
#tokenid = "N{t[4AJHBa6]T@#$22"
from gSearch import *
from existingCandidate import *
from addCandLanguages import *
from buildCandidate import *
from buildSearchString import *
from buildSendEducation import *
from buildSendExperiences import *
from createCandOptSearch import *
from getProfileProxy import *
from responseProxyCurl import *
from addStrapi import *
from checkForVars import *
import urllib.parse

def processSearchGo(res, nbPages, varPts, firmPts, languagePts, MinPoints, searchName, list_variables, FIRMList, Language, searchID, jobtitles, stageTerms, jobID, jobPts, locPts):
    
    # import update strapi
    
    #print("processSearchGo) running")
    # res, nbPages, varPts, firmPts, languagePts, MinPoints, searchName, list_variables, FIRMList, Language, psssID
    print("should show all patterns: ", res)
    print(nbPages)
    print(varPts)
    print(firmPts)
    print(languagePts)
    print(MinPoints)
    print(searchName)
    print(list_variables)
    print(Language)
    print(FIRMList)
    print(searchID)
    print(jobtitles)
    print("processSearchGo) - work experiences terms - ", stageTerms) # eg. alternance, stagiaire etc...

    

    # % Update search status to "running" = OK 
    
    # testUrl = "https://strapi-1oni.onrender.com/control-panels/"

    testUrl = "control-panels/"

    liveId = str(searchID)

    payload = {"action": "Running"}
    
    # airUrl, candId, payload
    runUpdate = updateStrapiApi_PC(testUrl, liveId, payload)
    
    # process patterns, loop, (res is the number of search patterns)
    
    for items in res:
        
        testUrl = "control-panels"
        query = "?_where[id]="
        #searchVal = liveId
        searchVal = str(searchID)
        testTrigger = strapiApi(testUrl, query, searchVal)
        
        if testTrigger[0]['action'] == "Running":
            #print("search is still live")
            
            # get location
            if testTrigger[0]['location']:
                targetLocation = testTrigger[0]['location']
                print("processSearchGo) target location is : ", targetLocation)
            else:
                #print("processSearchGo) location not set")
                targetLocation = "not set"

            # get yrs exp - Yearsexp
            if testTrigger[0]['yearsexp']:
                targetyrsexp = testTrigger[0]['yearsexp']
                #print("processSearchGo) target yrs experience is : ", targetyrsexp)
            else:
                #print("processSearchGo) targetyrsexp not set")
                targetyrsexp = 0


            # get all towns
            # if (testTrigger[0]['location'] isset) AND (testTrigger[0]['location'] != "not set")
                # get all towns where parentcity == testTrigger[0]['location']
                # build list
                # pass list to checkForVars
            if (targetLocation) and (targetLocation != "not set"):
                print("get all towns")
                testUrl = "towns"
                query = "?_where[parentcity]="

                #searchValLoc = "Paris"

                searchValLoc = targetLocation

                testTrigger = strapiApi(testUrl, query, searchValLoc)
                allTowns = []

                for record_variables in testTrigger:

                    if 'townname' in record_variables:
                    # list_variables.append(test_variables[0][record_variables])
                        allTowns.append(record_variables['townname'])
                    # print("printing each SEARCH VARIABLE item")
                    #print(list_variables)


            
                    else:
                        print("no towns found")


            # run google searches
            test1 = gSearch(items, nbPages)
            #print(test1)

            # Check if there are any results 

            if test1['search_information']['organic_results_state'] == "Fully empty":

                print("processSearchGo) NO RESULTS FOR THIS PATTERN: ", items)

            else: 
                #print("continue!")

                for li in test1['organic_results']:

                # check if profile is already in db (linkedin_url)

                    # try to set LI url to UTF8 - for bloody french accents!

                    decoded_liUrl = urllib.parse.unquote(li["link"])

                    #print("processSearchGo) this is url we are searching for : " + li["link"])
                    #existCand = existingCandidate(li["link"])
                    existCand = existingCandidate(decoded_liUrl)

                    tempName = li["title"]
                    #print("processSearchGo) in db or not? ", existCand)

                    # call proxycurl if new candidate:  
                    if(existCand == "goproxyCurl"):

                        #print("processSearchGo) Run proxy curl - NEW CAND ------ ")

                        test = getProfileProxyCurl(li["link"])
                        test2 = handPcResponse(test, li["link"])

                        # should put try in here in case no json returned, move to next?
                        try:
                            scrapedProfile = test2.json()
                        except:
                            continue
                        #print("processSearchGo) scraped profile : ", scrapedProfile)

                        testAdd = "test"
                        # Gets "people also viewed", adds to Candidates Searches

                        for value in scrapedProfile["people_also_viewed"]: 
    
                            #print("processSearchGo) processing 'people also viewed'")
                            # build object with these fields : link, name, summary, location
                            payload = {}
                            payload["name"] = value["name"]
                            payload["urlli"] = value["link"]
                            payload["details"] = value["summary"]
                            payload["notes"] = value["location"]
                            payload["profiletype"] = "people_also_viewed"
                            
                            #goUrl = "https://strapi-1oni.onrender.com/candidates-searches"

                            goUrl = "candidates-searches"
                            
                            testAdd = addStrapiApi(goUrl, payload)

                        #print("processSearchGo) which extra profiles were added ? ", testAdd)
                        # End "people also viewed"

                        # Build candidate, get ID, current job title, current firms
                            # added "stageTerms" so that I can exclude stage from total

                        newid, currJtitle, currFirm, currLocation, currYrsExp, candName = buildCandidate(scrapedProfile, li["link"], stageTerms)

                        ############# buildSendExperiences (workexperiences)
                        # build array of jobtitles, firms
                        # workIds, jobtitles, firms, allworkexperiences
                        jobIds, jobtitlesTS, firmsTS, allworkexperiences  = buildSendExperiences(scrapedProfile, newid, stageTerms)

                        ############# addCandLanguages (get languages) = OK ############@
                        languageIds = addCandLanguages(scrapedProfile) 

                        ############# buildSendEducation (get scrapedProfile) = OK ############
                        educationIds = buildSendEducation(scrapedProfile)

                        # fill in any blanks for education and work history
                        if not educationIds:

                        # CHECKED, correct id
                            educationIds = [23387]
                        #print("test is not set")

                        else:
                            print("education is set")

                            # !!! THIS IS WORK EXPERIENCE

                        if not jobIds:

                            # WORK HISTORY ID CHECKED = OK

                            jobIds = [3362]
                            
                        else:
                            
                            print("job id is set")

                        # Update candidate (education, work exp, languages, skills)
                         
                        payload = {"educations": educationIds, "work_histories": jobIds, 
                        "cand_languages": languageIds, "skills":[33994]}

                        #sUrl = "https://strapi-1oni.onrender.com/candidates/"

                        sUrl = "candidates/"    

                        cand = newid

                        finalCandData = updateStrapiApi_PC(sUrl, cand, payload)

                        #print("processSearchGo) did candidate update work ? ", finalCandData)

                        # Create optimised search field
                        #
                        creatOptSearchField = createCandOptSearch(cand)
                        #print("**************** optimised search): ", creatOptSearchField)                                        

                        # Get job titles and search variables and look for them 

                        # search vars : jobtitles, list_variables, FIRMList - should be okay

                        # jobtitlesTS (all job titles), firmsTS (all firms), creatOptSearchField (all data?)
                        # currJtitle, currFirm
                        # targetyrsexp
                        #checkVar = checkForVars(jobtitlesTS, firmsTS, creatOptSearchField, currJtitle, currFirm, allworkexperiences) # current jobtitle, current company, list of previous jobtitles, all search vars 

                        checkForVars(jobtitlesTS, firmsTS, creatOptSearchField, currJtitle, currFirm, allworkexperiences,
						searchName, list_variables, FIRMList, Language, searchVal, jobtitles, allTowns, targetyrsexp, currLocation, currYrsExp, cand, jobID,
                        varPts, firmPts, languagePts, jobPts, locPts, candName)

                        # add cand to job / search or not 
                        


                    else: 

                        continue
                # if test1['organic_results']:

                
            

                # call proxycurl if new candidate

            
        else:
            #print("Log info: Google search stopped")
            return "search no longer active"
            #print("search deactivated")
    
    return "done"