from bs4 import BeautifulSoup
import urllib2
import html5lib
import time


#url = 'http://www.cnbc.com/pre-markets/'
url = 'http://www.bloomberg.com/markets/stocks/futures'

#def scraper(self):
page = urllib2.urlopen(url)
#soup = BeautifulSoup(page, 'html.parser')
soup = BeautifulSoup(page, 'html5lib')
target = soup.find("tr", {"class": "data-table__row"}) #gets DJIA instead of S&P 500
#target2 = soup.find("tbody", {"class": "data-table__body"}) #gets the entire America's table
#target2 = soup.find_all("tbody", {"class": "data-table__body"}) #finds a bunch of stuff
target3 = soup.find_all("td")

print "Timestamp: %s" % (time.strftime('%Y-%m-%d %H:%M:%S'))
print "Futures:"
print "DJIA: " + str(target3[3].text)
print "DJIA Change: " + str(target3[4].text)
print "S&P 500: " + str(target3[12].text)
print "S&P 500 Change: " + str(target3[13].text)
print "NASDAQ: " + str(target3[21].text)
print "NASDAQ: Change: "+ str(target3[22].text)
print "---"
print "ROW Futures"
print "Euro STOXX 50: " + str(target3[75].text)
print "Euro STOXX 50 Change: " + str(target3[76].text)
print "FTSE 100: " + str(target3[84].text)
print "FTSE 100 Change: " + str(target3[85].text)
print "Hang Seng: " + str(target3[264].text)
print "Hange Seng Change: " + str(target3[265].text)
print "Nikkei 225: " + str(target3[309].text)
print "Nikkei 225 Change: " + str(target3[310].text) 


#target = soup.find("tbody", {"tr": "data-future-table-chart-symbol"}).span.contents
#target = soup.find("tr", {"data-future-table-chart-symbol": "SP"}) #close
#target = soup.find("td", {"class": "arrow"}).td.contents

#return target[0]

#futures = scraper(url)
#print futures

 i = 0
 for p in target3: #prints all the elements in the target3 list with line numbers to generate the map that I care about below.
 	print i, p
 	i += 1



