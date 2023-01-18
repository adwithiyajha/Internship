#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[42]:


import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import warnings
warnings.filterwarnings('ignore')


# In[68]:


driver = webdriver.Chrome(r"C:\Users\adwit\Downloads\chromedriver_win32\chromedriver.exe")


# ----------------------------------------------------------------------------------------------------------------------------

# QUESTION 1

# In[18]:


driver.get("http://www.naukri.com/")


# In[19]:


designation1 = driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[1]/div/div/div/input")
designation1.send_keys('Data Analyst')


# In[20]:


location1 = driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location1.send_keys('Bangalore')


# In[21]:


search1 = driver.find_element(By.CLASS_NAME,"qsbSubmit")
search1.click()


# In[22]:


job_title1 = []
job_location1 = []
company_name1 = []
experience1 = []


# In[24]:


#Title Name
title_tags1 = driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags1[0:10]:
    title1 = i.text
    job_title1.append(title1)
    
#Location Name
location_tags1 = driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags1[0:10]:
    location1 = i.text
    job_location1.append(location1)
    
#Company Name
company_tags1 = driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags1[0:10]:
    company1 = i.text
    company_name1.append(company1)
    
#Experience Required
experience_tags1 = driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags1[0:10]:
    exp1 = i.text
    experience1.append(exp1)


# In[25]:


Data_Analyst = pd.DataFrame({'Title':job_title1,'Location':job_location1,'Company Name':company_name1,'Experience Required':experience1})
Data_Analyst


# -----------------------------------------------------------------------------------------------------------------------------

# QUESTION 2

# In[26]:


driver.get("http://www.naukri.com/")


# In[27]:


designation2 = driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[1]/div/div/div/input")
designation2.send_keys('Data Scientist')


# In[28]:


location2 = driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location2.send_keys('Bangalore')


# In[29]:


search2 = driver.find_element(By.CLASS_NAME,"qsbSubmit")
search2.click()


# In[30]:


job_title2 = []
job_location2 = []
company_name2 = []
experience2 = []


# In[31]:


#Title Name
title_tags2 = driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags2[0:10]:
    title_2 = i.text
    job_title2.append(title_2)
    
#Location Name
location_tags2 = driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags2[0:10]:
    location_2 = i.text
    job_location2.append(location_2)
    
#Company Name
company_tags2 = driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags2[0:10]:
    company_2 = i.text
    company_name2.append(company_2)
    
#Experience Required
experience_tags2 = driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags2[0:10]:
    exp2 = i.text
    experience2.append(exp2)


# In[32]:


Data_Scientist = pd.DataFrame({'Title':job_title2,'Location':job_location2,'Company Name':company_name2,'Experience Required':experience2})
Data_Scientist


# ------------------------------------------------------------------------------------------------------------------------------

# QUESTION 3

# In[33]:


driver.get("http://www.naukri.com/")


# In[34]:


designation3 = driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[1]/div/div/div/input")
designation3.send_keys('Data Scientist')


# In[35]:


search3 = driver.find_element(By.CLASS_NAME,"qsbSubmit")
search3.click()


# In[36]:


filter_loc = driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[5]/div[2]/div[2]/label/i")
filter_loc.click()


# In[37]:


filter_sal = driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[6]/div[2]/div[2]/label/i")
filter_sal.click()


# In[38]:


job_title3 = []
job_location3 = []
company_name3 = []
experience3 = []


# In[39]:


#Title Name
title_tags3 = driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags3[0:10]:
    title_3 = i.text
    job_title3.append(title_3)
    
#Location Name
location_tags3 = driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags3[0:10]:
    location_3 = i.text
    job_location3.append(location_3)
    
#Company Name
company_tags3 = driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags3[0:10]:
    company_3 = i.text
    company_name3.append(company_3)
    
#Experience Required
experience_tags3 = driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags3[0:10]:
    exp3 = i.text
    experience3.append(exp3)


# In[40]:


Data_Scientist_Filtered = pd.DataFrame({'Title':job_title3,'Location':job_location3,'Company Name':company_name3,'Experience Required':experience3})
Data_Scientist_Filtered


# -----------------------------------------------------------------------------------------------------------------------------

# QUESTION 4

# In[44]:


driver.get("http://www.flipkart.com/")


# In[45]:


cross_login = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/button")
cross_login.click()


# In[46]:


item = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
item.send_keys('sunglasses')


# In[47]:


search4 = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
search4.click()


# In[48]:


brand4 = []
description4 = []
price4 = []
discount4 = []


# In[49]:


start = 0
end = 3
for page in range(start,end):
    brand_tags4 = driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in brand_tags4:
        brand4.append(i.text)
    description_tags4 = driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in description_tags4:
        description4.append(i.text)
    price_tags4 = driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in price_tags4:
        price4.append(i.text)
    discount_tags4 = driver.find_elements(By.XPATH,'//div[@class="_3Ay6Sb"]')
    for i in discount_tags4:
        discount4.append(i.text)
    next_button = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]")
    next_button.click()
    time.sleep(5)


# In[51]:


brand4 = brand4[0:100]
description4 = description4[0:100]
price4 = price4[0:100]
discount4 = discount4[0:100]


# In[52]:


sunglasses = pd.DataFrame({'Brand':brand4,'Description':description4,'Price':price4,'Flipkart Discount':discount4})
sunglasses


# ---------------------------------------------------------------------------------------------------------------------------

# QUESTION 5

# In[53]:


driver.get("https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART")


# In[54]:


rating = []
summary = []
full_review = []


# In[56]:


start = 0
end = 10
for page in range(start,end):
    rating_tags = driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
    for i in rating_tags:
        rating.append(i.text)
    summary_tags = driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
    for i in summary_tags:
        summary.append(i.text)
    full_review_tags = driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
    for i in full_review_tags:
        full_review.append(i.text)
    next_button5 = driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button5.click()
    time.sleep(3)


# In[60]:


iphone_reviews = pd.DataFrame({'Ratings':rating[0:100],'Review Summary':summary[0:100],'Full Review':full_review[0:100]})
iphone_reviews


# ----------------------------------------------------------------------------------------------------------------------------

# QUESTION 6

# In[61]:


driver.get("http://www.flipkart.com/")


# In[62]:


item = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
item.send_keys('sneakers')


# In[63]:


search6 = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
search6.click()


# In[64]:


brand6 = []
description6 = []
price6 = []


# In[65]:


start = 0
end = 3
for page in range(start,end):
    brand_tags6 = driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in brand_tags6:
        brand6.append(i.text)
    description_tags6 = driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in description_tags6:
        description6.append(i.text)
    price_tags6 = driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in price_tags6:
        price6.append(i.text)
    next_button6 = driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]")
    next_button6.click()
    time.sleep(3)


# In[67]:


sneakers = pd.DataFrame({'Brand':brand6[0:100],'Description':description6[0:100],'Price':price6[0:100]})
sneakers


# ----------------------------------------------------------------------------------------------------------------------------

# QUESTION 7

# In[84]:


driver.get("https://www.amazon.in/")


# In[85]:


item7 = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
item7.send_keys('Laptop')


# In[86]:


search7 = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
search7.click()


# In[87]:


filter7 = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[6]/li[13]/span/a/span")
filter7.click()


# In[97]:


title7 = []
rating7 = []
price7 = []


# In[98]:


#Title Name
title_tags7 = driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
for i in title_tags7[0:10]:
    title_7 = i.text
    title7.append(title_7)
    
#Location Name
rating_tags7 = driver.find_elements(By.XPATH,'//span[@class="a-icon-alt"]')
for i in rating_tags7[0:10]:
    rating_7 = i.text
    rating7.append(rating_7)
    
#Company Name
price_tags7 = driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
for i in price_tags7[0:10]:
    price_7 = i.text
    price7.append(price_7)


# In[99]:


amazon_laptops = pd.DataFrame({'Laptop Name':title7,'Laptop Rating':rating7,'Laptop Price':price7})
amazon_laptops


# ---------------------------------------------------------------------------------------------------------------------------

# QUESTION 8

# In[114]:


driver.get("http://www.azquotes.com/")


# In[115]:


top_quotes = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a")
top_quotes.click()


# In[116]:


quote = []
author = []
qtype = []


# In[117]:


start = 0
end = 10
loop = 0
for page in range(start,end):
    quote_tags = driver.find_elements(By.XPATH,'//a[@class="title"]')
    for i in quote_tags:
        quote.append(i.text)
    author_tags = driver.find_elements(By.XPATH,'//div[@class="author"]')
    for i in author_tags:
        author.append(i.text)
    qtype_tags = driver.find_elements(By.XPATH,'//div[@class="tags"]')
    for i in qtype_tags:
        qtype.append(i.text)
    if loop < 9:
        next_button8 = driver.find_element(By.XPATH,'//li[@class="next"]')
        next_button8.click()
        loop +=1
    time.sleep(3)


# In[121]:


top_quotes = pd.DataFrame({'Quote':quote,'Author':author,'Tupe of Quote':qtype})
top_quotes


# -----------------------------------------------------------------------------------------------------------------------------

# QUESTION 9

# In[122]:


driver.get("http://www.jagranjosh.com/")


# In[123]:


gk = driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[6]/div/div[1]/header/div[3]/ul/li[9]/a")
gk.click()


# In[124]:


prime = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div[10]/div/div/ul/li[2]/a")
prime.click()


# In[135]:


pname = []
life = []
term = []
remark = []


# In[136]:


#Prime Minister Name
pname_tags1 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[2]/td[2]/p/strong/a')
for i in pname_tags1:
    pname.append(i.text)
pname_tags2 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[3]/td[2]/p')
for i in pname_tags2:
    pname.append(i.text)
pname_tags3 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[4]/td[2]/p')
for i in pname_tags3:
    pname.append(i.text)
pname_tags4 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[5]/td[2]/p')
for i in pname_tags4:
    pname.append(i.text)
pname_tags5 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[6]/td[2]/p/strong/a')
for i in pname_tags5:
    pname.append(i.text)
pname_tags6 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[7]/td[2]/p')
for i in pname_tags6:
    pname.append(i.text)
pname_tags7 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[8]/td[2]/p')
for i in pname_tags7:
    pname.append(i.text)
pname_tags8 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[9]/td[2]/p/strong/a')
for i in pname_tags8:
    pname.append(i.text)
pname_tags9 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[10]/td[2]/p/a/strong')
for i in pname_tags9:
    pname.append(i.text)
pname_tags10 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[11]/td[2]/p')
for i in pname_tags10:
    pname.append(i.text)
pname_tags11 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[12]/td[2]/p/strong/a')
for i in pname_tags11:
    pname.append(i.text)
pname_tags12 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[13]/td[2]/p')
for i in pname_tags12:
    pname.append(i.text)
pname_tags13 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[14]/td[2]/p/strong/a')
for i in pname_tags13:
    pname.append(i.text)
pname_tags14 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[15]/td[2]/p')
for i in pname_tags14:
    pname.append(i.text)
pname_tags15 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[16]/td[2]/p')
for i in pname_tags15:
    pname.append(i.text)
pname_tags16 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[17]/td[2]/p/a/strong')
for i in pname_tags16:
    pname.append(i.text)
pname_tags17 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[18]/td[2]/p/strong/a')
for i in pname_tags17:
    pname.append(i.text)
pname_tags18 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[19]/td[2]/p/a/strong')
for i in pname_tags18:
    pname.append(i.text)

    
#Born-Death
life_tags1 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[2]/td[3]/p')
for i in life_tags1:
    life.append(i.text)
life_tags2 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[3]/td[3]/p')
for i in life_tags2:
    life.append(i.text)
life_tags3 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[4]/td[3]/p')
for i in life_tags3:
    life.append(i.text)
life_tags4 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[5]/td[3]/p')
for i in life_tags4:
    life.append(i.text)
life_tags5 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[6]/td[3]/p')
for i in life_tags5:
    life.append(i.text)
life_tags6 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[7]/td[3]/p')
for i in life_tags6:
    life.append(i.text)
life_tags7 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[8]/td[3]/p')
for i in life_tags7:
    life.append(i.text)
life_tags8 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[9]/td[3]/p')
for i in life_tags8:
    life.append(i.text)
life_tags9 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[10]/td[3]/p')
for i in life_tags9:
    life.append(i.text)
life_tags10 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[11]/td[3]/p')
for i in life_tags10:
    life.append(i.text)
life_tags11 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[12]/td[3]/p')
for i in life_tags11:
    life.append(i.text)
life_tags12 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[13]/td[3]/p')
for i in life_tags12:
    life.append(i.text)
life_tags13 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[14]/td[3]/p')
for i in life_tags13:
    life.append(i.text)
life_tags14 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[15]/td[3]/p')
for i in life_tags14:
    life.append(i.text)
life_tags15 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[16]/td[3]/p')
for i in life_tags15:
    life.append(i.text)
life_tags16 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[17]/td[3]/p')
for i in life_tags16:
    life.append(i.text)
life_tags17 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[18]/td[3]/p')
for i in life_tags17:
    life.append(i.text)
life_tags18 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[19]/td[3]/p')
for i in life_tags18:
    life.append(i.text)
    
#Term of Office
term_tags1 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[2]/td[4]/p[1]/span')
for i in term_tags1:
    term.append(i.text)
term_tags2 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[3]/td[4]/p[1]/span')
for i in term_tags2:
    term.append(i.text)
term_tags3 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[4]/td[4]/p[1]/span')
for i in term_tags3:
    term.append(i.text)
term_tags4 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[5]/td[4]/p[1]')
for i in term_tags4:
    term.append(i.text)
term_tags5 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[6]/td[4]/p[1]/span')
for i in term_tags5:
    term.append(i.text)
term_tags6 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[7]/td[4]/p[1]/span')
for i in term_tags6:
    term.append(i.text)
term_tags7 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[8]/td[4]/p[1]/span')
for i in term_tags7:
    term.append(i.text)
term_tags8 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[9]/td[4]/p[1]/span')
for i in term_tags8:
    term.append(i.text)
term_tags9 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[10]/td[4]/p[1]/span')
for i in term_tags9:
    term.append(i.text)
term_tags10 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[11]/td[4]/p[1]/span')
for i in term_tags10:
    term.append(i.text)
term_tags11 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[12]/td[4]/p[1]/span')
for i in term_tags11:
    term.append(i.text)
term_tags12 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[13]/td[4]/p[1]/span')
for i in term_tags12:
    term.append(i.text)
term_tags13 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[14]/td[4]/p[1]/span')
for i in term_tags13:
    term.append(i.text)
term_tags14 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[15]/td[4]/p[1]/span')
for i in term_tags14:
    term.append(i.text)
term_tags15 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[16]/td[4]/p[1]/span')
for i in term_tags15:
    term.append(i.text)
term_tags16 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[17]/td[4]/p[1]/span')
for i in term_tags16:
    term.append(i.text)
term_tags17 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[18]/td[4]/p[1]/span')
for i in term_tags17:
    term.append(i.text)
term_tags18 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[19]/td[4]/p/span')
for i in term_tags18:
    term.append(i.text)

    
#Remark
remark_tags1 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[2]/td[5]/p')
for i in remark_tags1:
    remark.append(i.text)
remark_tags2 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[3]/td[5]/p')
for i in remark_tags2:
    remark.append(i.text) 
remark_tags3 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[4]/td[5]/p')
for i in remark_tags3:
    remark.append(i.text)    
remark_tags4 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[5]/td[5]/p')
for i in remark_tags4:
    remark.append(i.text)    
remark_tags5 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[6]/td[5]/p')
for i in remark_tags5:
    remark.append(i.text)    
remark_tags6 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[7]/td[5]/p')
for i in remark_tags6:
    remark.append(i.text)    
remark_tags7 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[8]/td[5]/p')
for i in remark_tags7:
    remark.append(i.text)    
remark_tags8 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[9]/td[5]/p')
for i in remark_tags8:
    remark.append(i.text)    
remark_tags9 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[10]/td[5]/p')
for i in remark_tags9:
    remark.append(i.text)    
remark_tags10 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[11]/td[5]/p')
for i in remark_tags10:
    remark.append(i.text)    
remark_tags11 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[12]/td[5]/p')
for i in remark_tags11:
    remark.append(i.text)    
remark_tags12 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[13]/td[5]/p')
for i in remark_tags12:
    remark.append(i.text)    
remark_tags13 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[14]/td[5]/p')
for i in remark_tags13:
    remark.append(i.text)    
remark_tags14 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[15]/td[5]/p')
for i in remark_tags14:
    remark.append(i.text)    
remark_tags15 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[16]/td[5]/p')
for i in remark_tags15:
    remark.append(i.text)    
remark_tags16 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[17]/td[5]/p')
for i in remark_tags16:
    remark.append(i.text)    
remark_tags17 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[18]/td[5]/p')
for i in remark_tags17:
    remark.append(i.text)    
remark_tags18 = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[19]/td[5]/p')
for i in remark_tags18:
    remark.append(i.text)    


# In[139]:


prime_ministers = pd.DataFrame({'Prime Minister':pname,'Born-Death':life,'Term of Office':term,'Remarks':remark})
prime_ministers


# -----------------------------------------------------------------------------------------------------------------------------

# QUESTION 10

# In[140]:


driver.get("https://www.motor1.com/")


# In[144]:


time.sleep(10)
crossad = driver.find_element(By.XPATH,'/html/body/div[15]/div/div/div/div/div/div/button')
crossad.click()


# In[145]:


options = driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/div/div[1]/div')
options.click()


# In[146]:


features = driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[3]/ul/li[5]/button')
features.click()


# In[147]:


lists = driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[3]/ul/li[6]/ul/li[1]/a')
lists.click()


# In[148]:


exp_50 = driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div[1]/div[1]/div/div/div[9]/div/div[1]/h3/a')
exp_50.click()


# In[149]:


car_name = []


# In[150]:


#Car Name
car_tags1 = driver.find_elements(By.XPATH,'//h3[@class="subheader"]')
for i in car_tags1:
    car_name.append(i.text)


# In[153]:


most_expensive_cars = pd.DataFrame({'Car Name':car_name[0:50]})
most_expensive_cars


# In[ ]:




