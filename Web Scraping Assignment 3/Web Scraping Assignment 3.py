#!/usr/bin/env python
# coding: utf-8
WEB SCRAPING ASSIGNMENT 3 - EXCEPTION HANDLING
# In[280]:


import selenium
import pandas as pd
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings
warnings.filterwarnings('ignore')


# In[281]:


driver = webdriver.Chrome(r"C:\Users\adwit\Downloads\chromedriver_win32\chromedriver.exe")


# --------------------------------------------------------------------------------------------------------------------------

# QUESTION 1

# In[62]:


driver.get("http://www.amazon.in/")


# In[63]:


product = input('Enter Product Name: ')
print('Product entered is: ',product)


# In[64]:


item1 = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
item1.send_keys(product)


# In[65]:


search1 = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
search1.click()


# -----------------------------------------------------------------------------------------------------------------------------

# QUESTION 2

# In[66]:


brand = []
prod_name = []
price = []
ret_ex = []
delivery = []
available = []
url = []


# In[67]:


start = 0
end = 2
for page in range(start,end):
    try:
        url_tags = driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
        for i in url_tags:
            url.append(i.get_attribute('href'))
        next_button = driver.find_element(By.XPATH,'//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
        next_button.click()
        time.sleep(5)
        
    except NoSuchElementException as e:
        print('Exception Raised:',e)
        url.append('No URL')


# In[68]:


for i in url:
    driver.get(i)
    time.sleep(10)
    
    #Brand Name
    try:
        brand_tags = driver.find_elements(By.XPATH,'//span[@class="a-size-base po-break-word"]')
        for i in brand_tags[0:1]:
            brand.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Raised: ',e)
        brand.append('No Data')
        
    
    #Product Name
    try:
        product_tags = driver.find_elements(By.XPATH,'//span[@class="a-size-large product-title-word-break"]')
        for i in product_tags:
            prod_name.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Raised: ',e)
        prod_name.append('No Data')

        
    #Price
    try:
        price_tags = driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
        for i in price_tags[0:1]:
            price.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Raised: ',e)
        price.append('No Data') 
        
        
        
    #Return-Exchange
    try:
        ret_ex_tags = driver.find_elements(By.XPATH,'//a[@class="a-size-small a-link-normal a-text-normal"]')
        for i in ret_ex_tags[2:3]:
            ret_ex.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Raised: ',e)
        ret_ex.append('No Data')
        
        
    #delivery
    try:
        delivery_tags = driver.find_elements(By.XPATH,'//span[@class="a-text-bold"]')
        for i in delivery_tags[0:1]:
            delivery.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Raised: ',e)
        delivery.append('No Data')
        
        
    #availability
    try:
        available_tags = driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-success"]')
        for i in available_tags:
            available.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Raised: ',e)
        available.append('No Data')
        


# In[69]:


print(len(url),len(brand),len(prod_name),len(price),len(ret_ex),len(delivery),len(available))


# Unequal lengths in lists

# In[71]:


amazon_search = pd.DataFrame({'Product Name':prod_name,'Brand':brand,'URL':url,'Price':price,'Delivery':delivery,'Availability':available[0:124]})
amazon_search


# In[72]:


amazon_search.to_csv(r"C:\Users\adwit\OneDrive\Desktop\amazon_search4.csv")


# --------------------------------------------------------------------------------------------------------------------------

# QUESTION 3

# In[24]:


driver.get('https://www.google.co.in/imghp?hl=en&tab=ri&ogbl')


# In[25]:


image_list = ['fruits','cars','Machine Learning','Guitar','Cake']


# In[30]:


fruits = []
cars = []
machine_learning = []
guitar = []
cake = []

all_images = []
for i in image_list:
    
    try:
        driver.get('https://www.google.co.in/imghp?hl=en&tab=ri&ogbl')
        time.sleep(2)
        image_search = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        image_search.send_keys(i)
        time.sleep(2)
        search3 = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button/div/span")
        search3.click()
    
        image_tags = driver.find_elements(By.XPATH,'//img[@class="rg_i Q4LuWd"]')
        for i in image_tags[0:10]:
            all_images.append(i.get_attribute('src'))
            
    except NoSuchElementException as e:
        all_images.append('No Image')


# In[33]:


fruits = all_images[0:10]
cars = all_images[10:20]
machine_learning = all_images[20:30]
guitar = all_images[30:40]
cake = all_images[40:50]


# In[34]:


image_df = pd.DataFrame({'Fruits':fruits,'Cars':cars,'Machine Learning':machine_learning,'Guitar':guitar,'Cake':cake})
image_df


# -------------------------------------------------------------------------------------------------------------------------------

# QUESTION 4

# In[77]:


driver.get('http://www.flipkart.com/')


# In[78]:


time.sleep(5)
cross_login = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/button")
cross_login.click()


# SEARCHING FOR ONEPLUS NORD

# In[79]:


item4 = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
item4.send_keys('oneplus nord')


# In[80]:


search4 = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
search4.click()


# In[81]:


purl = []


# In[86]:


try:
    purl_tags = driver.find_elements(By.XPATH,'//a[@class="_1fQZEK"]')
    for i in purl_tags:
        purl.append(i.get_attribute('href'))
    
        
except NoSuchElementException as e:
    print('Exception Raised:',e)
    purl.append('No URL')


# In[123]:


brand = []
name = []
colour = []
ram = []
rom = []
p_camera = []
display = []
battery = []
price = []


# In[124]:


for i in purl:
    driver.get(i)
    time.sleep(5)
    read_more = driver.find_element(By.XPATH,'//button[@class="_2KpZ6l _1FH0tX"]')
    read_more.click
    time.sleep(2)
    #Brand Name
    try:
        brand_tags4 = driver.find_elements(By.XPATH,'//span[@class="B_NuCI"]')
        for i in brand_tags4:
            brand.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Raised: ',e)
        brand.append('No Data')
        
    
    #Model Name
    try:
        name_tags4 = driver.find_elements(By.XPATH,'//li[@class="_21lJbe"]')
        for i in name_tags4[2:3]:
            name.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Raised: ',e)
        name.append('No Data')
        
        
    #Colour
    try:
        colour_tags4 = driver.find_elements(By.XPATH,'//li[@class="_21lJbe"]')
        for i in colour_tags4[3:4]:
            colour.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Raised: ',e)
        colour.append('No Data')
        
        
    #RAM
    try:
        ram_tags4 = driver.find_elements(By.XPATH,'//li[@class="_21Ahn-"]')
        for i in ram_tags4[0:1]:
            ram.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Raised: ',e)
        ram.append('No Data')
        
        
    #ROM
    try:
        rom_tags4 = driver.find_elements(By.XPATH,'//li[@class="_21Ahn-"]')
        for i in rom_tags4[0:1]:
            rom.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Raised: ',e)
        rom.append('No Data')
        
        
    #Primary Camera
    try:
        p_camera_tags4 = driver.find_elements(By.XPATH,'//li[@class="_21Ahn-"]')
        for i in p_camera_tags4[2:3]:
            p_camera.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Raised: ',e)
        p_camera.append('No Data')
    
        
        
    #Display Size
    try:
        display_tags4 = driver.find_elements(By.XPATH,'//li[@class="_21Ahn-"]')
        for i in display_tags4[1:2]:
            display.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Raised: ',e)
        display.append('No Data')
        
        
    #Battery Size
    try:
        battery_tags4 = driver.find_elements(By.XPATH,'//li[@class="_21Ahn-"]')
        for i in battery_tags4[3:4]:
            battery.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Raised: ',e)
        battery.append('No Data')
        
        
    #Price
    try:
        price_tags4 = driver.find_elements(By.XPATH,'//div[@class="_30jeq3 _16Jk6d"]')
        for i in price_tags4:
            price.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Raised: ',e)
        price.append('No Data')
        
        


# In[125]:


print(len(purl),len(brand),len(name),len(colour),len(ram),len(rom),len(p_camera),len(display),len(battery),len(price))


# Equal Lengths

# In[126]:


phone_df = pd.DataFrame({'Brand':brand,'Model Name':name,'Colour':colour,'RAM':ram,'ROM':rom,'Primary Camera':p_camera,'Display Size':display,'Price':price})
phone_df


# In[127]:


phone_df.to_csv(r"C:\Users\adwit\OneDrive\Desktop\phone_df.csv")


# ----------------------------------------------------------------------------------------------------------------------------

# QUESTION 5

# In[189]:


city = input('Enter City to be Searched: ')
print('City entered is: ',city)


# In[207]:


from selenium.webdriver.common.action_chains import ActionChains


# In[217]:


try:
    wait = WebDriverWait(driver,10)
    driver.get("https://www.google.com/maps/@28.6468495,77.3439278,15z")
    wait.until(EC.element_to_be_clickable((By.ID,"searchboxinput"))).send_keys(city)
    wait.until(EC.element_to_be_clickable((By.ID,"searchbox-searchbutton"))).click()
    time.sleep(5)
    ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//html/body")).context_click().perform()
    time.sleep(2)
    coordinate_tag = driver.find_elements(By.XPATH,'//div[@class="mLuXec"]')
    for i in coordinate_tag[0:1]:
        print(i.text)
except NoSuchElementException as e:
    print('Exception Raised:',e)
    print('Coordinate Not Found')


# -------------------------------------------------------------------------------------------------------------------------------

# QUESTION 6

# SKIPPED AS CONFIRMED ON TICKET - FUNDING DEALS TAB EMPTY ON trak.in

# -----------------------------------------------------------------------------------------------------------------------------

# QUESTION 7

# In[224]:


driver.get("https://www.digit.in/")


# In[225]:


gaming = driver.find_element(By.XPATH,"/html/body/div[2]/div/ul/li[5]/a")
gaming.click()


# In[226]:


search7 = driver.find_element(By.XPATH,"/html/body/div[2]/div/ul/li[5]/div[2]/div/div[2]/div/ul[3]/li[4]/a")
search7.click()


# In[227]:


search_best = driver.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div[11]/h2/a")
search_best.click()


# In[231]:


lurl = []


# In[232]:


try:
    lurl_tags = driver.find_elements(By.XPATH,'//a[@class="review spec"]')
    for i in lurl_tags:
        lurl.append(i.get_attribute('href'))
    
        
except NoSuchElementException as e:
    print('Exception Raised:',e)
    lurl.append('No URL')


# In[246]:


name = []
os = []
display = []
processor = []
memory = []


# In[247]:


for i in lurl:
    driver.get(i)
    time.sleep(5)

    #Laptop Name
    try:
        name_tags7 = driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[2]/h1")
        name.append(name_tags7.text)
            
    except NoSuchElementException as e:
        print('Exception Raised: ',e)
        name.append('No Data')
        
        
    #Operating System
    try:
        os_tags7 = driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[3]/div[2]/div[3]/div/ul/li[1]/div/p[2]/strong")
        os.append(os_tags7.text)
            
    except NoSuchElementException as e:
        print('Exception Raised: ',e)
        os.append('No Data')
        
        
    #Display Size
    try:
        display_tags7 = driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[3]/div[2]/div[3]/div/ul/li[2]/div/p[2]/strong")
        display.append(display_tags7.text)
            
    except NoSuchElementException as e:
        print('Exception Raised: ',e)
        display.append('No Data')
        
        
    #Processor
    try:
        processor_tags7 = driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[3]/div[2]/div[3]/div/ul/li[3]/div/p[2]/strong")
        processor.append(processor_tags7.text)
            
    except NoSuchElementException as e:
        print('Exception Raised: ',e)
        processor.append('No Data')
        
        
    #Memory
    try:
        memory_tags7 = driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[3]/div[2]/div[3]/div/ul/li[4]/div/p[2]/strong")
        memory.append(memory_tags7.text)
            
    except NoSuchElementException as e:
        print('Exception Raised: ',e)
        memory.append('No Data')


# In[248]:


print(len(name),len(os),len(display),len(processor),len(memory))


# In[249]:


best_laptops = pd.DataFrame({'Laptop Name':name,'Operating System':os,'Display Size':display,'Processor':processor,'Memory':memory})
best_laptops


# -------------------------------------------------------------------------------------------------------------------------------

# QUESTION 8

# In[252]:


driver.get("http://www.forbes.com/")


# In[255]:


options = driver.find_element(By.XPATH,'//div[@class="_69hVhdY4"]')
options.click()


# In[256]:


b1 = driver.find_element(By.XPATH,"/html/body/div[1]/header/nav/div[1]/div/div/div[2]/ul/li[1]/div[1]")
b1.click()


# In[257]:


b2 = driver.find_element(By.XPATH,"/html/body/div[1]/header/nav/div[1]/div/div/div[2]/ul/li[1]/div[2]/div[3]/ul/li[1]")
b2.click()


# In[258]:


rank = []
name = []
worth = []
age = []
citizen = []
source = []
industry = []


# In[261]:


start = 0
end = 13
loop = 0
for page in range(start,end):
    time.sleep(3)
    #RANK
    try:
        rank_tags = driver.find_elements(By.XPATH,'//div[@class="rank"]')
        for i in rank_tags:
            rank.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Found',e)
        rank.append('No Data')
        
        
    #Name
    try:
        name_tags8 = driver.find_elements(By.XPATH,'//div[@class="personName"]')
        for i in name_tags8:
            name.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Found',e)
        name.append('No Data')
        
        
    #Net Worth
    try:
        worth_tags = driver.find_elements(By.XPATH,'//div[@class="netWorth"]')
        for i in worth_tags:
            worth.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Found',e)
        worth.append('No Data')
        
        
    #Age
    try:
        age_tags = driver.find_elements(By.XPATH,'//div[@class="age"]')
        for i in age_tags:
            age.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Found',e)
        age.append('No Data')
        
        
    #Citizen
    try:
        citizen_tags = driver.find_elements(By.XPATH,'//div[@class="countryOfCitizenship"]')
        for i in citizen_tags:
            citizen.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Found',e)
        citizen.append('No Data')
        
        
    #Source
    try:
        source_tags = driver.find_elements(By.XPATH,'//span[@class="source-text"]')
        for i in source_tags:
            source.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Found',e)
        source.append('No Data')
        
        
    #Industry
    try:
        industry_tags = driver.find_elements(By.XPATH,'//div[@class="category"]')
        for i in industry_tags:
            industry.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Found',e)
        industry.append('No Data')
        
    if loop <13:
        next_button = driver.find_element(By.XPATH,'//div[@class="next-page"]')
        next_button.click()
        loop +=1
        
      


# In[262]:


print(len(rank),len(name),len(worth),len(age),len(citizen),len(source),len(industry))


# In[270]:


billionaires = pd.DataFrame({'Rank':rank,'Name':name,'Net Worth':worth,'Age':age,'Citizenship':citizen,'Source/Companies':source,'Industry/Industries':industry})
billionaires


# -----------------------------------------------------------------------------------------------------------------------------

# QUESTION 9

# USING RANDOM YOUTUBE VIDEO - SIDEMEN HOLIDAY

# In[271]:


driver.get("https://www.youtube.com/watch?v=5NxKNrfqUjs&t=4037s")


# In[272]:


comments = []
upvotes = []
time = []


# In[273]:


#Comments
try:
    comments_tags = driver.find_elements(By.XPATH,'//yt-formatted-string[@class="style-scope ytd-comment-renderer"]')
    for i in comments_tags[0:500]:
        comments.append(i.text)
            
except NoSuchElementException as e:
    print('Exception Found',e)
    comments.append('No Data')
    
    
#Upvotes
try:
    upvotes_tags = driver.find_elements(By.XPATH,'//span[@class="style-scope ytd-comment-action-buttons-renderer"]')
    for i in upvotes_tags[0:500]:
        upvotes.append(i.text)
            
except NoSuchElementException as e:
    print('Exception Found',e)
    upvotes.append('No Data')
    
    
#Time It Was Posted
try:
    time_tags = driver.find_elements(By.XPATH,'//a[@class="yt-simple-endpoint style-scope yt-formatted-string"]')
    for i in time_tags[64:564]:
        time.append(i.text)
            
except NoSuchElementException as e:
    print('Exception Found',e)
    time.append('No Data')


# In[274]:


print(len(comments),len(upvotes),len(time))


# In[279]:


yt_comments = pd.DataFrame({'Comments':comments,'Upvotes':upvotes,'Time It Was Posted':time})
yt_comments


# --------------------------------------------------------------------------------------------------------------------------

# QUESTION 10

# In[317]:


driver.get("https://www.hostelworld.com/")


# In[318]:


menu = driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div[2]/div/div/div[1]/header/div/button[2]")
menu.click()


# In[319]:


hostels = driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div[2]/div/div/div[1]/header/div[2]/div/div[2]/ul[2]/li[2]/a")
hostels.click()


# In[320]:


england = driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div/div[3]/ul/li[1]/div/ul/li[12]/a")
england.click()


# In[321]:


london = driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div/a")
london.click()


# In[322]:


search = driver.find_element(By.XPATH,'//button[@class="search-button"]')
search.click()


# In[323]:


hurl = []
name = []
distance = []
rating = []
tot_reviews = []
p_price = []
d_price = []


# In[325]:


start = 0
end = 1
loop = 0
for page in range(start,end):
    
    #PAGE URL
    try:
        hurl_tags = driver.find_elements(By.XPATH,'//a[@class="view-button"]')
        for i in hurl_tags:
            hurl.append(i.get_attribute('href'))
        
    except NoSuchElementException as e:
        print('Exception Raised:',e)
        hurl.append('No URL')
        
    
    #HOSTEL NAME
    try:
        name_tags10 = driver.find_elements(By.XPATH,'//h2[@class="title title-6"]')
        for i in name_tags10:
            name.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Found',e)
        name.append('No Data')
    
    
    #DISTANCE FROM CITY CENTRE
    try:
        dist_tags = driver.find_elements(By.XPATH,'//span[@class="description"]')
        for i in dist_tags:
            distance.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Found',e)
        distance.append('No Data')
        
        
        
    #RATING
    try:
        rating_tags10 = driver.find_elements(By.XPATH,'//div[@class="rating rating-summary-container big"]')
        for i in rating_tags10:
            rating.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Found',e)
        rating.append('No Data')
    
    
    #TOTAL REVIEWS
    try:
        rev_tags = driver.find_elements(By.XPATH,'//div[@class="reviews"]')
        for i in rev_tags:
            tot_reviews.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Found',e)
        tot_reviews.append('No Data')
    
    
    
    #PRIVATE ROOM PRICE
    try:
        priv_tags = driver.find_elements(By.XPATH,'//div[@class="price-col"]')
        for i in priv_tags[0::2]:
            p_price.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Found',e)
        p_price.append('No Data')
        
        
        
    #DORM ROOM PRICE
    try:
        dorm_tags = driver.find_elements(By.XPATH,'//div[@class="price-col"]')
        for i in dorm_tags[1::2]:
            d_price.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Found',e)
        d_price.append('No Data')
    
    
    
    if loop <1:
        next_button = driver.find_element(By.XPATH,'//div[@class="pagination-item pagination-next"]')
        next_button.click()
        loop +=1
        time.sleep(5)
        
   


# In[340]:


print(len(hurl),len(name),len(distance),len(rating),len(tot_reviews),len(p_price),len(d_price))


# In[335]:


facilities = []
description = []


# In[336]:


for i in hurl:
    driver.get(i)
    
    
    #Description
    try:
        desc_tags = driver.find_elements(By.XPATH,'//div[@class="content collapse-content"]')
        for i in desc_tags[0:1]:
            description.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Found',e)
        description.append('No Data')
        
        
    #Facilities
    try:
        fac_tags = driver.find_elements(By.XPATH,'//ul[@class="facilities"]')
        for i in fac_tags[0:1]:
            facilities.append(i.text)
            
    except NoSuchElementException as e:
        print('Exception Found',e)
        facilities.append('No Data')
        
        
    


# In[337]:


print(len(description),len(facilities))


# In[342]:


london_hostels = pd.DataFrame({'Hostel Name':name,'Distance From City Centre':distance,'Overall Rating':rating,'Total Reviews':tot_reviews,'Price for Private Room':p_price,'Price for Dorms':d_price,'Hostel Description':description,'Facilities':facilities})
london_hostels


# In[ ]:




