def DivList(vals, divVal):
	bottomVals = []
	topVals = []
	for val in vals:
		if(val < divVal):
			bottomVals.append(val)
		else:
			topVals.append(val)
	return (bottomVals, topVals)
print(DivList([1,2,3,4,5,6,7,8,9], 5)) #([1, 2, 3, 4], [5, 6, 7, 8, 9])