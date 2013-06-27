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


terr = TerrainModel()
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
		#self.loadOnce makes the game load the objects only once -> type: boolean
		self.loadOnce = True
		base.enableParticles()
		#base.cTrav.showCollisions(render)
		
		self.accept('escape', sys.exit ) # exit on esc
		
	def loadObjects(self):
		'''Function that loads objects.
		   We can create different functions like this for each scene
		'''
		print "Once"
			
	def gameLoop(self, task):
		'''This function run every frame of the game
		'''
		#Frame duration
		deltaTime = task.time - task.last
		task.last = task.time

		player.Player.currPlayer.camera.moveCameraXY()
		#this function returns Task.cont
		return Task.cont


