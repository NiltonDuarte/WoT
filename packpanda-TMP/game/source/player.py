"""File that holds the player class"""
from tower import *
from troop import *
from camera import *
from commonFunctions import *
import collision



class Player:
	"""Player class that holds his towers, health and camera"""
	
	playerDict = {}
	currPlayer = None #Holds the current player object
	inactivePlayer = None #Holds the inactive player object

	def __init__(self, playerNumber,name):
		self.playerNumber = playerNumber
		Player.playerDict[self.playerNumber] = self
		self.name = name
		Player.inactivePlayer = Player.currPlayer
		Player.currPlayer = self
		self.health = 100
		self.towerList = []
		self.camera = MyCamera()
		self.currency = 100
		self.playerBitMask = BitMask32(int(playerNumber[-1]))
		self.enemyTarget = [-95,0] if playerNumber == "Player2" else [95,0]

		#Game engine part------------------
		self.initAtkTime = 0
		self.isDead = False
		#----------------------------------

	def loadPlayer(self):
		self.camera.loadCamera()
		
	def setHealth(self, health):
		self.health = health
		
	def updateHealth(self, value):
		self.health += value
		if self.health <= 0:
			self.isDead = True
		
	def addTower(self, towerType):
		if len(self.towerList) == 0:
			self.towerList.append(Tower(self,towerType))
			self.towerList[-1].initModel([-300,-300,-300])
			self.towerList[-1].towerModel.towerMovingColor()			
		elif self.towerList[-1].towerInicialized:
			self.towerList.append(Tower(self,towerType))
			self.towerList[-1].initModel([-300,-300,-300])
			self.towerList[-1].towerModel.towerMovingColor()
		else: 
			self.towerList[-1].delete()
			self.towerList.append(Tower(self,towerType))
			self.towerList[-1].initModel([-300,-300,-300])
			self.towerList[-1].towerModel.towerMovingColor()
			
	def getTower(self,index):
		return	self.towerList[index]
		
	def getTowerList(self):
		return self.towerList
			
	def delTower(self, towerIndex):
		return

	def sumToCurrency (self, sumCurrency):
		self.currency += sumCurrency
	
	def setCurrentPlayer(self):
		Player.currPlayer = self

	def updateTime(self):
		self.initAtkTime = globalClock.getFrameTime()
		
	def attackEnemy(self, task):	
		currTime = globalClock.getFrameTime()
		if (currTime - self.initAtkTime) < 10:
			for towerObj in self.towerList:
				towerObj.spawnTroop()
		else: return Task.done
		return Task.cont
	
	def collideTroopEventAgainTowerRange(entry):
		collindingFromNode = entry.getFromNode()
		collindingIntoNode = entry.getIntoNode()
		troopObj = Troop.troopDict[collindingFromNode.getTag("TroopID")]
		towerObj = Tower.towerDict[collindingIntoNode.getTag("TowerID")]
		troopObj.updatePosition([entry.getContactPos(render).getX(), entry.getContactPos(render).getY(), entry.getContactPos(render).getZ()])
		towerObj.shootProjectile(troopObj.position)
		return
		
	def collideTroopEventIntoProjectile(entry):
		#print entry.getFromNodePath(), "colliding with", entry.getIntoNodePath()
		collidingIntoNode = entry.getIntoNode()
		collidingFromNode = entry.getFromNode()

		projectileObj = Projectile.projectileDict[collidingIntoNode.getTag("ProjectileID")]
		troopObj = Troop.troopDict[collidingFromNode.getTag("TroopID")]
		if (projectileObj.colliding == False):
		#BUG - projetil nao eh apagado corretamente, gerando erro ao tentar fazer nova colisao apos ser apagado do dicionario
				
			projectileObj.projectileModel.ignoreAll()
			projectileObj.colliding = True
		damage = 0.8 * vector3Module(projectileObj.actorNode.getPhysicsObject().getVelocity()) * projectileObj.mass
		troopObj.updateLife(-damage)
		if troopObj.isDead:
			Player.currPlayer.currency += troopObj.reward
		return
		
	def collideTroopEventIntoObjective(entry):		
		Player.currPlayer.updateHealth(-10)
		collidingFromNode = entry.getFromNode()
		troopObj = Troop.troopDict[collidingFromNode.getTag("TroopID")]
		troopObj.updatePosition([entry.getContactPos(render).getX(), entry.getContactPos(render).getY(), entry.getContactPos(render).getZ()])
		troopObj.killTroop()
		
		
	@staticmethod
	def mouseScroll(action):
		if (Player.currPlayer != None):
				Player.currPlayer.camera.scrollCamera(action)

	@staticmethod
	def moveCameraXY():
		if (Player.currPlayer != None):
			Player.currPlayer.camera.moveCameraXY()


	collision.addCollisionEventAgain("TroopClass_cnode","TowerClass_Rangecnode",collideTroopEventAgainTowerRange)
	collision.addCollisionEventInto("TroopClass_cnode","ProjectileClass_cnode",collideTroopEventIntoProjectile)
	collision.addCollisionEventInto("TroopClass_cnode","objective_cnode",collideTroopEventIntoObjective)

