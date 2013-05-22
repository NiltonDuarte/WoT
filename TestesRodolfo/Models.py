#importing panda3D modules
import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject
#This will help move the objects
from direct.task.Task import Task
#Vec2 and Vec3 will help positioning the objects
from panda3d.core import Vec2,Vec3

from pandac.PandaModules import *


#gameModelsNode is a child node of render that will holds all models of the game
gameModelsNode = render.attachNewNode("Game Models Node")
gameModelsNode.setShaderAuto()
#physicsNode is a child node of render that will be responsible for the basic physics calculations
physicsNode = NodePath("PhysicsNode")
physicsNode.reparentTo(render)
#Enabling the physics engine
base.enableParticles()

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
		'''Applying normal mapping: needs lightning'''
		#self.textureStage = TextureStage('ts')
		#self.textureStage.setMode(TextureStage.MNormal)
		#self.tower.setTexture(self.textureStage, self.texture)
		self.tower.setTexture(self.texture, 1)
		#Setting the position of the tower and sphere
		self.position = Vec3(*position)
		self.tower.setPos(self.position)
		self.sphere.setPos(self.position)
		'''
		LIGHTNING SYSTEM
		self.dlight = DirectionalLight('dlight0')
		self.dlight.setColor(VBase4(1, 1, 1, 1))
		self.dlnp = render.attachNewNode(self.dlight)
		self.dlnp.setHpr(0, -5, 10)
		render.setLight(self.dlnp)
		'''


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
		
		
class Projectile(DirectObject):
	'''This class imports the projectile model
	   that is shot by the towers
	'''
	def __init__(self):
		#Loading the projectile model
		self.projectile = loader.loadModel("Exported_Models/Projectile")
		self.projectile.reparentTo(gameModelsNode)
		#Setting the position of the projectile
		self.position = Vec3(-15, 10,15)
		self.projectile.setPos(self.position)
		#Setting the physics of the projectile
		self.setPhysics()  #Now we can apply forces to the projectile
		self.setImpulseForce([10,0,13])
		
	def setPhysics(self):
		'''This function sets the projectile to be a child of physicsNode and 
		   a child of physicsManager.
		'''
		#ActorNode is the component of the physics system that tracks interactions and applies them to the projectile model 
		self.actorNode = ActorNode("projectile_Physics")
		#self.actorNodePath is now attached to the physicsNode
		self.actorNodePath = physicsNode.attachNewNode(self.actorNode)
		base.physicsMgr.attachPhysicalNode(self.actorNode)
		self.projectile.reparentTo(self.actorNodePath)
		#Setting the mass of our projectile
		self.actorNode.getPhysicsObject().setMass(100)   
		
		
	def setImpulseForce(self,impulseForces):
		'''This function sets the direcional force to our projectile
		'''
		self.actorNode.getPhysicsObject().addImpulse(Vec3(*impulseForces))
		
		
		
