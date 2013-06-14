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
player = Player()

physicsObj = Physics()

mousePicking = MousePicking()

collisionObj = CollisionWoT(mousePicking, player)

#createBtn = createObjectButton("Create",[1.0, 0, -0.7],0.2,player, mousePicking)
sceneBtn = sceneButton("Play Game",[-0.5, 0, -0.5],0.12,player,physicsObj)

gameHud = GameHud(player, mousePicking)
class World(DirectObject):
	def __init__(self):
		#Adding the main task of the game (the game loop)
		self.gameTask = taskMgr.add(self.gameLoop, "gameLoop")
		taskMgr.add(mousePicking.mouseRayUpdate, "updatePicker")
		self.gameTask.last = 0
		#self.loadOnce makes the game load the objects only once -> type: boolean
		self.loadOnce = True
		base.cTrav.showCollisions(render)
		
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

		#Interactions between different objects

        
		#this function returns Task.cont
		return Task.cont


