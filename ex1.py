def piglatin():
	words = input(">")
	words = words.lower()
	words = words.split(' ')
	word2 = []
	print (words)
	for word in words:
		wordlist = list(word)
		if wordlist[0] == 'a'or wordlist[0] =='e'or wordlist[0] =='i'or wordlist[0] =='o'or wordlist[0] =='u':
			wordlist.append('hay')
			wordlisted = ''.join(wordlist)
			word2.append(wordlisted)
			print (word2)
		elif wordlist[0] == 'q' and wordlist[1] == 'u':
			wordlist.pop(0)
			wordlist.pop(1)
			wordlist.append('quay')
			wordlisted = ''.join(wordlist)
			word2.append(wordlisted)
			print (word2)
		elif wordlist[0] != 'a'and wordlist[0] !='e'and wordlist[0] !='i'and wordlist[0] !='o'and wordlist[0] !='u'and wordlist[0] != 'q' :
			i = 0
			while wordlist[0] != 'a'and wordlist[0] !='e'and wordlist[0] !='i'and wordlist[0] !='o'and wordlist[0] !='u'and wordlist[0] !='y':
				print (wordlist)
				print (i)
				a = wordlist[0]
				wordlist.pop(0)
				wordlist.append(a)
				i = i + 1
				if i > len(words):
					break
			wordlist.append('ay')
			wordlisted = ''.join(wordlist)
			word2.append(wordlisted)
			print (word2)

		else :
			pass

PigLatin = piglatin()
