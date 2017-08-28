
#### For 113th


PairString = []
Date = []
Volume = []
Page = []
CongRec = []

for i in range(1, 28):
  for j in range(1,1500):
    if i < 10:
      web_address= 'http://www.heinonline.org/HOL/Page?collection=congrec&handle=hein.congrec/cr113000' + str(i) + '&type=Text&id=' + str(j)
    else:
      web_address= 'http://www.heinonline.org/HOL/Page?collection=congrec&handle=hein.congrec/cr11300' + str(i) + '&type=Text&id=' + str(j)
    web_page = urllib2.urlopen(web_address)
    soup = BeautifulSoup(web_page.read())
    soup.prettify()
    text2 = soup.find_all('pre')[0].text
    pattern = r"\r\n\t\t\t\t M[rs]"
    Newtxt = re.split(pattern,text2)
    FinalText = []
    for k in range(0,len(Newtxt)):
        FinalText.append(Newtxt[k].replace("\r\n\t\t\t\t", ""))
    searchterm = "pair"
    for p in FinalText:
        if re.search(searchterm, p):
            PairString.append(p)
            Date.append(FinalText[0].split()[3] + " " + FinalText[0].split()[4] + " " + FinalText[0].split()[5])
            Volume.append(i)
            Page.append(j)
            CongRec.append(113)

###For 114

PairString114 = []
Date114 = []
Volume114 = []
Page114 = []
CongRec114 = []

for i in range(1, 25):
  for j in range(1,1500):
    if i < 10:
      web_address= 'http://www.heinonline.org/HOL/Page?collection=congrec&handle=hein.congrec/cr114000' + str(i) + '&type=Text&id=' + str(j)
  else:
      web_address= 'http://www.heinonline.org/HOL/Page?collection=congrec&handle=hein.congrec/cr11400' + str(i) + '&type=Text&id=' + str(j)
      web_page = urllib2.urlopen(web_address)
      soup = BeautifulSoup(web_page.read())
      soup.prettify()
      text2 = soup.find_all('pre')[0].text
      pattern = r"\r\n\t\t\t\t M[rs]"
      Newtxt = re.split(pattern,text2)
      FinalText = []
      for k in range(0,len(Newtxt)):
          FinalText.append(Newtxt[k].replace("\r\n\t\t\t\t", ""))
      searchterm = "pair"
      for p in FinalText:
          if re.search(searchterm, p):
              PairString114.append(p)
              Date114.append(FinalText[0].split()[3] + " " + FinalText[0].split()[4] + " " + FinalText[0].split()[5])
              Volume114.append(i)
              Page114.append(j)
              CongRec114.append(114)
