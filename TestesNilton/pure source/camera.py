from direct.showbase.DirectObject import DirectObject

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
		#Setting our camera position to be top-down
		self.X = 0
		self.Y = -170  #terrainBoundLower[1] + (terrainBoundLower[1])/2
		self.Z = 150
		base.camera.setX(self.X)     
		base.camera.setY(self.Y)  #depth
		base.camera.setZ(self.Z)	#height
		#Setting the limits of our camera
		self.leftBorder = -50       #terrainBoundLower[0]/2
		self.rightBorder = 50       #terrainBoundUpper[0]/2
		self.upperBorder = -0     #terrainBoundLower[1]
		self.bottomBorder = -170    #2.5*terrainBoundLower[1]
		#Variables to help moving the camera
		self.mouseX = 0
		self.mouseY = 0
		self.mouseOnScreen = False

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
				self.X += 4
				base.camera.setX(self.X)
				#print "Moving rightwards"
			elif(self.mouseX < -0.93 and self.X > self.leftBorder):
				self.X -= 4
				base.camera.setX(self.X)
				#print "Moving leftwards"
			#else:
				#print "Not moving in X direction"
			#Creating 2 invisible borders to the vertical axis (y axis)	
			if(self.mouseY > 0.93 and self.Y < self.upperBorder):
				self.Y += 4
				base.camera.setY(self.Y)
				#print "Moving rightwards"
			elif(self.mouseY < -0.93 and self.Y > self.bottomBorder):
				self.Y -= 4
				base.camera.setY(self.Y)
				#print "Moving leftwards"
			#else:
				#print "Not moving in the Y direction"
				
	def scrollCamera(self, actions):
		if ( actions["scroll_UP"] == 1 and self.Z > 120):
			self.Z -= 1
		if ( actions["scroll_DOWN"] == 1 and self.Z < 180):
			self.Z += 1 
		base.camera.setZ(self.Z)
		#print self.Z
			
			

