from bs4 import BeautifulSoup
import urllib.request
import urllib.robotparser
import re





url = "http://life.com"
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response,"html.parser")

print(response.geturl())

def getSoupTitle(soup):
    return soup.title
#def getSouptext(soup,num):
    ##for i in range(num):
      # texts.append(paragraphs)
    #return texts
#print(getSouptext(soup,10))

#print(len(soup.contents))
def printHead(soup):
    head_tag = soup.head
    for i in head_tag:
        print (i)
    print (len(head_tag))

def printContents(soup):
    for i in range(len(soup.contents)):
        print (soup.contents[i])

def childIteration(soup):
    for child in soup.head.descendants:
        print(child)
def childString(soup):
    for string in soup.stripped_strings:
        print(repr(string))


def printList(list):
    print("length of the list=",len(list))
    for i in list:
        print (i,"\n")


def getLinks (soup):
    links = soup.find_all("a", attrs={"href":True})
    #print (links)
    #printList(links)
    #print(len(links))
    urls=[]
    for i in links:
            urls.append(i)
    return urls
def getCrwalUrls(soup):
    urls=soup.find_all("a")
    url_list=[]
    for a in urls:
        if (a.get("href")):
            url_list.append(a.get("href"))
    return url_list


#print(findlinksre(soup))

#print(getCrwalUrls(soup))

printList(getLinks(soup))
#printList(getCrwalUrls(soup))
#print (getLinks(soup))

#childString(soup)
#childIteration(soup)
#printContents(soup)
#print(soup.head.contents)
#f = open("file1.html","w")
#f.write(str(soup))
#f.close()