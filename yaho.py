from bs4 import BeautifulSoup
import urllib.request
from lxml import html
quote_page = "https://www.yahoo.com/search?p="
searchitem = "iphone+X"

page = urllib.request.urlopen(quote_page+searchitem)

pagesoup =  BeautifulSoup(page, "html.parser")

#print(pagesoup.prettify)
#a = list(pagesoup.children)
#print(a)
links=list()
#prices = pagesoup.find_all("div", attrs = {"class":"pricesTxt"})
prices = pagesoup.find_all(class_="pricesTxt")
links = pagesoup.find_all("div", attrs={"class":"ComparePricesBtn"})


print(prices)
print (links)


