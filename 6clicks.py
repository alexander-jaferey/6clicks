import urllib2

print "Choose your destination"

userInput = raw_input("Point me to a valid Wikipedia article title. '<A_Title>' I trust you.\n")
userDest = "http://en.wikipedia.org/w/index.php?title=" + userInput + "&printable=yes"
response = urllib2.urlopen(userDest)
destArticle = response.read()

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