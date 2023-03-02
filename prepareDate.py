def prepareDate(start, end):

    from dateutil.relativedelta import relativedelta
    import datetime

    # see what we've received

    # assume there is a month and year

    # check if there is a day
        # use try block
        # try:
              # print(x)
          # except:
              # print("Something went wrong")
    try:
        if start["day"] and end['day']:

            print(" 1 - BBBBBBBBBBBBBBB - start[day] and end[day]")
            print("day is assigned continue")
            startDate = datetime.datetime(start["year"], start["month"], start["day"])
            endDate = datetime.datetime(end["year"], end["month"], end["day"])

            duration = relativedelta(endDate, startDate)
            # print("if start[day] and end[day]) testing duration: ", duration.days)
            print("if start[day] and end[day]) testing duration: ", duration.days)

    # check if startDate is identical to endDate
        # if yes, change end["day"] to 30


    # if no "day" assigned set defaults

        else:
            print(" 2 - BBBBBBBBBBBBBBB - ELSE start[day] and end[day]")
            start["day"] = 1
            end["day"] = 30

            print(" 3 - BBBBBBBBBBBBBBB - else) default day assigned")
            startDate = datetime.datetime(start["year"], start["month"], start["day"])
            endDate = datetime.datetime(end["year"], end["month"], end["day"])

    # check if start month and year == end month and year
    # if this is the case set duration to 1 month

            if start["year"] == end["year"] and start["month"] == end["month"]:

                print(" 4 - BBBBBBBBBBBBBBB - if start[year] == end[year] and start[month] == end[month]")

                # duration = relativedelta(endDate, startDate)
                duration.months = 1

# prob could be here

            else:

                print(" 5 - BBBBBBBBBBBBBBB - ELSE - if start[year] == end[year] and start[month] == end[month]")

                duration = relativedelta(endDate, startDate)
                print("else) testing duration: ", duration)

# no day found or error, add my own day

    except:

        print(" 6 - BBBBBBBBBBBBBBB - EXCEPT")

        start["day"] = 1
        end["day"] = 30
        start["month"] = 1
        end["month"] = 1

        print(" 7 - BBBBBBBBBBBBBBB - else) default day assigned")
        startDate = datetime.datetime(start["year"], start["month"], start["day"])
        endDate = datetime.datetime(end["year"], end["month"], end["day"])

        duration = relativedelta(endDate, startDate)
        print("else) testing duration: ", duration)

# if duration is less than 1 month then return "less than one month"
# if years and months are set then convert to years

    if duration.years and not duration.months:

        print("only years present")
        duration = duration.years

    elif duration.months and not duration.years:

        print("only months present")
        duration = duration.months / 12
        duration = round(duration, 1)

    elif duration.years and duration.months:

        print("months and years present")

        # convert months to years
        monthsToYears = duration.months / 12
        duration = monthsToYears + duration.years
        duration = round(duration, 1)

    elif not duration.years and not duration.months:
        duration = duration.days

    return duration