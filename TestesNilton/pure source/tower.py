"""Tower Class File"""

#importing other modules
from random import randint
import uuid
import xml.etree.ElementTree as ET
#importing our modules
from commonFunctions import *
from projectile import *
from troop import *
import collision
from pandaImports import *
from pandac.PandaModules import CollisionSphere
from panda3d.core import PandaNode

class TowerModel(DirectObject):
	'''This class imports the tower model and do the needed transformations
	   to show it on the game screen.
	'''
	def __init__(self, position, model):
		#PandaNode.__init__(self, "TowerModel")
		#Loading the tower model
		self.tower = loader.loadModel(model[0])
		self.tower.reparentTo(render)
		#loading the ball that stays above the tower
		self.sphere = loader.loadModel(model[1])
		self.sphere.reparentTo(render)
		#loading the canons that stays inside the ball
		self.canons = loader.loadModel(model[2])
		self.canons.reparentTo(render)
		self.canons.hprInterval(5,Point3(360,0,0)).loop()
		#Setting the texture to the tower
		self.texture = loader.loadTexture(model[3])
		self.tower.setTexture(self.texture, 1)
		#self.color is the color of the sphere and tinting the sphere
		self.color = [1,0,0]
		self.sphere.setColor(*self.color)
		self.canons.setColor(0,0,0)
		#Setting the position of the tower, sphere and canons
		self.tower.setPos(Vec3(*position))
		self.sphere.setPos(Vec3(*position))
		self.canons.setPos(Vec3(*position))
		
	def moveTowerModel(self,position):
		self.tower.setPos(Vec3(*position))
		self.sphere.setPos(Vec3(*position))
		self.canons.setPos(Vec3(*position))
		
	def towerSelectedColor(self,color = [0,0,1]):
		self.sphere.setColor(*color)

	def towerMovingColor(self, color = [0,1,0]):
		self.sphere.setColor(*color)
		
	def resetColor(self):
		self.sphere.setColor(*self.color)
		
	def setCollisionNode (self, nodeName, rangeView, ID):
		self.towerCollider = self.tower.attachNewNode(CollisionNode(nodeName + '_Rangecnode'))
		self.towerCollider.node().addSolid(CollisionSphere(0,0,0,rangeView))
		self.towerCollider = self.tower.attachNewNode(CollisionNode(nodeName + '_cnode'))
		self.towerCollider.node().addSolid(CollisionBox(Point3(0,0,7.5),4,4,7.5))
		self.towerCollider.setTag("TowerID", ID)
		print "CollisionNodeTag = ",self.towerCollider.getTag("TowerID")
	
	"""	
	def setCollisionNode (self, collisionNodeName, rangeView):
		self.towerCollider = self.tower.attachNewNode(Tower(collisionNodeName + '_Rangecnode'))
		self.towerCollider.node().addSolid(CollisionSphere(0,0,0,rangeView))
		self.towerCollider = self.tower.attachNewNode(Tower(collisionNodeName + '_cnode'))
		self.towerCollider.node().addSolid(CollisionBox(Point3(0,0,5.5),4,4,5.5))		
	"""
class Tower():
	"""This class defines all attributes and functions
	of a tower
	"""

	towerDict = {}

	def __init__(self, towerType='Torre Inicial', confFile='torre.xml'):

		self.name = "TowerClass"
		self.ID = str(uuid.uuid4())
		Tower.towerDict[self.ID] = self

		#Getting configuration
		self.cfTree = ET.parse(confFile)
		self.cfRoot = self.cfTree.getroot()
		for element in self.cfRoot.findall('torre'):
			if (element.get('tipo') == towerType):
				self.typ = element

		#Getting model configuration
		self.modelTag = self.typ.find('model')
		self.model = []
		self.model.append(self.modelTag.find('base').text)
		self.model.append(self.modelTag.find('sphere').text)
		self.model.append(self.modelTag.find('canon').text)
		self.model.append(self.modelTag.find('texture').text)


		#Shooting power of the tower
		self.shootPower = 0 #Nao usar esta variavel. Usar listShootPower[0]
		self.shootPowerTag = self.typ.find('shootPower')
		self.shootPowerMin = int(self.shootPowerTag.find('Min').text)
		self.shootPowerMax = int(self.shootPowerTag.find('Max').text)
		self.listShootPower = [self.shootPower, self.shootPowerMax, self.shootPowerMin]


		#Frequency of shooting
		self.txShoot = 0 #Nao usar esta variavel. Usar listTxShoot[0]
		self.txShootTag = self.typ.find('txShoot')
		self.txShootMin = int(self.txShootTag.find('Min').text)
		self.txShootMax = int(self.txShootTag.find('Max').text)
		self.listTxShoot = [self.txShoot, self.txShootMax, self.txShootMin]


		#Tower range of view
		self.rangeView = 20 #Nao usar esta variavel! Usar listRangeView[0]
		self.rangeViewTag = self.typ.find('rangeView')
		self.rangeViewMin = int(self.rangeViewTag.find('Min').text)
		self.rangeViewMax = int(self.rangeViewTag.find('Max').text)
		self.listRangeView = [self.rangeView, self.rangeViewMax, self.rangeViewMin]


		#Speed of troop crafting
		self.txTroops = 0 #Nao usar esta variavel! Usar listTxTroops[0]
		self.txTroopsTag = self.typ.find('txTroops')
		self.txTroopsMin = int(self.txTroopsTag.find('Min').text)
		self.txTroopsMax = int(self.txTroopsTag.find('Max').text)
		self.listTxTroops = [self.txTroops, self.txTroopsMax, self.txTroopsMin]

		self.listAttributes = [self.listShootPower, self.listTxShoot, self.listRangeView, self.listTxTroops]


		#Number of points that the tower will receive
		self.initialPoints = 100

		#Position of the tower
		self.position = [0,0,0]
		
		self.projectileParameters = [100, #@mass
									5, #@spreadRay
									0, #@spreadPercentage
									0, #@dot
									50, #@damageDuration
									0, #@slow
									30, #@slowDuration
									0, #@chanceCritical
									]
		self.projectiles = [] #projectiles.append(Projectile())
		
		#[@lifeMin, @lifeMax, @speedMin, @speedMax,	@resistenceMin, @resistenceMax]
		self.troopParameters = [100,250,10,30,10,25]
		self.troop = None
		
		#Graphical part------------------

		self.towerModel = None
		self.towerInicialized = False
		self.artPath = "../HUD images/purpleTowerArt.png"

		#----------------------------------

            
	def initTower(self):
		"""Initialize the tower with random values inside a interval"""
		if (self.initialPoints >= \
			(self.shootPowerMin + self.txShootMin + self.rangeViewMin + self.txTroopsMin) \
			and self.initialPoints <= \
			(self.shootPowerMax + self.txShootMax + self.rangeViewMax + self.txTroopsMax)):  
                      
			#Attributing the minimum values
			self.listShootPower[MIN] = self.shootPowerMin
			self.listTxShoot[MIN] = self.txShootMin
			self.listRangeView[MIN] = self.rangeViewMin
			self.listTxTroops[MIN] = self.txTroopsMin
            
			#Attributing the maximum values
			self.listShootPower[MAX] = self.shootPowerMax
			self.listTxShoot[MAX] = self.txShootMax
			self.listRangeView[MAX] = self.rangeViewMax
			self.listTxTroops[MAX] = self.txTroopsMax
            
			#Attributing random values
			startRandomAttributes(self.listAttributes, self.initialPoints)
			
			
			self.initCollisionNode()
			self.moveTower(self.position)
			self.towerInicialized = True
		else:
			print "Error with the number of initial points of the tower", (self.shootPowerMin + self.txShootMin + self.rangeViewMin + self.txTroopsMin), "- ", (self.shootPowerMax + self.txShootMax + self.rangeViewMax + self.txTroopsMax)
			
			
	def defineParameters(self,listParam):
		"""Gets the values of listParam and puts them in this order
		[@shootPowerMin, @shootPowerMax, 
		@txShootMin, @txShootMax,
		@rangeViewMin, @rangeViewMax,
		@txTroopsMin, @txTroopsMax]
		"""
		if len(listParam) != 8: print "Error with the parameters of listParam of the tower"; return
		self.shootPowerMin = listParam[0]
		self.shootPowerMax = listParam[1]
		self.txShootMin = listParam[2]
		self.txShootMax = listParam[3]
		self.rangeViewMin = listParam[4]
		self.rangeViewMax = listParam[5]
		self.txTroopsMin = listParam[6]
		self.txTroopsMax = listParam[7]


	def setInitialPoints(self, points):
		self.initialPoints = points

	def initModel(self, position):
		self.position = position
		self.towerModel = TowerModel(position,self.model)

	def moveTower(self,position):
		self.position = position
		self.towerModel.moveTowerModel(position)

	def setName(self,towerName):
		self.name = towerName

	def initCollisionNode(self):
		self.towerModel.setCollisionNode(self.name, self.listRangeView[0], self.ID);

	def shootProjectile(self,position, impulseForce):
		self.projectiles.append(Projectile())
		self.projectiles[-1].defineParameters(self.projectileParameters)
		self.projectiles[-1].position = position
		self.projectiles[-1].impulseForce = impulseForce
		self.projectiles[-1].initProjectile()
		
	def createTroop(self):
		self.troop = Troop(self)
		self.troop.defineParameters(self.troopParameters)
		self.troop.position = [self.position[0]+randint(-15,15), self.position[1]+randint(-15,15),self.position[2]]
		self.troop.initTroop()

	def aimShoot(self, targetPosition):
		directionVector = vector3Sub(targetPosition, self.position)
		#aimImpulseForce 


