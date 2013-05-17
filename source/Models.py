#importing panda3D modules
import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject
#This will help move the objects
from direct.task.Task import Task
#Vec2 and Vec3 will help positioning the objects
from panda3d.core import Vec2,Vec3
from panda3d.core import Point2, Point3
from pandac.PandaModules import CollisionHandlerEvent, CollisionNode, CollisionBox, CollisionTraverser, BitMask32, CollisionRay


#modelsNode is a child node of render that will holds all models of the game
gameModelsNode = render.attachNewNode("Game Models Node")

class TowerModel(DirectObject):
	'''This class imports the tower model and do the needed transformations
	   to show it on the game screen.
	'''
	def __init__(self, position, color):
		#Loading the tower model
		self.tower = loader.loadModel("../arquivos de modelo/Tower")
		self.tower.reparentTo(gameModelsNode)
		#loading the ball that stays above the tower
		self.sphere = loader.loadModel("../arquivos de modelo/Sphere")
		self.sphere.reparentTo(gameModelsNode)
		#self.color is the color of the sphere
		self.color = color
		#Tinting the sphere
		self.sphere.setColor(*self.color)
		#Setting the texture to the tower
		self.texture = loader.loadTexture("../texturas/tower_Texture.png")
		self.tower.setTexture(self.texture, 1)
		#Setting the position of the tower and sphere
		self.position = Vec3(*position)
		self.tower.setPos(self.position)
		self.sphere.setPos(self.position)


class TerrainModel(DirectObject):
	'''This class imports the terrain model and do the needed transformations
	   to show it on the game screen.
	'''
	def __init__(self):
		#Loading the terrain model
		self.terrain = loader.loadModel("../arquivos de modelo/Terrain")
		self.terrain.reparentTo(gameModelsNode)
		#Setting the texture to the terrain
		self.texture = loader.loadTexture("../texturas/terrain_Texture.png")
		self.terrain.setTexture(self.texture, 1)
		#Setting the position of the terrain
		self.position = Vec3(1, 10, 0)
		self.terrain.setPos(self.position)
		#Scaling the terrain
		self.terrain.setSx(0.3)
		self.terrain.setSy(0.3)
        	terrainCollider = self.terrain.attachNewNode(CollisionNode('terrain_cnode'))
        	terrainCollider.node().addSolid(CollisionBox(*self.terrain.getTightBounds()))
		

class Ball(DirectObject):
	def __init__(self):
		self.ball = loader.loadModel("../arquivos de modelo/ball")
		self.ball.reparentTo(gameModelsNode)
		#Setting the position of the tower and sphere
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
		
	def fall(self):
		self.position[2]-=0.1
		self.ball.setPos(self.position)
