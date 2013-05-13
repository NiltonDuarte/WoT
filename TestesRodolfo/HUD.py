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

from direct.gui.DirectGui import *
#This is used to set the color of lifebar and other objects
from panda3d.core import ColorAttrib

#hudTexts is the node that will hold all text nodes of the game
hudTexts = render2d.attachNewNode("HUD Texts")

#HUD_models holds all the models that HUD will use
HUD_models = render.attachNewNode("HUD Models")

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

#---------------------------------- TROOPS HUD ---------------------------------------------------------------		

class lifeBar(DirectObject):
	def __init__(self, position):
		#self.lifebar contains the model
		self.lifebar = loader.loadModel("Exported_Models/LifeBar")
		self.lifebar.reparentTo(HUD_models)
		#self.position contains the position of the lifebar -> type: Vec3
		self.position = position
		self.lifebar.setPos(self.position)
		#self.color helps tinting the lifebar model
		self.color = 0.0
		#The initial color of the lifebar is green
		self.lifebar.setColor(self.color,1-self.color, 0, 1.0)
		#self.size is the size of the lifebar
		self.size = 1.0
		self.lifebar.setSx(self.size)
	
	def changeColor(self):
		'''Changes the color of the lifebar from green to red
		'''
		if(self.size < 0.3):
			self.color = 1.0
			self.lifebar.setColor(self.color,1-self.color, 0, 1.0)
			#print "Almost dying"
		
	def changeSize(self):
		'''Change the size of the lifebar to tell the player
		   when the troop will die
		'''
		if(self.size > 0):
			self.size -= 0.01
			self.lifebar.setSx(self.size)
		#Here we kill our troop
		#else:
			#print "Died"
		
	def attachPosition(self, targetPosition):
		'''Puts the lifebar above the troop
		'''
		self.position[0], self.position[1], self.position[2] = targetPosition[0], targetPosition[1], targetPosition[2]+2
		self.lifebar.setPos(self.position)
		


#---------------------------------- BUTTONS ------------------------------------------------------------------

class gameButton(DirectObject):
	'''Creates the buttons for the game's interface.
		This class serves as the base for all other buttons classes.
	'''
	def __init__(self):
		#self.text contains the text to be displayed -> type: String
		self.text = ""
		#self.position contains the position of the button -> type: Point2
		self.position = Point2(0,0)
		#self.scale contains the size of the button -> type: Float
		self.scale = .00

		
class sceneButton(gameButton):
	'''Creates a button that changes between scenes
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
		print "Scene Changed"
		

class createObjectButton(gameButton):
	'''Creates a button that changes between scenes
	'''
	def __init__(self, text, position, scale):
		#self.text contains the text to be displayed -> type: String
		self.text = text
		#self.position contains the position of the button -> type: Point2
		self.position = position
		#self.scale contains the size of the button -> type: Float
		self.scale = scale
		#self.image contais the image of the object that this button will be able to create
		#self.image = img
		#self.button is the button with our own properties above -> type: DirectButton 
		self.button = DirectButton(text=("%s")%self.text, pos = position, scale = scale, command=self.createObject)

	def createObject(self):
		print "Object Created"

