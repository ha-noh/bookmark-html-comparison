#html files to compare
original = open("bookmark files/original.html", "r")
modified = open("bookmark files/", "r")

#extract href attributes from a file and store their urls

#compare two lists of urls
#(1) list urls present in 'original' but not in 'modified' under 'Removed'
#(2) list urls present in 'modified' but not in 'original' under 'Added'