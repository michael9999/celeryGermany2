from getStrapiApi import *

def getConfigStrapi(id):

    # search_tab = "status"

    # queryString = "filterByFormula=SEARCH('%s', {%s})" % (search_val, search_tab)
    # patterns = airApi(url, queryString, search_val, search_tab)

    testUrl = "search-configs"
    query = "?_where[id]="
    # searchVal = "Live"
    searchVal = id

    #query = "?_where[id]="
    #searchVal = searchid

    patterns = getStrapiApi(testUrl, query, searchVal)

    #print("testing patterns $$$$$$$$$$$$$$ : ", patterns)

    list_patterns = list()

    for record in patterns:

        if 'pattern' in record:

            #print("pattern found ***************")
            #print(record['pattern'])

            list_patterns.append(record['pattern'])


    #print("print all patterns:  ")
    #print(list_patterns)
    return list_patterns

