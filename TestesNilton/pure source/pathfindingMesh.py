import xml.etree.ElementTree as ET
"""This file receives an XML mesh and generete the mesh for navigation"""

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
WEIGHT = 4




class Mesh:
	"""Mesh class, a mesh is a matrix that fit our terrain"""
	def __init__(self, fileXML = "terrain.xml"):
		self.fileXML = fileXML
		self.xmlTree = ET.parse(fileXML)
		self.xmlRoot = self.xmlTree.getroot()
		self.rangeI = int(self.xmlRoot.find("Data").find("DivsX").text)
		self.rangeJ = int(self.xmlRoot.find("Data").find("DivsY").text)
		#print "rangeI, rangeJ = ",self.rangeI, ",", self.rangeJ
		#This is a 4D matrix, the 2D part is the cell index, the 3D the cell data, and 4D the cell points
		#meshMatrix[i][j][UP][0] is the x position of the point UP in cell ij 
		self.meshMatrix = [[[[None,None],[None,None],[None,None],[None,None],1] for j in range(self.rangeJ)]for i in range(self.rangeI)]
		self.initMesh()
		

	def initMesh(self):
		"""Read the XML file, fill the matrix with the points on XML"""	
		cellsET = self.xmlRoot.find("Cells")
		for cell in cellsET.findall("Cell"):
			i = (int(cell.find("Index").text)-1)/self.rangeI
			j = (int(cell.find("Index").text)-1)%self.rangeI
			print "[i][j] = [",i,"][",j,"]"
			indexAux = 0
			for point in cell.findall("Point"):
				self.meshMatrix[i][j][indexAux][0] = float(point.find("Pos").text[1:-1].split(',')[0])
				self.meshMatrix[i][j][indexAux][1] = float(point.find("Pos").text[1:-1].split(',')[1])
				indexAux += 1
	
	def getLowerScore(self, scoreList, useSet):
		"""Gets the element whose score is lower than ever"""
		aux = [None, 10**10]
		for i in range(len(useSet)):
			if aux[1] > scoreList[useSet[i]] and scoreList[useSet[i]] != None:
				aux[1] = scoreList[useSet[i]]
				aux[0] = useSet[i]
		if aux[0] in useSet:
			return aux[0]
			
	def getNeighbors(self, node):
		"""Gets neighbors from given node"""
		indexI = (node-1)/self.rangeI
		indexJ = (node-1)%self.rangeJ
		
		neighbors = []
		
		#These above only work if self.rangeI equals to self.rangeJ		
		if indexI > 0:
			neighbors.append(1+indexJ+(self.rangeI*(indexI-1)))
		if indexJ > 0:
			neighbors.append(indexJ+(self.rangeI*indexI))
		if indexI < self.rangeI-1:
			neighbors.append(1+indexJ+(self.rangeI*(indexI+1)))
		if indexJ < self.rangeI-1:
			neighbors.append(2+indexJ+(self.rangeI*indexI))
		
		return neighbors
	
	def reconstructPath(self, cameFrom, node, goal):
		"""Reconstruct the path"""
		if (node in cameFrom or node == goal) and cameFrom[node] != None:
			p = self.reconstructPath(cameFrom, cameFrom[node], goal)
			return p+[node]
		else:
			return [node]
			
	def getCell(self, x, y):
		"""Gives the cell where is an element in position x,y"""
		#Distance from two points of two different cells for getting cell dimension 
		distFromBorder = (self.meshMatrix[1][0][UP][1]-self.meshMatrix[0][0][DOWN][1])/2
		cellHeight = 4*distFromBorder	#Cell dimension
		cellIndexJ = 0
		cellIndexI = 0
		
		#Normalize x,y between 0 and 200, 'cause x,y are between -100 and 100
		normX = x + (self.rangeI*cellHeight)/2
		normY = y + (self.rangeJ*cellHeight)/2
		
		for j in range(self.rangeJ):
			cellColumn = j+1
			#If the x belongs to a given cell
			if normX > 0 and normX > (cellColumn-1)*cellHeight and normX < cellColumn*cellHeight:
				cellIndexJ = cellColumn-1
				break
		for i in range(self.rangeI):
			cellRow = i+1
			#If the y belongs to a given cell
			if normY > 0 and normY > (cellRow-1)*cellHeight and normY < cellRow*cellHeight:
				cellIndexI = cellRow-1
				break

		#Once again, this only works if self.rangeI equals to self.rangeJ
		cell = 1 + cellIndexJ + (self.rangeI*cellIndexI)
		
		return cell
			
	
	def A_Star_Algorithm(self, xTroop, yTroop, goalCell):
		"""A* algorithm for path finding"""
		initCell = self.getCell(xTroop, yTroop)
		
		usedSet = []			#The set of nodes already evaluated
		toUseSet = [initCell]	#The set of nodes to be used
		cameFrom = [None for i in range((self.rangeI*self.rangeJ)+1)]	#This holds each node's father
		
		#10 is any value greater than our greatest weight
		score = [10 for i in range((self.rangeI*self.rangeJ)+1)]		#This holds cell's weight
		score[initCell] = 0
		
		while len(toUseSet):
			currentCell = self.getLowerScore(score, toUseSet)
			if currentCell == goalCell:
				#Goal cells usually are from last column, as the last possible value for indexJ
				return self.reconstructPath(cameFrom, goalCell, goalCell)
			
			toUseSet.remove(currentCell)
			usedSet.append(currentCell)
			neighborNodes = self.getNeighbors(currentCell)	#Neighbors list for visiting
			
			for neighbor in neighborNodes:
				indexI = (neighbor-1)/self.rangeI
				indexJ = (neighbor-1)%self.rangeJ
				auxScore = score[currentCell] + self.meshMatrix[indexI][indexJ][WEIGHT]
				
				if neighbor in usedSet and auxScore >= score[neighbor]:
					continue	#Does nothing and go on to the next neighbor on the list
				
				if neighbor not in toUseSet or auxScore < score[neighbor]:
					cameFrom[neighbor] = currentCell	#Let's write down our sequences of cells
					score[neighbor] = auxScore
					if neighbor not in toUseSet:
						toUseSet.append(neighbor)
		
		return False
		
	def getPointsSequence(self, cellSequence):
		pointsSequence = []
		
		auxIndexI = 0
		auxIndexJ = 0
		
		for i in range(len(cellSequence)):
			indexI = (cellSequence[i]-1)/self.rangeI
			indexJ = (cellSequence[i]-1)%self.rangeJ
			point = []
			
			if auxIndexI < indexI:
				point = self.meshMatrix[indexI][indexJ][UP]
			elif auxIndexI > indexI:
				point = self.meshMatrix[indexI][indexJ][DOWN]
			elif auxIndexJ < indexJ:
				point = self.meshMatrix[indexI][indexJ][LEFT]
			elif auxIndexJ > indexJ:
				point = self.meshMatrix[indexI][indexJ][RIGHT]
			
			pointsSequence.append(point)
			auxIndexI = indexI
			auxIndexJ = indexJ
			
		return pointsSequence


mesh = Mesh()
print "\n",mesh.meshMatrix
cellSequence = mesh.A_Star_Algorithm(-72, -72, 83)
print cellSequence
print mesh.getPointsSequence(cellSequence)