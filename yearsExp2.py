import datetime
from dateutil.relativedelta import relativedelta

def YearsExp(yrStart, mnthStart, dyStart, yrEnd, mnthEnd, dyEnd):


    print("yearsExp2) started")
    totalDurationYrs = 0
    totalDurationMnths = 0        
    
    response = {}

    startDate = datetime.datetime(yrStart, mnthStart, dyStart)
    endDate = datetime.datetime(yrEnd, mnthEnd, dyEnd)


    duration = relativedelta(endDate, startDate)

    #print("YearsExp) - duration is -  ", duration)

# 3 possibilities
# a. months only
# b. years only
# c. months and years

    if duration.months and duration.years:

        print("YearsExp2) - months and years")
        #print(duration.months)

# convert to string

        stringMonth = str(duration.months)
        stringYear = str(duration.years)

# convert string to int

        durationMonth = int(stringMonth)
        durationYear = int(stringYear)

        response["type"] = "months & years"
        response["nbmonths"] = durationMonth
        response["nbyears"] = durationYear

        # str(difDate.years) + '.' + str(difDate.months)
        # duration = int(float(finalDate))
        # print("is this an int? ", duration)

    elif duration.months:

        print("YearsExp2) - months only ran")
# convert date to string

        stringDate = str(duration.months)
        #print("before conversion", stringDate)
        test2 = type(stringDate)
        #print("Type is: ", test2)

# convert string to int

        duration = int(stringDate)
        #print("months only) nb of months: ", stringDate)
        response["type"] = "months only"
        response["nbmonths"] = stringDate

    elif duration.years:

        print("YearsExp2) - years only ran")
        # convert date to string

        stringYear = str(duration.years)
        #print("before conversion", stringYear)
        test2 = type(stringYear)
        #print("Type is: ", test2)

# convert string to int

        duration = int(stringYear)
        #print("years only) nb of years: ", duration)
        response["type"] = "years only"
        response["nbyears"] = duration

# if no duration, identical date for start and finish, set duration to 0

    else:

        print("YearsExp2) No duration: ", duration)
        response["type"] = "No duration"
        response["nbyears"] = 0


    return response