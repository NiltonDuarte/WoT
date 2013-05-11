#importing our modules
from HUD import *
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


#modelsNode is a child node of render that will holds all models of the game
modelsNode = render.attachNewNode("Models Node")


class Ball(DirectObject):
	def __init__(self):
		self.ball = loader.loadModel("Exported_Models/ball")
		self.ball.reparentTo(modelsNode)
		self.position = Vec3(1, 10, 0)
		self.ball.setPos(self.position)
		#Array with the keys
		self.keys = {"UP" : 0, "DOWN" : 0, "RIGHT" : 0, "LEFT" : 0}
        #Setting the keys
		self.accept("arrow_up", self.setKey, ["UP",1])       #key pressed
		self.accept("arrow_up-up", self.setKey, ["UP",0])    #key released
		self.accept("arrow_down", self.setKey, ["DOWN",1])
		self.accept("arrow_down-up", self.setKey, ["DOWN",0])
		self.accept("arrow_right", self.setKey, ["RIGHT",1])
		self.accept("arrow_right-up", self.setKey, ["RIGHT",0])
		self.accept("arrow_left", self.setKey, ["LEFT",1])
		self.accept("arrow_left-up", self.setKey, ["LEFT",0])
		self.ball.setColor(0,1.0,0,1.0)

	#Setting the state of the keys
	def setKey(self, key, val):
		self.keys[key] = val

    #Funcao responsavel por movimentar a bola    
	def moveBall(self):
		#Seta a nova posicao do objeto
		if ( self.keys["UP"] == 1):
			self.position += Vec3(0,0.1,0)
		if ( self.keys["DOWN"] == 1):
			self.position += Vec3(0,-0.1,0)
		if ( self.keys["RIGHT"] == 1):
			self.position += Vec3(0.1,0,0)
		if ( self.keys["LEFT"] == 1):
			self.position += Vec3(-0.1,0,0)
		self.ball.setPos(self.position)

bnt = sceneButton("HUE HUE",Point3(1,0,0),.05)
t = gameText('comida',"SUSHI",Vec3(0.5,0, 0), 0.07)
b = Ball()

life = lifeBar(Vec3(0,10,2))

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
		
		life.changeColor()
		
		#this function returns Task.cont
		return Task.cont



		
w = World()
run()
