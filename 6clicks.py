import urllib2
from bs4 import BeautifulSoup

print "Choose your destination"

CLICKS = 6

userInput = raw_input("Point me to a valid Wikipedia article title. '<A_Title>' I trust you.\n")
USERDEST = "http://en.wikipedia.org/w/index.php?title=" + userInput + "&printable=yes"
response = urllib2.urlopen(USERDEST)
DESTARTICLE = response.read()
soup = BeautifulSoup(DESTARTICLE, 'html.parser')

DESTTITLE = soup.title

print "Choose your source"

userInput = raw_input("Random starting point? y/n\n")

if userInput == "y":
	response = urllib2.urlopen('http://en.wikipedia.org/w/index.php?title=Special:Random&printable=yes')
	sourceArticle = response.read()
else:
	userInput = raw_input("Point me to a valid Wikipedia article title. '<A_Title>' I trust you.\n")
	userSource = "http://en.wikipedia.org/w/index.php?title=" + userInput + "&printable=yes"
	response = urllib2.urlopen(userSource)
	sourceArticle = response.read()

'''
Html source, Clicks left -> Success or Fail

From html source, present links to user.
Will either return a success or failure if correct article is not reached in
the given amount of clicks.

'''
def PickLinksIn(articleSource, CLICKS):

	soup = BeautifulSoup(articleSource, 'html.parser')

	# If the user picked the destination, terminate
	if DESTTITLE == soup.title:
		print "Success!"
		return "Success!"

	# If user ran out of clicks, terminate
	if CLICKS <= 1:
		print "Sorry, you did not reach your article in the clicks allotted.."
		return "Fail!"
	CLICKS -= 1

	print "Which link will you follow?"

	# Gets the text and link of every anchor tag within an article that refs
	# another wiki page.
	links = [{
			  "name": a.string,    \
			  "link": a.get('href')\
			 } \
			 for a in soup.find_all('a')\
			 if a.get('href') is not None and "/wiki/" in a.get('href')\
			    and  a.string is not None and "#" not in a.get('href')]

	# Iterates through each link to show user the options.
	counter = 1
	for a in links:
		try:
			print str(counter) + " : " + a['name']
			print "\t" + a['link'][:50] + "...."
			counter += 1
		except:
			continue

	# Gets the user input
	link_number = int(raw_input("Number?\n"))
	# The link the user referenced
	link_href = links[link_number-1]['link']

	# Otherwise, recurr!
	if link_href[:5] == "/wiki":
		link_href = "http://en.wikipedia.org" + link_href
	response = urllib2.urlopen(link_href)
	sourceArticle = response.read()

	PickLinksIn(sourceArticle, CLICKS)

PickLinksIn(sourceArticle, CLICKS)
