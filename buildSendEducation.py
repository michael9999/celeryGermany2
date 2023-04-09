from prepareDate import *
from addStrapi import *

def buildSendEducation(testDate):

    # set array of work experiences
    educIds = []

    nb = len(testDate["education"])
    print("buildSendEducation) ", nb)

    #print(testDate["experiences"][0])
    #for i in nb:
    for i in range(0, nb):

        print("***********************running loop nb: ", i)

        educationToAdd = {}

    # check there is both a start and end date
        if testDate["education"][i]["starts_at"]:

            # "starts_at": {
            #        "day": null,
            #        "month": 11,
            #        "year": 2017
            #    },

            print("printing month", testDate["education"][i]["starts_at"]["month"])

    # start date

            if testDate["education"][i]["starts_at"]["day"]:

                testDay = str(testDate["education"][i]["starts_at"]["day"])
                testMonth = str(testDate["education"][i]["starts_at"]["month"])
                testYear = str(testDate["education"][i]["starts_at"]["year"])
                textStartDate = testDay + "/" + testMonth + "/" + testYear
                #print("1) full start date is", textStartDate)
                educationToAdd["start"] = textStartDate

            else:

                testMonth = str(testDate["education"][i]["starts_at"]["month"])
                testYear = str(testDate["education"][i]["starts_at"]["year"])
                textStartDate = testMonth + "/" + testYear
                #print("2) full start date is", textStartDate)
                educationToAdd["start"] = textStartDate

    # end date
    # check if "end date" is a dictionary, if not, move to next
    # if = dictionary, build date as above
    # if isinstance(element, dict):
    # prepareDate(start, end) pass in "ends_at" object:

        if isinstance(testDate["education"][i]["ends_at"], dict) and isinstance(testDate["education"][i]["starts_at"], dict):

            #print("isinstance(testDate) - ends_at and starts_at present");
            #print("isinstance(testDate) starts_at ---------", testDate["education"][i]["starts_at"])
            #print("isinstance(testDate) ends_at ---------", testDate["education"][i]["ends_at"])

            educationToAdd["duration"] = prepareDate(testDate["education"][i]["starts_at"], testDate["education"][i]["ends_at"])
            #print("Duration of experience: ****** ", educationToAdd["duration"])

        if isinstance(testDate["education"][i]["ends_at"], dict):

            #print("This is a dictionary")
            #print("printing month ends at", testDate["education"][i]["ends_at"]["month"])
            testMonth = str(testDate["education"][i]["ends_at"]["month"])
            testYear = str(testDate["education"][i]["ends_at"]["year"])
            textEndDate = testMonth + "/" + testYear
            #print("full END date is", textEndDate)
            educationToAdd["end"] = textEndDate

        else:
            continue

    # calculate duration of each experience
    # check if start and end are present and are both dictionaries/objects
    # if yes, pass to function to calculate duration

    #  "degree_name": "Master 2",
    #  "school": "Université Paris Nanterre",
    #  "description": "Thesis: Conciliation within the ICSIDInternship: SNCF

    #  "field_of_study": "International Commercial Law",
    #        "degree_name": "Master 2",
    #        "school": "Université Paris Nanterre",
    #        "description": "Thesis: Conciliation within the ICSIDInternship: SNCF


        if testDate["education"][i]["degree_name"]:

            currEducTitle = testDate["education"][i]["degree_name"]
            educationToAdd["qualification_name"] = currEducTitle
            #print(educationToAdd)

        else:
            educationToAdd["qualification_name"] = "Not provided"
# if degree name and school are present put them together

        if testDate["education"][i]["degree_name"] and testDate["education"][i]["field_of_study"]:

            currEducTitle = testDate["education"][i]["degree_name"] + " - " + testDate["education"][i]["field_of_study"]
            educationToAdd["qualification_name"] = currEducTitle
            #print(educationToAdd)


        if testDate["education"][i]["school"]:

            currSchool = testDate["education"][i]["school"]
            educationToAdd["school_name"] = currSchool
            #print(educationToAdd)

        else:
            educationToAdd["school_name"] = "Not provided"

        if testDate["education"][i]["description"]:

            currDescription = testDate["education"][i]["description"]
            educationToAdd["description"] = str(currDescription)
            #print(educationToAdd)

        else:
            educationToAdd["description"] = "Not provided"

    # Send to strapi

        #print("@@@@@@@@@@@@@@@@@@@ - PRINT FINAL DATA TO ADD @@@@@@@@@@@@@@@@@@@", educationToAdd)

    # Add to Strapi educations here

    # https://strapi-public-test.herokuapp.com/admin/educations
    # def addStrapiApi(airUrl, payload):

        #targetUrl = "https://strapi-1oni.onrender.com/educations"

        targetUrl = "educations"

        goApi = addStrapiApi(targetUrl, educationToAdd)

        educIds.append(goApi["id"])

    # TO DO: check if no education data, if none then add place holder

    #educIds.append("1834")

    return educIds

# Update Candidate function