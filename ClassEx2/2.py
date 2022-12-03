def splitStr(string, query):
	queryRes = []
	elemStart = -1
	for i in range(len(string)):
		char = string[i]
		if(char == query):
			if(i > elemStart+1):
				queryRes.append(string[elemStart+1:i])
			elemStart = i
		elif(i == len(string)-1):
			if(i >= elemStart+1):
				queryRes.append(string[elemStart+1:i+1])
	return queryRes
def ReadData(filename):
	file = open(filename, "r")
	data = []
	for line in file:
		row = splitStr(line.strip(), "#")
		row[0] = int(row[0])
		row[1] = int(row[1])
		data.append(row)

	file.close()
	return data
def QueryTopNames(year, gender, amount):
	pass
print(ReadData("data.txt"))
# import random
# names = [("LUCIA","F"), ("HUGO","M"), ("MATEO","M"), ("SOFIA","F"), ("ALEJANDRO","M"), ("DANIEL","M")]
# for i in range(20, 10, -1):
# 	for j in range(1,20):
# 		name = random.choice(names)
# 		print("20{0}#{1}#{2}#{3}".format(i,j,name[0],name[1]))

