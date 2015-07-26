# import urllib2
from urllib.request import urlopen
import urllib.request
# from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup


opener = urllib.request.FancyURLopener({})
url = "http://stackoverflow.com/"
f = opener.open(url)
content = f.read()
print(content[:50])


print(' --- ')
opener = urllib.request.FancyURLopener({})
url = "http://raleigh.craigslist.org/search/sss"
f = opener.open(url)
content = f.read()
print(content[:50])
print(' ')

# urlpage = urlopen('http://raleigh.craigslist.org/search/sss')


soup = BeautifulSoup(content, 'html.parser')

# soup = BeautifulSoup(urlopen('http://raleigh.craigslist.org/search/sss', 'html_parser').read())

# print(soup({'class':'hdrlink'}))
# print(soup.find(class="hdrlink"))
# print(soup.findAll("span", { "class" : "pl" }))

for thing in soup.findAll("span", { "class" : "price" }):
	print(thing.text)

	# tds = row('td')
	# print(tds[0].string)
