from bs4 import BeautifulSoup
import urllib.request
page = urllib.request.urlopen("http://www.example.com")

page_soup = BeautifulSoup(page,"html.parser")

#print(page_soup.prettify())


def gettag (soup,tag):
    return(soup.find_all(tag))

def getname(soup):
    namelist = soup.find_all(True)
    for i in range(len(namelist)):
        print(namelist[i].name)

#print(page_soup.a.text)

#gettag(page_soup,"p")

#getname(page_soup)

f = open("myfile.txt","w")
f.write("first line \n")
#f.write(str(gettag(page_soup,"a")))
f.write("\n")
texta=(page_soup.find("p").string)
print(texta)
f.close()



