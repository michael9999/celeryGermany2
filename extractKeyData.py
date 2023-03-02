def extractKeyData(test):

    print("extractKeyData): data passed in, ", test)

    dataToAdd = " "

    if test["notes"]:
        dataToAdd = dataToAdd + ", " + test["notes"]
        #print(dataToAdd)

    if test["name"]:
        dataToAdd = dataToAdd + ", " + test["name"]
        #print(dataToAdd)

    if test["company"]:
        dataToAdd = dataToAdd + ", " + test["company"]
        #print(dataToAdd)

    if test["job_title"]:
        dataToAdd = dataToAdd + ", " + test["job_title"]
        #print(dataToAdd)

    # deal with work history

    for x in test["work_histories"]:

        #print(x["jobtitle"])
        #print(x["job_descriptions"])
        #print(x["company_name"])

        if x["jobtitle"]:

            dataToAdd = dataToAdd + ", " + x["jobtitle"]

        if x["job_descriptions"]:

            dataToAdd = dataToAdd + ", " + x["job_descriptions"]

        if x["company_name"]:

            dataToAdd = dataToAdd + ", " + x["company_name"]

    #print("work history loop finished: ", dataToAdd)

    # deal with skills

    if test["skills"]:

        for x in test["skills"]:


            #print(x["skill"])
            if x["skill"]:

                dataToAdd = dataToAdd + ", " + x["skill"]

    #print("skills loop finished: ", dataToAdd)

    # deal with education

    if test["educations"]:

        for x in test["educations"]:

            #print(x["school_name"])
            #print(x["description"])
            #print(x["qualification_name"])

            if x["school_name"]:

                dataToAdd = dataToAdd + ", " + x["school_name"]

            if x["description"]:

                dataToAdd = dataToAdd + ", " + x["description"]

            if x["qualification_name"]:

                dataToAdd = dataToAdd + ", " + x["qualification_name"]

    #print("education loop finished: ", dataToAdd)

    return dataToAdd