def dic(file):
	d = {}
	with open(file) as f :
		cont = f.read().rstrip().split(" ")
		for word in cont:
			if word[0] in d:
				d[word[0]].append(word)
			else:
				d[word[0]] = [word]

	return d



#print dic("file.txt")
