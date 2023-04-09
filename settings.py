def init():
    global myList
    global currStrapiUrl
    global tokenid
    global api_key
    global serp_api_key
    import os

    # main site
    #tokenid = os.getenv('TOKEN_ID', "N{t[4AJHBa6]T@#$22")

    # Strapi
    tokenid = os.getenv('TOKEN_ID', "team")
    

    # Starpi URL
    currStrapiUrl = os.getenv('CELERY_URL', "http://localhost:1337/")
    

    # Proxy curl
    api_key = os.getenv('PROXY_CURL', "http://localhost:1337/")
    

    # Serpapi SERPAPI_KEY
    serp_api_key = os.getenv('SERPAPI_KEY', "http://localhost:1337/")
    

    myList = []
    # local
    #currStrapiUrl = "http://localhost:1337/"
    # live
    # currStrapiUrl = "https://strapi-1oni.onrender.com/"

