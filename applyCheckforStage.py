    # Choose query via variable
import sys
import requests, json

    # 31/07/2019

# split string up based on how site returns data
# valueToCheck = data we are searching in
# listToCheck = data we are looking for
# returns "found" or "not found"

# testDate["experiences"][i] - object holding experiences

def applyCheckforStage(listToCheck, valueToCheck):


    print("applyCheckforStage) has started")

    # check what was passed in
    print("applyCheckforStage - 1) listToCheck : ", listToCheck)
    print("applyCheckforStage - 2) valueToCheck : ", valueToCheck)

    # build combined variable - jobtitle and job description applyCheckforStage

    if valueToCheck["title"]:

        print("applyCheckforStage - 2.1) title present : ", valueToCheck["title"])

    else:

        print("applyCheckforStage - 2.2) NO title present : ")
        valueToCheck["title"] = "not given"

    if valueToCheck["description"]:

        print("applyCheckforStage - 2.3) description present : ", valueToCheck["description"])

    else:

        print("applyCheckforStage - 2.4) NO description present : ")
        valueToCheck["description"] = "not given"  

    combinedExp = valueToCheck["title"] + " - " + valueToCheck["description"]

    print("applyCheckforStage - 2.5) combinedExp : ", combinedExp) # OK

    # print("applyCheckforStage - 3) combinedExp : ", combinedExp)

    # convert list of stage terms to lower
    listLower = [item.lower() for item in listToCheck]

    print("applyCheckforStage 2.6) check that the list is lower case : ", listLower)
    #print(listLower)

    # itext, jurl

    #linkedinLower = valueToCheck.lower()
    linkedinLower = combinedExp.lower()

    print("applyCheckforStage 2.7) check that the list2 is lower case : ", linkedinLower)
    #print("applyCheckforStage) check if everything is lowercase")
    #print(linkedinLower)


    for itemB in listLower:
        if itemB in linkedinLower:
            print("applyCheckforStage 2.8) KW MATCH FOUND")
            #print(linkedin_all)
            #print("applyCheckforStage) MATCH ON " + itemB + " in : " + linkedinLower)

            result = "found"
            #pointsComp = int(pointsComp)
            #maxPoints = int(maxPoints)
            #age_int = int(age)
            # give points
            #pointsComp += maxPoints
            #print("points KW1 after KW1 check : ")
            #print(pointsComp)
            # send to Airtables ?

        else:
            print("applyCheckforStage 2.9) no match on KW one")
            result = "not found"


    print("applyCheckforStage - 4) result: ", result)

    return result
