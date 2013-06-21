from HUD import *
from direct.fsm.FSM import FSM
"""This Module control the Finite State Machines. Game states, initial state(initial screen) and the play state(player 1 and player 2)"""


class gameFSM(FSM):
	
	def __init__(self):
		FSM.__init__(self, "WoT")
		self.currHUD = None

	def enterInitScreen(self):
		self.currHUD = InitialScreenHUD(self)
		self.currHUD.initHUD()
		
	def exitInitScreen(self):
		self.currHUD.__del__()
		
	def enterPlayScreen(self):
		self.currHUD = PlayScreenHUD(self)
		self.currHUD.initHUD()
		
	def exitPlayScreen(self):
		self.currHUD.__del__()
	
	
	
