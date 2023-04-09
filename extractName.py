import sys
import requests, json

    # 31/07/2019

# split string up based on how site returns data
# function requires a search name, url, query, search tab & search value

def formatName(searchEngine, Cname2):

    if searchEngine == "linkedin":

        #print("url target is Linkedin")

        # use a function here to get firstname and surname
        searchType = "linkedin"
        Cname3 = Cname2.split(' -')[0]
        CnameFinal = Cname3.strip()
        #print("this is the stripped candidate name")
        #print(CnameFinal)

        # check name is made up of 2 names, if 2 then proceed

    elif searchEngine == "viadeo":
        #Edouard Merlin (France) | Viadeo
        #print("target is viadeo")
        searchType = "viadeo"
        #Cname3 = Cname2.split(' ')[1]
        #CnameFinal = Cname3.strip()
        #print("this is the stripped candidate name (viadeo)")
        #print(CnameFinal)

        firstname = Cname2.split(' ', 3)[0]
        surname = Cname2.split(' ', 3)[1]

        Cname3 = firstname + " " + surname
        #CnameFinal = Cname3.strip()

        #finalCount = len(Cname3.split())

        #print("here's the number of names in the string")
        #print(Cname3)

        #print("this is the stripped candidate name (viadeo)")
        CnameFinal = Cname3


    else:
        #print("$$$$$$$$$$$$$$$$ target not recognised **********************")
        searchType = "not recognised"


    #Cname = itext.split(' -')[0]
    #Cname = Cname.strip()

    # check name is made up of 2 names, if 2 then proceed

    #finalCount = len(Cname.split())


    return CnameFinal