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
		base.camera.setX(1)     
		base.camera.setY(-190)  #depth
		base.camera.setZ(100)	#height
		
		
