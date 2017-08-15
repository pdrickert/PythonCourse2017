#Go to https://polisci.wustl.edu/faculty/specialization
#Go to the page for each of the professors.
#Create a .csv file with the following information for each professor:
# 	-Specialization
# 	-Name
# 	-Title
# 	-E-mail
# 	-Web page

from bs4 import BeautifulSoup
import urllib2
import csv
import random
import time
import os
import re

web_address='https://polisci.wustl.edu/faculty/specialization'
web_page = urllib2.urlopen(web_address)

soup = BeautifulSoup(web_page.read())
soup.prettify()
Prof_urls = []
for a in soup.find_all('a', href=True)[14:56]:
	Prof_urls.append("https://polisci.wustl.edu" + a['href'])

Prof_urls[16] = 'https://polisci.wustl.edu/Matthew_Gabel'
Prof_urls[32] = 'https://polisci.wustl.edu/Matthew_Gabel'



name = []
for n in Prof_urls:
	web_address= n
	web_page = urllib2.urlopen(web_address)
	soup = BeautifulSoup(web_page.read())
	soup.prettify()
	name.append(soup.find_all('h1')[2].text)




email = []
for n in Prof_urls:
	web_address= n
	web_page = urllib2.urlopen(web_address)
	soup = BeautifulSoup(web_page.read())
	soup.prettify()
	if "@" in soup.find_all('a', href=True)[16].text:
		email.append(soup.find_all('a', href=True)[16].text)
	elif "@" in soup.find_all('a', href=True)[15].text:
		email.append(soup.find_all('a', href=True)[15].text)
	elif "@" in soup.find_all('a', href=True)[17].text:
		email.append(soup.find_all('a', href=True)[17].text)
	else:
		email.append("No Email Found")




title = []
for n in Prof_urls:
	web_address= n
	web_page = urllib2.urlopen(web_address)
	soup = BeautifulSoup(web_page.read())
	soup.prettify()
	if "edu" not in soup.find_all('div', "field-item even")[1].text:
		title.append(soup.find_all('div', "field-item even")[1].text)
	elif "edu" not in soup.find_all('div', "field-item even")[0].text:
		title.append(soup.find_all('div', "field-item even")[0].text)
	else:
		title.append("No Title Found")




web_address='https://polisci.wustl.edu/faculty/specialization'
web_page = urllib2.urlopen(web_address)
soup = BeautifulSoup(web_page.read())
soup.prettify()
spec_list=[]
specialization = soup.find_all('h3')
for sub in specialization:
	for sibling in sub.next_siblings:
		if sibling in specialization:
			break
		else:
			try:
				sibling.get_text()
				spec_list.append(sub)
			except:
				pass

TitleDict={}
for i in range(0,41):
	TitleDict[name[i]] = {title[i]}

SpecialDict = {}
for i in range(0,41):
	SpecialDict[name[i]] = {spec_list[i]}

EmailDict = {}
for i in range(0,41):
	SpecialDict[name[i]] = {email[i]}





website = []
for n in Prof_urls:
	web_address= n
	web_page = urllib2.urlopen(web_address)
	soup = BeautifulSoup(web_page.read())
	soup.prettify()
	if "@" not in soup.find_all('a', href=True)[16].text and "pdf" not in soup.find_all('a', href=True)[16].text:
		website.append(link.get(href))
	elif "@" not in soup.find_all('a', href=True)[15].text and "pdf" not in soup.find_all('a', href=True)[15].text:
		website.append(soup.find_all('a', href=True)[15].text)
	elif "@" not in soup.find_all('a', href=True)[17].text and "pdf" not in soup.find_all('a', href=True)[17].text:
		website.append(soup.find_all('a', href=True)[17].text)
	else:
		website.append("No Website")


website = []
for n in Prof_urls:
	web_address= n
	web_page = urllib2.urlopen(web_address)
	soup = BeautifulSoup(web_page.read())
	soup.prettify()
	for a in soup.find_all('a', href=True)[15]:
		PossibleWebsite = (a['href'])
		if "http" in PossibleWebsite and "cv" not in PossibleWebsite:
			website.append(PossibleWebsite)
		else:
			website.append("No Website")

web_address='https://polisci.wustl.edu/faculty/specialization'
web_page = urllib2.urlopen(web_address)
soup = BeautifulSoup(web_page.read())
soup.prettify()
soup.find_all('strong')
soup.find_all('div')
