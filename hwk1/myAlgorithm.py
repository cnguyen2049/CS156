#Shunt
import sys
import heapq

inputFile = sys.argv[1]
#heuristic = sys.argv[2]

values ={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9}



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
	test = []
	for eachRow in startingMap:
		test.append(eachRow)
		for element in eachRow:
			output = output + element
	return test

"""
This function finds the coordinates of the air plane
and fuel
"""
def planeFinder(startingMap,item):
	global startX , startY
	y = 0
	for eachRow in startingMap:
		x = 0
		for column in eachRow:
			for key in values:
				if column == key: 
					startX = x
					startY = y
					return values[key]
			x = x + 1
			#print "X is %d" %(x)
		y = y + 1
		#print "Y is %d" %(y)

"""
A node function 
"""

def Node(coordinates,heuristic):
	return coordinates,heuristic

"""
Beginning to implement A star algorithm
"""
def astar (node,start,goal): #start and goal will be coordinates
	frontier = []
	frontier.put(start,0);
	openList = []
	closedList = []
	accumulated_cost = []
	openList = None
	accumulated_cost = []
	


input1 = readFile(inputFile)
out = printOut(input1)
location = planeFinder(input1,values)
print "X is %d " %(startX)
print "Y is %d " % (startY)



"""
Sample code for heap in python
pushing and adding to heap
"""
print location
heap = []
testNode = Node(7,(startX,startY))
testNode2 = Node(5,(5,5))
heapq.heappush(heap,testNode)
heapq.heappush(heap,testNode2)
#heapq.heapify(heap)
getValue = heapq.heappop(heap)[0]
print getValue


