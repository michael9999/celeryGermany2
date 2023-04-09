    # Choose query via variable
import sys
import requests, json

    # 31/07/2019

# split string up based on how site returns data
# valueToCheck = data we are searching in
# listToCheck = data we are looking for
# returns "found" or "not found"

def applyCheck(listToCheck, valueToCheck, pointsComp):

    # set points to zero

    listLower = [item.lower() for item in listToCheck]

    #print("applyCheck) check that the list is lower case")
    #print(listLower)

    # itext, jurl

    linkedinLower = valueToCheck.lower()
    #print("applyCheck) check if everything is lowercase")
    #print(linkedinLower)


    for itemB in listLower:
        if itemB in linkedinLower:
            #print("applyCheck) KW MATCH FOUND")
            #print(linkedin_all)
            #print("applyCheck) MATCH ON " + itemB + " in : " + linkedinLower)

            result = "found"
            pointsComp += 1
            #pointsComp = pointsComp
            break
            #maxPoints = int(maxPoints)
            #age_int = int(age)
            # give points
            #pointsComp += maxPoints
            #print("points KW1 after KW1 check : ")
            #print(pointsComp)
            # send to Airtables ?

        else:
            #print("applyCheck) no match on KW one")
            result = "not found"
            #pointsComp = pointsComp
            pointsComp = 0



    return pointsComp
