from pandaImports import *

class HUDMap(DirectObject):
	def __init__(self):
		self.X, self.Y, self.Z = 0, 0, 500
		self.angle = 90
		self.hudMap = Camera("hudMap")
		self.myHUDMap = render.attachNewNode(self.hudMap) 
		self.myHUDMap.setName("HUDMap Camera")
		self.myHUDMap.setHpr(0.0 , -self.angle, 0.0)
		self.myHUDMap.setX(self.X) 
		self.myHUDMap.setY(self.Y) 
		self.myHUDMap.setZ(self.Z) 
		#Creating the display
		self.createRegion()
			
	def createRegion(self):
		self.leftBorder, self.rightBorder = 0.8, 1 
		self.bottomBorder, self.topBorder = 0.8, 1
		self.displayRegion = base.win.makeDisplayRegion(self.leftBorder, self.rightBorder, self.bottomBorder, self.topBorder)
		self.displayRegion.setCamera(self.myHUDMap)
		
