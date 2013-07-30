from pandaImports import *

class HUDMap(DirectObject):
	def __init__(self):
		#Creating the camera
		self.hudMap = Camera("hudMap")
		self.myHUDMap = render.attachNewNode(self.hudMap) 
		self.myHUDMap.setName("HUDMap Camera")
		
		#Setting the position and orientation of the camera
		self.angle = 90
		self.myHUDMap.setHpr(0.0 , -self.angle, 0.0)
		self.X, self.Y, self.Z = 0, 0, 500
		self.myHUDMap.setX(self.X) 
		self.myHUDMap.setY(self.Y) 
		self.myHUDMap.setZ(self.Z) 
		
		#Creating the display region and some attributes
		self.createRegion()
		self.width = self.getWidth()
		self.height = self.getHeight()
		self.aspectRatio = self.getAspectRatio()
		
		#Making the HUDmap not be hidden by other objects
		self.displayRegion.setClearColorActive(True)
		self.displayRegion.setClearColor((0.5, 0.5, 0.5, 1))
		self.displayRegion.setClearDepthActive(True)  #Z buffer
			
	def createRegion(self):
		self.leftBorder, self.rightBorder = 0.8, 1 
		self.bottomBorder, self.topBorder = 0.8, 1
		self.displayRegion = base.win.makeDisplayRegion(self.leftBorder, self.rightBorder, self.bottomBorder, self.topBorder)
		self.displayRegion.setCamera(self.myHUDMap)
		
	def getHeight(self):
		'''Return the height of our display region'''
		return float(self.displayRegion.getPixelHeight())
		
	def getWidth(self):
		'''Return the width of our display region'''
		return float(self.displayRegion.getPixelWidth())
	
	def getAspectRatio(self):
		'''Return the aspect ratio of our display region'''
		return float(self.width/self.height)

	def destroy(self):
		self.myHUDMap.removeNode()
		base.win.removeDisplayRegion(self.displayRegion)
		
