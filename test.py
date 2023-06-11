# Full trial 3 - HERE

# click on all pages, 1 by 1 - WORKS

for li in li_list:
    await page.evaluate('element => element.scrollIntoView()', li)
    
    print("this is run nb %%%%% : ")
    random_number = random.randint(2000, 3000)
    print(random_number)
    await page.wait_for_timeout(random_number)
    
    await li.dispatch_event('click')
    
    random_number = random.randint(2000, 3000)
    print(random_number)
    #await page.wait_for_timeout(random_number)
    
    try:
        await li.click()
        
        random_number = random.randint(4000, 5000)
        print(random_number)
        await page.wait_for_timeout(random_number)
        
        # get data here
        
        #- jobtitle, = OK
        
        await page.wait_for_selector("div.jobsearch-JobInfoHeader-title-container h2")
        jobtitle = page.locator('div.jobsearch-JobInfoHeader-title-container h2')
        jobtitleText = await jobtitle.text_content()
        print(jobtitleText)
        
        # - company name = OK 
            
        # try with div 
        await page.wait_for_selector('div.jobsearch-CompanyInfoContainer div[data-company-name = "true"]')
        companySearch = page.locator('div.jobsearch-CompanyInfoContainer div[data-company-name = "true"]')
        countSpan = await companySearch.count()

        print(countSpan)
            
        for i in range(countSpan):
           
            if (i == 0):

                text = await companySearch.nth(0).text_content()
        
                finalCompany = text 

                print("company name: ", finalCompany)
                
                
            else:
                print("no company info found")
            
        
        # - full job description
        
        description = await page.query_selector('div#jobDescriptionText')
        des2 = await description.text_content()
        print("full job description: ", des2)
            
        
        # - get job ID 
        
        span_element = await page.query_selector('span[data-indeed-apply-jobid]')
        job_id = await span_element.get_attribute('data-indeed-apply-jobid')
        print("unique job ID is: ", job_id)
        
        
        # - get Apply URL
        
        span_element2 = await page.query_selector('span[data-indeed-apply-joburl]')
        job_url = await span_element2.get_attribute('data-indeed-apply-joburl')

        print("job url is: ", job_url)
        
        
         #    - location etc... = OK
         
        company_location = await li.query_selector('div.companyLocation')
    
        location_text = await company_location.text_content()
        print("job location is: ", location_text)
            
        
        #    - salary & type of post, = OK
        
        try:
    
            spans = page.locator('div#salaryInfoAndJobType>span')
    
            countSpan = await spans.count()
    
            print("nb of spans found: ", countSpan)
    
            if(countSpan > 1):
        
                print("salary should be present")
        
                # get salary
        
                for i in range(countSpan):
           
                    if (i == 0):

                        text = await spans.nth(0).text_content()
                        print("salary: ", text)
                        finalSalary = text
                        text = await spans.nth(1).text_content()
                        finalContractType = text
                        print("contract: ", text)
            
            elif (countSpan == 1): # Assume contract type
                
                text = await spans.nth(0).text_content()
                print("contract type: ", text)
                finalContractType = text
                
                
                
            else:
                
                print("more than I expected, shit")

        except:
    
            print("(2) no salary present (div#salaryInfoAndJobType>span)")    
        
        
        
        #    - apply link

    
        random_number = random.randint(2000, 3000)
        print(random_number)
        await page.wait_for_timeout(random_number)
        print("--------------------- END --------------------")
        
    except:
        continue
# ---------- click on next page

# ------------------------------

links = page.locator('a[data-testid="pagination-page-next"]')
count = await links.count()
print(count)
if(count > 0):
    
    # loop through all jobs on 1st page
    
    #new_page = page.locator('a[data-testid="pagination-page-next"]')
    #go = await new_page.click()
    i = 0
    
    while page.query_selector('a[data-testid="pagination-page-next"]'):
        
        i = i + 1 
        
        if(i > 2):
            break
        
        else: 
            print("select found")
            new_page = page.locator('a[data-testid="pagination-page-next"]')
            go = await new_page.click()
            
            random_number = random.randint(2000, 3000)
            print(random_number)
            await page.wait_for_timeout(random_number)
            
            li_list = await page.locator('ul.jobsearch-ResultsList>li').element_handles()
    
            for li in li_list:
                await page.evaluate('element => element.scrollIntoView()', li)
    
                print("this is run nb %%%%% : ")
                random_number = random.randint(2000, 3000)
                print(random_number)
                await page.wait_for_timeout(random_number)
    
                await li.dispatch_event('click')
    
                random_number = random.randint(2000, 3000)
                print(random_number)
    #await page.wait_for_timeout(random_number)
    
                try:
                    await li.click()
        
                    random_number = random.randint(4000, 5000)
                    print(random_number)
                    await page.wait_for_timeout(random_number)
        
                    # get data here
        
                    #- jobtitle, = OK
        
                    await page.wait_for_selector("div.jobsearch-JobInfoHeader-title-container h2")
                    jobtitle = page.locator('div.jobsearch-JobInfoHeader-title-container h2')
                    jobtitleText = await jobtitle.text_content()
                    print(jobtitleText)
        
                    # - company name = OK 
            
                    # try with div 
                    await page.wait_for_selector('div.jobsearch-CompanyInfoContainer div[data-company-name = "true"]')
                    companySearch = page.locator('div.jobsearch-CompanyInfoContainer div[data-company-name = "true"]')
                    countSpan = await companySearch.count()

                    print(countSpan)
            
                    for i in range(countSpan):
           
                        if (i == 0):

                            text = await companySearch.nth(0).text_content()
        
                            finalCompany = text 

                            print("company name: ", finalCompany)
                
                
                        else:
                            print("no company info found")
            
        
                    # - full job description
        
                    description = await page.query_selector('div#jobDescriptionText')
                    des2 = await description.text_content()
                    print("full job description: ", des2)
            
        
                    # - get job ID 
        
                    span_element = await page.query_selector('span[data-indeed-apply-jobid]')
                    job_id = await span_element.get_attribute('data-indeed-apply-jobid')
                    print("unique job ID is: ", job_id)
        
        
                    # - get Apply URL
        
                    span_element2 = await page.query_selector('span[data-indeed-apply-joburl]')
                    job_url = await span_element2.get_attribute('data-indeed-apply-joburl')

                    print("job url is: ", job_url)
        
        
                    #    - location etc... = OK
         
                    company_location = await li.query_selector('div.companyLocation')
    
                    location_text = await company_location.text_content()
                    print("job location is: ", location_text)
            
        
                    #    - salary & type of post, = OK
        
                    try:
    
                        spans = page.locator('div#salaryInfoAndJobType>span')
    
                        countSpan = await spans.count()
    
                        print("nb of spans found: ", countSpan)
    
                        if(countSpan > 1):
        
                            print("salary should be present")
        
                        # get salary
        
                            for i in range(countSpan):
           
                                if (i == 0):

                                    text = await spans.nth(0).text_content()
                                    print("salary: ", text)
                                    finalSalary = text
                                    text = await spans.nth(1).text_content()
                                    finalContractType = text
                                    print("contract: ", text)
            
                        elif (countSpan == 1): # Assume contract type
                
                            text = await spans.nth(0).text_content()
                            print("contract type: ", text)
                            finalContractType = text
                
                
                
                        else:
                
                            print("more than I expected, shit")

                    except:
    
                        print("(2) no salary present (div#salaryInfoAndJobType>span)")    
        
        
        
        #    - apply link

                except:
                    continue
    
                random_number = random.randint(2000, 3000)
                print(random_number)
                await page.wait_for_timeout(random_number)
                print("--------------------- END --------------------")
        
            
# ---------- click on next page
        
        
        # loop through all jobs on selected page
        
        
    
else:
    print("no target")
    