from searchStrapiApi import *

def getSearchVariablesStrapi(term):

    list_variables = list()

    #url_variables = "https://api.airtable.com/v0/apppmg1WJ5qoYztTV/Variables"

    testUrl = "variables"

    # try contains
    query = "?_where[type_contains]="
    searchVal = term

# convert list to string
    # search_val_variables = term[0]
    # search_tab_variables = "Type"

    #print("this is the SEARCH TERM : ")
    #print(searchVal)

# strapiApi(airUrl, queryString, search_val)

    #test_variables = airApi(url_variables, queryString_variables, search_val_variables, search_tab_variables)

    test_variables = strapiApi(testUrl, query, searchVal)

    #print("print names of search variables: ")
    #print(test_variables)

    # put all search terms in a list

    for record_variables in test_variables:

        if 'name' in record_variables:
            # list_variables.append(test_variables[0][record_variables])
            list_variables.append(record_variables['name'])
            # print("printing each SEARCH VARIABLE item")
            #print(list_variables)

    print("getSearchVariablesStrapi) - ", list_variables)

    return list_variables

def getJobTitlesStrapi(term):

    list_variables = list()

    #url_variables = "https://api.airtable.com/v0/apppmg1WJ5qoYztTV/Variab"

    testUrl = "jobtitles"

    # try contains
    query = "?_where[type_contains]="
    searchVal = term

# convert list to string
    # search_val_variables = term[0]
    # search_tab_variables = "Type"

    #print("this is the SEARCH TERM : ")
    #print(searchVal)

# strapiApi(airUrl, queryString, search_val)

    #test_variables = airApi(url_variables, queryString_variables, search_val_variables, search_tab_variables)

    test_variables = strapiApi(testUrl, query, searchVal)

    #print("print names of search variables: ")
    #print(test_variables)

    # put all search terms in a list

    for record_variables in test_variables:

        if 'name' in record_variables:
            # list_variables.append(test_variables[0][record_variables])
            list_variables.append(record_variables['name'])
            # print("printing each SEARCH VARIABLE item")
            #print(list_variables)

    return list_variables



def getFirmsStrapi(comp):

    try:

        #print("getFirms(): TEST")
        #print(comp)
        comp = comp[0]
        #print("getFirms(): TEST")
        #print(comp)
        firms_to_search = list()

        testUrl = "firms"
        query = "?_where[type_contains]="
        searchVal = comp

        # strapiApi(airUrl, queryString, search_val)

        test_variables = strapiApi(testUrl, query, searchVal)
        #print("printing test_variables:")
        #print(test_variables)

        for firm_variables in test_variables:

            if 'name' in firm_variables:

                #print("*************** printing firms: ")

                firms_to_search.append(firm_variables['name'])
                #print(firms_to_search)

    except Exception as e:

        print("error: ")
        print(e)

# returns a list of firms to search for

    return firms_to_search


def getSearchTargetsStrapi():

    search_targets = list()

    testUrl = "search-targets"
    query = "?_where[status]="
    searchVal = "Live"

    test_variables = strapiApi(testUrl, query, searchVal)

    # test_variables = airApi(url_variables, queryString_variables, search_val_variables, search_tab_variables)

    #print("printing each search URL **************")


    for search in test_variables:

        if 'name' in search:

            search_targets.append(search['url'])

            #print(search['url'])

    #print("printing all search targets (end of loop)")
    #print(search_targets)

    return search_targets


def getLocationStrapi():

    search_locations = list()
    testUrl = "locations"
    query = "?_where[status]="
    searchVal = "Live"

    test_variables = strapiApi(testUrl, query, searchVal)

    #print("printing each location URL **************")

    for location in test_variables:

        if 'city' in location:

            search_locations.append(location['city'])

            print(location['city'])

            #print(search_locations)

    return search_locations


def getLanguagesStrapi():

    languages = list()
    testUrl = "languages"
    query = "?_where[status]="
    searchVal = "Live"

    print("printing each language **************")

    test_variables = strapiApi(testUrl, query, searchVal)

    #print("Printing test_variables")
    #print(test_variables)

    #print("printing each language **************")

    for language in test_variables:

        if 'name' in language:

            languages.append(language['name'])
            #print(language['name'])

    return languages

#getSearchVariablesStrapi
def getExclusionTermsStrapi():

    removed = list()
    testUrl = "exclusions"
    query = "?_where[status]="
    searchVal = "Live"

    test_variables = strapiApi(testUrl, query, searchVal)

    #print("getExclusionTermsStrapi) exclusions terms: ", test_variables)

    for excluded in test_variables:

        #print(excluded['name'])

        if 'name' in excluded:

            removed.append(excluded['name'])

    print("getExclusionTermsStrapi) exclusions terms: ", removed)

    return removed
