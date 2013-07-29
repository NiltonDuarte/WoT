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



#sceneBtn = sceneButton("Teste Game",[-1.5, 0, -0.5],0.12)

gameScreenFSM = gameScreenFSM()
gameScreenFSM.request("InitScreen")
#gameScreenFSM.request("PlayScreen")


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
		#base.oobeCull()
		
		#Closes game when esc key is pressed
		self.accept('escape', sys.exit ) 
		
		#mouse wheel moving the camera
		self.accept("wheel_down", Player.mouseScroll, ["scroll_DOWN"])
		self.accept("wheel_up", Player.mouseScroll, ["scroll_UP"])

		

			
	def gameLoop(self, task):
		'''This function run every frame of the game
		'''
		#Frame duration
		deltaTime = task.time - task.last
		task.last = task.time
		
		#Getting the FPS of the game
		#print globalClock.getAverageFrameRate()

		Player.moveCameraXY()

		for  pkey in Projectile.projectileDict.keys():
			p = Projectile.projectileDict[pkey]
			if (p.colliding == True):
				p.projectileModel.projectileInstance.removeNode()
				del Projectile.projectileDict[pkey]
		for  pkey in Troop.troopDict.keys():
			troop = Troop.troopDict[pkey]
			if (troop.isDead):
				if (troop.isAnimationFinished()):
					del Troop.troopDict[pkey]
		
		#this function returns Task.cont
		return Task.cont


