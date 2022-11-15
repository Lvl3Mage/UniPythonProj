def RemoveDuplicates(vals):
	indivVals = []
	for val in vals:
		if (val not in indivVals):
			indivVals.append(val)
	return indivVals
print(RemoveDuplicates([1,5, 2,3,4,5,6,7,8,9, 3, 5, 10, 2])) # [1, 5, 2, 3, 4, 6, 7, 8, 9, 10]