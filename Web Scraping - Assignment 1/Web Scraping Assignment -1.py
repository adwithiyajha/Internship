#!/usr/bin/env python
# coding: utf-8

# QUESTION 1

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page1 = requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[4]:


page1


# In[5]:


wik = BeautifulSoup(page1.content)
wik


# In[6]:


headers = wik.find_all(['h1','h2','h3','h4'])
print('List of all headers: ',*headers, sep='\n\n')


# ----------------------------------------------------------------------------------------------------------------------------

# QUESTION 2

# In[7]:


page2 = requests.get('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc')
page2


# In[8]:


imdb1 = BeautifulSoup(page2.content)
imdb1


# In[9]:


def get_movie_names(imdb1):
    selection_class = 'lister-item-header'
    movie_name_tags = imdb1.find_all('h3',{'class':selection_class})
    names1 = []
    
    for i in movie_name_tags:
        a = i.find('a').text
        names1.append(a)
        
    return names1
    


# In[10]:


names1 = get_movie_names(imdb1)


# In[11]:


names1


# In[12]:


len(names1)


# In[13]:


page2_1 = requests.get('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&start=51&ref_=adv_nxt')
page2_1


# In[14]:


imdb1_2 = BeautifulSoup(page2_1.content)
imdb1_2


# In[15]:


def get_movie_names2(imdb1_2):
    selection_class = 'lister-item-header'
    movie_name_tags = imdb1_2.find_all('h3',{'class':selection_class})
    names1_2 = []
    
    for i in movie_name_tags:
        a = i.find('a').text
        names1_2.append(a)
        
    return names1_2


# In[16]:


names1_2 = get_movie_names2(imdb1_2)


# In[17]:


names1_2


# In[18]:


names1 = names1 + names1_2


# In[19]:


names1


# In[20]:


year1 = []
for i in imdb1.find_all('span',class_="lister-item-year text-muted unbold"):
    year1.append(i.text)
    
year1


# In[21]:


year1_2 = []
for i in imdb1_2.find_all('span',class_="lister-item-year text-muted unbold"):
    year1_2.append(i.text)
    
year1_2


# In[22]:


year1 = year1 + year1_2
year1


# In[23]:


rating1 = []
for i in imdb1.find_all('strong'):
    rating1.append(i.text)
    
rating1


# In[24]:


rating1 = rating1[2:]

rating1


# In[25]:


rating1_2 = []
for i in imdb1_2.find_all('strong'):
    rating1_2.append(i.text)
    
rating1_2


# In[26]:


rating1_2 = rating1_2[2:]

rating1_2


# In[27]:


rating1 = rating1 + rating1_2

rating1


# In[28]:


len(names1)


# In[29]:


import pandas as pd

imdb_top100 = pd.DataFrame({'Name':names1, 'Rating':rating1, 'Year Of Release':year1})

imdb_top100


# ------------------------------------------------------------------------------------------------------------------------------

# QUESTION 3

# In[30]:


page3 = requests.get('https://www.imdb.com/list/ls056092300/')
page3


# In[31]:


imdb2 = BeautifulSoup(page3.content)
imdb2


# In[32]:


def get_movie_hindi(imdb2):
    selection_class = 'lister-item-header'
    movie_name_tags = imdb2.find_all('h3',{'class':selection_class})
    names2 = []
    
    for i in movie_name_tags:
        a = i.find('a').text
        names2.append(a)
        
    return names2


# In[33]:


names2 = get_movie_hindi(imdb2)


# In[34]:


names2


# In[35]:


year2 = []
for i in imdb2.find_all('span',class_="lister-item-year text-muted unbold"):
    year2.append(i.text)
    
year2


# In[36]:


rating2 = []
for i in imdb2.find_all('div',class_="ipl-rating-star small"):
    rating2.append(i.text)
    
rating2


# In[37]:


rating2 = [i.split('\n')[8] for i in rating2]

rating2


# In[38]:


len(rating2)


# In[39]:


imdb_top100_indian = pd.DataFrame({'Name':names2, 'Rating':rating2, 'Year Of Release':year2})

imdb_top100_indian


# ------------------------------------------------------------------------------------------------------------------------------

# QUESTION 4

# In[40]:


page4 = requests.get("https://presidentofindia.nic.in/former-presidents.htm")
page4


# In[41]:


pres = BeautifulSoup(page4.content)
pres


# In[42]:


pres_names = []
for i in pres.find_all('h3'):
    pres_names.append(i.text)
    
pres_names


# In[43]:


pres_terms = []
for i in pres.find_all('div',class_="presidentListing"):
    pres_terms.append(i.text)
    
pres_terms


# In[44]:


pres_term = [i.split('\n')[2] for i in pres_terms]

pres_term


# In[45]:


pres_term = [i.split(':')[1] for i in pres_term]

pres_term


# In[46]:


pres_list = pd.DataFrame({'President Names':pres_names,'Term of Office':pres_term})

pres_list


# ------------------------------------------------------------------------------------------------------------------------------

# QUESTION 5

# (a) Top 10 ODI Teams

# In[47]:


page5_1 = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
page5_1


# In[48]:


team = BeautifulSoup(page5_1.content)
team


# In[49]:


team_name = []
for i in team.find_all ('span',class_="u-hide-phablet"):
    team_name.append(i.text)
    
team_name = team_name[0:10]
team_name


# In[58]:


team_matches = []
for i in team.find_all('td',class_="rankings-block__banner--matches"):
    team_matches.append(i.text)
    
team_matches = team_matches[0:10]
team_matches


# In[59]:


team_matches2 = []

for i in team.find_all('td',class_="table-body__cell u-center-text"):
    team_matches2.append(i.text)
    
team_matches = team_matches + team_matches2[0:18]
team_matches


# In[60]:


team_matches.remove('3,400')
team_matches.remove('3,572')
team_matches.remove('4,238')
team_matches.remove('2,584')
team_matches.remove('2,392')
team_matches.remove('3,129')
team_matches.remove('2,858')
team_matches.remove('1,419')
team_matches.remove('2,902')
team_matches


# In[61]:


team_points = []
for i in team.find_all('td',class_="rankings-block__banner--points"):
    team_points.append(i.text)
    
team_points


# In[62]:


team_points2 = []

for i in team.find_all('td',class_="table-body__cell u-center-text"):
    team_points2.append(i.text)
    
team_points2 = team_points2[1:18]
team_points2


# In[63]:


team_points2.remove('32')
team_points2.remove('39')
team_points2.remove('24')
team_points2.remove('24')
team_points2.remove('33')
team_points2.remove('32')
team_points2.remove('20')
team_points2.remove('41')

team_points = team_points + team_points2
team_points


# In[64]:


team_rating = []
for i in team.find_all('td',class_="rankings-block__banner--rating u-text-right"):
    team_rating.append(i.text)

team_rating


# In[65]:


team_rating = [i.split('\n')[1] for i in team_rating]
team_rating = [i.split('                            ')[1] for i in team_rating]

team_rating


# In[66]:


team_rating2 = []
for i in team.find_all('td',class_="table-body__cell u-text-right rating"):
    team_rating2.append(i.text)

team_rating = team_rating+team_rating2[0:9]
team_rating


# In[67]:


odi_team_ranking = pd.DataFrame({'TEAM':team_name,'MATCHES':team_matches,'POINTS':team_points,'RATING':team_rating})

odi_team_ranking


# TOP 10 ODI BATSMEN

# In[68]:


page5_2 = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')
page5_2


# In[69]:


bat = BeautifulSoup(page5_2.content)
bat


# In[70]:


bat_name = []
for i in bat.find_all('div',class_="rankings-block__banner--name-large"):
    bat_name.append(i.text)
    
bat_name


# In[71]:


bat_name2 = []
for i in bat.find_all('td',class_="table-body__cell rankings-table__name name"):
    bat_name2.append(i.text)
    
bat_name2 = bat_name2[0:9]
bat_name2


# In[72]:


bat_name2= [i.split('\n')[1] for i in bat_name2]

bat_name2


# In[73]:


bat_name = bat_name + bat_name2

bat_name


# In[74]:


bat_team = []
for i in bat.find_all('div',class_="rankings-block__banner--nationality"):
    bat_team.append(i.text)
    
bat_team


# In[75]:


bat_team = [i.split('\n')[2] for i in bat_team]

bat_team


# In[76]:


bat_team2 = []
for i in bat.find_all('span',class_="table-body__logo-text"):
    bat_team2.append(i.text)
    
bat_team2 = bat_team2[0:9]
bat_team2


# In[77]:


bat_team = bat_team + bat_team2
bat_team


# In[78]:


bat_rating = []
for i in bat.find_all('div',class_="rankings-block__banner--rating"):
    bat_rating.append(i.text)
    
bat_rating


# In[79]:


bat_rating2 = []
for i in bat.find_all('td',class_="table-body__cell rating"):
    bat_rating2.append(i.text)
    
bat_rating2 = bat_rating2[0:9]
bat_rating2


# In[80]:


bat_rating = bat_rating + bat_rating2
bat_rating


# In[81]:


batsmen_ranking = pd.DataFrame({'Player Name':bat_name,'Team':bat_team,'Rating':bat_rating})
batsmen_ranking


# TOP 10 ODI BOWLERS

# In[82]:


page5_3 = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')
page5_3


# In[83]:


bowl = BeautifulSoup(page5_3.content)
bowl


# In[84]:


bowl_name = []
for i in bowl.find_all('div',class_="rankings-block__banner--name-large"):
    bowl_name.append(i.text)
    
bowl_name


# In[85]:


bowl_name2 = []
for i in bowl.find_all('td',class_="table-body__cell rankings-table__name name"):
    bowl_name2.append(i.text)
    
bowl_name2 = bowl_name2[0:9]
bowl_name2


# In[86]:


bowl_name2= [i.split('\n')[1] for i in bowl_name2]
bowl_name = bowl_name + bowl_name2

bowl_name


# In[87]:


bowl_team = []
for i in bowl.find_all('div',class_="rankings-block__banner--nationality"):
    bowl_team.append(i.text)
    
bowl_team = [i.split('\n')[2] for i in bowl_team]

bowl_team


# In[88]:


bowl_team2 = []
for i in bowl.find_all('span',class_="table-body__logo-text"):
    bowl_team2.append(i.text)
    
bowl_team2 = bowl_team2[0:9]
bowl_team = bowl_team + bowl_team2
bowl_team


# In[89]:


bowl_rating = []
for i in bowl.find_all('div',class_="rankings-block__banner--rating"):
    bowl_rating.append(i.text)
    
bowl_rating


# In[90]:


for i in bowl.find_all('td',class_="table-body__cell rating"):
    bowl_rating.append(i.text)
    
bowl_rating = bowl_rating[0:10]
bowl_rating


# In[91]:


bowler_ranking = pd.DataFrame({'Bowler Name':bowl_name,'Team':bowl_team,'Rating':bowl_rating})
bowler_ranking


# --------------------------------------------------------------------------------------------------------------------------------

# QUESTION 6

# (a) WOMEN'S ODI TEAM RANKING

# In[92]:


page6_1 = requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
page6_1


# In[93]:


wteam = BeautifulSoup(page6_1.content)
wteam


# In[94]:


wteam_name = []
for i in wteam.find_all ('span',class_="u-hide-phablet"):
    wteam_name.append(i.text)
    
wteam_name = wteam_name[0:10]
wteam_name


# In[95]:


wteam_matches = []
for i in wteam.find_all('td',class_="rankings-block__banner--matches"):
    wteam_matches.append(i.text)
    
wteam_matches = wteam_matches[0:10]
wteam_matches


# In[96]:


wteam_matches2 = []

for i in wteam.find_all('td',class_="table-body__cell u-center-text"):
    wteam_matches2.append(i.text)
    
wteam_matches = wteam_matches + wteam_matches2[0:17]
wteam_matches


# In[97]:


wteam_matches.remove('3,342')
wteam_matches.remove('3,098')
wteam_matches.remove('2,820')
wteam_matches.remove('2,553')
wteam_matches.remove('2,535')
wteam_matches.remove('983')
wteam_matches.remove('572')
wteam_matches.remove('1,519')
wteam_matches


# In[98]:


wteam_points = []
for i in wteam.find_all('td',class_="rankings-block__banner--points"):
    wteam_points.append(i.text)
    
wteam_points


# In[99]:


wteam_points2 = []

for i in wteam.find_all('td',class_="table-body__cell u-center-text"):
    wteam_points2.append(i.text)
    
wteam_points2 = wteam_points2[1:18]
wteam_points2


# In[100]:


wteam_points2.remove('26')
wteam_points2.remove('27')
wteam_points2.remove('25')
wteam_points2.remove('27')
wteam_points2.remove('13')
wteam_points2.remove('8')
wteam_points2.remove('24')
wteam_points2.remove('8')

wteam_points = wteam_points + wteam_points2
wteam_points


# In[101]:


wteam_rating = []
for i in wteam.find_all('td',class_="rankings-block__banner--rating u-text-right"):
    wteam_rating.append(i.text)

wteam_rating


# In[102]:


wteam_rating = [i.split('\n')[1] for i in wteam_rating]
wteam_rating = [i.split('                            ')[1] for i in wteam_rating]

wteam_rating


# In[103]:


wteam_rating2 = []
for i in wteam.find_all('td',class_="table-body__cell u-text-right rating"):
    wteam_rating2.append(i.text)

wteam_rating = wteam_rating+wteam_rating2[0:9]
wteam_rating


# In[104]:


women_team_ranking = pd.DataFrame({'TEAM':wteam_name,'MATCHES':wteam_matches,'POINTS':wteam_points,'RATING':wteam_rating})

women_team_ranking


# TOP 10 ODI WOMEN'S BATTING

# In[105]:


page6_2 = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')
page6_2


# In[106]:


wbat = BeautifulSoup(page6_2.content)
wbat


# In[107]:


wbat_name = []
for i in wbat.find_all('div',class_="rankings-block__banner--name-large"):
    wbat_name.append(i.text)
    
wbat_name


# In[108]:


wbat_name2 = []
for i in wbat.find_all('td',class_="table-body__cell rankings-table__name name"):
    wbat_name2.append(i.text)
    
wbat_name2 = wbat_name2[0:9]
wbat_name2


# In[109]:


wbat_name2= [i.split('\n')[1] for i in wbat_name2]

wbat_name = wbat_name + wbat_name2


# In[110]:


wbat_name


# In[111]:


wbat_team = []
for i in wbat.find_all('div',class_="rankings-block__banner--nationality"):
    wbat_team.append(i.text)
    
wbat_team


# In[112]:


wbat_team = [i.split('\n')[2] for i in wbat_team]

wbat_team


# In[113]:


wbat_team2 = []
for i in wbat.find_all('span',class_="table-body__logo-text"):
    wbat_team2.append(i.text)
    
wbat_team2 = wbat_team2[0:9]
wbat_team = wbat_team + wbat_team2
wbat_team


# In[114]:


wbat_rating = []
for i in wbat.find_all('div',class_="rankings-block__banner--rating"):
    wbat_rating.append(i.text)
    
wbat_rating


# In[115]:


wbat_rating2 = []
for i in wbat.find_all('td',class_="table-body__cell rating"):
    wbat_rating2.append(i.text)
    
wbat_rating2 = wbat_rating2[0:9]
wbat_rating2


# In[116]:


wbat_rating = wbat_rating + wbat_rating2
wbat_rating


# In[117]:


women_batsmen_ranking = pd.DataFrame({'Player Name':wbat_name,'Team':wbat_team,'Rating':wbat_rating})
women_batsmen_ranking


# TOP 10 ODI WOMEN'S BOWLERS

# In[118]:


page6_3 = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/bowling')
page6_3


# In[119]:


wbowl = BeautifulSoup(page6_3.content)
wbowl


# In[120]:


wbowl_name = []
for i in wbowl.find_all('div',class_="rankings-block__banner--name-large"):
    wbowl_name.append(i.text)
    
wbowl_name


# In[121]:


wbowl_name2 = []
for i in wbowl.find_all('td',class_="table-body__cell rankings-table__name name"):
    wbowl_name2.append(i.text)
    
wbowl_name2 = wbowl_name2[0:9]
wbowl_name2


# In[122]:


wbowl_name2= [i.split('\n')[1] for i in wbowl_name2]
wbowl_name = wbowl_name + wbowl_name2

wbowl_name


# In[123]:


wbowl_team = []
for i in wbowl.find_all('div',class_="rankings-block__banner--nationality"):
    wbowl_team.append(i.text)
    
wbowl_team = [i.split('\n')[2] for i in wbowl_team]

wbowl_team


# In[124]:


wbowl_team2 = []
for i in wbowl.find_all('span',class_="table-body__logo-text"):
    wbowl_team2.append(i.text)
    
wbowl_team2 = wbowl_team2[0:9]
wbowl_team = wbowl_team + wbowl_team2
wbowl_team


# In[125]:


wbowl_rating = []
for i in wbowl.find_all('div',class_="rankings-block__banner--rating"):
    wbowl_rating.append(i.text)
    
wbowl_rating


# In[126]:


for i in wbowl.find_all('td',class_="table-body__cell rating"):
    wbowl_rating.append(i.text)
    
wbowl_rating = wbowl_rating[0:10]
wbowl_rating


# In[127]:


women_bowler_ranking = pd.DataFrame({'Bowler Name':wbowl_name,'Team':wbowl_team,'Rating':wbowl_rating})
women_bowler_ranking


# -----------------------------------------------------------------------------------------------------------------------------

# QUESTION 7

# In[128]:


page7 = requests.get('https://www.cnbc.com/world/?region=world')
page7


# In[129]:


news = BeautifulSoup(page7.content)
news


# In[130]:


header = []
for i in news.find_all('div',class_="LatestNews-headlineWrapper"):
    header.append(i.text)
header


# In[131]:


headline = [i.split('Ago')[1] for i in header]

headline


# In[132]:


timestamp = [i.split('Ago')[0] for i in header]

timestamp


# In[176]:


link = []
for i in news.find_all('a',href=True):
    link.append(i['href'])
    
link    


# In[177]:


list = ['#MainContent',
 '//www.cnbc.com/world/',
 '/',
 '/markets/',
 '/pre-markets/',
 '/us-markets/',
 '/markets-europe/',
 '/china-markets/',
 '/markets-asia-pacific/',
 '/world-markets/',
 '/currencies/',
 '/cryptocurrency/',
 '/futures-and-commodities/',
 '/bonds/',
 '/funds-and-etfs/',
 '/business/',
 '/economy/',
 '/finance/',
 '/health-and-science/',
 '/media/',
 '/real-estate/',
 '/energy/',
 '/climate/',
 '/transportation/',
 '/industrials/',
 '/retail/',
 '/wealth/',
 '/life/',
 '/small-business/',
 '/investing/',
 '/personal-finance/',
 '/fintech/',
 '/financial-advisors/',
 '/options-action/',
 '/etf-street/',
 'https://buffett.cnbc.com',
 '/earnings/',
 '/trader-talk/',
 '/technology/',
 '/cybersecurity/',
 '/enterprise/',
 '/internet/',
 '/media/',
 '/mobile/',
 '/social-media/',
 '/cnbc-disruptors/',
 '/tech-guide/',
 '/politics/',
 '/white-house/',
 '/policy/',
 '/defense/',
 '/congress/',
 '/equity-opportunity/',
 '/europe-politics/',
 '/china-politics/',
 '/asia-politics/',
 '/world-politics/',
 '/tv/',
 '/live-audio/',
 '/latest-video/',
 '/top-video/',
 '/video-ceo-interviews/',
 '/europe-television/',
 '/asia-business-day/',
 '/podcast/',
 '/digital-original/',
 '/watchlist/',
 '/investingclub/',
 '/investingclub/charitable-trust/',
 '/investingclub/analysis/',
 '/investingclub/trade-alerts/',
 '/investingclub/video/',
 '/investingclub/education/',
 '/pro/',
 '/pro/news/',
 '/pro/',
 '#',
 '#',
 '/make-it/',
 '/select/',
 '/?region=usa',
 '/world/',
 '/watchlist/',
 '#',
 '#',
 '/',
 '/markets/',
 '/business/',
 '/investing/',
 '/technology/',
 '/politics/',
 '/tv/',
 '/watchlist/',
 '/investingclub/',
 '/pro/',
 '#',
 '#',
 '#',
 '#',
 '#',
 'https://www.cnbc.com/2023/01/12/european-markets-live-updates-stocks-data-earnings-and-news.html',
 'https://www.cnbc.com/2023/01/11/stock-market-news-futures-open-to-close.html',
 'https://www.cnbc.com/quotes/US10Y',
 'https://www.cnbc.com/2023/01/11/binance-plans-15-30percent-hiring-spree-in-2023-even-as-rivals-cut-jobs.html',
 'https://www.cnbc.com/2023/01/11/apple-reportedly-considering-touchscreen-mac-laptop-for-2025.html',
 'https://www.cnbc.com/2023/01/11/jim-cramer-likes-these-5-reasonably-valued-stocks-in-the-sp-500.html',
 'https://www.cnbc.com/2023/01/11/ftx-has-recovered-5-billion-worth-of-liquid-assets-lawyers-say-bankman-fried-crypto.html',
 'https://www.cnbc.com/2023/01/11/cpi-inflation-is-expected-to-have-declined-in-december.html',
 'https://www.cnbc.com/2023/01/11/cpi-inflation-is-expected-to-have-declined-in-december.html',
 'https://www.cnbc.com/2023/01/12/asia-pacific-cpi-inflation-indexes.html',
 'https://www.cnbc.com/2023/01/11/jim-cramer-explains-why-the-december-cpi-number-is-a-big-deal.html',
 'https://www.cnbc.com/2023/01/12/new-year-new-job-but-is-january-the-right-time-to-find-a-new-job.html',
 'https://www.cnbc.com/2023/01/12/new-year-new-job-but-is-january-the-right-time-to-find-a-new-job.html',
 'https://www.cnbc.com/2023/01/12/chinas-reopening-set-to-boost-hong-kongs-property-market.html',
 'https://www.cnbc.com/2023/01/12/chinas-reopening-set-to-boost-hong-kongs-property-market.html',
 'https://www.cnbc.com/2023/01/12/new-year-new-job-but-is-january-the-right-time-to-find-a-new-job.html',
 'https://www.cnbc.com/2023/01/12/the-world-is-at-the-dawn-of-a-new-industrial-age-iea-says-.html',
 'https://www.cnbc.com/2023/01/12/european-markets-live-updates-stocks-data-earnings-and-news.html',
 'https://www.cnbc.com/2023/01/12/chinas-reopening-set-to-boost-hong-kongs-property-market.html',
 '/pro/',
 'https://www.cnbc.com/2023/01/12/evercore-isi-top-picks-for-2023.html',
 '/pro/',
 'https://www.cnbc.com/2023/01/12/morgan-stanley-names-esg-stocks-with-improving-financials-and-upside-.html',
 'https://www.cnbc.com/2023/01/11/amazon-union-victory-at-new-york-warehouse-upheld-by-labor-board.html',
 'https://www.cnbc.com/2023/01/11/microsoft-looked-at-figma-but-didnt-put-in-an-offer-ahead-adobe-deal.html',
 '/pro/',
 'https://www.cnbc.com/2023/01/12/shares-of-london-stock-exchange-group-are-under-valued-fund-strategist-says.html',
 '/pro/',
 'https://www.cnbc.com/2023/01/12/morgan-stanley-has-a-top-pick-in-chinese-tech-sees-share-price-rising.html',
 'https://www.cnbc.com/2023/01/11/lucrative-side-hustles-from-2022-take-less-than-15-hours-per-week.html',
 'https://www.cnbc.com/2023/01/11/cramers-lightning-round-i-would-hold-onto-biomarin-pharmaceutical.html',
 'https://www.cnbc.com/2023/01/11/jim-cramer-likes-these-5-reasonably-valued-stocks-in-the-sp-500.html',
 'https://www.cnbc.com/2023/01/12/asia-pacific-cpi-inflation-indexes.html',
 'https://www.cnbc.com/2023/01/11/charts-suggest-the-market-could-rally-for-the-next-couple-months-jim-cramer-says.html',
 'https://www.cnbc.com/2023/01/11/jim-cramer-explains-why-the-december-cpi-number-is-a-big-deal.html',
 'https://www.cnbc.com/2023/01/11/stock-market-news-futures-open-to-close.html',
 'https://www.cnbc.com/2023/01/11/starbucks-orders-return-to-office.html',
 'https://www.cnbc.com/2023/01/11/frankie-muniz-announces-he-is-now-a-full-time-race-car-driver.html',
 '/pro/',
 'https://www.cnbc.com/2023/01/11/pro-picks-watch-all-of-wednesdays-big-stock-calls-on-cnbc.html',
 'https://www.cnbc.com/2023/01/11/burning-man-sues-biden-administration-over-geothermal-project.html',
 'https://www.cnbc.com/2023/01/11/cameron-winklevoss-and-barry-silbert-are-in-a-bitter-battle-in-crypto.html',
 'https://www.cnbc.com/2023/01/11/apple-reportedly-considering-touchscreen-mac-laptop-for-2025.html',
 'https://www.cnbc.com/2023/01/11/cpi-inflation-is-expected-to-have-declined-in-december.html',
 '/investingclub/',
 'https://www.cnbc.com/2023/01/11/eli-lilly-is-a-recession-resistant-stock-with-major-growth-potential.html',
 'https://www.cnbc.com/2023/01/11/new-study-experiencing-racism-can-affect-the-gut-microbiome.html',
 'https://www.cnbc.com/2023/01/11/biden-administration-will-select-drugs-for-medicare-price-negotiations-by-september.html',
 'https://www.cnbc.com/2023/01/11/alphabet-to-cut-staff-of-health-sciences-unit-verily-by-15percent.html',
 'https://www.cnbc.com/2023/01/11/nike-chairman-mark-parker-will-become-chairman-of-disney.html',
 'https://www.cnbc.com/2023/01/11/kevin-mccarthy-wont-push-george-santos-to-resign.html',
 '/us-market-movers/']

len(list)


# In[178]:


len(headline)


# In[179]:


links = link[115:151]
links


# In[180]:


links.remove('/pro/')
links.remove('/pro/')
links.remove('/pro/')
links.remove('/pro/')
links.remove('/pro/')
links.remove('/investingclub/')

links


# In[181]:


len(links)


# In[182]:


News_Headlines = pd.DataFrame({'Headline':headline,'Timestamp':timestamp,'News Link':links})
News_Headlines


# ----------------------------------------------------------------------------------------------------------------------------

# QUESTION 8

# In[183]:


page8 = requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
page8


# In[184]:


art = BeautifulSoup(page8.content)
art


# In[185]:


article = []
for i in art.find_all('h2',class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg"):
    article.append(i.text)
    
article


# In[186]:


author = []
for i in art.find_all('span',class_="sc-1w3fpd7-0 dnCnAO"):
    author.append(i.text)
    
author


# In[187]:


pdate = []
for i in art.find_all('span',class_="sc-1thf9ly-2 dvggWt"):
    pdate.append(i.text)
    
pdate


# In[188]:


artlink = []
for i in art.find_all('a',href=True):
    artlink.append(i['href'])
    
artlink  


# In[189]:


'#skip-to-content-anchor',
 'http://www.elsevier.com',
 'https://account.elsevier.com/auth',
 'https://elsevier.com/about',
 'https://www.elsevier.com/connect',
 'https://www.elsevier.com/about/careers',
 'https://elsevier.com/about',
 'https://www.elsevier.com/connect',
 'https://www.elsevier.com/about/careers',
 'https://www.elsevier.com/rd-solutions',
 'https://www.elsevier.com/clinical-solutions',
 'https://www.elsevier.com/research-platforms',
 'https://www.elsevier.com/research-intelligence',
 'https://www.elsevier.com/education',
 'https://www.elsevier.com/solutions',
 'https://www.elsevier.com/rd-solutions',
 'https://www.elsevier.com/clinical-solutions',
 'https://www.elsevier.com/research-platforms',
 'https://www.elsevier.com/research-intelligence',
 'https://www.elsevier.com/education',
 'https://www.elsevier.com/solutions',
 'https://www.elsevier.com/authors',
 'https://www.elsevier.com/editors',
 'https://www.elsevier.com/reviewers',
 'https://www.elsevier.com/librarians',
 'https://www.elsevier.com/strategic-partners',
 'https://www.elsevier.com/open-access',
 'https://www.elsevier.com/societies',
 'https://www.elsevier.com/authors',
 'https://www.elsevier.com/editors',
 'https://www.elsevier.com/reviewers',
 'https://www.elsevier.com/librarians',
 'https://www.elsevier.com/strategic-partners',
 'https://www.elsevier.com/open-access',
 'https://www.elsevier.com/societies',
 'https://www.elsevier.com/books-and-journals',
 'https://webshop.elsevier.com/?utm_source=ecom&utm_medium=top&utm_campaign=webshop',
 'https://www.elsevier.com/books-and-journals',
 'https://webshop.elsevier.com/?utm_source=ecom&utm_medium=top&utm_campaign=webshop',
 'https://global-checkout.elsevier.com',
 'https://account.elsevier.com/auth',
 'https://www.sciencedirect.com/science/journal/00043702',
 'https://www.editorialmanager.com/artint/default.aspx',
 'https://www.elsevier.com/',
 'https://www.elsevier.com/search-results?labels=journals',
 '/artificial-intelligence',
 '/artificial-intelligence/most-downloaded-articles',
 'https://www.sciencedirect.com/science/journal/00043702',
 'https://www.editorialmanager.com/artint/default.aspx',
 'https://www.sciencedirect.com/science/journal/00043702',
 'https://www.elsevier.com/journals/artificial-intelligence/0004-3702/guide-for-authors',
 'https://www.editorialmanager.com/artint/default.aspx',
 'https://authors.elsevier.com/tracking/landingpage/selection.do',
 'https://www.elsevier.com/journals/artificial-intelligence/0004-3702/subscribe?subscriptiontype=institutional',
 'https://www.sciencedirect.com/science/article/pii/S0004370221000862',
 'https://www.sciencedirect.com/science/article/pii/S0004370221000722',
 'https://www.sciencedirect.com/science/article/pii/S0004370215000910',
 'https://www.sciencedirect.com/science/article/pii/S0004370298000551',
 'https://www.sciencedirect.com/science/article/pii/S0004370216300790',
 'https://www.sciencedirect.com/science/article/pii/S0004370218305988',
 'https://www.sciencedirect.com/science/article/pii/S0004370220301855',
 'https://www.sciencedirect.com/science/article/pii/S0004370214001386',
 'https://www.sciencedirect.com/science/article/pii/S0004370299000521',
 'https://www.sciencedirect.com/science/article/pii/S0004370219300116',
 'https://www.sciencedirect.com/science/article/pii/S0004370220301533',
 'https://www.sciencedirect.com/science/article/pii/S0004370207000793',
 'https://www.sciencedirect.com/science/article/pii/S0004370216300285',
 'https://www.sciencedirect.com/science/article/pii/S0004370220301958',
 'https://www.sciencedirect.com/science/article/pii/S0004370297000635',
 'https://www.sciencedirect.com/science/article/pii/S0004370221000515',
 'https://www.sciencedirect.com/science/article/pii/S0004370221000539',
 'https://www.sciencedirect.com/science/article/pii/S0004370221000096',
 'https://www.sciencedirect.com/science/article/pii/S0004370216300868',
 'https://www.sciencedirect.com/science/article/pii/S0004370221000588',
 'https://www.sciencedirect.com/science/article/pii/S0004370221000102',
 'https://www.sciencedirect.com/science/article/pii/S0004370213001082',
 'https://www.sciencedirect.com/science/article/pii/S000437029700043X',
 'https://www.sciencedirect.com/science/article/pii/S0004370221000734',
 'https://www.sciencedirect.com/science/article/pii/S0004370209001398',
 'https://www.sciencedirect.com/science/journal/00043702',
 'https://www.sciencedirect.com/user/alerts',
 'https://www.sciencedirect.com/user/register?utm_campaign=sd_recommender_ELSJLS&utm_channel=elseco&dgcid=sd_recommender_ELSJLS',
 'http://www.elsevier.com/authors/home',
 'https://www.editorialmanager.com/artint/default.aspx',
 'https://www.editorialmanager.com/artint/default.aspx',
 'https://researcheracademy.elsevier.com',
 'https://www.elsevier.com/about/policies/copyright/permissions',
 'https://webshop.elsevier.com',
 'https://service.elsevier.com/app/home/supporthub/publishing/#authors',
 'https://authors.elsevier.com/tracking/landingpage/selection.do',
 'https://www.elsevier.com/librarians',
 'https://www.elsevier.com/journals/artificial-intelligence/0004-3702/subscribe?subscriptiontype=institutional',
 'http://www.elsevier.com/editors',
 'http://www.elsevier.com/editors/perk',
 'https://www.elsevier.com/editors/guest-editors',
 'https://service.elsevier.com/app/home/supporthub/publishing/#editors',
 'http://www.elsevier.com/reviewers',
 'https://www.elsevier.com/reviewers/how-to-review',
 'https://www.editorialmanager.com/artint/default.aspx',
 'https://www.elsevier.com/reviewers/becoming-a-reviewer-how-and-why#recognizing',
 'https://service.elsevier.com/app/home/supporthub/publishing/#reviewers',
 'https://www.elsevier.com',
 '//www.elsevier.com/legal/elsevier-website-terms-and-conditions',
 '//www.elsevier.com/legal/privacy-policy',
 '//www.elsevier.com/legal/cookienotice',
 '//www.elsevier.com/sitemap',
 'https://www.relx.com/']


# In[190]:


waste = ['#skip-to-content-anchor',
 'http://www.elsevier.com',
 'https://account.elsevier.com/auth',
 'https://elsevier.com/about',
 'https://www.elsevier.com/connect',
 'https://www.elsevier.com/about/careers',
 'https://elsevier.com/about',
 'https://www.elsevier.com/connect',
 'https://www.elsevier.com/about/careers',
 'https://www.elsevier.com/rd-solutions',
 'https://www.elsevier.com/clinical-solutions',
 'https://www.elsevier.com/research-platforms',
 'https://www.elsevier.com/research-intelligence',
 'https://www.elsevier.com/education',
 'https://www.elsevier.com/solutions',
 'https://www.elsevier.com/rd-solutions',
 'https://www.elsevier.com/clinical-solutions',
 'https://www.elsevier.com/research-platforms',
 'https://www.elsevier.com/research-intelligence',
 'https://www.elsevier.com/education',
 'https://www.elsevier.com/solutions',
 'https://www.elsevier.com/authors',
 'https://www.elsevier.com/editors',
 'https://www.elsevier.com/reviewers',
 'https://www.elsevier.com/librarians',
 'https://www.elsevier.com/strategic-partners',
 'https://www.elsevier.com/open-access',
 'https://www.elsevier.com/societies',
 'https://www.elsevier.com/authors',
 'https://www.elsevier.com/editors',
 'https://www.elsevier.com/reviewers',
 'https://www.elsevier.com/librarians',
 'https://www.elsevier.com/strategic-partners',
 'https://www.elsevier.com/open-access',
 'https://www.elsevier.com/societies',
 'https://www.elsevier.com/books-and-journals',
 'https://webshop.elsevier.com/?utm_source=ecom&utm_medium=top&utm_campaign=webshop',
 'https://www.elsevier.com/books-and-journals',
 'https://webshop.elsevier.com/?utm_source=ecom&utm_medium=top&utm_campaign=webshop',
 'https://global-checkout.elsevier.com',
 'https://account.elsevier.com/auth',
 'https://www.sciencedirect.com/science/journal/00043702',
 'https://www.editorialmanager.com/artint/default.aspx',
 'https://www.elsevier.com/',
 'https://www.elsevier.com/search-results?labels=journals',
 '/artificial-intelligence',
 '/artificial-intelligence/most-downloaded-articles',
 'https://www.sciencedirect.com/science/journal/00043702',
 'https://www.editorialmanager.com/artint/default.aspx',
 'https://www.sciencedirect.com/science/journal/00043702',
 'https://www.elsevier.com/journals/artificial-intelligence/0004-3702/guide-for-authors',
 'https://www.editorialmanager.com/artint/default.aspx',
 'https://authors.elsevier.com/tracking/landingpage/selection.do',
 'https://www.elsevier.com/journals/artificial-intelligence/0004-3702/subscribe?subscriptiontype=institutional']

len(waste)


# In[191]:


len(article)


# In[192]:


len(artlink)


# In[193]:


artlinks = artlink[54:79]
artlinks


# In[194]:


Top_Downloaded_Articles = pd.DataFrame({'Article Name':article,'Authors':author,'Publishing Date':pdate,'Article Link':artlinks})

Top_Downloaded_Articles


# -----------------------------------------------------------------------------------------------------------------------------

# QUESTION 9

# In[195]:


page9 = requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')
page9


# In[196]:


dine = BeautifulSoup(page9.content)
dine


# In[197]:


rest_name = []
for i in dine.find_all('a',class_="restnt-name ellipsis"):
    rest_name.append(i.text)
    
rest_name


# In[198]:


cuisine = []
for i in dine.find_all('span',class_="double-line-ellipsis"):
    cuisine.append(i.text)
    
cuisine


# In[199]:


cuisine = [i.split('|')[1] for i in cuisine]

cuisine


# In[200]:


location = []
for i in dine.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)
    
location


# In[201]:


rest_rating = []
for i in dine.find_all('div',class_="restnt-rating rating-4"):
    rest_rating.append(i.text)
    
rest_rating


# In[202]:


rest_images = []
for i in dine.find_all("img",class_="no-img"):
    rest_images.append(i.get('data-src'))
    
rest_images


# In[203]:


dineout_buffets = pd.DataFrame({'Restaurant':rest_name,'Cuisine':cuisine,'Location':location,'Rating':rest_rating,'Image Link':rest_images})

dineout_buffets


# ----------------------------------------------------------------------------------------------------------------------------

# QUESTION 10

# In[204]:


page10 = requests.get('https://scholar.google.com/citations?view_op=top_venues&hl=en')
page10


# In[ ]:




