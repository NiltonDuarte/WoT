from direct.showbase.DirectObject import DirectObject
from Models import *
from math import *

class MyCamera(DirectObject):
	'''This class uses the base.camera of panda3D to reuse
	   existing methods and create new ones
	'''
	cameraEnabled = False
	
	def __init__(self):
		#Disabling mouse default function to enable moving the panda camera with our code
		base.disableMouse()
		#Setting the angle of our camera
		self.angle = 45
		base.camera.setHpr(0.0 , -self.angle, 0.0)
		base.camLens.setFov(40)
		self.camFov = base.camLens.getFov()
		#Setting our camera position to be top-down
		self.X = 0
		self.Y = -150   
		self.Z = 150 #z 150 min = 100 max = 222 z = 100 min = 28 max = 98
		self.leftBorder, self.rightBorder, self.upperBorder, self.bottomBorder = None, None, None, None
		self.updateLimits()
		base.camera.setX(self.X)     
		base.camera.setY(self.Y)  #depth
		base.camera.setZ(self.Z)  #height
		#Variables to help moving the camera
		self.mouseX = 0
		self.mouseY = 0
		self.mouseOnScreen = False

	def updateLimits(self):
		#Setting the limits of our camera
		self.fovYMin = self.Z*sin(radians(self.angle - (self.camFov[1]/2) ))/cos(radians(self.angle - (self.camFov[1]/2) )) 
		self.fovYMax = self.Z*sin(radians(self.angle + (self.camFov[1]/2) ))/cos(radians(self.angle + (self.camFov[1]/2) ))
		self.fovX = self.Z*sin(radians(self.camFov[0]/2 ))/cos(radians(self.camFov[0]/2 )) 
		
		self.leftBorder = TerrainModel.leftBorder + self.fovX    #terrainBoundLower[0]/2
		self.rightBorder = TerrainModel.rightBorder - self.fovX   #terrainBoundUpper[0]/2
		self.upperBorder = TerrainModel.upperBorder - self.fovYMax - 20     #terrainBoundLower[1]
		self.bottomBorder = TerrainModel.bottomBorder - self.fovYMin - 20    #2.5*terrainBoundLower[1]

		
	def loadCamera(self):
		base.camera.setX(self.X)     
		base.camera.setY(self.Y)  #depth
		base.camera.setZ(self.Z)	#height
		base.camera.setHpr(0.0 , -self.angle, 0.0)
		
	def moveCameraXY(self):
		#, leftBorder, rightBorder, upperBorder, bottomBorder
		#Getting the position of the mouse
		if base.mouseWatcherNode.hasMouse() and MyCamera.cameraEnabled:
			self.mouseX = base.mouseWatcherNode.getMouseX()
			self.mouseY = base.mouseWatcherNode.getMouseY()
			self.mouseOnScreen = True
		else:
			self.mouseOnScreen = False
		
		#The camera only moves when the mouse is on the screen
		if(self.mouseOnScreen):
			#print self.Y
			#Creating 2 invisible borders on the right and left side (x axis)	
			if(self.mouseX > 0.93 and self.X < self.rightBorder):
				self.X += 3
				base.camera.setX(self.X)

			elif(self.mouseX < -0.93 and self.X > self.leftBorder):
				self.X -= 3
				base.camera.setX(self.X)
				
			#Creating 2 invisible borders to the vertical axis (y axis)
			if(self.mouseY > 0.93 and self.Y < self.upperBorder):
				self.Y += 3
				base.camera.setY(self.Y)

			elif(self.mouseY < -0.93 and self.Y > self.bottomBorder):
				self.Y -= 3
				base.camera.setY(self.Y)

				
	def scrollCamera(self, action):
		if ( action == "scroll_UP" and self.Z > 120):
			self.Z -= 2
		if ( action == "scroll_DOWN" and self.Z < 180):
			self.Z += 2 
		base.camera.setZ(self.Z)
		self.updateLimits()

			
			

