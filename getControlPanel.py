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
        print("getControlPanelData(): Entry found")

        # Set variables Names of lists (Firms and Search variables)

        firm_list_names = list()
        search_var_list_names = list()

        # Check that we can access all details from ControlPanel

## !!!!!! - Use this loop if I want to process multiple searches from Controlpanel at the same time

        for record in test[0]:

        ######## Get name of search variable list


            if 'searchterms' in record:
                #for term in record['searchterms']:
                #search_var_list_names.append(test[0][record])
                search_var_list_names.append(test[0][record])
                print("print search term")
                print(search_var_list_names)


            if 'firms' in record:
                # for comp in record['fields']['FirmList']:
                firm_list_names.append(test[0][record])
                print("print firms")
                print(firm_list_names)


            if 'nbpages' in record:
                #for pagina in record['fields']['Nb_pages_search_engine']:
                    #nbPages = pagina
                #nbPages = record['fields']['Nb_pages_search_engine']
                nbPages = test[0][record]
                print("print nb pages")
                print(nbPages)


            if 'variablepoints' in record:

                # varPts = record['fields']['VariablePoints']
                varPts = test[0][record]
                print("print var points")
                print(varPts)


            if 'firmpoints' in record:

                firmPts = test[0][record]


            if 'languagepoints' in record:

                languagePts = test[0][record]


            if 'minpoints' in record:

                MinPoints = test[0][record]


            if 'name' in record:

                searchName = test[0][record]

            if 'id' in record:

                idNb = test[0][record]

    return search_var_list_names, firm_list_names, nbPages, varPts, firmPts, languagePts, MinPoints, searchName, idNb