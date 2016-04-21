from bs4 import BeautifulSoup
import urllib2
import html5lib
import time


#url = 'http://www.cnbc.com/pre-markets/'
url = 'http://www.bloomberg.com/markets/stocks/futures'

page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html5lib')
target = soup.find("tr", {"class": "data-table__row"}) #gets DJIA instead of S&P 500
target = soup.find_all("td")

print "Timestamp: %s" % (time.strftime('%Y-%m-%d %H:%M:%S'))
print "Futures:"
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


