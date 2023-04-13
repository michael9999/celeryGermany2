from searchStrapiApi import *

def getControlPanelDataStrapi(searchid):

    print("(getControlPanelDataStrapi) - Starting")
    testUrl = "control-panels"
    #query = "?_where[action]="
    #searchVal = "Live"

    query = "?_where[id]="
    # this is the search name
    searchVal = searchid

    test = strapiApi(testUrl, query, searchVal)

    firm_list_names = list()
    search_var_list_names = list()
    nbPages =""
    varPts = 0
    firmPts = 0
    languagePts = 0
    MinPoints = 0
    searchName = ""
    idNb = ""
    jobbytitles = ""
    jobtitlePoints = 0
    locationPoints = 0


    # strapiApi(airUrl, queryString, search_val)

    ########### TESTS IF ANY LIVE SEARCHES ARE PRESENT IN control panel
    try:

        if not "action" in test[0]:

            print("no entry found - no live searches found")

        # Email field is present profile already in system, based on name check against 'Name' field in DB

        # Add to database, continue with CODE
    except:
        print("EXCEPT CLAUSE, no entry found")

        # Live searches were found
    else:
        #print("getControlPanelData(): Entry found new")

        # Set variables Names of lists (Firms and Search variables)

        firm_list_names = list()
        search_var_list_names = list()

        # Check that we can access all details from ControlPanel

## !!!!!! - Use this loop if I want to process multiple searches from Controlpanel at the same time

        for record in test[0]:

        ######## Get name of search variable list

            # check for assigned job id

            #if record == "job": 
                #print("JOB ID is:", test[0][record]['id'])
            #    jobID = test[0][record]['id']
            if 'job' in record:
                jobID = test[0][record]['id']


            if 'searchterms' in record:
                #for term in record['searchterms']:
                #search_var_list_names.append(test[0][record])
                search_var_list_names.append(test[0][record])
                #print("print search term")
                #print(search_var_list_names)


            if 'firms' in record:
                # for comp in record['fields']['FirmList']:
                firm_list_names.append(test[0][record])
                #print("print firms")
                #print(firm_list_names)


            if 'nbpages' in record:
                #for pagina in record['fields']['Nb_pages_search_engine']:
                    #nbPages = pagina
                #nbPages = record['fields']['Nb_pages_search_engine']
                nbPages = test[0][record]
                #print("print nb pages")
                #print(nbPages)


            if 'variablepoints' in record:


                if test[0]['variablepoints'] == None:
            
                    print("no points")
                    varPts = 0  
                    
                else:

                    print(test[0]['variablepoints'])
                    #MinPoints = test[0][record]    
                    varPts = test[0]['variablepoints']    

                # varPts = record['fields']['VariablePoints']
                #varPts = test[0][record]
                #print("print var points")
                #print(varPts)


            if 'firmpoints' in record:

                if test[0]['firmpoints'] == None:
            
                    print("no points")
                    firmPts = 0  
                    
                else:

                    print(test[0]['firmpoints'])
                    #MinPoints = test[0][record]    
                    firmPts = test[0]['firmpoints']    

                #firmPts = test[0][record]


            if 'languagepoints' in record:

                if test[0]['languagepoints'] == None:
            
                    print("no points")
                    languagePts = 0  
                    
                else:

                    print(test[0]['languagepoints'])
                    #MinPoints = test[0][record]    
                    languagePts = test[0]['languagepoints']


            if 'minpoints' in record:

                if test[0]['minpoints'] == None:
            
                    print("no points")
                    MinPoints = 0  
                    
                else:

                    print(test[0]['minpoints'])
                    #MinPoints = test[0][record]    
                    MinPoints = test[0]['minpoints'] #jobtitlePoints
               

            if 'jobtitlepoints' in record:
        
                # check actual points have been set for jobtitle points

                if test[0]['jobtitlepoints'] == None:
            
                    print("no points")
                    jobtitlePoints = 0  
                    
                else:

                    print(test[0]['jobtitlepoints'])
                    jobtitlePoints = test[0]['jobtitlepoints'] #jobtitlePoints


            if 'locationpoints' in record:
        
                if test[0]['locationpoints'] == None:
            
                    print("no points")
                    locationPoints = 0  

                else:

                    print(test[0]['jobtitlepoints'])
                    locationPoints = test[0]['locationpoints']

                  

            if 'jobtitles' in record: 

                jobbytitles = test[0][record]

            if 'name' in record:

                searchName = test[0][record]

            if 'id' in record:

                idNb = test[0][record]

    return search_var_list_names, firm_list_names, nbPages, varPts, firmPts, languagePts, MinPoints, searchName, idNb, jobbytitles, jobID, jobtitlePoints, locationPoints