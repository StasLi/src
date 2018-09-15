from bs4 import BeautifulSoup
import urllib.request
import os


url = "https://en.wikipedia.org/wiki/Colt_Python"

response = urllib.request.urlopen(url)
data= response.read()
#soup = BeautifulSoup(response, "html.parser")
#print(response.read())
#print (soup.prettify())
#path = "/example/1/strangefolder"
#os.makedirs(path)
#f = open("C://example/1.html","wb")
#f.write(data)
#f.close()
#a= [1,2,3]
#print(a[:None])
for i in range(5):
    response = urllib.request.urlopen("https://en.wikipedia.org/wiki/Colt_Python")
    data = response.read()
    f = open("C:/example/" +str(i) + ".html", "wb")
    f.write(data)
    f.close
