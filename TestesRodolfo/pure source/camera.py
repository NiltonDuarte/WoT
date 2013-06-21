from direct.showbase.DirectObject import DirectObject

class MyCamera(DirectObject):
	'''This class uses the base.camera of panda3D to reuse
	   existing methods and create new ones
	'''
	def __init__(self):
		#Disabling mouse default function to enable moving the panda camera with our code
		base.disableMouse()
		#Setting the angle of our camera
		self.angle = 45
		base.camera.setHpr(0.0 , -self.angle, 0.0)
		#Setting our camera position to be top-down
		self.X = 1
		self.Y = -240
		self.Z = 250
		base.camera.setX(self.X)     
		base.camera.setY(self.Y)  #depth
		base.camera.setZ(self.Z)	#height
		#Variables to help moving the camera
		self.mouseX = 0
		self.mouseY = 0
		self.mouseOnScreen = False 
		
	def moveCameraXY(self):
		#Getting the position of the mouse
		if base.mouseWatcherNode.hasMouse():
			self.mouseX = base.mouseWatcherNode.getMouseX()
			self.mouseY = base.mouseWatcherNode.getMouseY()
			self.mouseOnScreen = True
		else:
			self.mouseOnScreen = False
		
		#The camera only moves when the mouse is on the screen
		if(self.mouseOnScreen):
			#Creating 2 invisible borders on the right and left side (x axis)	
			if(self.mouseX > 0.90):
				self.X += 4
				base.camera.setX(self.X)
				#print "Moving rightwards"
			elif(self.mouseX < -0.90):
				self.X -= 4
				base.camera.setX(self.X)
				#print "Moving leftwards"
			else:
				print "Not moving in X direction"
			#Creating 2 invisible borders to the vertical axis (y axis)	
			if(self.mouseY > 0.90):
				self.Y += 4
				base.camera.setY(self.Y)
				#print "Moving rightwards"
			elif(self.mouseY < -0.90):
				self.Y -= 4
				base.camera.setY(self.Y)
				#print "Moving leftwards"
			else:
				print "Not moving in the Y direction"
			
			

