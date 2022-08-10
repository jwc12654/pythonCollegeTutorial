def mostCommonName(L):
	names = {}
	maxVal = 0
	itm = ""
	s = set()
	if len(L) == 0:
		return None
	for item in L:
		names[item] = names.get(item,0)+1
		if names[item] > maxVal:
			maxVal = names[item]
			itm = item 
	for item in names:
		if names[item] == maxVal:
			s.add(item)
	if len(s) == 1: 
		return itm 

	return s
	