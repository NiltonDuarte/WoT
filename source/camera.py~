#ARquivo com a classe camera

from direct.showbase.DirectObject import DirectObject

class Camera(DirectObject):
	'''This class uses the base.camera of panda3D to reuse
	   existing methods and create new ones
	'''
	def __init__(self):
		#Disabling mouse default function to enable moving the panda camera with our code
		base.disableMouse()
		#self.angle is the angle of the panda camera
		self.angle = 45
		#Setting our camera position to be top-down
		base.camera.setZ(50)
		base.camera.setY(-40)
		base.camera.setX(1)
		base.camera.setHpr(0.0 , -self.angle, 0.0)
		
		