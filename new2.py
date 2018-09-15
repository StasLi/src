from bs4 import BeautifulSoup
import urllib.request
base_url = 'https://en.wikipedia.org'
search_url ="https://en.wikipedia.org/wiki/WKIK"
response = urllib.request.urlopen(search_url)
soup = BeautifulSoup(response,"html.parser")



for link in soup.find_all('a', href=True):
    if 'en.wikipedia.org' not in link['href']:
        print("Found the URL:", 'https://en.wikipedia.org'+link['href'])
    elif 'http' not in link['href']:
        print("Found the URL:", 'https://'+link['href'])
    else:
        print("Found the URL:", link['href'])