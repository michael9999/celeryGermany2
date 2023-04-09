from getProfileProxy import *
import time

def handPcResponse(response, test):
    
# status= getProfile.status_code

    status = response.status_code

    #print("HandPcResponse) 1 before while) status code is ------------------ : ", status)

    #print("HandPcResponse) 2) response object is ------------------ : ", response)

    retry = 5

    if status != 200:

        print("Task runProxyCurlSingleLatest) 2 before while) server error, status code is: ", status)
        max_guesses = 5
        nb = 0

        while nb < max_guesses:

            # wait for a minute

            time.sleep(30)

            print("Task runProxyCurlSingleLatest) run: ", nb)

            # retry

            getProfile = getProfileProxyCurl(test)
            status = getProfile.status_code
            print("Task runProxyCurlSingleLatest) in while) status code is : ", status)

            if status != 200:

                print("Task runProxyCurlSingleLatest) inside IF), status code is,", status)
                nb+=1
                continue

            else:
                return getProfile
                break


    else:
        #print("Task runProxyCurlSingleLatest) else, 1st for) running")
        #print("Task runProxyCurlSingleLatest) : ", status)

    # 1.2 Scrape data

        getProfile = getProfileProxyCurl(test)

    # 1.3 Check http response code, attempt 5 times


        status= getProfile.status_code

        #print("Task runProxyCurlSingleLatest) case 2) status code is : ", status)

        #print("Task runProxyCurlSingleLatest) case 2) scraped data is : ", getProfile)

        retry = 5

        if status != 200:

            #print("Task runProxyCurlSingleLatest) case2 If) server error, status code is: ", status)
            max_guesses = 5
            nb = 0

            while nb < max_guesses:

                # wait for a minute

                time.sleep(30)

                #print("Task runProxyCurlSingleLatest) case2) run: ", nb)

                # retry

                getProfile = getProfileProxyCurl(test)
                status = getProfile.status_code
                #print("Task runProxyCurlSingleLatest) case2) status code is : ", status)

                if status != 200:

                    #print("Task runProxyCurlSingleLatest) case2 in while loop) status code is not 200: ", status)
                    nb += 1
                    continue

                else:
                    
                    return getProfile
                    

            # print("Task runProxyCurlSingle) After status checks) status code should be 200: ", status)
            # print("Task runProxyCurlSingle) test contents of scrapedProfile: ", getProfile)
        
        else:
            return getProfile