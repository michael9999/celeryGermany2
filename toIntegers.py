# convert dates to integers
def toIntegers(toInt):

    intsConverted = {}

    if isinstance(toInt, dict):

        for i in toInt:

            # need a try catch here for Non dictionary values
            try:
                intsConverted[i] = int(toInt[i])

            except:
                intsConverted[i] = 1

    #print("print from toIntegers")
    #print(intsConverted)

    return intsConverted