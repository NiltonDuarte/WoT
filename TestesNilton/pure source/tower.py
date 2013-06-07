"""Tower Class File"""

#importing other modules
from random import randint

#importing our modules
from commonFunctions import *
from projectile import *
from troops import *
from pandaImports import *
from pandac.PandaModules import CollisionSphere
from panda3d.core import PandaNode

class TowerModel(DirectObject, PandaNode):
	'''This class imports the tower model and do the needed transformations
	   to show it on the game screen.
	'''
	def __init__(self, position, color, towerClass):
		self.towerClass = towerClass
		#PandaNode.__init__(self, "TowerModel")
		#Loading the tower model
		self.tower = loader.loadModel("../arquivos de modelo/Tower")
		self.tower.reparentTo(render)
		#loading the ball that stays above the tower
		self.sphere = loader.loadModel("../arquivos de modelo/Sphere")
		self.sphere.reparentTo(render)
		#self.color is the color of the sphere and tinting the sphere
		self.color = color
		self.sphere.setColor(*self.color)
		#Setting the texture to the tower
		self.texture = loader.loadTexture("../texturas/tower_Texture.png")
		self.tower.setTexture(self.texture, 1)
		#Setting the position of the tower and sphere
		self.tower.setPos(Vec3(*position))
		self.sphere.setPos(Vec3(*position))
		
	def moveTowerModel(self,position):
		self.sphere.setColor(*self.color)
		self.tower.setPos(Vec3(*position))
		self.sphere.setPos(Vec3(*position))
		
	def setCollisionNode (self, collisionNodeName, rangeView):
		#self.tower.attachNewNode(self)
		#print "self.tower.getNode(0).getChild(1) = ",self.tower.getNode(0).getChild(1)
		#print "self = ", self
		self.towerCollider = self.tower.attachNewNode(CollisionNode(collisionNodeName + '_Rangecnode'))
		self.towerCollider.node().addSolid(CollisionSphere(0,0,0,rangeView))
		self.towerCollider = self.tower.attachNewNode(CollisionNode(collisionNodeName + '_cnode'))
		self.towerCollider.node().addSolid(CollisionBox(Point3(0,0,5.5),4,4,5.5))
	
	"""	
	def setCollisionNode (self, collisionNodeName, rangeView):
		self.towerCollider = self.tower.attachNewNode(Tower(collisionNodeName + '_Rangecnode'))
		self.towerCollider.node().addSolid(CollisionSphere(0,0,0,rangeView))
		self.towerCollider = self.tower.attachNewNode(Tower(collisionNodeName + '_cnode'))
		self.towerCollider.node().addSolid(CollisionBox(Point3(0,0,5.5),4,4,5.5))		
	"""
class Tower():
    """This class defines all attributes and functions
	   of a tower
    """

    
    def __init__(self, initTowerFunc = False, points=0, listOfParameters=[]):
		
        self.name = "ClasseTorre"
		#Shooting power of the tower
        self.shootPower = 0 #Nao usar esta variavel. Usar listShootPower[0]
        self.shootPowerMin = 10
        self.shootPowerMax = 40
        self.listShootPower = [self.shootPower, self.shootPowerMax, self.shootPowerMin]

        #Frequency of shooting
        self.txShoot = 0 #Nao usar esta variavel. Usar listTxShoot[0]
        self.txShootMin = 10
        self.txShootMax = 40
        self.listTxShoot = [self.txShoot, self.txShootMax, self.txShootMin]

        #Tower range of view
        self.rangeView = 20 #Nao usar esta variavel! Usar listRangeView[0]
        self.rangeViewMin = 10
        self.rangeViewMax = 40
        self.listRangeView = [self.rangeView, self.rangeViewMax, self.rangeViewMin]

        #Speed of troop crafting
        self.txTroops = 0 #Nao usar esta variavel! Usar listTxTroops[0]
        self.txTroopsMin = 10
        self.txTroopsMax = 30
        self.listTxTroops = [self.txTroops, self.txTroopsMax, self.txTroopsMin]

        self.listAttributes = [self.listShootPower, self.listTxShoot, self.listRangeView, self.listTxTroops]

        #Number of points that the tower will receive
        self.initialPoints = 300
        
        #Position of the tower
        self.position = [0,0,0]
        
        self.projectiles = [] #projeteis.append(Projetil())
        self.tropas = [] #tropas.append(Tropa())
        #Graphical part------------------
        
        self.towerModel = None
        self.towerInicialized = False
        
        #----------------------------------
        
        if (len(listOfParameters) > 0 and points and initTowerFunc):
            self.initialPoints = points
            self.defineParameters(listOfParameters)
            self.initTower()
            
    def initTower(self):
		"""Initialize the tower with random values inside a interval"""
		if (self.initialPoints >= \
            (self.shootPowerMin + self.txShootMin + self.rangeViewMin + self.txTroopsMin) \
            and self.initialPoints <= \
            (self.shootPowerMax + self.txShootMax + self.rangeViewMax + self.txTroopsMax)):            
            #Attributing the minimum values
			self.listShootPower[MIN] = self.shootPowerMin
			self.listTxShoot[MIN] = self.txShootMin
			self.listRangeView[MIN] = self.rangeViewMin
			self.listTxTroops[MIN] = self.txTroopsMin
            
            #Attributing the maximum values
			self.listShootPower[MAX] = self.shootPowerMax
			self.listTxShoot[MAX] = self.txShootMax
			self.listRangeView[MAX] = self.rangeViewMax
			self.listTxTroops[MAX] = self.txTroopsMax
            
            #Attributing random values
			startRandomAttributes(self.listAttributes, self.initialPoints)
		else:
			print "Error with the number of initial points of the tower"
			
			
    def defineParameters(self,listParam):
		"""Gets the values of listParam and puts them in this order
			[@shootPowerMin, @shootPowerMax, 
			 @txShootMin, @txShootMax,
			 @rangeViewMin, @rangeViewMax,
			 @txTroopsMin, @txTroopsMax]
		"""
		if len(listParam) != 8: print "Error with the parameters of listParam of the tower"; return
		self.shootPowerMin = listParam[0]
		self.shootPowerMax = listParam[1]
		self.txShootMin = listParam[2]
		self.txShootMax = listParam[3]
		self.rangeViewMin = listParam[4]
		self.rangeViewMax = listParam[5]
		self.txTroopsMin = listParam[6]
		self.txTroopsMax = listParam[7]


    def setInitialPoints(self, points):
        self.initialPoints = points
                
    def initModel(self, position, color):
        self.position = position
        self.towerModel = TowerModel(position,color,self)
        
    def moveTower(self,position):
		self.position = position
		self.towerModel.moveTowerModel(position)
    
    def setName(self,towerName):
		self.name = towerName
	
    def initCollisionNode(self):
		self.towerModel.setCollisionNode(self.name, self.listRangeView[0]);
		    
    def shootProjectile(self,position, impulseForce, physicsObj):
		self.projectiles.append(Projectile())
		self.projectiles[-1].position = position
		self.projectiles[-1].impulseForce = impulseForce
		self.projectiles[-1].initProjectile(physicsObj)



