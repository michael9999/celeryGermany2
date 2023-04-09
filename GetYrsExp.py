from toIntegers import *
from yearsExp2 import *
from applyCheckforStage import *
from dateutil.relativedelta import relativedelta
from datetime import date

# testDate = experience object

def GetYrsExp(testDate, stageTerms):

    print("GetYrsExp) stageTerms ", stageTerms)
    nb = len(testDate["experiences"])
    print(nb)

    totalDurationYrs = 0
    totalDurationMnths = 0

    #print(testDate["experiences"][0])
    #for i in nb:
    for i in range(0, nb):

        print("GetYrsExp 1) ***********************running loop nb: ", i)

    # check there is both a start and end date
        if testDate["experiences"][i]["starts_at"]:

            #print(testDate["experiences"][i]["starts_at"])
            returnedStartInts = toIntegers(testDate["experiences"][i]["starts_at"])
            print("GetYrsExp 2) if testDate[experiences][i][starts_at]) test value of returnedStartInts", returnedStartInts)

            if isinstance(testDate["experiences"][i]["ends_at"], dict):

    # we have start and end dates

                print("GetYrsExp 3) if isinstance) end date is ", testDate["experiences"][i]["ends_at"], "- *****run nb***** - ", i)

    # convert date variables to integers
                returnedEndInts = toIntegers(testDate["experiences"][i]["ends_at"])

                print("GetYrsExp 4) Test returnedEndInts) ", returnedEndInts);

    # run calculate function

    # def YearsExp(yrStart, mnthStart, dyStart, yrEnd, mnthEnd, dyEnd):

                durationOne = YearsExp(returnedStartInts["year"], returnedStartInts["month"], returnedStartInts["day"], returnedEndInts["year"], returnedEndInts["month"], returnedEndInts["day"]);

                print("GetYrsExp 5) Just after YearsExp) Should be duration of each period of work ----- ", durationOne)

    # Handle years or months, if years = ok, if only months convert to years
    # years
                if durationOne["type"] == "months only":

                    print("GetYrsExp 6) if durationOne.month) running")

                    # convert to integer

                    durationOne["nbmonths"] = int(durationOne["nbmonths"])

                    #mnths = durationOne.month / 12;

                    #print(round(mnths, 1))

                    totalDurationMnths = durationOne["nbmonths"] + totalDurationMnths

                    print("GetYrsExp 7) IF months only) test duration of months - ", totalDurationMnths)
                    # totalDuration += durationOne.years

                elif durationOne["type"] ==  "months & years":

                    print("GetYrsExp 8) if durationOne.year) running")

                    totalDurationYrs = durationOne["nbyears"] + totalDurationYrs

            else:

                print("GetYrsExp) 9) NO end date found")

                today = date.today()

                print("GetYrsExp 10) Today's date:", today)

                # convert to string

                dateStr = today.strftime("%d %m %Y")

                newDate = dateStr.split(" ")

                # newDate ['05', '07', '2021']

                # convert today's date to integers

                tyear = int(newDate[2])
                tmonth = int(newDate[1])
                tday = int(newDate[0])

                returnedStartInts = toIntegers(testDate["experiences"][i]["starts_at"])

                durationOne = YearsExp(returnedStartInts["year"], returnedStartInts["month"], returnedStartInts["day"], tyear, tmonth, tday);

                print("GetYrsExp 11) durationOne is : )))))))))))))))))))))))))))))))) ", durationOne)


    # calculate based on date on which the entry was made
    # calculate total nb of years exp (all exps) by using difference between current date and date entry was added.

                # Handle years or months, if years = ok, if only months convert to years
    # years
                if durationOne["type"] == "months only":

                    print("GetYrsExp 12) if durationOne.month) running")

                    # convert to integer

                    durationOne["nbmonths"] = int(durationOne["nbmonths"])

                    #mnths = durationOne.month / 12;

                    #print(round(mnths, 1))

                    # !!!!!!! only do this if experience isn't an apprenticeship

                    testVar = applyCheckforStage(stageTerms, testDate["experiences"][i])

                    # check if "stage" term was found

                    if testVar == "found":

                        print("GetYrsExp 13) 'stage' term found, don't add to yrs exp")

                    else:    

                        # testDate["experiences"][i]["title"]
                        # testDate["experiences"][i]["description"]
                        print("GetYrsExp 14) 'stage' term NOT!! found, ADD to yrs exp")

                        totalDurationMnths = durationOne["nbmonths"] + totalDurationMnths

                        print("GetYrsExp 14) IF months only) test duration of months - ", totalDurationMnths)
                    # totalDuration += durationOne.years

                elif durationOne["type"] ==  "months & years":

                    print("GetYrsExp) months & years) running")


                    # applyCheck(listToCheck, valueToCheck)

                    # !!!!!!! only do this if experience isn't an apprenticeship

                    testVar = applyCheckforStage(stageTerms, testDate["experiences"][i])

                    # check if "stage" term was found

                    if testVar == "found":

                        print("GetYrsExp) 'stage' term found, don't add to yrs exp")

                    else:

                        print("GetYrsExp) 'stage' term NOT!! found, ADD to yrs exp")
                        totalDurationYrs = durationOne["nbyears"] + totalDurationYrs


        else:
            print("GetYrsExp 15) 2) NO start date found, continue")
            continue


    print("GetYrsExp 16) total yr tally -- ", totalDurationYrs)
    print("GetYrsExp 17) total months tally -- ", totalDurationMnths)

    totalDurationMnths = totalDurationMnths / 12

    totalDurationMnths = round(totalDurationMnths, 1)

    # value for "duration" field in Candidates table
    finalNbYears = totalDurationMnths + totalDurationYrs

    print("GetYrsExp 18) testing months converted to years * ", totalDurationMnths)
    print("GetYrsExp 19) TOTAL NB OF YRS : ", finalNbYears)

    if finalNbYears:
        finalNbYears = finalNbYears
    else:
        finalNbYears = 0

    return finalNbYears
