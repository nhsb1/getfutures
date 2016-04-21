from bs4 import BeautifulSoup
import urllib2
import html5lib
import wget


url = 'http://www.cnbc.com/pre-markets/'

#def scraper(self):
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

getsoup = wget.download(url)
#target = soup.find("tbody", {"tr": "data-future-table-chart-symbol"}).span.contents
#target = soup.find("tr", {"data-future-table-chart-symbol": "SP"}) #close
#target = soup.find("td", {"class": "arrow"}).td.contents

#return target[0]

#futures = scraper(url)
#print futures

#print soup
print getsoup