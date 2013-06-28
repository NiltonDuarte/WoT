import xml.etree.ElementTree as ET
from pandaImports import *

"""This is a standalone program that receive an egg file and generate a navigation mesh in XML that wil be read in WoT game"""

class LoadTerrainModel(DirectObject):
	'''This class imports the terrain model and do the needed transformations
	   to show it on the game screen.
	'''
	def __init__(self, modelPath):
		#Loading the terrain model
		self.terrain = loader.loadModel(modelPath)
		self.terrain.reparentTo(render)
		
		#Setting the position of the terrain
		self.position = Vec3(0, 0, 0)
		self.terrain.setPos(self.position)

		self.terrainBoundLower, self.terrainBoundUpper = self.terrain.getTightBounds()
		self.terrainSizeX = terrainBoundUpper[0] - terrainBoundLower[0]
		self.terrainSizeY = terrainBoundUpper[1] - terrainBoundLower[1]
		

	
class MeshGen:

	def __init__(self, xDivs, yDivs, terrainModel):
		self.xDivs = xDivs
		self.yDivs = yDivs
		self.terrainModel = terrainModel
		self.cellSizeX = terrainModel.terrainSizeX / xDivs
		self.cellSizeY = terrainModel.terrainSizeY / yDivs

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
			
		p1,p2,p3,p4, center, cellIndex = 0
		for yDivIndex in range(self.yDivs):
			for xDivIndex in range(self.xDivs):
				pX = xDivIndex*cellSizeX
				pY = yDivIndex*cellSizeY
				p1 = (pX +cellSizeX/2, pY + cellSizeY/4)
				p2 = (pX + cellSizeX/4, pY + cellSizeY/2)
				p3 = (pX + cellSizeX/2, pY + cellSizeY*3/4)
				p4 = (pX + cellSizeX*3/4, pY + cellSizeY/2)
				center = (pX +cellSizeX/2, pY + cellSizeY/2)
				#Escrever no XML  neighbors = [FRONT, RIGHT, BACK, LEFT] Verificar se BACK existe, 0 < BACK < xDivs*yDivs
					#Nó cellIndex,1 ; p1 ; center ; neighbors = [cellIndex,3 ; cellIndex,2 ; (cellIndex-self.xDivs),3 ; cellIndex,4]
					#Nó cellIndex,2 ; p2 ; center ; neighbors = [cellIndex,4 ; cellIndex,3 ; (cellIndex-1),4 ; cellIndex,1]
					#Nó cellIndex,3 ; p3 ; center ; neighbors = [cellIndex,1 ; cellIndex,4 ; (cellIndex+self.xDivs),1 ; cellIndex,2]
					#Nó cellIndex,4 ; p4 ; center ; neighbors = [cellIndex,2 ; cellIndex,1 ; (cellIndex+1),2 ; cellIndex,3]
					
				cellIndex ++
