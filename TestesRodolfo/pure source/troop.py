"""Everything related to Troop is here"""
from random import randint
import uuid
import collision
import physics
from pandaImports import *

from direct.actor.Actor import Actor #this module enalbes animation

class TroopModel(DirectObject):
	"""This class imports the tower model and do the needed transformations
	   to show it on the game screen.
	"""
	def __init__(self, position, color):
		#Loading the troop model
		self.troop = Actor()
		self.troop.loadModel("../arquivos de modelo/Troop")
		self.troop.reparentTo(render)
		#print "find = ", str(self.canons.find('**/Shoot'))
		self.troop.loadAnims({'Key 1': "../arquivos de modelo/Troop"})
		self.troop.loop('Key 1')

		#self.color is the color of the sphere and tinting the sphere
		self.color = color

		#Setting the texture to the tower
		#self.texture = loader.loadTexture("../texturas/tower_Texture.png")
		#self.troop.setTexture(self.texture, 1)
		#Setting the position of the tower, sphere and canons
		self.troop.setPos(Vec3(*position))
		
		self.troopColliderNP = None

	def moveTroopModel(self,position):
		self.troop.setPos(Vec3(*position))

		
	def setCollisionNode (self, collisionNodeName, ID):
		self.troopColliderNP = self.troop.attachNewNode(CollisionNode(collisionNodeName + '_cnode'))
		self.troopColliderNP.node().addSolid(CollisionBox(Point3(0,0,7.5),4,4,7.5))
		self.troopColliderNP.setTag("TroopID", ID)
		collision.addCollider(self.troopColliderNP)

class Troop:
	"""This class defines all attributes and functions
	of a troop
	"""
	troopDict = {}
	def __init__(self, position = [0,0,0], initTroopFunc = False, initialPoints=230, listOfParameters=[]):
		self.name = "TroopClass"
		self.ID = str(uuid.uuid4())
		Troop.troopDict[self.ID] = self
		#Life of a troop
		self.life = 0
		self.lifeMin = 100
		self.lifeMax = 250
		self.listLife = [self.life, self.lifeMax, self.lifeMin]

		#Speed of a troop
		self.speed = 0
		self.speedMin = 10
		self.speedMax = 30
		self.listSpeed = [self.speed, self.speedMax, self.speedMin]

		#Resistence of a troop
		self.resistence = 0
		self.resistenceMin = 10
		self.resistenceMax = 25
		self.listResistence = [self.resistence, self.resistenceMax, self.resistenceMin]

		self.listAttributes = [self.listLife, self.listSpeed, self.listResistence]


		#Position of the troop
		self.position = position
		self.positionBefore = [0,0,0]

		self.initialPoints = initialPoints

		#Graphical part------------------

		self.troopModel = TroopModel(position,[0,0,0])
		self.troopModel.setCollisionNode(self.name, self.ID)

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
		else:
			print "Error with the number of initial points of the tower" 

	def setInitialPoints(self, points):
		self.initialPoints = points

	def initModel(self, position, color):
		self.moveTroop(position)

	def moveTroop(self,position):
		self.position = position
		self.troopModel.moveTroopModel(position)


	def initCollisionNode(self):
		self.troopModel.setCollisionNode(self.name, self.ID);
		




