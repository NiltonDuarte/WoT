"""File that holds the player class"""
from tower import *
from camera import *
import collision

class Player:
	"""Player class that holds his towers, health and camera"""
	
	playerDict = {}
	currPlayer = None

	def __init__(self, name):
		Player.playerDict[name] = self
		self.name = name
		Player.currPlayer = self
		self.health = 100
		self.towerList = [Tower()]
		self.camera = MyCamera()
		self.currency = 100
	
	def setHealth(self, health):
		self.health = health
		
	def sumToHealth(self, sumHealth):
		self.health += sumHealth
		
	def addTower(self):
		if self.towerList[-1].towerInicialized:
			print "If towerInicialized = ", self.towerList[-1].towerInicialized
			self.towerList.append(Tower())
			self.towerList[-1].initModel([-300,-300,-300], [.0,.5,.0, .5])
		elif (self.towerList[-1].towerModel == None):
			self.towerList[-1].initModel([-300,-300,-300], [.0,.5,.0, .5])
			
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
		return
		
	def collideTroopEventAgainProjectile(entry):
		print entry.getFromNodePath(), "colliding with", entry.getIntoNodePath()

	#DO.accept('TroopClass_cnode-again-TowerClass_Rangecnode', collideTroopEventAgainTowerRange)
	collision.addCollisionEventAgain("TroopClass_cnode","TowerClass_Rangecnode",collideTroopEventAgainTowerRange)
	collision.addCollisionEventAgain("TroopClass_cnode","ProjectileClass_cnode",collideTroopEventAgainProjectile)

