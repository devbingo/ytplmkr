import urllib.request

from Tools.scripts.treesync import raw_input
from bs4 import BeautifulSoup
import requests

print("Enter the url to extract links:")
theurl=input()
thepage=requests.get(theurl)
#thepage=urllib.request.urlopen(theurl)d
print(thepage.content)
soup=BeautifulSoup(thepage.content,'html.parser')
for link in soup.find("a"):
    print(link.get("href"))










