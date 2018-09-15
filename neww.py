from bs4 import BeautifulSoup
import urllib.request
base_url = 'https://en.wikipedia.org'
search_url ="https://en.wikipedia.org/wiki/WKIK"
response = urllib.request.urlopen(search_url)
soup = BeautifulSoup(response,"html.parser")
final_url=[]
for link in soup.find_all('a', href=True):
    #print ("Found the URL:", link['href'])
    if link['href'] != '#' and link['href'].strip() != '':
       final_url.append(base_url + link['href'])
print (final_url)