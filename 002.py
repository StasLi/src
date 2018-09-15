from bs4 import BeautifulSoup
import urllib.request

url = "https://en.wikipedia.org/wiki/Colt_Python"

response = urllib.request.urlopen(url)
soup = BeautifulSoup(response,"html.parser")

print(response.geturl())
print("*********************************")
def getSoupTitle(soup):
    return soup.title

def printList(list,number):
    print("length of the list=",len(list))
    for i in list[:number]:
        print (i,"\n")

def getUrls(soup):
    urls=soup.find_all("a")
    url_list=[]
    for a in urls:
        #excluding tel ,mailto, and #(same page) links
        if (a.get("href"))and("tel" not in a.get("href"))and("mailto" not in a.get("href")) and ("#" not in a.get("href")):
        # part of URLs on wiki presented as \\url without http start and part of the URLs presented as \w\index or \wiki\,
        # so we need to check and to "repair" those links
            if str(a.get("href"))[:2]=="//":
                url_list.append("https:"+a.get("href"))
            elif str(a.get("href"))[:2]=="/w":
                url_list.append("https://en.wikipedia.org" + a.get("href"))
            else:
                url_list.append(a.get("href"))
    return url_list









def main():


    printList((getUrls(soup)),280)
if __name__ == "__main__":
    main()