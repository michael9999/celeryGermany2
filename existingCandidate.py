from searchStrapiApi import strapiApi

def existingCandidate(gresult):



    testUrl = "candidates"
    query = "?_where[li_url]="
    searchVal = gresult
    # strapiApi(testUrl, query, searchVal)

    cand_search = strapiApi(testUrl, query, searchVal)

    if cand_search:
        resultCand = "already in db"
    
    else:
        resultCand = "goproxyCurl"

    return resultCand





