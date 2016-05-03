#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib2
import html5lib
import time
from argparse import ArgumentParser 


#url = 'http://www.cnbc.com/pre-markets/'
url = 'http://www.bloomberg.com/markets/stocks/futures'
gasupport = ""
garesistance = ""
target = ""
dowprice = ""
dowchange = ""
spprice = ""
spchange = ""
nasdaqprice = ""
nasdaqchange = ""
europrice = ""
eurochange  = ""
ftseprice = "" 
ftsechange = ""
hangsengprice = ""
hangsengchange = ""
nikkeiprice = ""
nikkeichange = ""


def getArgs():
	global gasupport, garesistance
	parser = ArgumentParser(description = 'Get Arguments')
	parser.add_argument("-s", "--support", required=False, dest="support", help="Initialize S&P support level", metavar="support")
	parser.add_argument("-r", "--resistance", required=False, dest="resistance", help="Initialize S&P resistance level", metavar="resistance")
	args = parser.parse_args()
	gasupport = args.support
	garesistance = args.resistance
	return (gasupport, garesistance)

def getSoup():
	global url, target
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page, 'html5lib')
	target = soup.find("tr", {"class": "data-table__row"}) #gets DJIA instead of S&P 500
	target = soup.find_all("td")

def getFutures():
	global dowprice, dowchange, spprice, spchange, nasdaqprice, nasdaqchange, europrice, ftseprice, ftsechange, hangsengprice, hangsengchange, nikkeiprice, nikkeichange
	dowprice = str(target[3].text)
	dowchange = str(target[4].text)
	spprice = str(target[12].text)
	spchange = str(target[13].text)
	nasdaqprice = str(target[21].text)
	nasdaqchange = str(target[22].text)
	europrice = str(target[75].text)
	eurochange = str(target[76].text)
	ftseprice = str(target[84].text)
	ftsechange = str(target[88].text)
	hangsengprice = str(target[264].text)
	hangsengchange = str(target[265].text)
	nikkeiprice = str(target[309].text)
	nikkeichange = str(target[310].text)

def printReport():
	print "Timestamp: %s" % (time.strftime('%Y-%m-%d %H:%M:%S'))
	print "Futures:"
	print "S&P Support Set: " + gasupport
	print "S&P resistance Set: " + garesistance
	print "DOW Price: " + dowprice
	print "DJIA Change: " + dowchange
	print "S&P 500: " + spprice
	print "S&P 500 Change: " + spchange
	print "NASDAQ: " + nasdaqprice
	print "NASDAQ: Change: "+ nasdaqchange
	print "---"
	print "ROW Futures"
	print "Euro STOXX 50: " + europrice
	print "Euro STOXX 50 Change: " + eurochange
	print "FTSE 100: " + ftseprice
	print "FTSE 100 Change: " + ftsechange
	print "Hang Seng: " + hangsengprice
	print "Hange Seng Change: " + hangsengchange
	print "Nikkei 225: " + nikkeiprice
	print "Nikkei 225 Change: " + nikkeichange 



mySoup = getSoup()
myargs = getArgs()
myFutures = getFutures()
myReport = printReport()






#target = soup.find("tbody", {"tr": "data-future-table-chart-symbol"}).span.contents
#target = soup.find("tr", {"data-future-table-chart-symbol": "SP"}) #close
#target = soup.find("td", {"class": "arrow"}).td.contents

#return target[0]

#futures = scraper(url)
#print futures

# i = 0
# for p in target: #prints all the elements in the target list with line numbers to generate the map that I care about below.
# 	print i, p
# 	i += 1

#Map
#print soup
#print target[3] #prints DJIA current price
#print target[4] #prints DJIA up/down
#S&P 500 min price = 12
#S&P 500 mini change = 13
#NASDAQ price = 21
#NASDAQ change = 22
#Mexican IPC price = 30
#Mexican IPC change = 31
#VG1:IND - Euro STOXX 50 = 75
#EUroStoxx50 change = 76
#FTSE 100, Z 1:IND, price 84, change 85
#GX1:IND - DAX30 = 93, change 94
#XU1:IND - FTSE China A50, price = 264, change 265
#HI1:IND - Hang Seng, price = 273, change = 274
#NK1:IND - Nikkei 225, price = 309, change = 310


