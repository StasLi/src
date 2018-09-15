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

dict = re.compile("#|tel|.svg|mailto|.jpg|:|//|Main_Page")

def getUrls(starturl):
    dict = re.compile("#|tel|.svg|mailto|.jpg|:|//|Main_Page")
    response = urllib.request.urlopen(starturl)
    soup = BeautifulSoup(response, "html.parser")
    urls = soup.find_all("a")
    url_list = []

    for a in urls:
        if (str(a.get("href"))[:5] == "/wiki")and not dict.search(a.get("href")):
            url_list.append("https://en.wikipedia.org" + a.get("href"))
    return url_list


def CrawlUrl(url, depth):
    if depth == 0:
        return None
    return (CrawlUrl(getUrls(url)[depth - 1], depth - 1))


def main():
    printList((getUrls("https://en.wikipedia.org/wiki/Colt_Python")), 500)
    # CrawlUrl("https://en.wikipedia.org/wiki/Colt_Python",1)


if __name__ == "__main__":
    main()
