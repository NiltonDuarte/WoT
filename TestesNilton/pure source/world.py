#importing our modules
from imports import *
#Other modules
import sys #to close the game screen with escape key

from pandaImports import *

#Setting the size of our game screen
wp = WindowProperties()
window_Width = 1200
window_Height = 640
wp.setSize(window_Width, window_Height)
base.win.requestProperties(wp)

#miniMap = HUDMap()
terr = TerrainModel()

"""
upperWall = WallFortune([0, 100, 0], "../arquivos de modelo/Wall")
bottomWall = WallFortune([0, -100, 0], "../arquivos de modelo/Wall")
leftWall = WallFortune([-100, 0, 0], "../arquivos de modelo/Wall_of_Fortune")
leftWall.rotateZ(90)
rightWall = WallFortune([100, 0, 0], "../arquivos de modelo/Wall_of_Fortune")
rightWall.rotateZ(270)
"""
player1 = Player("Player1", "lylyh")
player2 = Player("Player2", "Niltin")



sceneBtn = sceneButton("Teste Game",[-1.5, 0, -0.5],0.12)

gameScreenFSM = gameScreenFSM()
gameScreenFSM.request("InitScreen")
#gameFSM.request("PlayScreen")


class World(DirectObject):
	def __init__(self):
		#Adding the main task of the game (the game loop)
		self.gameTask = taskMgr.add(self.gameLoop, "gameLoop")
		taskMgr.add(mousePicking.mouseRayUpdate, "updatePicker")
		self.gameTask.last = 0
		#PStatClient.connect()
		
		base.enableParticles()
		base.enableAllAudio()
		base.enableMusic(True)
		base.enableSoundEffects(True)

		#base.cTrav.showCollisions(render)
		
		#Closes game when esc key is pressed
		self.accept('escape', sys.exit ) 
		
		#Array with the mouse actions
		self.mouseActions = {"scroll_UP" : 0, "scroll_DOWN" : 0}
		self.accept("wheel_down", self.setAction, ["scroll_DOWN", 1, "scroll_UP", 0])
		self.accept("wheel_up", self.setAction, ["scroll_DOWN", 0, "scroll_UP", 1])
		self.accept("mouse2", self.setAction, ["scroll_DOWN", 0, "scroll_UP", 0])

		
	#Setting the state of the actions
	def setAction(self, action, val, action2, val2):
		self.mouseActions[action] = val
		self.mouseActions[action2] = val2
			
	def gameLoop(self, task):
		'''This function run every frame of the game
		'''
		#Frame duration
		deltaTime = task.time - task.last
		task.last = task.time

		Player.currPlayer.camera.moveCameraXY()
		Player.currPlayer.camera.scrollCamera(self.mouseActions)
		#print self.mouseActions
		
		for  pkey in Projectile.projectileDict.keys():
			p = Projectile.projectileDict[pkey]
			if (p.colliding == True):
				p.projectileModel.projectileInstance.removeNode()
				del Projectile.projectileDict[pkey]
		for  pkey in Troop.troopDict.keys():
			troop = Troop.troopDict[pkey]
			if (troop.isDead):
				del Troop.troopDict[pkey]
		
		#this function returns Task.cont
		return Task.cont


