################################################################
#This file will have all classes related to the HUD of our game
################################################################

#Importing our modules
from imports import *
from tower import *


#importing panda3D
import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject
from panda3d.core import TextNode, TransparencyAttrib

#importing onscreenImage
from direct.gui.OnscreenImage import OnscreenImage


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

class GameHud (DirectObject):
	def __init__(self,player, mousePicking):
		"""
		self.screenImage = loader.loadModel('../HUD images/gameBackground.egg')
		self.background = self.screenImage.find('**/gameBackground')
		#self.background.setScale(3.75,1,2)
		self.background.reparentTo(aspect2d)
		self.myImage=OnscreenImage(image = '../HUD images/gameBackgroundQuadrada.png', scale = (3.2,1,3.2) )
		self.myImage.setTransparency(TransparencyAttrib.MAlpha)
		
		
		"""
		
		self.player = player
		self.mousePicking = mousePicking
		self.gameFrame = DirectFrame(	image = '../HUD images/gameBackgroundQuadrada.png',
								frameColor=(0,0,0,0.0),
								frameSize=(-1, 1, -1, 1),
								scale = (3.2,1,3.2)
								)
		self.gameFrame.setTransparency(TransparencyAttrib.MAlpha)
		self.addAlphaTowerButton();
		self.addBetaTowerButton();
		self.addGamaTowerButton();
		self.addOmegaTowerButton();
		self.plusAttribButton();
		self.minusAttribButton();
		
	def addAlphaTowerButton(self):
		position = [-1.25, 0, -0.74]
		scale = 0.14
		texture = loader.loadTexture("../texturas/greenTower_Button.png")
		button = DirectButton(pos = position, scale = scale, image = texture, command=self.createTower)
	def addBetaTowerButton(self):
		position = [-0.9, 0, -0.74]
		scale = 0.14
		texture = loader.loadTexture("../texturas/greenTower_Button.png")
		button = DirectButton(pos = position, scale = scale, image = texture, command=self.createTower)

	def addGamaTowerButton(self):
		position = [-0.55, 0, -0.74]
		scale = 0.14
		texture = loader.loadTexture("../texturas/greenTower_Button.png")
		button = DirectButton(pos = position, scale = scale, image = texture, command=self.createTower)

	def addOmegaTowerButton(self):
		position = [-0.2, 0, -0.74]
		scale = 0.14
		texture = loader.loadTexture("../texturas/greenTower_Button.png")
		button = DirectButton(pos = position, scale = scale, image = texture, command=self.createTower)

	def createTower(self):
		self.player.addTower()
		self.mousePicking.towerFollowMouse = True
		print "Object Created"		
		
	def plusAttribButton(self):
		scale = 0.07
		text = "+"
		button = DirectButton(text=("%s")%text, pos = [0.55, 0, -0.612], scale = scale, frameSize = (-0.25,0.35,-0.15,0.43))
		button = DirectButton(text=("%s")%text, pos = [0.55, 0, -0.657 ], scale = scale, frameSize = (-0.25,0.35,-0.15,0.43))
		
	def minusAttribButton(self):
		scale = 0.07
		text = "-"
		button = DirectButton(text=("%s")%text, pos = [0.6, 0, -0.612], scale = scale, frameSize = (-0.25,0.35,-0.15,0.43))
		button = DirectButton(text=("%s")%text, pos = [0.6, 0, -0.657], scale = scale, frameSize = (-0.25,0.35,-0.15,0.43))
		
		
		


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
	def __init__(self, text, position, scale, player,physicsObj):
		#self.text contains the text to be displayed -> type: String
		self.text = text
		#self.position contains the position of the button -> type: Point2
		self.position = Point3(*position)
		#self.scale contains the size of the button -> type: Float
		self.scale = scale
		#self.button is the button with our own properties above -> type: DirectButton 
		self.button = DirectButton(text=("%s")%self.text, pos = self.position, scale = self.scale, command=self.changeScene, extraArgs=[player,physicsObj])

	def changeScene(self, player, physicsObj):
		for tower in player.getTowerList():
			tower.shootProjectile(tower.position, [10,0,13],physicsObj)
			tower.createTroop()
		print "Scene Changed"
		

class createObjectButton(gameButton):
	'''Creates a button that changes between scenes
	'''

	def __init__(self, text, position, scale, player, mousePicking): 
		#Setting the texture to the tower
		self.texture = loader.loadTexture("../texturas/greenTower_Button.png")
		#self.text contains the text to be displayed -> type: String
		self.text = text
		#self.position contains the position of the button -> type: Point2
		self.position = Point3(*position)
		#self.scale contains the size of the button -> type: Float
		self.scale = scale
		#self.image contais the image of the object that this button will be able to create
		#self.image = img
		#self.button is the button with our own properties above -> type: DirectButton 
		self.button = DirectButton(pos = position, scale = scale, image = self.texture, command=self.createObject, extraArgs=[mousePicking, player] )


        
	def createObject(self, mousePicking, player):
		player.addTower()
		mousePicking.towerFollowMouse = True
		print "Object Created"

