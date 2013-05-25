"""Everything related to Projectile is here"""
from Models import ProjectileModel


class Projectile:
	"""This class defines all attributes and functions
	   of a projectile
    """

	def __init__(self):
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
               
	def initProjectile(self,physicsObj):
		self.initModel(self.position)
		self.actorNode, self.actorNodePath = physicsObj.setPhysicNodes("Projectile_FromTower", self.projectileModel.projectile)
		physicsObj.setImpulseForce(self.actorNode,self.impulseForce)
		physicsObj.setMass(self.actorNode,self.mass)
	
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
        




