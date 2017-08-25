from bs4 import BeautifulSoup
import urllib2
import random
import time
import os
import re

SenateVoteString = []
SenatePresentMember = []
SenateAbsentMember = []
PresVote = []
AbsVote = []
Date = []
CongRec = []

for j in range(1,2000):
    time.sleep(random.uniform(0,3))
    try:
        web_address= 'http://www.heinonline.org/HOL/Page?collection=congrec&handle=hein.congrec/cr1230007&type=Text&id=' + str(j)
        web_page = urllib2.urlopen(web_address)
        soup = BeautifulSoup(web_page.read())
        soup.prettify()
        text = soup.find_all('pre')[0].text
        pattern = r"\r\n\t\t\t\t M[rs]"
        Newtxt = re.split(pattern,text)
        FinalText = []
        for k in range(0,len(Newtxt)):
            FinalText.append(Newtxt[k].replace("\r\n\t\t\t\t", ""))
            searchterm = "on this vote I have a pair"
            for p in FinalText:
                if re.search(searchterm, p):
                    SenateVoteString.append(p)
                    Names = []
                    Capitals = (re.findall(r'([A-Z]+\b)', SenateVoteString[-1]))
                    for n in range(len(Capitals)):
                        if len(Capitals[n])>1:
                            Names.append(Capitals[n])
                    SenatePresentMember.append(Names[0])
                    SenateAbsentMember.append(Names[-1])
                    Date.append(FinalText[0].split()[0] + " " + FinalText[0].split()[1] + " " + FinalText[0].split()[2])
                    if "nay" in SenateVoteString[-1].split("yea")[1]:
                        PresVote.append(0)
                        AbsVote.append(1)
                    else:
                        PresVote.append(1)
                        AbsVote.append(0)
                else:
                    pass
    except IndexError:
        pass
