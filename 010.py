from bs4 import BeautifulSoup
import urllib.request
import re


def printList(list):
    print("length of the list= ", len(list))
    for i in list:
        print(i, "\n")


# function that takes start URL and number of pages for all get, if number is 0
# will take all pages
def getLinks(starturl, amountofpages):
    response = urllib.request.urlopen(starturl)
    soup = BeautifulSoup(response, "html.parser")
    # Filtering pages, leaving only wiki information pages
    dict = re.compile("#|tel|.svg|mailto|.jpg|:|//|Main_Page")
    url_list = []
    urls = soup.find_all("a",href=True)
    if amountofpages == 0:
        amountofpages = None
    for url in urls[:amountofpages]:
        if (str(url.get("href"))[:5] == "/wiki") and not dict.search(url.get("href")):
            # append the base wikipedia URL
            url_list.append("https://en.wikipedia.org" + url.get("href"))
    return url_list


# recursive function that get empty list, starting page in list form,
# depth of crawling and amount of pages for every crawl
def getLinksRec(full_list, current_list, depth, amount):
    #print("fullist lenthg=", len(full_list))
    #print("depth=", depth)
    if depth == 0:
        # exit point
        #print("fullist lenthg= ", len(full_list))
        return full_list
    nextlevel = []
    for url in current_list:
        newlevel = getLinks(url, amount)
        nextlevel += newlevel
        full_list += newlevel
    #printList(full_list)
    return getLinksRec(full_list, nextlevel, depth - 1, amount)

def downloadPages(urllist):
    for url in urllist:
        response = urllib.request.urlopen(url)
        data=response.read()
        f=open("C:/example/"+str(url)[30:]+".html","wb")
        f.write(data)
        f.close


def main():
    a = getLinksRec([], ["https://en.wikipedia.org/wiki/Colt_Python"], 3,20)
    printList(a)
    #downloadPages(a)



if __name__ == "__main__":
    main()
