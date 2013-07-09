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
	
	@staticmethod
	def getLowerScore(scoreList, useSet):
		aux = [None, 10**10]
		for i in range(len(useSet)):
			if aux[1] > scoreList[useSet[i]] and scoreList[useSet[i]] != None:
				aux[1] = scoreList[useSet[i]]
				aux[0] = useSet[i]
		if aux[0] in useSet:
			return aux[0]
	
	@staticmethod		
	def getNeighbors(node, N):
		indexI = (node-1)/N
		indexJ = (node-1)%N
		
		neighbors = []
		
		if indexI > 0:
			neighbors.append(1+indexJ+(N*(indexI-1)))
		if indexJ > 0:
			neighbors.append(indexJ+(N*indexI))
		if indexI < N-1:
			neighbors.append(1+indexJ+(N*(indexI+1)))
		if indexJ < N-1:
			neighbors.append(2+indexJ+(N*indexI))
		
		return neighbors
	
	@staticmethod
	def reconstructPath(cameFrom, node, goal):
		if (node in cameFrom or node == goal) and cameFrom[node] != None:
			p = Mesh.reconstructPath(cameFrom, cameFrom[node], goal)
			return p+[node]
		else:
			return [node]
	
	def A_Star_Algorithm(self, initCell, goalCell):
		"""A* algorithm for path finding"""
		usedSet = []			#The set of nodes already evaluated
		toUseSet = [initCell]	#The set of nodes to be used
		cameFrom = [None for i in range((self.rangeI*self.rangeJ)+1)]	#This holds each node's father
		
		score = [10 for i in range((self.rangeI*self.rangeJ)+1)]		#This holds cell's weight
		score[initCell] = 0
		
		while len(toUseSet):
			currentCell = Mesh.getLowerScore(score, toUseSet)
			if currentCell == goalCell:
				return Mesh.reconstructPath(cameFrom, goalCell, goalCell)
			
			toUseSet.remove(currentCell)
			usedSet.append(currentCell)
			neighborNodes = Mesh.getNeighbors(currentCell, self.rangeI)
			
			for neighbor in neighborNodes:
				indexI = (neighbor-1)/self.rangeI
				indexJ = (neighbor-1)%self.rangeJ
				auxScore = score[currentCell] + self.meshMatrix[indexI][indexJ][WEIGHT]
				
				if neighbor in usedSet and auxScore >= score[neighbor]:
					continue
				
				if neighbor not in toUseSet or auxScore < score[neighbor]:
					cameFrom[neighbor] = currentCell
					score[neighbor] = auxScore
					if neighbor not in toUseSet:
						toUseSet.append(neighbor)
		
		return False
		


mesh = Mesh()
print "\n",mesh.meshMatrix
print mesh.A_Star_Algorithm(1, 83)
