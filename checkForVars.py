from applyCheck import *
from applyYrsCheck import *
from addToJobList import *

def checkForVars(jobtitlesTS, firmsTS, creatOptSearchField, currJtitle, currFirm, allExperiences, searchName, list_variables, FIRMList, Language, searchID, jobtitles, targetLocation, targetyrsexp, currLocation, currYrsExp, cand, jobID, varPts, firmPts, languagePts, jobPts, locPts, candName):

    # checkForVars(jobtitlesTS, firmsTS, creatOptSearchField, currJtitle, currFirm, allworkexperiences,
						# searchName, list_variables, FIRMList, Language, psssID, jobtitles)

    #print("checkForVars running")

    #(jobtitlesTS, firmsTS, creatOptSearchField, currJtitle, currFirm)

    #print("checkForVars) check : ") # cand # jobID

    #print("checkForVars) JOB ID : ", jobID)

    #print("checkForVars) candidate strapi ID : ", cand)

    #print("checkForVars) jobtitlesTS (cand data): ", jobtitlesTS)

    #print("checkForVars) firmsTS (cand data): ",  firmsTS)

    #print("checkForVars) creatOptSearchField (cand data) : ",  creatOptSearchField)

    print("checkForVars) currJtitle (cand data) : ",  currJtitle)

    #print("checkForVars) currFirm (cand data) : ",  currFirm)

    #print("checkForVars) searchName (search data) : ",  searchName)

    #print("checkForVars) list_variables (search data) : ",  list_variables)

    #print("checkForVars) FIRMList (search data) : ",  FIRMList)

    #print("checkForVars) Language (search data) : ",  Language)

    #print("checkForVars) searchID (search data) : ",  searchID)

    print("checkForVars) jobtitles (search data) : ",  jobtitles)

    print("checkForVars) target location (search data) : ",  targetLocation) # currLocation

    #print("checkForVars) currLocation (search data) : ",  currLocation)

    #print("checkForVars) all work experiences (search data) : ",  allExperiences)

    #print("checkForVars) target years experience (search data) : ",  targetyrsexp)

    #print("checkForVars) candidate's nb of years experience (search data) : ",  currYrsExp)
 
    # perform all checks, apply scores currYrsExp
    
    # minimum pass =
        # current jobtitle = ok AND location = ok
    
    # 1) current jobtitle (text) IMPORTANT
        # 1 pt is added

    if (currJtitle) and (jobtitles):

        testPoints1 = applyCheck(jobtitles, currJtitle, 0)

    else: 
        print("checkForVars) -£££££££££££ jobtitle and list of titles not found")
        testPoints1 = 0


    # 2) #location = (text) IMPORTANT
        # 1 pt is added

    if (currLocation) and (targetLocation):

        testPoints2 = applyCheck(targetLocation, currLocation, 0)

    else: 
        #print("checkForVars) -£££££££££££ currentlocation and list of locations not found")
        testPoints2 = 0

    # ! check that jobtitle and location have been found 
    
    stageOnePoints = testPoints1 + testPoints2

    if (stageOnePoints == 2) or (stageOnePoints > 2):

        # continue with other checks
        # add candidate to job / search list
        #print("checkForVars) location and jobtitle matched")

    
        # 3) keyword search - list_variables, creatOptSearchField

        if (list_variables) and (creatOptSearchField):

            testPoints3 = applyCheck(list_variables, creatOptSearchField, varPts)

        else: 
            #print("checkForVars) -£££££££££££ list_variables and creatOptSearchField not found")
            testPoints3 = 0

        # 4) firm search - best to search roll-up field (creatOptSearchField) instead of currFirm

        if (FIRMList) and (creatOptSearchField):

            testPoints4 = applyCheck(FIRMList, creatOptSearchField, firmPts)

        else: 
            #print("checkForVars) -£££££££££££ list_variables and currFirm not found")
            testPoints4 = 0

        # 5) yrsExp 

        if (targetyrsexp) and (currYrsExp):

            testPoints5 = applyYrsCheck(targetyrsexp, currYrsExp, 0)


        else:
            #print("checkForVars) - no years experience found")
            testPoints5 = 0

        # 6) if nb of points is at least 2 then add candidate to job search

        finalPoints = (stageOnePoints + testPoints3 + testPoints4 + testPoints5)

        if (finalPoints > 2) or (finalPoints == 2):

            #print("checkForVars) points attained, add to joblist") # puts candidate in list of cands for job

            # cand = candidate ID
            # jobID = job ID 

            # add candidate to job list 

            addCand = addToJobList(cand, searchID, jobID, finalPoints, candName)

        else:
            print("checkForVars) points attained) not enough points, do nothing")    


    
    else: 
        # didn't meet criteria, return
        print("checkForVars) didn't meet criteria")


    
	#firms (text)
	
    #keyword (text) IMPORTANT
	#location = (text) IMPORTANT
	#if location = “paris” then pass in ile de France list
    
    
    
    
    
    
    # add candidate to specific search targetLocation
    
