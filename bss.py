from bs4 import BeautifulSoup
import urllib.request
from lxml import html

quote_page = "https://en.wikipedia.org/wiki/1882"
searchitem = ("iphone+x")

page = urllib.request.urlopen(quote_page)

pagesoup = BeautifulSoup(page, "html.parser")

#print(pagesoup.prettify)
#a = list(pagesoup.children)
#print(a)
links=list()
#prices = pagesoup.find_all("div", attrs = {"class":"pricesTxt"})
prices = pagesoup.find_all('div',class_="pricesTxt")
links = pagesoup.find_all("a", attrs={"href"})
#prices = pagesoup.find_all(class_="pricesTxt")
#firstprice = pagesoup.find('div',{'class':'pricesTxt'}).text




def getpricestable (priceslist):
    for i in range(len(priceslist)):
        print(priceslist[i].text)

def getlinks (linklist):
    for i in range(len(linklist)):
        print (linklist[i].find('a').get('href'))
#print (links)
#print(firstprice)

#getpricestable(prices)
getlinks(links)