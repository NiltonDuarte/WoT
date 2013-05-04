################################################################
#This file will have all classes related to the HUD of our game
################################################################
#importing panda3D
import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject
from panda3d.core import TextNode
#Vec2 and Vec3 will help positioning the objects
from panda3d.core import Vec2,Vec3
from panda3d.core import Point2, Point3, CardMaker
#
from direct.gui.DirectGui import *

#hudTexts is the node that will hold all text nodes of the game
hudTexts = render2d.attachNewNode("HUD Texts")

class gameText(DirectObject):
	'''This class creates texts that will be part of the HUD of the game
	'''
	def __init__(self, name, content, position, scale):
		#Writing our gameText and giving it a name(to help identifying which text is this)
		self.name = TextNode('%s'%name)
		self.name.setText("%s"%content)
		#now this gameText is child of hudTexts node
		self.textNodePath = hudTexts.attachNewNode(self.name)
		#positioning and scaling our gameText
		self.position = Vec3(position)
		self.textNodePath.setX(self.position[0]), self.textNodePath.setZ(self.position[2])
		self.textNodePath.setScale(scale)
		
	def attachToObject(self, targetNode, targetPosition):
		'''This function will make the text follow any object that we want to
		   targetNode is the 3D model and targetPosition is the position of the model
		'''
		# Convert the point to the 3-d space of the camera 
		p3 = base.cam.getRelativePoint(targetNode, targetPosition) 
		# Convert it through the lens to render2d coordinates 
		p2 = Point2(0,0) 
		base.camLens.project(p3, p2) 
		r2d = Point3(p2[0], p2[1], 0) 
		# And then convert it to aspect2d coordinates 
		a2d = aspect2d.getRelativePoint(render2d, r2d) 
		print r2d
		self.position = a2d
		self.textNodePath.setX(a2d[0]), self.textNodePath.setY(p3[1]), self.textNodePath.setZ(a2d[1])
		

#This number is just to test changing scenes
stage = 0

class gameButton(DirectObject):
	'''Creates the buttons for the game's interface.
	   gameButton can be used to change the game's scenes 
	   or 
	   to create objects like tower during gameplay action
	'''
	def __init__(self, text, position, scale):
		#self.text contains the text to be displayed -> type: String
		self.text = text
		#self.position contains the position of the button -> type: Point2
		self.position = position
		#self.scale contains the size of the button -> type: Float
		self.scale = scale
		#self.button is the button with our own properties above -> type: DirectButton 
		self.button = DirectButton(text=("%s")%self.text, pos = position, scale = scale, command=self.changeScene)
		
	def changeScene(self):
		global stage
		stage = 1







