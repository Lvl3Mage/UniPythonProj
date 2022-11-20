def InvertList(lst):
	lst = lst[:]
	for i in range(len(lst)//2):
		temp = lst[i]
		lst[i] = lst[-i-1]
		lst[-i-1] = temp
	return lst
evenList = [1,2,3,4,5,6]
oddList = [1,2,3,4,5,6,7]
print(InvertList(evenList)) # [6, 5, 4, 3, 2, 1]
print(InvertList(oddList)) # [7, 6, 5, 4, 3, 2, 1]
print(evenList) # [1, 2, 3, 4, 5, 6]
print(oddList) # [1, 2, 3, 4, 5, 6, 7]