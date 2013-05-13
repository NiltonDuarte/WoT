#importing panda3D modules
import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject
#This will help move the objects
from direct.task.Task import Task
#Vec2 and Vec3 will help positioning the objects
from panda3d.core import Vec2,Vec3


#modelsNode is a child node of render that will holds all models of the game
gameModelsNode = render.attachNewNode("Game Models Node")

class Tower(DirectObject):
	def __init__(self):
		#Loading the tower model
		self.tower = loader.loadModel("Exported_Models/Tower")
		self.tower.reparentTo(gameModelsNode)
		#loading the ball that stays above the tower
		self.sphere = loader.loadModel("Exported_Models/Sphere")
		self.sphere.reparentTo(gameModelsNode)
		#Setting the texture to the tower
		self.texture = loader.loadTexture("Textures/tower_Texture.png")
		self.tower.setTexture(self.texture, 1)
		#Setting the position of the tower and sphere
		self.position = Vec3(1, 10, 0)
		self.tower.setPos(self.position)
		self.sphere.setPos(self.position)
		#Tinting the sphere
		self.sphere.setColor(0.5, 0.0, 0.5, 0.5)
