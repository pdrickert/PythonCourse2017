from bs4 import BeautifulSoup
import urllib2
import csv
import random
import time
import os
import re
import sys
reload(sys)
sys.setdefaultencoding('UTF8')

petition_sites = []
for n in range(0,2):
  web_address='https://petitions.whitehouse.gov/?page=' + '%s' %n
  web_page = urllib2.urlopen(web_address)
  soup = BeautifulSoup(web_page.read())
  soup.prettify()
  for a in soup.find_all('a', href=True)[13:53][::2]:
  	petition_sites.append("https://petitions.whitehouse.gov" + a['href'])

web_address='https://petitions.whitehouse.gov/?page=2'
web_page = urllib2.urlopen(web_address)
soup = BeautifulSoup(web_page.read())
soup.prettify()
for a in soup.find_all('a', href=True)[13:19][::2]:
  petition_sites.append("https://petitions.whitehouse.gov" + a['href'])

title = []
for n in petition_sites:
  web_address= n
  web_page = urllib2.urlopen(web_address)
  soup = BeautifulSoup(web_page.read())
  soup.prettify()
  title.append(soup.find_all('h1')[0].text)



day = []
for n in petition_sites:
  web_address= n
  web_address= web_page = urllib2.urlopen(web_address)
  soup = BeautifulSoup(web_page.read())
  soup.prettify()
  CreatorDate=soup.find_all('h4')[0].text
  Date = CreatorDate[19:]
  day.append(Date)

tags = []
for n in petition_sites:
  web_address= n
  web_page = urllib2.urlopen(web_address)
  soup = BeautifulSoup(web_page.read())
  soup.prettify()
  if len(soup.find('article').find_all('h6')) == 1:
    single_petition_tag = "%s" %((soup.find('article').find_all('h6'))[0].text)
    tags.append(single_petition_tag)
  elif len(soup.find('article').find_all('h6')) == 2:
    single_petition_tag = "%s, %s" %((soup.find('article').find_all('h6'))[0].text, (soup.find('article').find_all('h6'))[1].text)
    tags.append(single_petition_tag)
  elif len(soup.find('article').find_all('h6')) == 3:
    single_petition_tag = "%s, %s, %s" %((soup.find('article').find_all('h6'))[0].text, (soup.find('article').find_all('h6'))[1].text, (soup.find('article').find_all('h6'))[2].text)
    tags.append(single_petition_tag)


signatures = []
for n in petition_sites:
  web_address= n
  web_page = urllib2.urlopen(web_address)
  soup = BeautifulSoup(web_page.read())
  soup.prettify()
  signatures.append(soup.find_all('span')[4].text)

for n in range(0,42, 1):
    if n == 0:
        with open('PythonProblemSet2.CSV', 'wb') as f:
            my_writer = csv.DictWriter(f, fieldnames =("Petition Title", "Petition Date", "Signature Numbers", "Tags"))
            my_writer.writeheader()
            my_writer.writerow({"Petition Title" : title[n], "Petition Date" : day[n], "Signature Numbers" : signatures[n], "Tags" : tags[n]})
    else:
        with open('PythonProblemSet2.CSV', 'ab') as f:
            my_writer = csv.DictWriter(f, fieldnames =("Petition Title", "Petition Date", "Signature Numbers", "Tags"))
            my_writer.writerow({"Petition Title" : title[n], "Petition Date" : day[n], "Signature Numbers" : signatures[n], "Tags" : tags[n]})

import sys
reload(sys)
sys.setdefaultencoding('ASCII')
