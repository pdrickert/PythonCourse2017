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

web_address='https://polisci.wustl.edu/faculty/specialization'
web_page = urllib2.urlopen(web_address)

soup = BeautifulSoup(web_page.read())
soup.prettify()
Prof_urls = []
for a in soup.find_all('a', href=True)[14:56]:
	Prof_urls.append("https://polisci.wustl.edu" + a['href'])
name = []
for page in Prof_urls:
	web_address= page
	web_page = urllib2.urlopen(web_address)
	soup = BeautifulSoup(web_page.read())
	soup.prettify()
	name.append(soup.find_all('h1'))
