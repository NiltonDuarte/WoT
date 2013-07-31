from HUD import *
from HUDMap import *
from Models import *
import player
import troop
import projectile
import mousePicking
import tower
from pandaImports import *
from direct.fsm.FSM import FSM

"""This Module control the Screens Finite State Machines. Initial state(initial screen) and the play screen state"""


class gamePlayFSM(FSM):
	
	def __init__(self, hudObj):
		FSM.__init__(self, "WoT Game Play")
		self.hudObj = hudObj
		self.currPlayer = None

		
		self.miniMap = HUDMap()
		self.terr = TerrainModel()


		self.upperWall = WallFortune([0, 100, 0], "../arquivos de modelo/Wall")
		#bottomWall = WallFortune([0, -100, 0], "../arquivos de modelo/Wall")
		self.leftWall = WallFortune([-100, 0, 0], "../arquivos de modelo/Wall_of_Fortune")
		self.leftWall.rotateZ(90)
		self.rightWall = WallFortune([100, 0, 0], "../arquivos de modelo/Wall_of_Fortune")
		self.rightWall.rotateZ(270)

		self.player1 = player.Player("Player1", "lylyh")
		self.player2 = player.Player("Player2", "Niltin")

	def __del__(self):
		self.terr.destroy()
		self.upperWall.destroy()
		self.leftWall.destroy()
		self.rightWall.destroy()
		self.miniMap.destroy()
		for  pkey in projectile.Projectile.projectileDict.keys():
			p = projectile.Projectile.projectileDict[pkey]
			p.projectileModel.projectileInstance.removeNode()
			del projectile.Projectile.projectileDict[pkey]
		for  pkey in troop.Troop.troopDict.keys():
			troopObj = troop.Troop.troopDict[pkey]
			troopObj.troopModel.troopInstance.removeNode()
			del troop.Troop.troopDict[pkey]
		for  pkey in tower.Tower.towerDict.keys():
			towerObj = tower.Tower.towerDict[pkey]
			towerObj.towerModel.towerInstance.removeNode()
			del tower.Tower.towerDict[pkey]

		
		
	def enterPlayer1(self):
		player.Player.inactivePlayer = player.Player.currPlayer
		player.Player.currPlayer = player.Player.playerDict["Player1"]
		self.currPlayer = player.Player.currPlayer
		self.currPlayer.loadPlayer()
		self.hudObj.updatePlayerDataTexts()
		mousePicking.pickerNode.setFromCollideMask(self.currPlayer.playerBitMask)
		#print "Here is Player ", player.Player.currPlayer.name



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
		#print "Here is Player ", player.Player.currPlayer.name
		
				
	def exitPlayer2(self):
		self.currPlayer.updateTime()
		taskMgr.add(self.currPlayer.attackEnemy, "attack")
		if mousePicking.MousePicking.lastClickedTower != None:
			mousePicking.MousePicking.lastClickedTower.towerModel.resetColor()
		self.hudObj.resetHUD()

	def update(self):
		for  pkey in projectile.Projectile.projectileDict.keys():
			p = projectile.Projectile.projectileDict[pkey]
			if (p.colliding == True):
				p.projectileModel.projectileInstance.removeNode()
				del projectile.Projectile.projectileDict[pkey]
		for  pkey in troop.Troop.troopDict.keys():
			troopObj = troop.Troop.troopDict[pkey]
			if (troopObj.isDead):
				if (troopObj.isAnimationFinished()):
					print "deleted"
					del troop.Troop.troopDict[pkey]
		
		
		
