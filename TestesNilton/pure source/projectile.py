"""Everything related to Projectile is here"""
import uuid
from pandaImports import *
from pandac.PandaModules import CollisionSphere
import collision
import physics

class ProjectileModel(DirectObject):
	'''This class imports the projectile model
	   that is shot by the towers
	'''
	def __init__(self, position):
		#Loading the projectile model
		self.projectile = loader.loadModel("../arquivos de modelo/Projectile")
		self.projectile.reparentTo(render)		
		#Setting the texture to the projectile
		self.texture = loader.loadTexture("../texturas/projectile_Texture.png")
		self.projectile.setTexture(self.texture, 1)
		self.projectile.hprInterval(1,Point3(200,160,260)).loop()
		#Setting the position of the projectile 
		self.projectile.setPos(Vec3(*position))
		self.projectileNP = None
		
	def setCollisionNode (self, collisionNodeName, ID):
		self.projectileNP = self.projectile.attachNewNode(CollisionNode(collisionNodeName + '_cnode'))
		self.projectileNP.node().addSolid(CollisionSphere(Point3(0,0,0),2))
		self.projectileNP.setTag("ProjectileID", ID)
		#collision.addCollider(self.projectileNP)

class Projectile:
	"""This class defines all attributes and functions
	   of a projectile
    """
	projectileDict = {}
	def __init__(self):
		self.name = "ProjectileClass"
		self.ID = str(uuid.uuid4())
		Projectile.projectileDict[self.ID] = self
		#Mass of projectile
		self.mass = 100
		#self.massMin = 5
		#self.massMax = 40
		#self.listMass = [self.mass, self.massMax]
	
		#Spread ray of the projectile
		self.spreadRay = 0 
		#self.spreadRayMin = 5
		#self.spreadRayMax = 10
		#self.listSpreadRay = [self.spreadRay, self.spreadRayMax]
	
		#Damage percentage of the spread
		self.spreadPercentage = 0
		#self.spreadPercentageMin = 10
		#self.spreadPercentageMax = 40
		#self.listSpreadPercentage = [self.spreadPercentage, self.spreadPercentageMax]
	
		#Damage of duration of projectile
		self.dot = 0
		self.damageDuration = 100
	
		#Slow caused by projectile
		self.slow = 0
		self.slowDuration = 70
	
		#Chance of critical damage
		self.chanceCritical = 0

		#Position of projectile
		self.position = [0,0,0]
		self.positionBefore = [0,0,0]
        
		#Graphical part---------------------
        
		self.projectileModel = None
		#----------------------------------
		#Physics part----------------------
		
		self.impulseForce = [0,0,0]
        #ActorNode is the component of the physics system that tracks interactions and applies them to the projectile model 
		self.actorNode = None
 		#self.actorNodePath will be attached to the physicsNode
		self.actorNodePath = None 
		
		#----------------------------------
               
	def initProjectile(self):
		self.initModel(self.position)
		self.initPhysics()
		self.initCollisionNode()
	
	def defineParameters(self,listParam):
		"""Gets the values of listParam and puts them in this order
			[@mass, @spreadRay, @spreadPercentage,
			@dot, @damageDuration,
			@slow, @slowDuration,
			@chanceCritical]
		"""
		if len(listParam) != 8: print "Error with the parameters of listParam of the projectile"; return
		
		self.mass = listParam[0]
		self.spreadRay = listParam[1]
		self.spreadPercentage = listParam[2]
		self.dot = listParam[3]
		self.damageDuration = listParam[4]
		self.slow = listParam[5]
		self.slowDuration = listParam[6]
		self.chanceCritical = listParam[7]

	def initModel(self, position):
		self.position = position
		self.projectileModel = ProjectileModel(self.position)
        
	def initCollisionNode(self):
		self.projectileModel.setCollisionNode(self.name, self.ID);
	
	def initPhysics(self):
		self.actorNode, self.actorNodePath = physics.setPhysicNodes("Projectile_pnode", self.projectileModel.projectile)
		physics.setImpulseForce(self.actorNode,self.impulseForce)
		physics.setMass(self.actorNode,self.mass)



