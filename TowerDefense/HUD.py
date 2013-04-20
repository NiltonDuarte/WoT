################################################################
#This file will have all classes related to the HUD of our game
################################################################
#importing panda3D
import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject
from panda3d.core import TextNode
#Vec2 and Vec3 will help positioning the objects
from panda3d.core import Vec2,Vec3
#This will help move the objects
from direct.task.Task import Task

#hudTexts is the node that will hold all text nodes of the game
hudTexts = aspect2d.attachNewNode("HUD Texts")

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
		
	def attachToObject(self, targetPosition):
		'''This function will make the text follow any object that we want to
		'''
		self.position = targetPosition
		self.textNodePath.setX(self.position[0]), self.textNodePath.setZ(self.position[2])
		
