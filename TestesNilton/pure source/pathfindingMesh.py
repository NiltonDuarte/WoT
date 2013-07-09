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
	
	def A_Star_Algorithm(self, initPoint):
		
		path = []
		return path


mesh = Mesh()
print "\n",mesh.meshMatrix
