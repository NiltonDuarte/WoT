from pandaImports import *
from panda3d.core import Point3

class TerrainModel(DirectObject):
	'''This class imports the terrain model and do the needed transformations
	   to show it on the game screen.
	'''
	def __init__(self):
		#Loading the terrain model
		self.terrain = loader.loadModel("../arquivos de modelo/Terrain1")
		self.terrain.reparentTo(render)
		#Setting the texture to the terrain
		self.texture = loader.loadTexture("../texturas/terrain_Texture.png")
		self.terrain.setTexture(self.texture, 1)
		#Setting the position of the terrain
		self.position = Vec3(0, 0, 0)
		self.terrain.setPos(self.position)
		#Scaling the terrain
		terrainBoundLower, terrainBoundUpper = self.terrain.getTightBounds()
		terrainBoundMiddleUpper, terrainBoundMiddleLower = list(terrainBoundUpper), list(terrainBoundLower)
		#terrainBoundUpper[0] = (terrainBoundUpper[0] + terrainBoundLower[0])/2
		terrainBoundMiddleUpper[0] = (terrainBoundUpper[0] + terrainBoundLower[0])/2
		terrainBoundMiddleLower[0] = (terrainBoundUpper[0] + terrainBoundLower[0])/2

		self.terrainColliderLeftNP = self.terrain.attachNewNode(CollisionNode('terrain_cnode'))
		self.terrainColliderLeftNP.node().addSolid(CollisionBox(terrainBoundLower, Point3(*terrainBoundMiddleUpper)))
		
		self.terrainColliderRightNP = self.terrain.attachNewNode(CollisionNode('terrain_cnode'))
		self.terrainColliderRightNP.node().addSolid(CollisionBox(Point3(*terrainBoundMiddleLower), terrainBoundUpper))
     
     def detachLeft()
		return
     
     def detachRight()   	

		

class Ball(DirectObject):
	def __init__(self):
		self.ball = loader.loadModel("../arquivos de modelo/ball")
		self.ball.reparentTo(render)
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
