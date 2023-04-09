def init():
    global myList
    global currStrapiUrl
    global tokenid
    import os

    # main site
    #tokenid = os.getenv('TOKEN_ID', "N{t[4AJHBa6]T@#$22")

    # local testing
    tokenid = os.getenv('TOKEN_ID', "team")

    currStrapiUrl = os.getenv('CELERY_URL', "http://localhost:1337/")

    myList = []
    # local
    #currStrapiUrl = "http://localhost:1337/"
    # live
    # currStrapiUrl = "https://strapi-1oni.onrender.com/"

