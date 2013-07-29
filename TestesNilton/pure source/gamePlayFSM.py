from HUD import *
from HUDMap import *
from Models import *
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

		
		miniMap = HUDMap()
		terr = TerrainModel()


		upperWall = WallFortune([0, 100, 0], "../arquivos de modelo/Wall")
		#bottomWall = WallFortune([0, -100, 0], "../arquivos de modelo/Wall")
		leftWall = WallFortune([-100, 0, 0], "../arquivos de modelo/Wall_of_Fortune")
		leftWall.rotateZ(90)
		rightWall = WallFortune([100, 0, 0], "../arquivos de modelo/Wall_of_Fortune")
		rightWall.rotateZ(270)

		player1 = player.Player("Player1", "lylyh")
		player2 = player.Player("Player2", "Niltin")


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
		
		
