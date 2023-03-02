from updateStrapi import *
from searchStrapiApi import *
import sys
import requests, json
global tokenid
tokenid = "N{t[4AJHBa6]T@#$22"
from gSearch import *

def processSearchGo(res, nbPages, varPts, firmPts, languagePts, MinPoints, searchName, list_variables, FIRMList, Language, psssID):
    
    # import update strapi
    
    print("processSearchGo) running")
    # res, nbPages, varPts, firmPts, languagePts, MinPoints, searchName, list_variables, FIRMList, Language, psssID
    print(res)
    print(nbPages)
    print(varPts)
    print(firmPts)
    print(languagePts)
    print(MinPoints)
    print(searchName)
    print(list_variables)
    print(Language)
    print(FIRMList)
    print(psssID)

    # % Update search status to "running" = OK 
    
    testUrl = "control-panels/"

    liveId = str(psssID)

    payload = {"action": "Running"}
    
    # airUrl, candId, payload
    runUpdate = updateStrapiApi_PC(testUrl, liveId, payload)
    
    # process patterns, loop
    
    for items in res:
        
        testUrl = "control-panels"
        query = "?_where[id]="
        #searchVal = liveId
        searchVal = str(psssID)
        testTrigger = strapiApi(testUrl, query, searchVal)
        
        if testTrigger[0]['action'] == "Running":
            print("search is still live")
            
            # run google searches
            test1 = gSearch(items, nbPages)
            print(test1)
            
        else:
            print("search deactivated")
    
    

## LIVE?
def processSearchStrapNewOct(res, nbPages, varPts, firmPts, languagePts, MinPoints, searchName, list_variables, FIRMList, Language, psssID):

# wait a few seconds to allow data to be added by last run

# "res" is an array of search patterns

    print("processSearchStrapNewOct) running")

    counter = 0

####### update "action" to "running"

    testUrl = "control-panels/"

    liveId = str(psssID)

    payload = {"action": "Running"}

    # updateStrapiApi(strapiUrl, payload, strapId)

    runUpdate = updateStrapiApi(testUrl, payload, liveId)


    # WORKS print out all patterns together
    # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    for items in res:

        # pass individual patterns to search function here

        #print("processSearchStrapiImmediateSearch): should print list of live patterns: ", items)

# NEW
        # check if I have the live search ID

        #print("(processSearchStrapNewOct) live search ID is ")
        #print(psssID)



        testUrl = "control-panels"
        query = "?_where[id]="
        #searchVal = liveId
        searchVal = str(psssID)
        testTrigger = strapiApi(testUrl, query, searchVal)

        # check if search is still live

        if testTrigger[0]['action'] == "Running":

            print("processSearchStrapNewOct) Search still live, current run: ")

            # required variables
            # "q": search_query_content,
            # "num": nbPages,

            #print("processSearchStrapNewOct) PROCESS SEARCH: ", items)

            test1 = gSearch(items, nbPages)

            counter = counter + 1

            # check if organic results were returned
            if test1['search_information']['organic_results_state'] == "Fully empty":

                print("processSearchStrapiImmediateSearch) NO RESULTS FOR THIS PATTERN: ", items)
                #print(test1)

            # results were returned, process
            else: # results were returned, start process

                title = list()

                if test1['organic_results']:

                # processing organic results here

                    for record2 in test1['organic_results']:

                        #print("zzzzzzzzz: TOP OF LOOP: for record2 in test1[organic_results]")
                        # set variable "insert or not"

                        immediateScrape = "No"

                        insertOK = "Yes"


                        if 'title' in record2:
                            title.append(record2['title'])

                        # put a function in here  to extract the candidate's name

                        # get 'title' value
                        itext = record2['title']

                        # get 'url' value
                        jurl = record2['link']

                        # Check that snippet exists
                        print("---- IS THERE A SNIPPET? ",  record2['snippet'])
                        print("---- END OF SNIPPET PRINT OUT")

                        try:

                        # get 'snippet' value
                            snippet = record2['snippet']
                        #    print("processSearchStrapiImmediateSearch) ANYTHING IN SNIPPET?")
                        #    print(snippet)

                        #print("this is the Snippet  0000000000000000000000000000000000000000000 ")
                        #print(snippet)
                        except:
                            print("except) processSearchStrapNewOct) SNIPPET ERROR £££££££££££££££££££££££££££££ ")
                            #print(record2

# Finally seems to be running
    

                        finally:
                            print("finally 1) processSearchStrapNewOct) END OF SNIPPET *************@@***************")

    # Check what the target site is (ex. linkedin or viadeo)

                        searchType = ""

    # for Linkedin
                        #if "linkedin" in items:
                        if "linkedin" in jurl:

                            #print("processSearchStrapiImmediateSearch) url target is Linkedin 1")
                            # use a function here to get firstname and surname
                            searchType = "linkedin"
                            newCandName = formatName(searchType, itext)

    # for Viadeo
                        elif "viadeo" in items:

                            #print("processSearchStrapiImmediateSearch) target is viadeo")
                            searchType = "viadeo"
                            newCandName = formatName(searchType, itext)

                        else:
                            print("processSearchStrapNewOct) $$$$$$$$$$$$$$$$ target not recognised **********************")
                            newCandName =""
                        #print ("this string returned from formatName function : ")
                        #print(newCandName)

                        # variable = formatName(searchEngine, title)

                        pointsComp = 0
                        #if 'title' in record['organic_results']:
                            #types.append(record['organic_results']['title'])
                        #print ("printing title " + record2['title'])


                        # check name is made up of 2 names, if 2 then proceed
                        Cname = newCandName
                        #print("processSearchStrapNewOct) (ln 1166) Check candidate name")
                        #print(Cname)

                        finalCount = len(Cname.split())

    # Do not continue if we can't search for the name

                        if finalCount <2:
                            #print ("only first part of name present")
                            continue



                        else:

# If 2 names then check if candidate is already in DB

                            # print("processSearchStrapNewOct) NAME is made up of 2 strings, PROCEED! = " + Cname)

                            testUrl = "candidates"
                            query = "?_where[name]="
                            searchVal = Cname

# check if candidate is already in DB

                            cand_search = strapiApi(testUrl, query, searchVal)

                            #print("processSearchStrapNewOct) Is this candidate already in the DB?")
                            #print("processSearchStrapiImmediateSearch) Value from api call : ")
                            #print(cand_search)
                            #print("printing itext")
                            #print(itext)

    # Check if the candidate already exists in DB
    # response_data['records'][0]['fields']
                            try:

                                #print("processSearchStrapNewOct) TRY block (ln 1204) started")

    # If 'id' check returns true, candidate already in DB

                                if 'id' in cand_search[0]:
# entry found in candidates, do not add

                                    print("processSearchStrapNewOct) Candidate found in DB 3333333333333333333333333333333333333333333333")

                                    insertOK = "No"
                                        # create/set variable here which stops insert lower down?
                                    continue

    # Candidate not found, PROCEED

                            except:

# set trigger to add cand to cand searches
                                insertOK = "Yes"

                                print("processSearchStrapNewOct) NOT FOUND, add candidate")

    # CHECK VARIABLES, ASSIGN POINTS
                                if(searchType == "viadeo"):

                                    itextFinal = snippet + " " + itext

                                else:
                                    itextFinal = itext

                                        # put title and snippet together
                                        # itext2 = snippet + " " + itext
                                    #print("processSearchStrapiImmediateSearch) Just before checkPoints function")
                                    variablePointsFinal = checkPoints(varPts, list_variables, itextFinal)

# if variables found then scrape automatically

                                    if variablePointsFinal > 0:

                                        print("$$$$$$$$$$ Variable found in data, scrape full candidate")
                                        immediateScrape = "Yes"

                                    #print("processSearchStrapNewOct) here are the points from the variable search")
                                    #print(variablePointsFinal)

                                        # CHECK FIRM LIST, ASSIGN points

                                        # check lis of companies
                                    #print("processSearchStrapNewOct) print list of companies CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC")
                                    #print(FIRMList)
                                    firmPointsFinal = checkPoints(firmPts, FIRMList, itextFinal)

                                    # sets trigger for immediate scrape

                                    if firmPointsFinal > 0:

# if firm is present in snippet, DO FULL SCRAPE
                                        print("$$$$$$ Firm found in data, scrape full candidate")
                                        immediateScrape = "Yes"

    # CHECK LANGUAGES, ASSIGN POINTS

                                    #print("processSearchStrapiImmediateSearch) check languages LLLLLLLLLLLLLLLLLLLLLLLLLLLL")
                                    #print(FIRMList)
                                    #print("processSearchStrapNewOct) Just before checkPoints LANGUAGE POINTS")
                                    languagePointsFinal = checkPoints(languagePts, Language, itextFinal)

                                        # check min pointsComp

                                    #print("processSearchStrapNewOct) minimum points: ")
                                    #print(MinPoints)

    # Calculate total points
                                    totalPoints = variablePointsFinal + firmPointsFinal + languagePointsFinal
                                        # check finalPoints
                                    #print("processSearchStrapNewOct) check final points")
                                    #print(totalPoints)
                                    MinPoints = int(MinPoints)

                                    if totalPoints >= MinPoints:
                                        print("processSearchStrapNewOct) (ln 1282) Sufficient points scored")

    # candidate has right nb of points

    # check if already in temporary database
    # CHANGED TO main DB
    # ***************************************************
    # ADD API CALL HERE
    # ^^^^^^^ HERE
                                            # check content's of profile url
                                        #print("processSearchStrapNewOct) this is LI url : " + jurl)
                                        #print("processSearchStrapNewOct) minimum points attained")
                                            #url = "https://api.airtable.com/v0/app4oLvpPDbjWQQCg/Candidates"
                                            #https://api.airtable.com/v0/app4oLvpPDbjWQQCg/Candidates_autoSearch

                                            #url = "https://api.airtable.com/v0/appNQUHCXuwYRISgk/CandidatesToScrape"

                                        search_val_variables = jurl
                                        search_tab_variables = "LIurl"

                                        #testUrl = "candidates-searches"
                                        testUrl = "candidates"
                                        #query = "?_where[urlli]=" li_url
                                        query = "?_where[li_url]="
                                        searchVal = jurl

                                            # queryString_variables = "filterByFormula=SEARCH('%s', {%s})" % (search_val, search_tab)

                                        url_search = strapiApi(testUrl, query, searchVal)
                                        #print("processSearchStrapiImmediateSearch) (ln 1308) data returned from Strapi search")
                                        #print(url_search)

                                            # url_search = airApi(url, queryString_variables, search_val, search_tab)

    # check if any results were returned

                                        try:

                # If 'id' check returns true, candidate already in DB

                                            if 'id' in url_search[0]:

# Cand exists in searches database, do not add
                                                #print("processSearchStrapiImmediateSearch) (ln 1326): if ID present")
                                                print("processSearchStrapNewOct) CANDIDATE FOUND in temporary DB: ", url_search[0])
                                                variablePointsFinal = 0
                                                firmPointsFinal = 0
                                                languagePointsFinal = 0
                                                insertOK = "No"
                                                    # should I set immediateScrape = "No"
                                                continue


# If Except clauses fires, Add candidate and proceed to points stage
                                        except:

                # Add candidate to temporary DB
    # ***************************************************
    # ADD API CALL HERE
                                            # print("processSearchStrapNewOct) (ln 1347)no id found (Except)")
                                            # print("processSearchStrapNewOct) NOT FOUND, ADD CAND TO DB")

    # get current date

                                            d = datetime.datetime.today()
                                            print ('Current date and time:', d)
                                            dformatted = d.strftime('%Y-%m-%d')

                                            #print("processSearchStrapiImmediateSearch) (ln 1359) check searchName")
                                            #print(searchName)
                                            #print("processSearchStrapiImmediateSearch) (ln 1361) check Cname")
                                            #print(Cname)

                                            payload = {"date":dformatted,"name":searchName,"profiletype":"No profile type",
                                                        "points":totalPoints, "urlli":jurl, "details":itext, "checked":"filler",
                                                        "candidatename":Cname, "query":items, "notes":"notes", "status":"To Process"}


                                                        # addAirApi(airUrl, queryString, search_val, search_tab, payload):
                                            urlTest = "https://strapi-public-test.herokuapp.com/candidates-searches"

                                                        # addCandNow = addAirApi(airUrl, payload)
                                            if insertOK != "No":

                                                # Add candidate to candidate searches
                                                addCandNow = addStrapiApi(urlTest, payload)
# set immediateScrape to "Yes" here?
                                                immediateScrape = "Yes"
                                                #print("processSearchStrapiImmediateSearch) result of cand add: ", addCandNow)
                                                #print("try to isolate id returned: ", addCandNow["id"])

                                                # Scrape candidate fully

                                                if immediateScrape == "Yes":

                                                    try:

                                                        if addCandNow["id"]:

                                                            #print("processSearchStrapiImmediateSearch) proxycurl call 0): ", addCandNow["id"])

                                                            scrapeUrl = "https://celery16-05.herokuapp.com/proxycurlsingle"

                                                            # int(nb)

                                                            testID = addCandNow["id"]
                                                            payload2 = {"cand_id": testID}

                                                            # addProxy(strapiUrl, payload):

                                                            fullScrapeNow = addProxy(scrapeUrl, payload2)
                                                            #print("result from addProxy: ", fullScrapeNow)


                                                    except:
                                                        print("addCandNow) new candidate add failed")
                                                        continue

                                                else:
                                                    print("immediateScrape 0), trigger was NO")

                                                #print(addCandNow)
                                                variablePointsFinal = 0
                                                firmPointsFinal = 0
                                                languagePointsFinal = 0
                                                continue

                                            else:
                                                variablePointsFinal = 0
                                                firmPointsFinal = 0
                                                languagePointsFinal = 0
                                                continue



                                    else:

                                        print("processSearchStrapiImmediateSearch) insufficient points")

                                        print("processSearchStrapiImmediateSearch) END µµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµ ")




    # assign points (if sufficient add to DB)
    # add to database




                else:
                    print("processSearchStrapiImmediateSearch) no organic results returned")





    # if "action" =! "Running" then kill script

        else:
            print("processSearchStrapiImmediateSearch) search has been stopped, abort script")
            sys.exit("processSearchStrapiImmediateSearch) Process has been stopped by the user")

    # Change searche's status to DONE

    testUrl = "control-panels/"

    liveId = str(psssID)

    payload = {"action": "DONE"}

    # updateStrapiApi(strapiUrl, payload, strapId)

    runUpdate = updateStrapiApi(testUrl, payload, liveId)

