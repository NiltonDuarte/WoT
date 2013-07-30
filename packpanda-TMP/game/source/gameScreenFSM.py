from HUD import *
import player
import mousePicking
import gamePlayFSM
import camera
from direct.fsm.FSM import FSM
"""This Module control the Play Finite State Machines. Player 1 and Player 2 state"""


class gameScreenFSM(FSM):
	
	def __init__(self):
		FSM.__init__(self, "WoT Screens")
		self.currHUD = None
		self.gamePlayFSM = None
		self.looserPlayerObj = None
		#Getting the main theme 
		self.mainThemeSong = Sound("../sounds/mainTheme.wav")
		self.mainThemeSong.setVolume(0.1)
		self.mainThemeSong.setLoop(True)

		#Getting the credits song
		self.creditsSong = Sound("../sounds/creditsTheme.wav")
		self.creditsSong.setVolume(0.1)
		self.creditsSong.setLoop(True)
		

	def enterInitScreen(self):
		self.currHUD = InitialScreenHUD(self)
		self.currHUD.initHUD()
		
	def exitInitScreen(self):
		self.currHUD.__del__()

	def enterCreditScreen(self):
		self.creditsSong.play()
		self.currHUD = CreditScreenHUD(self)
		self.currHUD.initHUD()
		
	def exitCreditScreen(self):
		self.creditsSong.stop()
		self.currHUD.__del__()
		
	def enterPlayScreen(self):
		self.mainThemeSong.play()
		self.currHUD = PlayScreenHUD(self,mousePicking.MousePicking)
		self.gamePlayFSM = gamePlayFSM.gamePlayFSM(self.currHUD)
		self.currHUD.initHUD()
		self.gamePlayFSM.request("Player1")
		mousePicking.MousePicking.gameHUD = self.currHUD
		camera.MyCamera.cameraEnabled = True
		
	def exitPlayScreen(self):
		self.mainThemeSong.stop()
		self.currHUD.__del__()
		self.gamePlayFSM.__del__()
		mousePicking.MousePicking.gameHUD = None
		camera.MyCamera.cameraEnabled = False
		
	def enterEndScreen(self):
		self.currHUD = EndScreenHUD()
		return
	
	def exitEndScreen(self):
		self.currHUD.__del__()
		return

	def update(self):
		self.currHUD.update()
		if self.gamePlayFSM != None:
			self.gamePlayFSM.update()
			for  pkey in player.Player.playerDict.keys():
				playerObj = player.Player.playerDict[pkey]
				if (playerObj.isDead):
					self.looserPlayerObj = playerObj
					self.request("EndScreen")
		
	
	
	

		

	
	
	
