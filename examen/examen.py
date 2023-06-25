def ReadDataFromFile(filename):
	# Created dataMat to store file data
	dataMat = []


	file = open(filename, "r")

	line = file.readline()

	while(line != ''):
		
		
		#removes the \n at the end if it's present
		if(line[-1] == "\n"):
			line = line[:-1]

		#get all the values from the line
		lineValues = SplitBy(line, "#")


		#add values to matrix
		dataMat.append(lineValues)

		line = file.readline()

	file.close()

	return dataMat


def SplitBy(stringToSplit, splitChar): # abcd#abc#123
	splitValues = []

	lastValue = '' # contains latest value after split

	for char in stringToSplit:
		if(char == splitChar):
			splitValues.append(lastValue)
			lastValue = ''
		else:
			lastValue += char

	if(lastValue != ''):
		splitValues.append(lastValue)

	return splitValues

TEAM_A_INDEX = 0
SCORE_A_INDEX = 1
TEAM_B_INDEX = 2
SCORE_B_INDEX = 3

def SummaryTeam(teamName, data): # returns the following list: [golesAFavor, golesEnContra, Puntos]

	totalScoredFor = 0
	totalScoredAgainst = 0
	totalPoints = 0

	for match in data:
		# if team played in match
		if(teamName in match): 
			scoredFor = 0;
			scoredAgainst = 0

			if(match[TEAM_A_INDEX] == teamName): # team has played on the A side
				scoredFor = int(match[SCORE_A_INDEX])
				scoredAgainst = int(match[SCORE_B_INDEX])

			elif(match[TEAM_B_INDEX] == teamName): # team has played on the B side
				scoredFor = int(match[SCORE_B_INDEX])
				scoredAgainst = int(match[SCORE_A_INDEX])

			# adding scores to totals
			totalScoredFor += scoredFor
			totalScoredAgainst += scoredAgainst

			#adding points
			if(scoredFor > scoredAgainst):#if won
				totalPoints += 3
			elif(scoredFor == scoredAgainst):# if draw
				totalPoints += 1


	return [totalScoredFor, totalScoredAgainst, totalPoints]


MatchData = ReadDataFromFile("resultadosprimera.txt")

print(SummaryTeam("Getafe", MatchData))
# Example data
# [
# 	['Celta de Vigo', '0', 'Malaga', '1'],
# 	['Sevilla', '2', 'Getafe', '1'],
# 	['Mallorca', '2', 'Espanyol', '1'],
# 	['Espanyol', '3', 'Mallorca', '2'],
# 	['Granada', '2', 'Rayo Vallecano', '0'],
# 	['Getafe', '1', 'Sevilla', '1']
# ]