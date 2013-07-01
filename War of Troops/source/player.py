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
	
	def setHealth(self, health):
		self.health = health
		
	def sumToHealth(self, sumHealth):
		self.health += sumHealth
		
	def addTower(self, towerType):
		if len(self.towerList) == 0:
			self.towerList.append(Tower(towerType))
			self.towerList[-1].initModel([-300,-300,-300])
			self.towerList[-1].towerModel.towerMovingColor()			
		elif self.towerList[-1].towerInicialized:
			self.towerList.append(Tower(towerType))
			self.towerList[-1].initModel([-300,-300,-300])
			self.towerList[-1].towerModel.towerMovingColor()
		"""elif (self.towerList[-1].towerModel == None):
			self.towerList[-1].initModel([-300,-300,-300])
			self.towerList[-1].towerModel.towerMovingColor()"""
			
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
	
	def collideTroopEventAgainTowerRange(entry):
		#print entry.getFromNodePath(), "colliding with", entry.getIntoNodePath()
		collindingFromNode = entry.getFromNode()
		collindingIntoNode = entry.getIntoNode()
		troopObj = Troop.troopDict[collindingFromNode.getTag("TroopID")]
		towerObj = Tower.towerDict[collindingIntoNode.getTag("TowerID")]
		towerObj.shootProjectile([troopObj.position[0] - towerObj.position[0], troopObj.position[1] - towerObj.position[1], 13])
		return
		
	def collideTroopEventAgainProjectile(entry):
		#print entry.getFromNodePath(), "colliding with", entry.getIntoNodePath()
		return

	#DO.accept('TroopClass_cnode-again-TowerClass_Rangecnode', collideTroopEventAgainTowerRange)
	collision.addCollisionEventAgain("TroopClass_cnode","TowerClass_Rangecnode",collideTroopEventAgainTowerRange)
	collision.addCollisionEventAgain("TroopClass_cnode","ProjectileClass_cnode",collideTroopEventAgainProjectile)

