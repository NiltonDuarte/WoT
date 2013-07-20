"""Everything related to Troop is here"""
from random import randint
import uuid
import collision
import physics
from commonFunctions import *
from pandaImports import *
import xml.etree.ElementTree as ET
from pathfindingMesh import *
import AI
from particleSystem import *

troopModelDict = {}
troopDeathModelDict = {}
#Getting configuration
typ = None
cfTree = ET.parse("troop.xml")
cfRoot = cfTree.getroot()
for element in cfRoot.findall('troop'):
	troopType = element.get('type')
	modelTag = element.find('model')
	#Loading the troop model
	troopModel = Actor(modelTag.find('path').text, {'walk' : modelTag.find('walkPath').text,
														'death' : modelTag.find('deathPath').text})
	print "troop ", troopType," instanced"
	troopModel.clearModelNodes()
	troopModel.flattenStrong()
	
	#Setting the position of the projectile 
	troopModel.setPos(0,0,0)
	
	#Animating the troop
	troopModel.loop('walk')
	
	#Setting the texture to the troop
	modelTexture = loader.loadTexture(modelTag.find('texture').text)
	troopModel.setTexture(modelTexture, 1)
	
	troopModelDict[troopType] = troopModel

for element in cfRoot.findall('troop'):
	troopType = element.get('type')
	modelTag = element.find('model')
	#Loading the troop model
	troopModel = Actor(modelTag.find('path').text, {'walk' : modelTag.find('walkPath').text,
														'death' : modelTag.find('deathPath').text})
	print "troop ", troopType," instanced"
	troopModel.clearModelNodes()
	troopModel.flattenStrong()
	
	#Setting the position of the projectile 
	troopModel.setPos(0,0,0)
	
	#Animating the troop
	troopModel.loop('death')
	
	#Setting the texture to the troop
	modelTexture = loader.loadTexture(modelTag.find('texture').text)
	troopModel.setTexture(modelTexture, 1)
	
	troopDeathModelDict[troopType] = troopModel

class TroopModel(DirectObject):
	"""This class imports the tower model and do the needed transformations
	   to show it on the game screen.
	"""
	def __init__(self, sourceTroop, position, modelType):
		self.sourceTroop = sourceTroop
		self.troopInstance = render.attachNewNode("Troop-Instance")
		troopModelDict[modelType].instanceTo(self.troopInstance)
		#Setting the position of the projectile 
		self.troopInstance.setPos(Vec3(*position))
		self.troopColliderNP = None

	def moveTroopModel(self,position):
		self.troopInstance.setPos(Vec3(*position))

		
	def setCollisionNode (self, collisionNodeName, ID):
		self.troopColliderNP = self.troopInstance.attachNewNode(CollisionNode(collisionNodeName + '_cnode'))
		self.troopColliderNP.node().addSolid(CollisionSphere(0,0,3.5,3.5)) #(Point3(0,0,3.5),2,2,3.5))
		self.troopColliderNP.node().setFromCollideMask(self.sourceTroop.sourceTower.enemyBitMask)
		self.troopColliderNP.setTag("TroopID", ID)
		collision.addCollider(self.troopColliderNP)

class Troop:
	"""This class defines all attributes and functions
	of a troop
	"""
	troopDict = {}
	def __init__(self, sourceTower, troopType, confFile = "troop.xml"):
		self.name = "TroopClass"
		self.ID = str(uuid.uuid4())
		Troop.troopDict[self.ID] = self
		self.sourceTower = sourceTower

		#Getting configuration
		self.modelType = troopType
		self.typ = None
		self.cfTree = ET.parse(confFile)
		self.cfRoot = self.cfTree.getroot()
		for element in self.cfRoot.findall('troop'):
			if (element.get('type') == troopType):
				self.typ = element
		if self.typ == None: print "Troop Type do not exist"; return
		
		#Getting model configuration
		self.modelTag = self.typ.find('model')
				
		#Life of a troop
		self.lifeTag = self.typ.find('life')		
		self.life = 0
		self.lifeMin = int(self.lifeTag.find('Min').text)
		self.lifeMax = int(self.lifeTag.find('Max').text)
		self.listLife = [self.life, self.lifeMax, self.lifeMin]

		#Speed of a troop
		self.speedTag = self.typ.find('speed')
		self.speed = 0
		self.speedMin = int(self.speedTag.find('Min').text)
		self.speedMax = int(self.speedTag.find('Max').text)
		self.listSpeed = [self.speed, self.speedMax, self.speedMin]

		#Resistence of a troop
		self.resistenceTag = self.typ.find('resistence')
		self.resistence = 0
		self.resistenceMin = int(self.resistenceTag.find('Min').text)
		self.resistenceMax = int(self.resistenceTag.find('Min').text)
		self.listResistence = [self.resistence, self.resistenceMax, self.resistenceMin]

		self.listAttributes = [self.listLife, self.listSpeed, self.listResistence]


		#Position of the troop
		self.position = sourceTower.position
		self.prevPosition = self.position

		self.initialPoints = int(self.typ.find('initialPoints').text)
		#Graphical part------------------
		self.color = [0,0,0]
		self.troopModel = None
		self.artPath = self.typ.find('artPath').text

		#----------------------------------
		#Game engine part------------------
		self.isDead = False
		#----------------------------------

	def defineParameters(self, listParam):
		"""Gets the values of listParam and puts them in this order
		[@lifeMin, @lifeMax, 
		@speedMin, @speedMax,
		@resistenceMin, @resistenceMax]
		"""
		if len(listParam) != 6: print "Error with the parameters of listParam of the troop"; return
		self.lifeMin = listParam[0]
		self.lifeMax = listParam[1]
		self.speedMin = listParam[2]
		self.speedMax = listParam[3]
		self.resistenceMin = listParam[4]
		self.resistenceMax = listParam[5]

	def initTroop(self):
		"""Initialize the troop with random values inside a interval, **based on tower's attributes**"""
		if (self.initialPoints >= \
		(self.lifeMin + self.speedMin + self.resistenceMin) \
		and self.initialPoints <= \
		(self.lifeMax + self.speedMax + self.resistenceMax)):  

			#Attributing the minimum values
			self.listLife[MIN] = self.lifeMin
			self.listSpeed[MIN] = self.speedMin
			self.listResistence[MIN] = self.resistenceMin


			#Attributing the maximum values
			self.listLife[MAX] = self.lifeMax
			self.listSpeed[MAX] = self.speedMax
			self.listResistence[MAX] = self.resistenceMax

			#Attributing random values
			startRandomAttributes(self.listAttributes, self.initialPoints)
			
			self.initModel(self.position)
			self.initCollisionNode()
			
			pathFollowList = navigationMesh.getPointsSequence(navigationMesh.A_Star_Algorithm(self.position[0], self.position[1], self.sourceTower.sourcePlayer.enemyTarget[0], self.sourceTower.sourcePlayer.enemyTarget[1]))
			AI.Ai.addCharAI(self.troopModel.troopInstance,"troop",0,pathFollowList)

			
		else:
			print "Error with the number of initial points of the tower" 

	def setInitialPoints(self, points):
		self.initialPoints = points

	def initModel(self, position):
		self.troopModel = TroopModel(self,position,self.modelType)

	def moveTroop(self,position):
		self.position = position
		self.troopModel.moveTroopModel(position)



	def initCollisionNode(self):
		self.troopModel.setCollisionNode(self.name, self.ID);

	def updatePosition(self, newPosition):
		self.prevPosition = self.position
		self.position = newPosition
		
	def updateLife(self, value):
		self.life += value
		if self.life <= 0:
			self.isDead = True
			self.troopModel.troopColliderNP.node().removeSolid(0)
			self.troopModel.troopInstance.removeNode()
			self.troopModel.troopInstance = render.attachNewNode("TroopDeath-Instance")
			troopDeathModelDict[troopType].instanceTo(self.troopModel.troopInstance)
			self.troopModel.troopInstance.setPos(*self.position)
			#Creating particle system for death animation
			particleSystem = ParticleSystem(self.position, self.troopModel.troopInstance)
			
			

		




