"""File that holds the player class"""
from tower import *
from camera import *

class Player:
	"""Player class that holds his towers, health and camera"""
	
		def __init__(self):
			self.health = 100
			self.towerList = [Tower()]
			self.camera = None
			self.currency = 100
		
		def setHealth(self, health):
			self.health = health
			
		def sumToHealth(self, sumHealth):
			self.health += sumHealth
			
		def addTower(self, tower):
			if self.towerList[-1].towerModel != None:
				self.towerList.append(tower)
				
		def delTower(self, towerIndex):
			
		def sumToCurrency (self, sumCurrency):
			self.currency += sumCurrency
			
