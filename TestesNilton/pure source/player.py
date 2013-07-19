"""File that holds the player class"""
from tower import *
from troop import *
from camera import *
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
		self.enemyTarget = [-90,0] if playerNumber == "Player2" else [90,0]

		self.initAtkTime = 0

	def loadPlayer(self):
		self.camera.loadCamera()
		
	def setHealth(self, health):
		self.health = health
		
	def sumToHealth(self, sumHealth):
		self.health += sumHealth
		
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

		projectileObj = Projectile.projectileDict[collidingIntoNode.getTag("ProjectileID")]

		if (projectileObj.colliding == False):
		#BUG - projetil nao eh apagado corretamente, gerando erro ao tentar fazer nova colisao apos ser apagado do dicionario
				
			projectileObj.projectileModel.ignoreAll()
			projectileObj.colliding = True
		return


	collision.addCollisionEventAgain("TroopClass_cnode","TowerClass_Rangecnode",collideTroopEventAgainTowerRange)
	collision.addCollisionEventInto("TroopClass_cnode","ProjectileClass_cnode",collideTroopEventIntoProjectile)

