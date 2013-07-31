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
from math import *
import physics
from Sound import *

#Getting the shoot sound effect
towerAttackSound = Sound("../sounds/towerAttack.wav")
towerAttackSound.setVolume(0.5)

towerPositioningSound = Sound("../sounds/towerPositioning.wav")
towerPositioningSound.setVolume(0.5)


towerModelDict = {}
#Getting configuration
typ = None
cfTree = ET.parse("tower.xml")
cfRoot = cfTree.getroot()
for element in cfRoot.findall('tower'):
	
	towerType = element.get('type')
	modelTag = element.find('model')
	
	
	#Loading the tower models
	
	#loading the sphere
	towerSphereModel = loader.loadModel(modelTag.find('sphere').text)
	print "tower ",towerType," instanced"
	#towerSphereModel.clearModelNodes()
	#towerSphereModel.flattenStrong()
	
	#Setting the position of the tower 
	towerSphereModel.setPos(0,0,0)
	
	#loading the base of the tower
	towerBase = loader.loadModel(modelTag.find('base').text)
	towerBase.setColorOff()
	#Setting the texture to the base
	texture = loader.loadTexture(modelTag.find('texture').text)
	towerBase.setTexture(texture, 1)
	towerBase.setPos(0,0,0)
	towerBase.reparentTo(towerSphereModel)
	
	#loading the cannons that stays inside the ball
	towerCannons = loader.loadModel(modelTag.find('cannon').text)
	towerCannons.reparentTo(towerSphereModel)
	towerCannons.setColorOff()
	towerCannons.setPos(0,0,0)
	towerCannons.hprInterval(5,Point3(360,0,0)).loop()

	towerModelDict[towerType] = towerSphereModel

	

class TowerModel(DirectObject):
	'''This class imports the tower model and do the needed transformations
	   to show it on the game screen.
	'''
	def __init__(self,sourceTower, position, modelTag, towerType):
		self.sourceTower = sourceTower
		self.nodeName = None
		self.ID = None
		self.colorTag = modelTag.find('color')
		self.color = [float(self.colorTag.find('r').text), 
					  float(self.colorTag.find('g').text),
					  float(self.colorTag.find('b').text)]
		self.selectedColorTag = modelTag.find('selectedColor')
		self.selectedColor = [float(self.selectedColorTag.find('r').text), 
							  float(self.selectedColorTag.find('g').text),
							  float(self.selectedColorTag.find('b').text)]
		self.movingColor = self.selectedColor
		
		
		
		#Loading the tower instance
		self.towerInstance = render.attachNewNode("Tower-Instance")
		towerModelDict[towerType].instanceTo(self.towerInstance)
		
		#self.color is the color of the sphere and tinting the sphere
		self.towerInstance.setColor(*self.color)
		#Setting the position of the tower, sphere and canons
		self.towerInstance.setPos(Vec3(*position))
		
		
	def moveTowerModel(self,position):
		self.towerInstance.setPos(Vec3(*position))
		#self.sphere.setPos(Vec3(*position))
		#self.canons.setPos(Vec3(*position))
		
	def towerSelectedColor(self,color = None):
		if color is None:
			color = self.selectedColor
		self.towerInstance.setColor(*color)

	def towerMovingColor(self, color = None):
		if color is None:
			color = self.movingColor
		self.towerInstance.setColor(*color)
		
	def resetColor(self):
		self.towerInstance.setColor(*self.color)
		
	def setCollisionNode (self, nodeName, rangeView, ID):
		self.nodeName = nodeName
		self.ID = ID
		self.towerRangeCollider = self.towerInstance.attachNewNode(CollisionNode(nodeName + '_Rangecnode'))
		self.towerRangeCollider.node().addSolid(CollisionSphere(0,0,0,rangeView))
		self.towerRangeCollider.setCollideMask(self.sourceTower.sourcePlayer.playerBitMask)
		self.towerRangeCollider.setTag("TowerID", ID)
		self.towerCollider = self.towerInstance.attachNewNode(CollisionNode(nodeName + '_cnode'))
		self.towerCollider.node().addSolid(CollisionBox(Point3(0,0,7.5),4,4,7.5))
		self.towerCollider.setTag("TowerID", ID)
		#print "CollisionNodeTag = ",self.towerCollider.getTag("TowerID")
	
	def updateTowerRange(self,rangeView):
		self.towerRangeCollider.node().clearSolids()
		#self.towerRangeCollider = self.towerInstance.attachNewNode(CollisionNode(self.nodeName + '_Rangecnode'))
		self.towerRangeCollider.node().addSolid(CollisionSphere(0,0,0,rangeView))
		self.towerRangeCollider.setCollideMask(self.sourceTower.sourcePlayer.playerBitMask)
		self.towerRangeCollider.setTag("TowerID", self.ID)
		
	def delete(self):
		self.towerInstance.removeNode()
		self.towerInstance = None
	
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

	def __init__(self, sourcePlayer, towerType):

		self.name = "TowerClass"
		self.ID = str(uuid.uuid4())
		Tower.towerDict[self.ID] = self
		self.towerType = towerType
		self.sourcePlayer = sourcePlayer
		self.enemyBitMask = sourcePlayer.inactivePlayer.playerBitMask
		#Getting configuration
		self.towerType = towerType
		self.typ = None
		self.cfTree = ET.parse('tower.xml')
		self.cfRoot = self.cfTree.getroot()
		for element in self.cfRoot.findall('tower'):
			if (element.get('type') == self.towerType):
				self.typ = element
		if self.typ == None: print "Tower Type do not exist"; return
		#Getting model configuration
		self.modelTag = self.typ.find('model')
		#Getting troop type
		self.troopType = self.typ.find('troopType').text
		#Getting projectile typefrom direct.interval.ActorInterval import ActorInterval
		self.projectileType = self.typ.find('projectileType').text

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

		#Tower price for purchase
		self.price = int(self.typ.find('price').text)
		#Update prices
		self.shootPowerPrice = int(self.shootPowerTag.find('price').text)
		self.txShootPrice = int(self.txShootTag.find('price').text)
		self.rangeViewPrice = int(self.rangeViewTag.find('price').text)
		self.txTroopsPrice = int(self.txTroopsTag.find('price').text)

		#Number of points that the tower will receive
		self.initialPoints = int(self.typ.find('initialPoints').text)

		#Position of the tower
		self.position = [0,0,0]
		
		self.projectiles = [] #projectiles.append(Projectile())
		
		self.troop = None
		
		#Graphical part------------------

		self.towerModel = None
		self.towerInicialized = False
		self.artPath = self.typ.find('artPath').text

		#----------------------------------
		
		#Game engine part------------------
		self.timeLastShoot = 0
		self.timeLastSpawn = 0
		self.lastValueUpdated = None
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
		self.towerModel = TowerModel(self, position, self.modelTag, self.towerType)
	
	def delete(self):
		if self.towerModel != None:
			self.towerModel.delete()
			self.towerModel = None
		del Tower.towerDict[self.ID]
		del self.sourcePlayer.towerList[-1]

	def moveTower(self,position):
		self.position = position
		self.towerModel.moveTowerModel(position)

	def setName(self,towerName):
		self.name = towerName

	def initCollisionNode(self):
		self.towerModel.setCollisionNode(self.name, self.listRangeView[0], self.ID);
		towerPositioningSound.play()

	def shootProjectile(self, targetPosition):
		timeSinceLastShoot = globalClock.getFrameTime() - self.timeLastShoot
		#print "timeLastShoot = ",self.timeLastShoot
		if (timeSinceLastShoot > 10.0/self.listTxShoot[0]):
			#print "Shooted timeLastShoot = ",self.timeLastShoot
			self.timeLastShoot = globalClock.getFrameTime()
			self.projectiles.append(Projectile(self.projectileType))
			self.projectiles[-1].position = [self.position[0], self.position[1], self.position[2]+12]
			self.projectiles[-1].impulseForce = self.aimShoot(targetPosition, self.projectiles[-1])		
			self.projectiles[-1].initProjectile()
			if(towerAttackSound.getSoundStatus() == 1):
				towerAttackSound.play()

	def spawnTroop(self):
		timeSinceLastSpawn = globalClock.getFrameTime() - self.timeLastSpawn
		if self.towerInicialized:
			if (timeSinceLastSpawn > 20.0/self.listTxTroops[0]):
				self.timeLastSpawn = globalClock.getFrameTime()
				self.createTroop()
		
	def createTroop(self):
		self.troop = Troop(self,self.troopType)
		self.troop.position = [self.position[0]+randint(-15,15), self.position[1]+randint(-15,15),self.position[2]]
		self.troop.initTroop()

	def aimShoot(self, targetPosition, projectileObj):
		targetPosition = targetPosition[:]
		targetPosition[2] += 4
		distanceVector = vector3Sub(targetPosition, projectileObj.position)
		distanceModule = vector2Module(distanceVector[:2])
		sinPhiAngle = distanceVector[1]/(distanceModule)
		cosPhiAngle = distanceVector[0]/(distanceModule)
		velocity = (self.listShootPower[0]/projectileObj.mass)
		thetaAngle = thetaCalc(velocity, physics.physicsGravity, distanceModule, distanceVector[2])
		aimImpulseForce = [self.listShootPower[0]*cosPhiAngle*cos(thetaAngle), self.listShootPower[0]*sinPhiAngle*cos(thetaAngle), self.listShootPower[0]*sin(thetaAngle)]
		return aimImpulseForce

	def getAttributePrice(self, attrType):
		if attrType == 'shootPower':
			return self.shootPowerPrice
		elif attrType == 'txShoot':
			return self.txShootPrice
		elif attrType == 'rangeView':
			return self.rangeViewPrice
		elif attrType == 'txTroops':
			return self.txTroopsPrice
	
	def updateAttribute(self, attrType, value):
		if value > 0:
			if attrType == 'shootPower':
				if self.sourcePlayer.currency >= self.shootPowerPrice*value:
					self.sourcePlayer.currency -= self.shootPowerPrice*value
					self.listShootPower[VALUE] += value
					self.lastValueUpdated = attrType
				else:
					error_Sound.play()
							
			elif attrType == 'txShoot':
				if self.sourcePlayer.currency >= self.txShootPrice*value:
					self.sourcePlayer.currency -= self.txShootPrice*value
					self.listTxShoot[VALUE] += value
					self.lastValueUpdated = attrType
				else:
					error_Sound.play()
				
			elif attrType == 'rangeView':
				if self.sourcePlayer.currency >= self.rangeViewPrice*value:
					self.sourcePlayer.currency -= self.rangeViewPrice*value
					self.listRangeView[VALUE] += value
					self.lastValueUpdated = attrType
					self.towerModel.updateTowerRange(self.listRangeView[VALUE])
				else:
					error_Sound.play()
				
			elif attrType == 'txTroops':
				if self.sourcePlayer.currency >= self.txTroopsPrice*value:
					self.sourcePlayer.currency -= self.txTroopsPrice*value
					self.listTxTroops[VALUE] += value
					self.lastValueUpdated = attrType
				else:
					error_Sound.play()

		elif self.lastValueUpdated != None:
			if attrType == 'shootPower' and attrType == self.lastValueUpdated:
				if self.sourcePlayer.currency >= self.shootPowerPrice*value:
					self.sourcePlayer.currency -= self.shootPowerPrice*value
					self.listShootPower[VALUE] += value
					self.lastValueUpdated = None
				else:
					error_Sound.play()
							
			elif attrType == 'txShoot' and attrType == self.lastValueUpdated:
				if self.sourcePlayer.currency >= self.txShootPrice*value:
					self.sourcePlayer.currency -= self.txShootPrice*value
					self.listTxShoot[VALUE] += value
					self.lastValueUpdated = None
				else:
					error_Sound.play()
				
			elif attrType == 'rangeView' and attrType == self.lastValueUpdated:
				if self.sourcePlayer.currency >= self.rangeViewPrice*value:
					self.sourcePlayer.currency -= self.rangeViewPrice*value
					self.listRangeView[VALUE] += value
					self.towerModel.updateTowerRange(self.listRangeView[VALUE])
					self.lastValueUpdated = None
				else:
					error_Sound.play()
				
			elif attrType == 'txTroops' and attrType == self.lastValueUpdated:
				if self.sourcePlayer.currency >= self.txTroopsPrice*value:
					self.sourcePlayer.currency -= self.txTroopsPrice*value
					self.listTxTroops[VALUE] += value
					self.lastValueUpdated = None
				else:
					error_Sound.play()
			



