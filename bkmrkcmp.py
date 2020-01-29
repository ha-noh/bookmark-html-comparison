#html files to compare
original = open("original.html", "r", encoding="utf-8")
modified = open("modified.html", "r", encoding="utf-8")

#extract href attributes from a file and store their urls
def storeURLs(file):
	list = []
	for line in file:
		if "HREF" in line:
			list.append( extractURL(line) )
	return list

#takes a string as input and outputs the URL inside as a string based on instances of "
def extractURL(line):
	substring = line.split("HREF=\"")[1].split("\"")[0]
	return substring

originalURLs = storeURLs(original)
modifiedURLs = storeURLs(modified)

#compare two lists of urls
#(1) list urls present in 'original' but not in 'modified' under 'Removed'
#(2) list urls present in 'modified' but not in 'original' under 'Added'
removedURLs = []
addedURLs = []

results = open("results.txt","w")
results.write("Removed URLs: \n")
for url in originalURLs:
	results.write(url + "\n")
#results.write("Added URLS: \n")
