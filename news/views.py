import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from django.shortcuts import render

#NDTV News
ndtv_links = []
ndtv_img_links = []
ndtv_headings=[]

#NEWS18
news18_links=[]
news18_img_links=[]
news18_headings=[]

#CNET
cnet_links=[]
cnet_img_links=[]
cnet_headings=[]

#Function to scrape NDTV website
def get_ndtv():
    page = requests.get("https://www.ndtv.com/")
    soup = BeautifulSoup(page.content, 'html.parser')
    #Get all links
    a = soup.find_all('div', class_='cont_cmn top-stories-68')
    l1=[]
    l2=[]
    l3=[]
    for x in a:
        for link in x.find_all('a'):
            l1.append(link.get('href'))
        for img in x.find_all('img'):
            l2.append(img['src']) 
        for hd in x.find_all('h2'):
            l3.append(hd.text)   
    
    [ndtv_links.append(x) for x in l1 if x not in ndtv_links]  
    [ndtv_img_links.append(x) for x in l2 if x not in ndtv_img_links]
    [ndtv_headings.append(x) for x in l3 if x not in ndtv_headings]
    
#Function to scrape News18
def get_news18():
    page2 = requests.get("https://www.news18.com/")
    soup2 = BeautifulSoup(page2.content, 'html.parser')
    #Get all links
    b = soup2.find_all('div', class_='vspacer30')
    l1=[]
    l2=[]
    l3=[]
    l4=["/buzz/","/movies/","/sports/","/cricketnext/","/tech/","/football/"]
    for x in b:
        for link in x.find_all('a'):
            a = link.get('href')
            if a not in l4:
                l1.append(a)
        for img in x.find_all('img'):
            l2.append(img['data-src']) 
        for hd in x.find_all('h4'):
            l3.append(hd.text)

    [news18_links.append(x) for x in l1 if x not in news18_links]  
    [news18_img_links.append(x) for x in l2 if x not in news18_img_links]
    [news18_headings.append(x) for x in l3 if x not in news18_headings]

    #for x in range(len(news18_links)-2):
    #    print(news18_links[x],"\n",news18_img_links[x],"\n",news18_headings[x],"\n\n")


#Function to srape CNET
def get_cnet():
    page3 = requests.get("https://www.cnet.com/news/")
    soup3 = BeautifulSoup(page3.content, 'html.parser')
    #Get all links
    b = soup3.find_all('div', class_='col-2 assetWrap')
    l1=[]
    l2=[]
    l3=[]
    for x in b:
        for link in x.find_all('a'):
            a=link.get('href')
            b='https://www.cnet.com'+link.get('href')
            l1.append(b)
        for img in x.find_all('img'):
            l2.append(img['src']) 
        for hd in x.find_all('h6'):
            l3.append(hd.text)

    [cnet_links.append(x) for x in l1 if x not in cnet_links]  
    [cnet_img_links.append(x) for x in l2 if x not in cnet_img_links]
    [cnet_headings.append(x) for x in l3 if x not in cnet_headings]
    
      

get_ndtv()
get_news18() 
get_cnet()

def index(req):
    return render(req, 'news/index.html', {'ndtv_news':ndtv_links, 'ndtv_img': ndtv_img_links, 'ndtv_headings':ndtv_headings, 'news18_news':news18_links, 'news18_img':news18_img_links,'news18_headings':news18_headings , 'cnet_news':cnet_links, 'cnet_img':cnet_img_links,'cnet_headings':cnet_headings})