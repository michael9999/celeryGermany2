from getStrapiApi import *
from addStrapi import *

def addCandLanguages(testDate):

    # set array of work experiences
    langIds = []

    nb = len(testDate["languages"]);
    print("buildSendEducation) ", nb);

    # get all languages from Strapi

    Url = "https://strapi-1oni.onrender.com/"
    langUrl = "cand-languages"

    getAllLangs = getStrapiApi(Url, langUrl)

    # put all strapi languages in object

    langObj = {}

    for lang in getAllLangs:

        langObj[lang["name"]] = lang["id"]

    #for i in nb:
    for i in range(0, nb):

        print("***********************running loop nb: ", i)

        langToAdd = {}

        langToAdd["name"] = testDate["languages"][i]

    # check if Language is already in strapi DB

        if langToAdd["name"] in langObj.keys():

            print("Language already in DB, get id")

            langIds.append(langObj[langToAdd["name"]])

        else:

            print("language not found, add to Strapi")

            targetUrl = "https://strapi-1oni.onrender.com/cand-languages"

            goApi = addStrapiApi(targetUrl, langToAdd)

            langIds.append(goApi["id"])


    return langIds

# Add languages to candidate profi