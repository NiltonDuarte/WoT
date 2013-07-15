from HUD import *
import player
import mousePicking
from pandaImports import *
from direct.fsm.FSM import FSM
import player
"""This Module control the Screens Finite State Machines. Initial state(initial screen) and the play screen state"""


class gamePlayFSM(FSM):
	
	def __init__(self, hudObj):
		FSM.__init__(self, "WoT Game Play")
		self.hudObj = hudObj
		self.currPlayer = None

	def enterPlayer1(self):
		player.Player.inactivePlayer = player.Player.currPlayer
		player.Player.currPlayer = player.Player.playerDict["Player1"]
		self.currPlayer = player.Player.currPlayer
		self.currPlayer.loadPlayer()
		self.hudObj.updatePlayerDataTexts()
		mousePicking.pickerNode.setFromCollideMask(self.currPlayer.playerBitMask)
		print "Here is Player ", player.Player.currPlayer.name



	def exitPlayer1(self):
		self.currPlayer.updateTime()
		taskMgr.add(self.currPlayer.attackEnemy, "attack")
		if mousePicking.MousePicking.lastClickedTower != None:
			mousePicking.MousePicking.lastClickedTower.towerModel.resetColor()
		self.hudObj.resetHUD()
		
	def enterPlayer2(self):
		player.Player.inactivePlayer = player.Player.currPlayer
		player.Player.currPlayer = player.Player.playerDict["Player2"]
		self.currPlayer = player.Player.currPlayer
		self.currPlayer.loadPlayer()
		self.hudObj.updatePlayerDataTexts()
		mousePicking.pickerNode.setFromCollideMask(self.currPlayer.playerBitMask)
		print "Here is Player ", player.Player.currPlayer.name
		
				
	def exitPlayer2(self):
		self.currPlayer.updateTime()
		taskMgr.add(self.currPlayer.attackEnemy, "attack")
		if mousePicking.MousePicking.lastClickedTower != None:
			mousePicking.MousePicking.lastClickedTower.towerModel.resetColor()
		self.hudObj.resetHUD()
		
		
