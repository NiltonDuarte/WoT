"""Everything related to Projectile is here"""
import uuid
from pandaImports import *
from pandac.PandaModules import CollisionSphere
import collision
import physics
import xml.etree.ElementTree as ET


projectileModelDict = {}
#Getting configuration
typ = None
cfTree = ET.parse("projectile.xml")
cfRoot = cfTree.getroot()
for element in cfRoot.findall('projectile'):
	projectileType = element.get('type')
	modelTag = element.find('model')
	#Loading the projectile model
	projectileModel = loader.loadModel(modelTag.find('path').text)
	print "projectile ",projectileType  ," instanced"
	projectileModel.clearModelNodes()
	projectileModel.flattenStrong()
	
	#Setting the position of the projectile 
	projectileModel.setPos(0,0,0)
	
	#Animating the projectile
	projectileModel.hprInterval(1,Point3(200,160,260)).loop()
	
	#Setting the texture to the projectile
	modelTexture = loader.loadTexture(modelTag.find('texture').text)
	projectileModel.setTexture(modelTexture, 1)
	projectileModelDict[projectileType] = projectileModel


class ProjectileModel(DirectObject):
	'''This class imports the projectile model
	   that is shot by the towers
	'''
	def __init__(self, position, modelType):
		#Instancing the projectile model
		self.projectileInstance = render.attachNewNode("Projectile-Instance")
		projectileModelDict[modelType].instanceTo(self.projectileInstance)
		#Setting the position of the projectile 
		self.projectileInstance.setPos(Vec3(*position))
		self.projectileNP = None
		
	def setCollisionNode (self, collisionNodeName, ID):
		self.projectileNP = self.projectileInstance.attachNewNode(CollisionNode(collisionNodeName + '_cnode'))
		self.projectileNP.node().addSolid(CollisionSphere(Point3(0,0,0),2))
		self.projectileNP.setTag("ProjectileID", ID)

class Projectile:
	"""This class defines all attributes and functions
	   of a projectile
    """
	projectileDict = {}
	def __init__(self, projectileType):
		self.name = "ProjectileClass"
		self.ID = str(uuid.uuid4())
		Projectile.projectileDict[self.ID] = self

		#Getting configuration
		confFile = "projectile.xml"
		self.typ = None
		self.cfTree = ET.parse(confFile)
		self.cfRoot = self.cfTree.getroot()
		for element in self.cfRoot.findall('projectile'):
			if (element.get('type') == projectileType):
				self.typ = element
		if self.typ == None: print "Projectile Type do not exist"; return
		
		#Getting model configuration
		self.modelType = projectileType
		
		#Mass of projectile
		self.mass = float(self.typ.find('mass').text)
		#self.massMin = 5
		#self.massMax = 40
		#self.listMass = [self.mass, self.massMax]
	
		#Spread ray of the projectile
		self.spreadRay = float(self.typ.find('spreadRay').text) 
		#self.spreadRayMin = 5
		#self.spreadRayMax = 10
		#self.listSpreadRay = [self.spreadRay, self.spreadRayMax]
	
		#Damage percentage of the spread
		self.spreadPercentage = float(self.typ.find('spreadPercentage').text)
		#self.spreadPercentageMin = 10
		#self.spreadPercentageMax = 40
		#self.listSpreadPercentage = [self.spreadPercentage, self.spreadPercentageMax]
	
		#Damage of duration of projectile
		self.dot = float(self.typ.find('dot').text)
		self.damageDuration = float(self.typ.find('damageDuration').text)
	
		#Slow caused by projectile
		self.slow = float(self.typ.find('slow').text)
		self.slowDuration = float(self.typ.find('slowDuration').text)
	
		#Chance of critical damage
		self.chanceCritical = float(self.typ.find('chanceCritical').text)

		#Position of projectile
		self.position = [0,0,0]
		self.prevPosition = [0,0,0]
        
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
		#Game engine part------------------
		self.colliding = False
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
		self.projectileModel = ProjectileModel(self.position, self.modelType)
        
	def initCollisionNode(self):
		self.projectileModel.setCollisionNode(self.name, self.ID);
	
	def initPhysics(self):
		self.actorNode, self.actorNodePath = physics.setPhysicNodes("Projectile_pnode", self.projectileModel.projectileInstance)
		physics.setImpulseForce(self.actorNode,self.impulseForce)
		physics.setMass(self.actorNode,self.mass)
	
	def updatePosition(self, newPosition):
		self.prevPosition = self.position
		self.position = newPosition



