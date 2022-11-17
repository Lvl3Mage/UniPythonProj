from test_module import test

def MaxRepetitions(string, query):
	maxOccurrences = 0
	queryLen = len(query)
	i = 0
	while i < len(string) - queryLen+1:
		if(string[i:i+queryLen] == query): # iterate until match
			match = True
			occurrences = 1
			j = queryLen
			while i+j+queryLen < len(string)+1 and match:# iterate with step = query length until a mismatch is found
				match = string[i+j:i+j+queryLen] == query
				if(match):
					occurrences += 1
				j+= queryLen
			if(occurrences > maxOccurrences):
				maxOccurrences = occurrences
		i+=1
	if(maxOccurrences == 0):
		maxOccurrences = None
	return maxOccurrences
	# El código de la función debe ir aquí
def MaxRepetitionsCAG(dnaString): # an alias for MaxRepetitions(dnaString, "CAG")
    return MaxRepetitions(dnaString, "CAG")
# –- Unit tests –-
if __name__== '__main__':
	  
	test(MaxRepetitionsCAG('GACGAC') == None)
	test(MaxRepetitionsCAG('CAGCAG') == 2)
	test(MaxRepetitionsCAG('TACGTACGTAT') == None)
	test(MaxRepetitionsCAG('CAGCAGTACCTCAGACGT') == 2)
	test(MaxRepetitionsCAG('GATCGATCGATGCTAGCTAGCGCATC') == None)
	test(MaxRepetitionsCAG('TACTCAGCAGGATGCAGCAGCAGCAGCAG') == 5)
