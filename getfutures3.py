#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib2
import html5lib
import time
from argparse import ArgumentParser 
from colorama import init, Fore, Back, Style
import re
from ConfigParser import SafeConfigParser


init(autoreset=True) #needed to clear and initalize colorama

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
gacolorize = ""
gaini=""
duperrormessage  = "YOU SPECIFIED SUPPORT AND RESISTANCE LEVELS VIA BOTH -s -r, and -i.  OVERRIDING WITH -I SETTINGS!"

def getArgs(): #returns command line arguments; support, resistance, colorize
	global gasupport, garesistance, gacolorize, gaini
	parser = ArgumentParser(description = 'Get Futures')
	parser.add_argument("-s", "--support", required=False, dest="support", help="Initialize S&P support level", metavar="support")
	parser.add_argument("-r", "--resistance", required=False, dest="resistance", help="Initialize S&P resistance level", metavar="resistance")
	parser.add_argument("-c", "--colorize", required=False, action="store_true", dest="colorize", help="Colorize support and resistance")
	parser.add_argument("-i", "--ini", required=False, action="store_true", dest="ini", help="Specify to use config.ini file (overrides -s -r)")
	args = parser.parse_args()
	gasupport = args.support
	garesistance = args.resistance
	gacolorize = args.colorize
	gaini = args.ini
	return (gasupport, garesistance, gacolorize)

def getSoup(): #returns a soup'd web-page 
	global url, target
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page, 'html5lib')
	target = soup.find("tr", {"class": "data-table__row"}) #gets DJIA instead of S&P 500
	target = soup.find_all("td")

def getFutures(): #returns futures pricies that I previously mapped by outputting everything to a txt file and tagging individual lines so that I could find everything  
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
	print "S&P 500: " + (spprice)
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

def sppRangeBound(): # sets spprice to yellow alert
	global spprice
	spprice = (Style.BRIGHT + Fore.YELLOW + spprice)

def sppSupportBroken(): # sets support level break to red to indcate broken support level, and current price to red 
	global spprice, gasupport
	spprice = (Style.BRIGHT + Fore.RED + spprice)
	gasupport = (Style.BRIGHT + Fore.RED + gasupport)

def sppResistanceBroken(): #sets resistance level break to red, and current price to greet
	global spprice, garesistance
	spprice = (Style.BRIGHT + Fore.GREEN + spprice)
	garesistance = (Style.BRIGHT + Fore.RED + garesistance)

def gaConfigParser(): #parses a config.ini file for sp_levels and supplies them if -s ABCD -r XYZA are not set.
	global gasupport, garesistance
	parser = SafeConfigParser()
	parser.read('config.ini')
	gasupport = parser.get('sp_levels', 'support')
	garesistance = parser.get('sp_levels', 'resistance')


mySoup = getSoup()
myargs = getArgs()
myFutures = getFutures()
spprice2 = spprice.replace(',','') #there was a comma in there making it non-numeric

if gasupport >= 0 or garesistance >=0: #if you've specified -s 
	if gaini is True:
		print (Style.BRIGHT + Fore.YELLOW + duperrormessage)
		gaConfigParser()
else:
	gaConfigParser()

if gacolorize is True:
	if  spprice2 >= gasupport and spprice2 <= garesistance: #if the current price is between suppor and resistance run the sppragebound
			sppRangeBound()
			myReport = printReport()
	elif spprice2 <= gasupport: #if support level has broken
			sppSupportBroken()
			myReport = printReport()
	elif spprice2 >= garesistance: #if resistance level has broken
			sppResistanceBroken()
			myReport = printReport()
else:
	myReport = printReport() #if colorize flag not set, just print the report


