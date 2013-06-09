"""File that holds the player class"""
from tower import *
from camera import *

class Player:
	"""Player class that holds his towers, health and camera"""
	
	def __init__(self):
		self.health = 100
		self.towerList = [Tower()]
		self.camera = MyCamera()
		self.currency = 100
	
	def setHealth(self, health):
		self.health = health
		
	def sumToHealth(self, sumHealth):
		self.health += sumHealth
		
	def addTower(self):
		if self.towerList[-1].towerModel != None:
			self.towerList.append(Tower())
			self.towerList[-1].initModel([-300,-300,-300], [.0,.5,.0, .5])
		else:
			self.towerList[-1].initModel([-300,-300,-300], [.0,.5,.0, .5])
			
	def getTower(self,index):
		return	self.towerList[index]
		
	def getTowerList(self):
		return self.towerList
			
	def delTower(self, towerIndex):
		return

	def sumToCurrency (self, sumCurrency):
		self.currency += sumCurrency
		
