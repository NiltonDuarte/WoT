from HUD import *
import player
import mousePicking
from direct.fsm.FSM import FSM
import player
"""This Module control the Screens Finite State Machines. Initial state(initial screen) and the play screen state"""


class gamePlayFSM(FSM):
	
	def __init__(self, hudObj):
		FSM.__init__(self, "WoT Game Play")
		self.hubObj = hudObj

	def enterPlayer1(self):
		player.Player.inactivePlayer = player.Player.currPlayer
		player.Player.currPlayer = player.Player.playerDict["Player1"]
		print "Here is Player ", player.Player.currPlayer.name



	def exitPlayer1(self):
		self.hubObj.resetHUD()
		
	def enterPlayer2(self):
		player.Player.inactivePlayer = player.Player.currPlayer
		player.Player.currPlayer = player.Player.playerDict["Player2"]
		print "Here is Player ", player.Player.currPlayer.name
		
				
	def exitPlayer2(self):
		self.hubObj.resetHUD()
		
		
