from bs4 import BeautifulSoup
import urllib.request
import re

url = "https://en.wikipedia.org/wiki/Colt_Python"

response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, "html.parser")

print(response.geturl())
print("*********************************")


def getSoupTitle(soup):
    return soup.title


def printList(list):
    print("length of the list=", len(list))
    for i in list:
        print(i, "\n")



def getLinks(starturl):
    response = urllib.request.urlopen(starturl)
    soup=BeautifulSoup(response, "html.parser")
    dict = re.compile("#|tel|.svg|mailto|.jpg|:|//|Main_Page")
    url_list = []
    urls = soup.find_all("a")
    for url in urls:
        if (str(url.get("href"))[:5] == "/wiki") and not dict.search(url.get("href")):
            url_list.append("https://en.wikipedia.org" + url.get("href"))
    return url_list[:15]


def getLinksRec(full_list, current_list):
    print (type(full_list))
    if len(full_list)>100:
        print("print before end= ",type(full_list))
        return full_list
    nextlevel = []

    for url in current_list:
        newlevel= getLinks(url)
        nextlevel +=newlevel
        full_list  += newlevel
    #printList(full_list)
    return getLinksRec(full_list, nextlevel)


def main():
    #url = "https://en.wikipedia.org/wiki/Colt_Python"
    #soup = getSoup(url)
    #linkslist = (getLinks("https://en.wikipedia.org/wiki/Colt_Python"))
    #print(type(linkslist))

    # printList(url_list, 300)

    a = getLinksRec([],["https://en.wikipedia.org/wiki/Colt_Python"])
    print(a)
    print("type of A is = ", type(a))
    #printList(a, 1000)
    #print(type(getLinks("https://en.wikipedia.org/wiki/Colt_Python")))
    #printList(getLinks("https://en.wikipedia.org/wiki/Colt_Python"),1000)


if __name__ == "__main__":
    main()
