import xml.etree.ElementTree as ET
from camera import *
from pandaImports import *

"""This is a standalone program that receive an egg file and generate a navigation mesh in XML that wil be read in WoT game"""

#Setting the size of our game screen
wp = WindowProperties()
window_Width = 1200
window_Height = 640
wp.setSize(window_Width, window_Height)
base.win.requestProperties(wp)

camera = MyCamera()


class LoadTerrainModel(DirectObject):
	'''This class imports the terrain model and do the needed transformations
	   to show it on the game screen.
	'''
	def __init__(self, modelPath):
		#Loading the terrain model
		self.terrain = loader.loadModel(modelPath)
		self.terrain.reparentTo(render)
		#Setting the texture to the terrain
		#self.texture = loader.loadTexture("../texturas/terrain_Texture.png")
		#self.terrain.setTexture(self.texture, 1)
		#Setting the position of the terrain
		self.position = Vec3(0, 0, 0)
		self.terrain.setPos(self.position)

		self.terrainBoundLower, self.terrainBoundUpper = self.terrain.getTightBounds()
		self.terrainCornerX, self.terrainCornerY = self.terrainBoundLower[0], self.terrainBoundLower[1]
		self.terrainSizeX = self.terrainBoundUpper[0] - self.terrainBoundLower[0]
		self.terrainSizeY = self.terrainBoundUpper[1] - self.terrainBoundLower[1]
		

	
class MeshGen:

	def __init__(self, outname, terrainModel, cellSizeX = False, cellSizeY = False , xDivs = False , yDivs = False ):
		self.terrainModel = terrainModel
		self.outname = outname
		if cellSizeX and cellSizeY:
			self.cellSizeX = cellSizeX
			self.cellSizeY = cellSizeY
			self.xDivs = int(terrainModel.terrainSizeX / cellSizeX)
			self.yDivs = int(terrainModel.terrainSizeY / cellSizeY)
		elif xDivs and xDivs: 
			self.xDivs = xDivs
			self.yDivs = yDivs
			self.cellSizeX = terrainModel.terrainSizeX / xDivs
			self.cellSizeY = terrainModel.terrainSizeY / yDivs
		else: return "error"

	def genMesh(self):
		"""
		 p = (xDivIndex*cellSizeX , yDivIndex*cellSizeY)
		 p______________
		 |			    |		p1 = p + (cellSizeX/2, cellSizeY/4)
		 |      p1      |		p2 = p + (cellSizeX/4, cellSizeY/2)
		 |			    |		p3 = p + (cellSizeX/2, cellSizeY*3/4)
		 |  p2      p4  |		p4 = p + (cellSizeX*3/4, cellSizeY/2)
		 |			    |
		 |      p3      |
		 |______________|

		 cell 1       cell 2       cell 3 ... cell  xDivs
		 cell xDivs+1 cell xDivs+2        ... cell 2*xDivs
		 .                                      .
		 .                                      .
		 .                                      .
		 cell (yDivs-1)*xDivs+1           ... cell yDivs*xDivs 
		"""
		meshET = ET.Element('Mesh')
		cellsET = ET.SubElement(meshET,'Cells')
		p1 = p2 = p3 = p4 = center = 0
		cellIndex = 1
		for yDivIndex in range(self.yDivs):
			for xDivIndex in range(self.xDivs):
				pX = terrainModel.terrainCornerX + xDivIndex*self.cellSizeX
				pY = terrainModel.terrainCornerY + yDivIndex*self.cellSizeY
				p1 = (pX + self.cellSizeX/2, pY + self.cellSizeY/4)
				p2 = (pX + self.cellSizeX/4, pY + self.cellSizeY/2)
				p3 = (pX + self.cellSizeX/2, pY + self.cellSizeY*3/4)
				p4 = (pX + self.cellSizeX*3/4, pY + self.cellSizeY/2)
				center = (pX + self.cellSizeX/2, pY + self.cellSizeY/2)
				#Escrever no XML  neighbors = [FRONT, RIGHT, BACK, LEFT] Verificar se BACK existe, 0 < BACK < xDivs*yDivs
				cellET = ET.SubElement(cellsET,'Cell')
				cellIndexET = ET.SubElement(cellET,'Cell')
				cellIndexET.text = 	str(cellIndex)
				centerET = ET.SubElement(cellET,'Center')
				centerET.text = str(center)
				
				#Noh cellIndex,1 ; p1 ; center ; neighbors = [cellIndex,3 ; cellIndex,2 ; (cellIndex-self.xDivs),3 ; cellIndex,4]
				pointET = ET.SubElement(cellET,'Point')
				pointIndexET = ET.SubElement(pointET,'Index')
				pointIndexET.text = str(cellIndex) + ",1"
				pointPosET = ET.SubElement(pointET,'Pos')
				pointPosET.text = str(p1)
				pointNeighborsET = ET.SubElement(pointET,'Neighbors')
				pointNeighborIndexET = ET.SubElement(pointNeighborsET,'FrontIndex')
				pointNeighborIndexET.text = str(cellIndex) + ",3"
				pointNeighborIndexET = ET.SubElement(pointNeighborsET,'RightIndex')
				pointNeighborIndexET.text = str(cellIndex) + ",2"
				pointNeighborIndexET = ET.SubElement(pointNeighborsET,'BackIndex')
				if cellIndex > self.xDivs:
					pointNeighborIndexET.text = str(cellIndex-self.xDivs) + ",3"
				else:
					pointNeighborIndexET.text = "0"
				pointNeighborIndexET = ET.SubElement(pointNeighborsET,'LeftIndex')
				pointNeighborIndexET.text = str(cellIndex) + ",4"
								
				#Noh cellIndex,2 ; p2 ; center ; neighbors = [cellIndex,4 ; cellIndex,3 ; (cellIndex-1),4 ; cellIndex,1]
				pointET = ET.SubElement(cellET,'Point')
				pointIndexET = ET.SubElement(pointET,'Index')
				pointIndexET.text = str(cellIndex) + ",2"
				pointPosET = ET.SubElement(pointET,'Pos')
				pointPosET.text = str(p2)
				pointNeighborsET = ET.SubElement(pointET,'Neighbors')
				pointNeighborIndexET = ET.SubElement(pointNeighborsET,'FrontIndex')
				pointNeighborIndexET.text = str(cellIndex) + ",4"
				pointNeighborIndexET = ET.SubElement(pointNeighborsET,'RightIndex')
				pointNeighborIndexET.text = str(cellIndex) + ",3"
				pointNeighborIndexET = ET.SubElement(pointNeighborsET,'BackIndex')
				if cellIndex%self.xDivs != 1:
					pointNeighborIndexET.text = str(cellIndex-1) + ",4"
				else:
					pointNeighborIndexET.text = "0"
				pointNeighborIndexET = ET.SubElement(pointNeighborsET,'LeftIndex')
				pointNeighborIndexET.text = str(cellIndex) + ",1"
				
				#Noh cellIndex,3 ; p3 ; center ; neighbors = [cellIndex,1 ; cellIndex,4 ; (cellIndex+self.xDivs),1 ; cellIndex,2]
				pointET = ET.SubElement(cellET,'Point')
				pointIndexET = ET.SubElement(pointET,'Index')
				pointIndexET.text = str(cellIndex) + ",3"
				pointPosET = ET.SubElement(pointET,'Pos')
				pointPosET.text = str(p3)
				pointNeighborsET = ET.SubElement(pointET,'Neighbors')
				pointNeighborIndexET = ET.SubElement(pointNeighborsET,'FrontIndex')
				pointNeighborIndexET.text = str(cellIndex) + ",1"
				pointNeighborIndexET = ET.SubElement(pointNeighborsET,'RightIndex')
				pointNeighborIndexET.text = str(cellIndex) + ",4"
				pointNeighborIndexET = ET.SubElement(pointNeighborsET,'BackIndex')
				if cellIndex+self.xDivs < self.xDivs*self.yDivs:
					pointNeighborIndexET.text = str(cellIndex+self.xDivs) + ",1"
				else:
					pointNeighborIndexET.text = "0"
				pointNeighborIndexET = ET.SubElement(pointNeighborsET,'LeftIndex')
				pointNeighborIndexET.text = str(cellIndex) + ",2"				
				#Noh cellIndex,4 ; p4 ; center ; neighbors = [cellIndex,2 ; cellIndex,1 ; (cellIndex+1),2 ; cellIndex,3]
				pointET = ET.SubElement(cellET,'Point')
				pointIndexET = ET.SubElement(pointET,'Index')
				pointIndexET.text = str(cellIndex) + ",1"
				pointPosET = ET.SubElement(pointET,'Pos')
				pointPosET.text = str(p4)
				pointNeighborsET = ET.SubElement(pointET,'Neighbors')
				pointNeighborIndexET = ET.SubElement(pointNeighborsET,'FrontIndex')
				pointNeighborIndexET.text = str(cellIndex) + ",2"
				pointNeighborIndexET = ET.SubElement(pointNeighborsET,'RightIndex')
				pointNeighborIndexET.text = str(cellIndex) + ",1"
				pointNeighborIndexET = ET.SubElement(pointNeighborsET,'BackIndex')
				if cellIndex%self.xDivs != 0:
					pointNeighborIndexET.text = str(cellIndex+1) + ",2"
				else:
					pointNeighborIndexET.text = "0"
				pointNeighborIndexET = ET.SubElement(pointNeighborsET,'LeftIndex')
				pointNeighborIndexET.text = str(cellIndex) + ",3"

								
				if True:
					self.ball = loader.loadModel("../arquivos de modelo/ball")
					self.ball.reparentTo(render)
					#Setting the position of the tower and sphere
					self.position = Vec3(*(list(p1) + [0]))
					self.ball.setPos(self.position)
					self.ball = loader.loadModel("../arquivos de modelo/ball")
					self.ball.reparentTo(render)
					#Setting the position of the tower and sphere
					self.position = Vec3(*(list(p2) + [0]))
					self.ball.setPos(self.position)
					self.ball = loader.loadModel("../arquivos de modelo/ball")
					self.ball.reparentTo(render)
					#Setting the position of the tower and sphere
					self.position = Vec3(*(list(p3) + [0]))
					self.ball.setPos(self.position)
					self.ball = loader.loadModel("../arquivos de modelo/ball")
					self.ball.reparentTo(render)
					#Setting the position of the tower and sphere
					self.position = Vec3(*(list(p4) + [0]))
					self.ball.setPos(self.position)
					#print "pontos = ", p1, ",",p2,",",p3,",",p4
				if True:
					self.ball = loader.loadModel("../arquivos de modelo/ball")
					self.ball.reparentTo(render)
					#Setting the position of the tower and sphere
					self.position = Vec3(*(list(center) + [0]))
					self.ball.setPos(self.position)
					self.ball.setColor(0,0,0)				
						
				cellIndex+= 1

		tree = ET.ElementTree(meshET)
		tree.write(self.outname +".xml")

terrainModel = LoadTerrainModel("../arquivos de modelo/Terrain1")
gen = MeshGen("teste", terrainModel,8,8)
gen.genMesh();
run()
