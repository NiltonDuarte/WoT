#importing our modules
from HUD import *
from Models import *
#sys module will be used to close the game window
import sys
#importing panda3D modules
import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject
#This will help move the objects
from direct.task.Task import Task
#Vec2 and Vec3 will help positioning the objects
from panda3d.core import Vec2,Vec3

#Setting the window size
from pandac.PandaModules import WindowProperties
wp = WindowProperties()
window_Width = 800
window_Height = 600
wp.setSize(window_Width, window_Height)
base.win.requestProperties(wp)






class World(DirectObject):
	def __init__(self):
		#Adding the main task of the game (the game loop)
		self.gameTask = taskMgr.add(self.gameLoop, "gameLoop")
		self.gameTask.last = 0
		#self.loadOnce makes the game load the objects only once -> type: boolean
		self.loadOnce = True
		
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
		b.moveBall()
		#b.fall()
		
		life.changeColor()
		life.changeSize()
		life.attachPosition(b.position)
		#this function returns Task.cont
		return Task.cont



		
w = World()
run()