#Shunt
import sys
import heapq

inputFile = sys.argv[1]
#heuristic = sys.argv[2]

letters ={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9}
numbers ={1:'A',2:'B',3'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I'}
goal = {'H':'H'}

class Node:
	def __init__(self,x,y,fuel,state,cost):
		self.x = x
		self.y = y
		self.fuel = fuel
		self.state = state
		self.cost = cost
		self.nextEl = None
	def get_self(self):	
		return self.fuel;
	def getNext():
		return self.nextEl


findKey(values,2)

class PriorityQueue:
	def __init__(self):
		self.elements = []
	def empty(self):
		return len(self.elements) == 0
	def length(self):
		return len(self.elements)
	def put(self, item,priority):
		heapq.heappush(self.elements,(priority,item))
	def get(self):
		return heapq.heappop(self.elements)[1]

def buildNode(x,y,fuel,state,cost):
	n = Node(x,y,fuel,state,cost)
	return n

MakeNode2 = buildNode(1,2,3,'A',5)
print MakeNode2.state
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
This function finds the coordinates
and the starting value of the fuel
"""
def Finder(startingMap,item):
	y = 0
	for eachRow in startingMap:
		x = 0
		for column in eachRow:
			for key in values:
				if column == key:
					return x,y,values[key]
			x = x + 1
			#print "X is %d" %(x)
		y = y + 1
		#print "Y is %d" %(y)


def euclidian(airplane,airport):
	x = airplane.x - airport.x
	y = airplane.y - airport.y
	euclidian = math.sqrt(x*x + y * y)
	return euclidian

def manhattan(airplane,airport):
	x = airplane.x - airport.x
	y = airplane.y - airport.y
	manhattan = abs(x) + abs(y)
	return manhattan

"""
Beginning to implement A star algorithm
"""
def can_move(Node,cost):
	if(Node.fuel-cost>0):
		return true
	else:
		return false



input1 = readFile(inputFile)

def astar (weather,start): #start and goal will be coordinates
	openList = PriorityQueue()
	openList.put(start,0);
	closedList = set()

	
	
	


#input1 = readFile(inputFile)
out = printOut(input1)
location = Finder(input1,values)




"""
Sample code for heap in python
pushing and adding to heap
"""



