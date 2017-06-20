from dictionary import dic

word = raw_input()

dic= dic("file.txt")

if word[0] in dic and word in  dic[word[0]]:
	print "Valid word"
else:
	print "Invalid word"
