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


def printList(list, number):
    print("length of the list=", len(list))
    for i in list[:number]:
        print(i, "\n")



def getSoup(starturl):
    response = urllib.request.urlopen(starturl)
    return BeautifulSoup(response, "html.parser")

def getLinks(soup,url_list):
    dict = re.compile("#|tel|.svg|mailto|.jpg|:|//|Main_Page")
    urls = soup.find_all("a")
    for url in urls:
        if (str(url.get("href"))[:5] == "/wiki")and not dict.search(url.get("href")):
            url_list.append("https://en.wikipedia.org" + url.get("href"))
    return url_list


def CrawlUrl(url, depth):
    if depth == 0:
        return None




def main():
    url = "https://en.wikipedia.org/wiki/Colt_Python"
    soup = getSoup(url)
    url_list = getLinks(soup,[1,2,3])
    printList(url_list,300)
    # CrawlUrl("https://en.wikipedia.org/wiki/Colt_Python",1)


if __name__ == "__main__":
    main()
