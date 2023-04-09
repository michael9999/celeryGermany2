def prepareDate(start, end):

    from dateutil.relativedelta import relativedelta
    import datetime

    # see what we've received

    print("prepareDate) Running")

    # assume there is a month and year

    # check if there is a day
        # use try block
        # try:
              # print(x)
          # except:
              # print("Something went wrong")
    try:
        if start["day"] and end['day']:

            print("prepareDate) 1 - BBBBBBBBBBBBBBB - start[day] and end[day]")
            print("prepareDate) day is assigned continue")
            startDate = datetime.datetime(start["year"], start["month"], start["day"])
            endDate = datetime.datetime(end["year"], end["month"], end["day"])

            duration = relativedelta(endDate, startDate)
            # print("if start[day] and end[day]) testing duration: ", duration.days)
            print("prepareDate) if start[day] and end[day]) testing duration: ", duration.days)

    # check if startDate is identical to endDate
        # if yes, change end["day"] to 30


    # if no "day" assigned set defaults

        else:
            print("prepareDate) 2 - BBBBBBBBBBBBBBB - ELSE start[day] and end[day]")
            start["day"] = 1
            end["day"] = 30

            print("prepareDate) 3 - BBBBBBBBBBBBBBB - else) default day assigned")
            startDate = datetime.datetime(start["year"], start["month"], start["day"])
            endDate = datetime.datetime(end["year"], end["month"], end["day"])

    # check if start month and year == end month and year
    # if this is the case set duration to 1 month

            if start["year"] == end["year"] and start["month"] == end["month"]:

                print("prepareDate) 4 - BBBBBBBBBBBBBBB - if start[year] == end[year] and start[month] == end[month]")

                # duration = relativedelta(endDate, startDate)
                duration.months = 1

# prob could be here

            else:

                print("prepareDate) 5 - BBBBBBBBBBBBBBB - ELSE - if start[year] == end[year] and start[month] == end[month]")

                duration = relativedelta(endDate, startDate)
                print("prepareDate) else) testing duration: ", duration)

# no day found or error, add my own day

    except:

        print("prepareDate) 6 - BBBBBBBBBBBBBBB - EXCEPT")

        start["day"] = 1
        end["day"] = 30
        start["month"] = 1
        end["month"] = 1

        print("prepareDate) 7 - BBBBBBBBBBBBBBB - else) default day assigned")
        startDate = datetime.datetime(start["year"], start["month"], start["day"])
        endDate = datetime.datetime(end["year"], end["month"], end["day"])

        duration = relativedelta(endDate, startDate)
        print("prepareDate) else) testing duration: ", duration)

# if duration is less than 1 month then return "less than one month"
# if years and months are set then convert to years

    if duration.years and not duration.months:

        print("prepareDate) only years present")
        duration = duration.years

        print("prepareDate) 1 final duration: ", duration)

    elif duration.months and not duration.years:

        print("prepareDate) only months present")
        duration = duration.months / 12
        duration = round(duration, 1)

        print("prepareDate) 2 final duration: ", duration)

    elif duration.years and duration.months:

        print("prepareDate) months and years present")

        # convert months to years
        monthsToYears = duration.months / 12
        duration = monthsToYears + duration.years
        duration = round(duration, 1)

        print("prepareDate) 3 final duration: ", duration)

    elif not duration.years and not duration.months:
        duration = duration.days

        print("prepareDate) 4 final duration: ", duration)

    print("prepareDate) ********************** FINAL DURATION BEFORE RETURN: ", duration)

    return duration