################################################################
#This file will have all classes related to the HUD of our game
################################################################

#Importing our modules
#from imports import *
from tower import *
import player
from commonFunctions import *
from Sound import *


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
HUD_models = aspect2d.attachNewNode("HUD Models")

#Getting the sound effects 
clickButtonSound = Sound("../sounds/buttonClick.wav")
clickButtonSound.setVolume(0.5)
turnPass_Sound = Sound("../sounds/changeTurn.wav")
turnPass_Sound.setVolume(0.5)

#Getting the main theme
mainThemeSong = Sound("../sounds/mainTheme.wav")
mainThemeSong.setVolume(0.1)
mainThemeSong.setLoop(True)

class PlayScreenHUD (DirectObject):
	def __init__(self, gameScreenFSM, mousePicking):
		self.gameScreenFSM = gameScreenFSM
		self.mousePicking = mousePicking
		self.playScreenFrame=None
		self.isoScale = 3.2
		self.scale = (self.isoScale,1,self.isoScale)
		self.artImage = None
		self.labelShootPower = self.labelTxShoot = self.labelRangeView = self.labelTxTroops = None
		self.labelMass = self.labelSpreadRay = self.labelSpreadPercentage = self.labelDot = self.labelDamageDuration = self.labelSlow = self.labelSlowDuration = self.labelChanceCritical = None
		self.labelLifeParam = self.labelSpeedParam = self.labelResistenceParam = None
		self.labelLife = self.labelSpeed = self.labelResistence = None
		#Creating a timer for this class
		taskMgr.add(self.timeCounter, "PlayScreenHUD timer")
		self.time = 0
		self.changeTurnText = None
		self.changeTurnTimer = 0
		
	def __del__(self):
		if (self.playScreenFrame != None):
			self.playScreenFrame.destroy()	
		return
		
	def timeCounter(self, task):
		self.time = task.time
	
		#print self.changeTurnText
		if(self.changeTurnText == None):
			self.changeTurnTimer = 0
		else:
			if(turnPass_Sound.getSoundStatus() == 1):
				self.changeTurnText.destroy()
				self.changeTurnText = None
			
		return Task.cont
		
	def initHUD(self):
		self.playScreenFrame = DirectFrame(HUD_models,
								image = '../HUD images/gameBackgroundQuadrada.png',
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
		self.addArtImage();
		self.addAttributeTexts();
		self.addPlayerDataTexts();
		self.turnPassButton();
		mainThemeSong.play()
			
	def addAlphaTowerButton(self):
		position = [-1.25/self.isoScale, 0, -0.74/self.isoScale]
		scale = 0.14/self.isoScale
		texture = loader.loadTexture("../HUD images/AlphaTower_Button.png")
		button = DirectButton(self.playScreenFrame, pos = position, scale = scale, image = texture, command=self.createTower, extraArgs = ["Alpha Tower"])
	def addBetaTowerButton(self):
		position = [-0.9/self.isoScale, 0, -0.74/self.isoScale]
		scale = 0.14/self.isoScale
		texture = loader.loadTexture("../HUD images/BetaTower_Button.png")
		button = DirectButton(self.playScreenFrame, pos = position, scale = scale, image = texture, command=self.createTower, extraArgs = ["Beta Tower"])
	def addGamaTowerButton(self):
		position = [-0.55/self.isoScale, 0, -0.74/self.isoScale]
		scale = 0.14/self.isoScale
		texture = loader.loadTexture("../HUD images/GamaTower_Button.png")
		button = DirectButton(self.playScreenFrame, pos = position, scale = scale, image = texture, command=self.createTower, extraArgs = ["Gama Tower"])

	def addOmegaTowerButton(self):
		position = [-0.2/self.isoScale, 0, -0.74/self.isoScale]
		scale = 0.14/self.isoScale
		texture = loader.loadTexture("../HUD images/OmegaTower_Button.png")
		button = DirectButton(self.playScreenFrame, pos = position, scale = scale, image = texture, command=self.createTower, extraArgs = ["Omega Tower"])

	def createTower(self, towerType):
		player.Player.currPlayer.addTower(towerType)
		self.mousePicking.towerFollowMouse = True
		print "Tower Created"	
		clickButtonSound.play()	
		
	def plusAttribButton(self):
		scale = 0.07/self.isoScale
		text = "+"
		button = DirectButton(self.playScreenFrame, text=("%s")%text, pos = [0.55/self.isoScale, 0, -0.615/self.isoScale], scale = scale, frameSize = (-0.25,0.35,-0.15,0.43))
		button = DirectButton(self.playScreenFrame, text=("%s")%text, pos = [0.55/self.isoScale, 0, -0.660/self.isoScale ], scale = scale, frameSize = (-0.25,0.35,-0.15,0.43))
		
	def minusAttribButton(self):
		scale = 0.07/self.isoScale
		text = "-"
		button = DirectButton(self.playScreenFrame, text=("%s")%text, pos = [0.6/self.isoScale, 0, -0.615/self.isoScale], scale = scale, frameSize = (-0.25,0.35,-0.15,0.43))
		button = DirectButton(self.playScreenFrame, text=("%s")%text, pos = [0.6/self.isoScale, 0, -0.660/self.isoScale], scale = scale, frameSize = (-0.25,0.35,-0.15,0.43))
	
	def turnPassButton(self):
		position = [1.5, 0, -0.5]
		text = "End Turn"
		scale = 0.12
		button = DirectButton(text=("%s")%text, pos = position, scale = scale, command=self.turnPass)
		
	def turnPass(self):
		self.gameScreenFSM.gamePlayFSM.request(player.Player.inactivePlayer.playerNumber)
		turnPass_Sound.play()
		self.drawChangeTurn()
		return
		
	def drawChangeTurn(self):
		#Creating the change turn text 
		self.changeTurnText = DirectFrame(self.playScreenFrame,
								image = '../HUD images/changeTurn_Text.png',
								frameColor=(0,0,0,0.0),
								frameSize=(-1, 1, -1, 1),
								pos = [0, 0, 0.05],
								scale = 0.4/self.isoScale
								)
		self.changeTurnText.setSx(3.8/self.isoScale)
		self.changeTurnText.setTransparency(TransparencyAttrib.MAlpha)
	
	def addArtImage(self):
		self.artImage = DirectFrame(self.playScreenFrame, 
								image = '../HUD images/defaultArt.png',
								frameColor=(0,0,0,0.0),
								frameSize=(-1, 1, -1, 1),
								pos = [-1.675/self.isoScale, 0, -0.74/self.isoScale],
								scale = 0.16/self.isoScale
								)
	def updateArtImage(self, artPath = "../HUD images/defaultArt.png"):
		self.artImage.destroy()
		self.artImage = DirectFrame(self.playScreenFrame, 
								image = artPath,
								frameColor=(0,0,0,0.0),
								frameSize=(-1, 1, -1, 1),
								pos = [-1.675/self.isoScale, 0, -0.74/self.isoScale],
								scale = 0.16/self.isoScale
								)
	def addAttributeTexts(self):
		#Tower
		self.labelShootPower = DirectLabel(self.playScreenFrame, text="-", text_bg = (0,0,0,0), frameColor = (0,0,0,0), pos = [0.35/self.isoScale, 0, -0.615/self.isoScale], scale = 0.05/self.isoScale)
		self.labelTxShoot = DirectLabel(self.playScreenFrame, text="-", text_bg = (0,0,0,0), frameColor = (0,0,0,0), pos = [0.35/self.isoScale, 0, -0.660/self.isoScale], scale = 0.05/self.isoScale)
		self.labelRangeView = DirectLabel(self.playScreenFrame, text="-", text_bg = (0,0,0,0), frameColor = (0,0,0,0), pos = [0.35/self.isoScale, 0, -0.705/self.isoScale], scale = 0.05/self.isoScale)
		self.labelTxTroops = DirectLabel(self.playScreenFrame, text="-", text_bg = (0,0,0,0), frameColor = (0,0,0,0), pos = [0.5/self.isoScale, 0, -0.750/self.isoScale], scale = 0.05/self.isoScale)
		#Projectile
		self.labelMass = DirectLabel(self.playScreenFrame, text="-", text_bg = (0,0,0,0), frameColor = (0,0,0,0), pos = [1/self.isoScale, 0, -0.615/self.isoScale], scale = 0.05/self.isoScale)
		self.labelSpreadRay = DirectLabel(self.playScreenFrame, text="-", text_bg = (0,0,0,0), frameColor = (0,0,0,0), pos = [1/self.isoScale, 0, -0.660/self.isoScale], scale = 0.05/self.isoScale)
		self.labelSpreadPercentage = DirectLabel(self.playScreenFrame, text="-", text_bg = (0,0,0,0), frameColor = (0,0,0,0), pos = [1.25/self.isoScale, 0, -0.660/self.isoScale], scale = 0.05/self.isoScale)
		self.labelDot = DirectLabel(self.playScreenFrame, text="-", text_bg = (0,0,0,0), frameColor = (0,0,0,0), pos = [1/self.isoScale, 0, -0.705/self.isoScale], scale = 0.05/self.isoScale)
		self.labelDamageDuration = DirectLabel(self.playScreenFrame, text="-", text_bg = (0,0,0,0), frameColor = (0,0,0,0), pos = [1.25/self.isoScale, 0, -0.705/self.isoScale], scale = 0.05/self.isoScale)
		self.labelSlow = DirectLabel(self.playScreenFrame, text="-", text_bg = (0,0,0,0), frameColor = (0,0,0,0), pos = [1/self.isoScale, 0, -0.750/self.isoScale], scale = 0.05/self.isoScale)
		self.labelSlowDuration = DirectLabel(self.playScreenFrame, text="-", text_bg = (0,0,0,0), frameColor = (0,0,0,0), pos = [1.25/self.isoScale, 0, -0.750/self.isoScale], scale = 0.05/self.isoScale)
		self.labelChanceCritical = DirectLabel(self.playScreenFrame, text="=-", text_bg = (0,0,0,0), frameColor = (0,0,0,0), pos = [1/self.isoScale, 0, -0.795/self.isoScale], scale = 0.05/self.isoScale)
		#Troop
		self.labelLifeParam = DirectLabel(self.playScreenFrame, text="---", text_bg = (0,0,0,0), frameColor = (0,0,0,0), pos = [1.6/self.isoScale, 0, -0.615/self.isoScale], scale = 0.05/self.isoScale)
		self.labelSpeedParam = DirectLabel(self.playScreenFrame, text="---", text_bg = (0,0,0,0), frameColor = (0,0,0,0), pos = [1.6/self.isoScale, 0, -0.660/self.isoScale], scale = 0.05/self.isoScale)
		self.labelResistenceParam = DirectLabel(self.playScreenFrame, text="---", text_bg = (0,0,0,0), frameColor = (0,0,0,0), pos = [1.6/self.isoScale, 0, -0.705/self.isoScale], scale = 0.05/self.isoScale)
		self.labelLife = DirectLabel(self.playScreenFrame, text="-", text_bg = (0,0,0,0), frameColor = (0,0,0,0), pos = [1.8/self.isoScale, 0, -0.615/self.isoScale], scale = 0.05/self.isoScale)
		self.labelSpeed = DirectLabel(self.playScreenFrame, text="-", text_bg = (0,0,0,0), frameColor = (0,0,0,0), pos = [1.8/self.isoScale, 0, -0.660/self.isoScale], scale = 0.05/self.isoScale)
		self.labelResistence = DirectLabel(self.playScreenFrame, text="-", text_bg = (0,0,0,0), frameColor = (0,0,0,0), pos = [1.8/self.isoScale, 0, -0.705/self.isoScale], scale = 0.05/self.isoScale)
		
	def updateTowerAttributeTexts(self, towerObj):
		#Tower
		self.labelShootPower["text"] = str(towerObj.listShootPower[VALUE])
		self.labelTxShoot["text"] = str(towerObj.listTxShoot[VALUE])
		self.labelRangeView["text"] = str(towerObj.listRangeView[VALUE])
		self.labelTxTroops["text"] = str(towerObj.listTxTroops[VALUE])
		#Projectile
		styp = None
		cfTree = ET.parse('projectile.xml')
		cfRoot = cfTree.getroot()
		for element in cfRoot.findall('projectile'):
			if (element.get('type') == towerObj.projectileType):
				typ = element
		self.labelMass["text"] = typ.find('mass').text
		self.labelSpreadRay["text"] = typ.find('spreadRay').text
		self.labelSpreadPercentage["text"] = typ.find('spreadPercentage').text
		self.labelDot["text"] = typ.find('dot').text
		self.labelDamageDuration["text"] = typ.find('damageDuration').text
		self.labelSlow["text"] = typ.find('slow').text
		self.labelSlowDuration["text"] = typ.find('slowDuration').text
		self.labelChanceCritical["text"] = typ.find('chanceCritical').text
		#Troop
		typ = None
		cfTree = ET.parse('troop.xml')
		cfRoot = cfTree.getroot()
		for element in cfRoot.findall('troop'):
			if (element.get('type') == towerObj.troopType):
				typ = element
		self.labelLifeParam["text"] = typ.find('life').find('Min').text + "-" + typ.find('life').find('Max').text
		self.labelSpeedParam["text"] = typ.find('speed').find('Min').text + "-" + typ.find('speed').find('Max').text
		self.labelResistenceParam["text"] = typ.find('resistence').find('Min').text + "-" + typ.find('resistence').find('Max').text
		self.labelLife["text"] = "-"
		self.labelSpeed["text"] = "-"
		self.labelResistence["text"] = "-"				
		
	def updateTroopAttributeTexts(self,troopObj):
		self.updateTowerAttributeTexts(troopObj.sourceTower)
		self.labelLife["text"] = str(troopObj.listLife[VALUE])
		self.labelSpeed["text"] = str(troopObj.listSpeed[VALUE])
		self.labelResistence["text"] = str(troopObj.listResistence[VALUE])
		
	def resetAttributeTexts(self):
		#Tower
		self.labelShootPower["text"] = "-"
		self.labelTxShoot["text"] = "-"
		self.labelRangeView["text"] = "-"
		self.labelTxTroops["text"] = "-"
		#Projectile
		self.labelMass["text"] = "-"
		self.labelSpreadRay["text"] = "-"
		self.labelSpreadPercentage["text"] = "-"
		self.labelDot["text"] = "-"
		self.labelDamageDuration["text"] = "-"
		self.labelSlow["text"] = "-"
		self.labelSlowDuration["text"] = "-"
		self.labelChanceCritical["text"] = "-"	
		#Troop
		self.labelLifeParam["text"] = "---"
		self.labelSpeedParam["text"] = "---"
		self.labelResistenceParam["text"] = "---"	
		self.labelLife["text"] = "-"
		self.labelSpeed["text"] = "-"
		self.labelResistence["text"] = "-"		


	def resetHUD(self):
		self.resetAttributeTexts()

	def addPlayerDataTexts(self):
		currPlayer = player.Player.currPlayer
		self.labelName = DirectLabel(self.playScreenFrame, text= currPlayer.name, text_bg = (0,0,0,0), frameColor = (0,0,0,0), pos = [-1.79/self.isoScale, 0, 0.94/self.isoScale], scale = 0.05/self.isoScale)

	def updatePlayerDataTexts(self):
		currPlayer = player.Player.currPlayer
		self.labelName["text"] = currPlayer.name
		
class InitialScreenHUD(DirectObject):
	def __init__(self, gameScreenFSM):
		self.gameScreenFSM = gameScreenFSM
		self.initialScreenFrame = None
		self.isoScale = 1
		self.scale = (self.isoScale,1,self.isoScale)
		
	def __del__(self):
		if (self.initialScreenFrame != None):
			self.initialScreenFrame.destroy()
		
	def initHUD(self):
		self.initialScreenFrame = DirectFrame(HUD_models,
								image = '../HUD images/initialScreen.png',
								frameColor=(0,0,0,0.0),
								frameSize=(-1, 1, -1, 1),
								scale = (1.9,1,1.2)
								)		
		button = DirectButton(self.initialScreenFrame, text=("PLAY GAME"), pos = [0/self.isoScale,0,-0.25/self.isoScale], scale = 0.06/self.isoScale, command= self.changeScene)

	def changeScene(self):
		self.gameScreenFSM.request("PlayScreen")
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
				#tower.shootProjectile([10,0,13])
				tower.createTroop()
		print "Scene Changed"
		


