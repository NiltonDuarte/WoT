################################################################
#This file will have all classes related to the HUD of our game
################################################################

#Importing our modules
from imports import *
from tower import *
import mousePicking
import player


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

class PlayScreenHUD (DirectObject):
	def __init__(self):
		self.playScreenFrame=None
		self.isoScale = 3.2
		self.scale = (self.isoScale,1,self.isoScale)
		return
	def __del__(self):
		if (self.playScreenFrame != None):
			self.playScreenFrame.destroy()	
		return
		
	def initHUD(self):
		self.playScreenFrame = DirectFrame(	image = '../HUD images/gameBackgroundQuadrada.png',
								frameColor=(0,0,0,0.0),
								frameSize=(-1, 1, -1, 1),
								scale = self.scale
								)
		self.playScreenFrame.setTransparency(TransparencyAttrib.MAlpha)
		self.addAlphaTowerButton();
		self.addBetaTowerButton();
		self.addGamaTowerButton();
		self.addOmegaTowerButton();
		self.plusAttribButton();
		self.minusAttribButton();
			
	def addAlphaTowerButton(self):
		position = [-1.25/self.isoScale, 0, -0.74/self.isoScale]
		scale = 0.14/self.isoScale
		texture = loader.loadTexture("../texturas/greenTower_Button.png")
		button = DirectButton(self.playScreenFrame, pos = position, scale = scale, image = texture, command=self.createTower)
	def addBetaTowerButton(self):
		position = [-0.9/self.isoScale, 0, -0.74/self.isoScale]
		scale = 0.14/self.isoScale
		texture = loader.loadTexture("../texturas/greenTower_Button.png")
		button = DirectButton(self.playScreenFrame, pos = position, scale = scale, image = texture, command=self.createTower)

	def addGamaTowerButton(self):
		position = [-0.55/self.isoScale, 0, -0.74/self.isoScale]
		scale = 0.14/self.isoScale
		texture = loader.loadTexture("../texturas/greenTower_Button.png")
		button = DirectButton(self.playScreenFrame, pos = position, scale = scale, image = texture, command=self.createTower)

	def addOmegaTowerButton(self):
		position = [-0.2/self.isoScale, 0, -0.74/self.isoScale]
		scale = 0.14/self.isoScale
		texture = loader.loadTexture("../texturas/greenTower_Button.png")
		button = DirectButton(self.playScreenFrame, pos = position, scale = scale, image = texture, command=self.createTower)

	def createTower(self):
		player.Player.currPlayer.addTower()
		mousePicking.towerFollowMouse = True
		print "Tower Created"		
		
	def plusAttribButton(self):
		scale = 0.07/self.isoScale
		text = "+"
		button = DirectButton(self.playScreenFrame, text=("%s")%text, pos = [0.55/self.isoScale, 0, -0.612/self.isoScale], scale = scale, frameSize = (-0.25,0.35,-0.15,0.43))
		button = DirectButton(self.playScreenFrame, text=("%s")%text, pos = [0.55/self.isoScale, 0, -0.657/self.isoScale ], scale = scale, frameSize = (-0.25,0.35,-0.15,0.43))
		
	def minusAttribButton(self):
		scale = 0.07/self.isoScale
		text = "-"
		button = DirectButton(self.playScreenFrame, text=("%s")%text, pos = [0.6/self.isoScale, 0, -0.612/self.isoScale], scale = scale, frameSize = (-0.25,0.35,-0.15,0.43))
		button = DirectButton(self.playScreenFrame, text=("%s")%text, pos = [0.6/self.isoScale, 0, -0.657/self.isoScale], scale = scale, frameSize = (-0.25,0.35,-0.15,0.43))
		

		
class InitialScreenHUD(DirectObject):
	def __init__(self):
		self.initialScreenFrame = None
		self.isoScale = 1
		self.scale = (self.isoScale,1,self.isoScale)
		
	def __del__(self):
		if (self.initialScreenFrame != None):
			self.initialScreenFrame.destroy()
		
	def initHUD(self):
		self.initialScreenFrame = DirectFrame(	image = '../HUD images/initialScreen.png',
								frameColor=(0,0,0,0.0),
								frameSize=(-1, 1, -1, 1),
								scale = (1.9,1,1.2)
								)		
		button = DirectButton(text=("PLAY GAME"), pos = [0/self.isoScale,0,-0.25/self.isoScale], scale = 0.12/self.isoScale, command= self.changeScene)

	def changeScene(self):	
		print "Scene Changed"
		
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
		self.position = Point3(*position)
		#self.scale contains the size of the button -> type: Float
		self.scale = scale
		#self.button is the button with our own properties above -> type: DirectButton 
		self.button = DirectButton(text=("%s")%self.text, pos = self.position, scale = self.scale, command=self.changeScene)

	def changeScene(self):
		for tower in player.Player.currPlayer.getTowerList():
			if tower.towerInicialized:
				tower.shootProjectile(tower.position, [10,0,13])
				tower.createTroop()
		print "Scene Changed"
		


