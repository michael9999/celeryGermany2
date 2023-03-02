from addStrapi import *
from prepareDate import *


def buildSendExperiences(testDate, candID):

    # set array of work experiences
    workIds = []

    nb = len(testDate["experiences"]);
    print("buildSendExperiences) ", nb);

    #print(testDate["experiences"][0])
    #for i in nb:
    for i in range(0, nb):

        print("buildSendExperiences) ***********************running loop nb: ", i)

        experienceToAdd = {}

    # check there is both a start and end date
        if testDate["experiences"][i]["starts_at"]:

            # "starts_at": {
            #        "day": null,
            #        "month": 11,
            #        "year": 2017
            #    },

            print("buildSendExperiences) printing month", testDate["experiences"][i]["starts_at"]["month"])

    # start date

            if testDate["experiences"][i]["starts_at"]["day"]:

                testDay = str(testDate["experiences"][i]["starts_at"]["day"])
                testMonth = str(testDate["experiences"][i]["starts_at"]["month"])
                testYear = str(testDate["experiences"][i]["starts_at"]["year"])
                textStartDate = testDay + "/" + testMonth + "/" + testYear
                print("buildSendExperiences) 1) full start date is", textStartDate)
                experienceToAdd["start"] = textStartDate

            else:

                testMonth = str(testDate["experiences"][i]["starts_at"]["month"])
                testYear = str(testDate["experiences"][i]["starts_at"]["year"])
                textStartDate = testMonth + "/" + testYear
                print("buildSendExperiences) 2) full start date is", textStartDate)
                experienceToAdd["start"] = textStartDate

    # end date
    # check if "end date" is a dictionary, if not, move to next
    # if = dictionary, build date as above
    # if isinstance(element, dict):
    # prepareDate(start, end) pass in "ends_at" object:

        if isinstance(testDate["experiences"][i]["ends_at"], dict) and isinstance(testDate["experiences"][i]["starts_at"], dict):

            print("buildSendExperiences) isinstance(testDate) - ends_at and starts_at present");
            print("buildSendExperiences) isinstance(testDate) starts_at ---------", testDate["experiences"][i]["starts_at"])
            print("buildSendExperiences) isinstance(testDate) ends_at ---------", testDate["experiences"][i]["ends_at"])

            experienceToAdd["duration"] = prepareDate(testDate["experiences"][i]["starts_at"], testDate["experiences"][i]["ends_at"])
            print("buildSendExperiences) Duration of experience: ****** ", experienceToAdd["duration"])

        if isinstance(testDate["experiences"][i]["ends_at"], dict):

            print("buildSendExperiences) This is a dictionary")
            print("buildSendExperiences) printing month ends at", testDate["experiences"][i]["ends_at"]["month"])
            testMonth = str(testDate["experiences"][i]["ends_at"]["month"])
            testYear = str(testDate["experiences"][i]["ends_at"]["year"])
            textEndDate = testMonth + "/" + testYear
            print("buildSendExperiences) full END date is", textEndDate)
            experienceToAdd["end"] = textEndDate

        else:
            print("No end date, put end date as Current")
            experienceToAdd["end"] = "Current"
            # continue

    # calculate duration of each experience
    # check if start and end are present and are both dictionaries/objects
    # if yes, pass to function to calculate duration


        if testDate["experiences"][i]["title"]:

            currJobTitle = testDate["experiences"][i]["title"]
            experienceToAdd["jobtitle"] = currJobTitle
            print(experienceToAdd)

    # if no job title, add "not provided", needed for main cand search

        else:
            experienceToAdd["jobtitle"] = "Not provided"

        if testDate["experiences"][i]["company"]:

            currCompany = testDate["experiences"][i]["company"]
            experienceToAdd["company_name"] = currCompany
            print(experienceToAdd)

        else:
            experienceToAdd["company_name"] = "Not provided";


        if testDate["experiences"][i]["description"]:

            currDescription = testDate["experiences"][i]["description"]
            experienceToAdd["job_descriptions"] = str(currDescription)
            print(experienceToAdd)

        else:
            experienceToAdd["job_descriptions"] = "Not provided"

        if testDate["experiences"][i]["location"]:

            currlocation = testDate["experiences"][i]["location"]
            experienceToAdd["locations"] = str(currlocation)
            print(experienceToAdd)

    # Send to strapi

        print("buildSendExperiences) @@@@@@@@@@@@@@@@@@@ - PRINT FINAL DATA TO ADD @@@@@@@@@@@@@@@@@@@", experienceToAdd)

    # Add to Strapi educations here

    # https://strapi-public-test.herokuapp.com/admin/educations
    # def addStrapiApi(airUrl, payload):

        targetUrl = "https://strapi-1oni.onrender.com/work-histories"
        
        # addStrapiApi(strapiUrl, payload)
        goApi = addStrapiApi(targetUrl, experienceToAdd)

        #workIds.append(goApi["id"])
        workIds.append(goApi["id"]) # candID

    # add generic work experience

    # workIds.append("3362")

    return workIds

# Works,