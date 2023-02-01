#!/usr/bin/env python
# coding: utf-8

# WEB SCRAPING ASSIGNMENT 4

# In[175]:


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


# In[176]:


driver = webdriver.Chrome(r"C:\Users\adwit\Downloads\chromedriver_win32\chromedriver.exe")


# -----------------------------------------------------------------------------------------------------------------------------

# QUESTION 1

# In[3]:


driver.get("https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos")


# In[56]:


rank = []
name = []
artist = []
date = []
views = []


# In[57]:


#RANK
try:
    rank_tags = driver.find_elements(By.XPATH,'//td[@align="center"]')
    for i in rank_tags[0:23:3]:
        rank.append(i.text)
    for i in rank_tags[23:24]:
        rank.append(i.text)
    for i in rank_tags[26:37:3]:
        rank.append(i.text)
    for i in rank_tags[37:71:2]:
        rank.append(i.text)
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    rank.append('No Data')
        
        
#NAME
try:
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[1]/td[2]/a")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[2]/td[2]/a")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[3]/td[2]/a")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[4]/td[2]")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[5]/td[2]/a")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[6]/td[2]/a")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[7]/td[2]")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[8]/td[2]")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[9]/td[2]/a")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[10]/td[2]")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[11]/td[2]/a")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[12]/td[2]/i/a")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[13]/td[2]/a")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[14]/td[2]/a")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[15]/td[2]/a")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[16]/td[2]/a")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[17]/td[2]/a")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[18]/td[2]/a")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[19]/td[2]/a")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[20]/td[2]")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[21]/td[2]/a")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[22]/td[2]/a")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[23]/td[2]/a")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[24]/td[2]/a")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[25]/td[2]/a")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[26]/td[2]/a")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[27]/td[2]/a")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[28]/td[2]/a")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[29]/td[2]")
    for i in name_tags:
        name.append(i.text)
    name_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[30]/td[2]")
    for i in name_tags:
        name.append(i.text)
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    name.append('No Data')
    

#ARTIST
try:
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[1]/td[3]/a")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[2]/td[3]/a")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[3]/td[3]")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[4]/td[3]/a")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[5]/td[3]/a")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[6]/td[3]/a")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[7]/td[3]/a")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[8]/td[3]/a")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[9]/td[3]/a")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[10]/td[3]")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[11]/td[3]/a")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[12]/td[3]")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[13]/td[3]/a")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[14]/td[3]/a")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[15]/td[3]/a")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[16]/td[3]/a")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[17]/td[3]/a")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[18]/td[3]/a")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[19]/td[3]/a")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[20]/td[3]/a")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[21]/td[3]/a")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[22]/td[3]/a")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[23]/td[3]/a")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[24]/td[3]/a")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[25]/td[3]/a")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[26]/td[3]/a")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[27]/td[3]/a")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[28]/td[3]/a")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[29]/td[3]")
    for i in artist_tags:
        artist.append(i.text)
    artist_tags = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/table[2]/tbody/tr[30]/td[3]")
    for i in artist_tags:
        artist.append(i.text)

except NoSuchElementException as e:
    print('Exception Raised: ',e)
    artist.append('No Data')
    

#UPLOAD DATE
try:
    date_tags = driver.find_elements(By.XPATH,'//td[@align="right"]')
    for i in date_tags[0:30]:
        date.append(i.text)
            
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    date.append('No Data')
        

#VIEWS
try:
    views_tags = driver.find_elements(By.XPATH,'//td[@align="center"]')
    for i in views_tags[1:24:3]:
        views.append(i.text)
    for i in views_tags[24:25]:
        views.append(i.text)
    for i in views_tags[27:38:3]:
        views.append(i.text)
    for i in views_tags[38:72:2]:
        views.append(i.text)
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    views.append('No Data')


# In[58]:


print(len(rank),len(name),len(artist),len(date),len(views))


# In[59]:


top_viewed_videos = pd.DataFrame({'RANK':rank,'NAME':name,'ARTIST':artist,'UPLOAD DATE':date,'VIEWS IN BILLIONS':views})
top_viewed_videos


# -------------------------------------------------------------------------------------------------------------------------------

# QUESTION 2

# In[63]:


driver.get("http://www.bcci.tv/")


# In[65]:


view_all = driver.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[2]/div/div[1]/div[2]/a")
view_all.click()


# In[66]:


time.sleep(2)
more = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/button")
more.click()


# In[74]:


title = []
series = []
place = []
date = []
time = []


# In[75]:


#TITLE
try:
    title_tags = driver.find_elements(By.XPATH,'//span[@class="matchOrderText ng-binding ng-scope"]')
    for i in title_tags:
        title.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    title.append('No Data')
    
    
#SERIES
try:
    series_tags = driver.find_elements(By.XPATH,'//span[@class="ng-binding"]')
    for i in series_tags:
        series.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    series.append('No Data')
    
    
#PLACE
try:
    place_tags = driver.find_elements(By.XPATH,'//span[@class="ng-binding ng-scope"]')
    for i in place_tags:
        place.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    place.append('No Data')
    
    
#DATE
try:
    date_tags = driver.find_elements(By.XPATH,'//h5[@class="ng-binding"]')
    for i in date_tags:
        date.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    date.append('No Data')
    
    
#TIME
try:
    time_tags = driver.find_elements(By.XPATH,'//h5[@class="text-right ng-binding"]')
    for i in time_tags:
        time.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    time.append('No Data')


# In[76]:


print(len(title),len(series),len(place),len(date),len(time))


# In[77]:


fixtures = pd.DataFrame({'Title':title,'Series':series,'Place':place,'Date':date,'Time':time})
fixtures


# ------------------------------------------------------------------------------------------------------------------------------

# QUESTION 3

# In[100]:


driver.get("http://statisticstimes.com/")


# In[101]:


from selenium.webdriver.common.action_chains import ActionChains


# In[102]:


ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[2]/div[2]")).context_click().perform()
ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[2]/div[2]/div/a[3]")).click().perform()


# In[103]:


gdp_page = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/ul/li[1]/a")
gdp_page.click()


# In[108]:


rank = []
state = []
gsdp1819 = []
gsdp1920 = []
share = []
gdp = []


# In[109]:


#RANK
try:
    rank_tags = driver.find_elements(By.XPATH,'//td[@class="data1"]')
    for i in rank_tags[0:33]:
        rank.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    rank.append('No Data')
    
    
#STATE
try:
    state_tags = driver.find_elements(By.XPATH,'//td[@class="name"]')
    for i in state_tags[0:33]:
        state.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    state.append('No Data')
    
    
#GSDP (18-19)
try:
    gsdp1819_tags = driver.find_elements(By.XPATH,'//td[@class="data sorting_1"]')
    for i in gsdp1819_tags[0:33]:
        gsdp1819.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    gsdp1819.append('No Data')
    
    
#GSDP (19-20)
try:
    gsdp1920_tags = driver.find_elements(By.XPATH,'//td[@class="data"]')
    for i in gsdp1920_tags[0:162:5]:
        gsdp1920.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    gsdp1920.append('No Data')
    
    
#SHARE
try:
    share_tags = driver.find_elements(By.XPATH,'//td[@class="data"]')
    for i in share_tags[1:163:5]:
        share.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    share.append('No Data')
    
    
#GDP
try:
    gdp_tags = driver.find_elements(By.XPATH,'//td[@class="data"]')
    for i in gdp_tags[2:164:5]:
        gdp.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    gdp.append('No Data')
    


# In[110]:


print(len(rank),len(state),len(gsdp1819),len(gsdp1920),len(share),len(gdp))


# In[112]:


indian_states_gdp = pd.DataFrame({'RANK':rank,'STATE':state,'GSDP (18-19)':gsdp1819,'GSDP (19-20)':gsdp1920,'SHARE':share,'GDP':gdp})
indian_states_gdp


# -------------------------------------------------------------------------------------------------------------------------------

# QUESTION 4

# In[114]:


driver.get("https://github.com/")


# In[115]:


menu = driver.find_element(By.XPATH,'//button[@class="js-details-target Button--link Button--medium Button d-lg-none color-fg-inherit p-1"]')
menu.click()


# In[117]:


open_source = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/button")
open_source.click()


# In[118]:


trending = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/div/ul[3]/li[3]/a")
trending.click()


# In[119]:


title = []
description = []
count = []
language = []


# In[120]:


#REPOSITORY TITLE
try:
    title_tags = driver.find_elements(By.XPATH,'//h1[@class="h3 lh-condensed"]')
    for i in title_tags:
        title.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    title.append('No Data')
    
    
#REPOSITORY DESCRIPTION
try:
    description_tags = driver.find_elements(By.XPATH,'//p[@class="col-9 color-fg-muted my-1 pr-4"]')
    for i in description_tags:
        description.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    description.append('No Data')
    
    
#CONTRIBUTER COUNT
try:
    count_tags = driver.find_elements(By.XPATH,'//a[@class="Link--muted d-inline-block mr-3"]')
    for i in count_tags[1::2]:
        count.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    count.append('No Data')
    

#LANGUAGE USED
try:
    lang_tags = driver.find_elements(By.XPATH,'//span[@class="d-inline-block ml-0 mr-3"]')
    for i in lang_tags:
        language.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    language.append('No Data')
   


# In[123]:


print(len(title),len(description),len(count),len(language))


# In[126]:


repositories = pd.DataFrame({'Repository Title':title,'Repositary Description':description,'Contributor Count':count,'Language Used':language})
repositories


# ------------------------------------------------------------------------------------------------------------------------------

# QUESTION 5

# In[129]:


driver.get("https://www.billboard.com/")


# In[131]:


charts = driver.find_element(By.XPATH,"/html/body/div[3]/header/div/div[2]/div/div/div[2]/div[2]/div/div/nav/ul/li[1]/a")
charts.click()


# In[133]:


top100 = driver.find_element(By.XPATH,"/html/body/div[3]/main/div[2]/div[1]/div[1]/div/div/div[3]/a")
top100.click()


# In[161]:


song = []
artist = []
lwrank = []
peak = []
weeks = []


# In[162]:


#SONG NAME
try:
    song_tags = driver.find_elements(By.XPATH,'//h3[@id="title-of-a-story"]')
    for i in song_tags[6:404:4]:
        song.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    song.append('No Data')
    
    
#ARTIST NAME
try:
    artist_tags_m = driver.find_element(By.XPATH,'//span[@class="c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet"]')
    artist.append(artist_tags_m.text)
    artist_tags = driver.find_elements(By.XPATH,'//span[@class="c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only"]')
    for i in artist_tags:
        artist.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    artist.append('No Data')
    
    
#LAST WEEK RANK
try:
    lwrank_tags_m = driver.find_element(By.XPATH,'//span[@class="c-label  a-font-primary-bold-l a-font-primary-m@mobile-max u-font-weight-normal@mobile-max lrv-u-padding-tb-050@mobile-max u-font-size-32@tablet"]')
    lwrank.append(lwrank_tags_m.text)
    lwrank_tags = driver.find_elements(By.XPATH,'//span[@class="c-label  a-font-primary-m lrv-u-padding-tb-050@mobile-max"]')
    for i in lwrank_tags[0:590:6]:
        lwrank.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    lwrank.append('No Data')
    


#PEAK RANK
try:
    peak_tags_m = driver.find_elements(By.XPATH,'//span[@class="c-label  a-font-primary-bold-l a-font-primary-m@mobile-max u-font-weight-normal@mobile-max lrv-u-padding-tb-050@mobile-max u-font-size-32@tablet"]')
    for i in peak_tags_m[1:2]:
        peak.append(i.text)
    peak_tags = driver.find_elements(By.XPATH,'//span[@class="c-label  a-font-primary-m lrv-u-padding-tb-050@mobile-max"]')
    for i in peak_tags[1:591:6]:
        peak.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    peak.append('No Data')
    
    
#WEEKS ON BOARD
try:
    weeks_tags_m = driver.find_elements(By.XPATH,'//span[@class="c-label  a-font-primary-bold-l a-font-primary-m@mobile-max u-font-weight-normal@mobile-max lrv-u-padding-tb-050@mobile-max u-font-size-32@tablet"]')
    for i in weeks_tags_m[2:3]:
        weeks.append(i.text)
    weeks_tags = driver.find_elements(By.XPATH,'//span[@class="c-label  a-font-primary-m lrv-u-padding-tb-050@mobile-max"]')
    for i in weeks_tags[2:592:6]:
        weeks.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    weeks.append('No Data')


# In[163]:


print(len(song),len(artist),len(lwrank),len(peak),len(weeks))


# In[165]:


billboard_top_100 = pd.DataFrame({'SONG NAME':song,'ARTIST':artist,'LAST WEEK RANK':lwrank,'PEAK RANK':peak,'WEEKS ON BOARD':weeks})
billboard_top_100


# --------------------------------------------------------------------------------------------------------------------------------

# QUESTION 6

# In[166]:


driver.get("https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare")


# In[171]:


book = []
author = []
sale = []
publisher = []
genre = []


# In[172]:


#BOOK NAME
try:
    book_tags = driver.find_elements(By.XPATH,'//td[@class="left"]')
    for i in book_tags[1::5]:
        book.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    book.append('No Data')
    
    
#AUTHOR NAME
try:
    author_tags = driver.find_elements(By.XPATH,'//td[@class="left"]')
    for i in author_tags[2::5]:
        author.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    author.append('No Data')
    
    
#VOLUME SALES
try:
    sale_tags = driver.find_elements(By.XPATH,'//td[@class="left"]')
    for i in sale_tags[3::5]:
        sale.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    sale.append('No Data')
    
    
    
#PUBLISHER NAME
try:
    publisher_tags = driver.find_elements(By.XPATH,'//td[@class="left"]')
    for i in publisher_tags[4::5]:
        publisher.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    publisher.append('No Data')
    
    
    
#GENRE
try:
    genre_tags = driver.find_elements(By.XPATH,'//td[@class="last left"]')
    for i in genre_tags:
        genre.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    genre.append('No Data')


# In[173]:


print(len(book),len(author),len(sale),len(publisher),len(genre))


# In[174]:


bestsellers = pd.DataFrame({'BOOK NAME':book,'AUTHOR':author,'SALE':sale,'PUBLISHER':publisher,'GENRE':genre})
bestsellers


# -------------------------------------------------------------------------------------------------------------------------------

# QUESTION 7

# In[177]:


driver.get("http://www.imdb.com/list/ls095964455/")


# In[208]:


name = []
year = []
genre = []
runtime = []
rating = []
votes = []


# In[209]:


#TV SHOW NAME
try:
    name_tags = driver.find_elements(By.XPATH,'//h3[@class="lister-item-header"]')
    for i in name_tags:
        name.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    name.append('No Data')
    
year = [i.split('(')[1] for i in name]
year = [i.split(')')[0] for i in year]
name = [i.split('.')[1] for i in name]
name = [i.split('(')[0] for i in name]
    
  
    
#TV SHOW GENRE
try:
    genre_tags = driver.find_elements(By.XPATH,'//span[@class="genre"]')
    for i in genre_tags:
        genre.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    genre.append('No Data')
    
    
#RUNTIME
try:
    runtime_tags = driver.find_elements(By.XPATH,'//span[@class="runtime"]')
    for i in runtime_tags:
        runtime.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    runtime.append('No Data')
    
    
#TV SHOW RATING
try:
    rating_tags = driver.find_elements(By.XPATH,'//span[@class="ipl-rating-star__rating"]')
    for i in rating_tags[0:2280:23]:
        rating.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    rating.append('No Data')
    
    
#VOTES
try:
    votes_tags = driver.find_elements(By.XPATH,'//span[@name="nv"]')
    for i in votes_tags:
        votes.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    votes.append('No Data')


# In[210]:


print(len(name),len(year),len(genre),len(runtime),len(rating),len(votes))


# In[211]:


most_watched_tv_shows = pd.DataFrame({'TV SHOW NAME':name,'YEAR SPAN':year,'GENRE':genre,'RUNTIME':runtime,'RATING':rating,'VOTES':votes})
most_watched_tv_shows


# -----------------------------------------------------------------------------------------------------------------------------

# QUESTION 8

# In[212]:


driver.get("https://archive.ics.uci.edu/")


# In[214]:


view_all = driver.find_element(By.XPATH,"/html/body/table[1]/tbody/tr/td[2]/span[2]")
view_all.click()


# In[221]:


name = []
dtype = []
task = []
atype = []
instances = []
attributes = []
year = []


# In[222]:


#DATASET NAME
try:
    name_tags = driver.find_elements(By.XPATH,'//p[@class="normal"]')
    for i in name_tags[8:4357:7]:
        name.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    name.append('No Data')
    
    
#DATASET TYPE
try:
    dtype_tags = driver.find_elements(By.XPATH,'//p[@class="normal"]')
    for i in dtype_tags[9:4358:7]:
        dtype.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    dtype.append('No Data')
    
    
#TASK
try:
    task_tags = driver.find_elements(By.XPATH,'//p[@class="normal"]')
    for i in task_tags[10:4359:7]:
        task.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    task.append('No Data')
    
    
#ATTRIBUTE TYPE
try:
    atype_tags = driver.find_elements(By.XPATH,'//p[@class="normal"]')
    for i in atype_tags[11:4360:7]:
        atype.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    atype.append('No Data')
    
    
#INSTANCES
try:
    instances_tags = driver.find_elements(By.XPATH,'//p[@class="normal"]')
    for i in instances_tags[12:4361:7]:
        instances.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    instances.append('No Data')
    
    
#ATTRIBUTES
try:
    attributes_tags = driver.find_elements(By.XPATH,'//p[@class="normal"]')
    for i in attributes_tags[13:4362:7]:
        attributes.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    attributes.append('No Data')
    
    
#YEAR
try:
    year_tags = driver.find_elements(By.XPATH,'//p[@class="normal"]')
    for i in year_tags[14:4363:7]:
        year.append(i.text)
        
except NoSuchElementException as e:
    print('Exception Raised: ',e)
    year.append('No Data')


# In[223]:


print(len(name),len(dtype),len(task),len(atype),len(instances),len(attributes),len(year))


# In[224]:


uci_datasets = pd.DataFrame({'Dataset Name':name,'Dataset Type':dtype,'Task':task,'Attribute Type':atype,'Instances':instances,'Attributes':attributes,'Year':year})
uci_datasets


# ------------------------------------------------------------------------------------------------------------------------------
