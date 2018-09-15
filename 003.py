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


def getUrls(starturl, depth):
    if depth == 0:
        return None
    response = urllib.request.urlopen(starturl)
    soup = BeautifulSoup(response, "html.parser")
    urls = soup.find_all("a")
    url_list = []
    for a in urls:
        # excluding tel ,mailto, and #(same page) links
        # if (a.get("href")) and ("tel" not in a.get("href")) and ("mailto" not in a.get("href")) and ("#" not in a.get("href"))and (".jpg" not in a.get("href"))and  (".svg" not in a.get("href"))and ("=edit" not in a.get("href")):
        if (a.get("href")):
            if not re.search("#|tel|.svg|mailto|.jpg|:|//", a.get("href")):
                # part of URLs on wiki presented as \\url without http start and part of the URLs presented as \w\index or \wiki\,
                # checking the urls we need
                if str(a.get("href"))[:5] == "/wiki":
                    url_list.append("https://en.wikipedia.org" + a.get("href"))
    for i in range(depth):
        getUrls(url_list[i], depth - 1)
    return url_list


def main():
    printList((getUrls("https://en.wikipedia.org/wiki/Colt_Python", 5)), 500)


if __name__ == "__main__":
    main()
