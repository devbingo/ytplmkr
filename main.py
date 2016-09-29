#!/usr/bin/python
import urllib.request

from Tools.scripts.treesync import raw_input
from bs4 import BeautifulSoup
import requests

print("Enter the url to extract links:")
theurl=input()
thepage=requests.get(theurl)
#thepage=urllib.request.urlopen(theurl)
#print(thepage.content)
        
soup=BeautifulSoup(thepage.content,"html.parser")
print("**************************")
print(soup.title)


links_all=[]
for links in soup.findAll('a'):
    if links.get('href'):
        links_all.append(links.get('href'))
print("****************ALL LINKS START***********************")

print(links_all)
print("****************ALL LINKS END***********************")
vlink=[]
for link in links_all:
    if "https://www.youtube" in link:
        vlink.append(link)
print("**********VALID LINKS ARE*****************************")
print(vlink)
print("****************VALID LINKS END***********************")
file=open("ytlinks.txt","w")
for vl in vlink:
    file.write(vl)
    file.write("\n")
file.close()
print("****************YT Links***********************")
print("****************YT Links***********************")
file2=open("ytlinks.txt",'r')
for line in file2:
    print("\n***",line,"***")

#fsdjkhfjksdhj









