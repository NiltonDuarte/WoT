#importing panda3D modules
import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject
#This will help move the objects
from direct.task.Task import Task
#Vec2 and Vec3 will help positioning the objects
from panda3d.core import Vec2,Vec3


#modelsNode is a child node of render that will holds all models of the game
gameModelsNode = render.attachNewNode("Game Models Node")

class TowerModel(DirectObject):
	'''This class imports the tower model and do the needed transformations
	   to show it on the game screen.
	'''
	def __init__(self, position, color):
		#Loading the tower model
		self.tower = loader.loadModel("Exported_Models/Tower")
		self.tower.reparentTo(gameModelsNode)
		#loading the ball that stays above the tower
		self.sphere = loader.loadModel("Exported_Models/Sphere")
		self.sphere.reparentTo(gameModelsNode)
		#self.color is the color of the sphere
		self.color = color
		#Tinting the sphere
		self.sphere.setColor(*self.color)
		#Setting the texture to the tower
		self.texture = loader.loadTexture("Textures/tower_Texture.png")
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
		self.terrain = loader.loadModel("Exported_Models/Terrain")
		self.terrain.reparentTo(gameModelsNode)
		#Setting the texture to the terrain
		self.texture = loader.loadTexture("Textures/terrain_Texture.png")
		self.terrain.setTexture(self.texture, 1)
		#Setting the position of the terrain
		self.position = Vec3(1, 10, 0)
		self.terrain.setPos(self.position)
		#Scaling the terrain
		self.terrain.setSx(0.3)
		self.terrain.setSy(0.3)
		
