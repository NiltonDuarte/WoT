#importing our modules
from imports import *

#from mousePicking import *

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




#t = gameText('comida',"SUSHI",[0.5,0, 0], 0.1)
b = Ball()
bolas = []
bolas.append(Ball())

life = lifeBar([0,10,2])

myCam = MyCamera()

terr = TerrainModel()
torres = []

#Torre roxa
torres.append(Torre())
torres[0].iniciarModelo([20,10,0], [0.5,0.0,0.5, 0.5])

fisicaObj = Physics()

collisionObj = CollisionWoT()

mousePicking = MousePicking(collisionObj)

createBtn = createObjectButton("Create",[1.0, 0, -0.7],0.2,torres, mousePicking)
sceneBtn = sceneButton("Play Game",[-0.5, 0, -0.5],0.12,torres,fisicaObj)

#** Let's manage now the collision events:
DO=DirectObject()
# if you went from step3 and step4, here should not be mysteries for you
DO.accept('mouseRay_cnode-into-terrain_cnode', collisionObj.collideEventIn)
DO.accept('mouseRay_cnode-out-terrain_cnode', collisionObj.collideEventOut)
DO.accept('mouseRay_cnode-again-terrain_cnode', collisionObj.collideEventAgain)

#** This is how we interact with mouse clicks
DO.accept('mouse1', mousePicking.mousePick, ['down',collisionObj])
DO.accept('mouse1-up', mousePicking.mousePick, ['up',collisionObj])


class World(DirectObject):
	def __init__(self):
		#Adding the main task of the game (the game loop)
		self.gameTask = taskMgr.add(self.gameLoop, "gameLoop")
        	taskMgr.add(mousePicking.mouseRayUpdate, "updatePicker")
		self.gameTask.last = 0
		#self.loadOnce makes the game load the objects only once -> type: boolean
		self.loadOnce = True
		base.cTrav.showCollisions(render)
		
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


