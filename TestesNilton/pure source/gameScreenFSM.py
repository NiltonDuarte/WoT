from HUD import *
import player
import mousePicking
import gamePlayFSM
from direct.fsm.FSM import FSM
"""This Module control the Play Finite State Machines. Player 1 and Player 2 state"""


class gameScreenFSM(FSM):
	
	def __init__(self):
		FSM.__init__(self, "WoT Screens")
		self.currHUD = None
		self.gamePlayFSM = None
		

	def enterInitScreen(self):
		self.currHUD = InitialScreenHUD(self)
		self.currHUD.initHUD()
		
	def exitInitScreen(self):
		self.currHUD.__del__()

		
	def enterPlayScreen(self):
		self.currHUD = PlayScreenHUD(self,mousePicking.MousePicking)
		self.gamePlayFSM = gamePlayFSM.gamePlayFSM(self.currHUD)
		self.currHUD.initHUD()
		mousePicking.MousePicking.gameHUD = self.currHUD
		player.Player.currPlayer.camera.cameraEnabled = True
		
	def exitPlayScreen(self):
		self.currHUD.__del__()
		player.Player.currPlayer.camera.cameraEnabled = False
		
	def enterEndScreen(self):
		return
	
	def exitEndScreen(self):
		return
	
	
	

		

	
	
	
