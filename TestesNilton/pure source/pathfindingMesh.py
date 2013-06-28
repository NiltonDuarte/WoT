"""This file receives an XML mesh and generete the mesh for navigation"""

FRONT = 0
RIGHT = 1
BACK = 2
LEFT = 3


class Node:
	"""Node class, a node hold information that will be needed for mesh"""
	def __init__ (self):
		self.centerPosXYZ = [0,0,0]
		self.blocked = False
		self.vertexNeighbor = [None,None,None,None]
		
	def setVertexNeighbor (self, neighborFRONT, neighborRIGHT, neighborBACK, neighborLEFT):
		self.vertexNeighbor = [neighborFRONT, neighborRIGHT, neighborBACK, neighborLEFT]

class Mesh:
	"""Mesh class, a mesh is made of Node's and the vertex's"""
	def __init__(self, fileXML):
		self.fileXML = fileXML
		self.name = name
		self.nodesDict = {} #node centerPos, node object
		self.initMesh()
		
	def addNode(self, node):
		self.nodesDict[node.name] = self

	def initMesh(self)
		"""Read the XML file, create the nodes and add them to the mesh"""
		pass
