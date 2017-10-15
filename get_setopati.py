import urllib2
from lxml import etree
import datetime



def get_news(url,xpath):
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
        req = urllib2.Request(url, headers=hdr)
	response = urllib2.urlopen(req)
	htmlparser = etree.HTMLParser()
	tree = etree.parse(response, htmlparser)
	for news in tree.xpath(xpath):
		print "News Title:",news.text
		print "News Source:",url.split('https://www.')[1].split('.com')[0]
		print "Date:",datetime.date.today()
		
		
get_news("https://www.setopati.com/","//h2[contains(@class,'specialmainnews')]/a")
get_news("https://www.onlinekhabar.com/","//div[@id='mst']//div[contains(@class,'news_loop')]//h3")


