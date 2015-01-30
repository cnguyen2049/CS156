
import sys

inputFile = sys.argv[1]
#heuristic = sys.argv[2]

plane = ''
airport = 'P'
fuelCost = 0;

"""
Beginning to write function to read in the text file
"""
def readFile(inputFile):
	inputMap = open(inputFile,'r')
	startingMap = []
	for line in inputMap:
		eachRow = []
		for character in line:
			if line != '\n':
				eachRow.append(character)
		startingMap.append(eachRow)	
	return startingMap


def printOut(startingMap):
	output = ""
	for eachRow in startingMap:
		for element in eachRow:
			output = output + element
	return output

def locationFinder(startingMap,item):
	y = 0
	for eachRow in startingMap:
		x = 0
		for column in eachRow:
			#print column
			if column == item: 
				return x,y
			x = x + 1
			#print "X is %d" %(x)
		y = y + 1
		#print "Y is %d" %(y)
	
input1 = readFile(inputFile)
out = printOut(input1)
print out 
location = locationFinder(input1,'P')
print location
