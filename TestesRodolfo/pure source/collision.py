from pandac.PandaModules import CollisionHandlerEvent, CollisionNode, CollisionTraverser, CollisionRay
from pandaImports import DirectObject

class CollisionWoT(DirectObject):
	'''This class handles all the collision events 
	   of our game
	'''
	def __init__(self, mousePicking, player):
		#base.cTrav maintains a list of colliders of all solid objects in the world to check collisions (runs every frame)
		base.cTrav=CollisionTraverser()
		
		#self.collisionHandler specifies what to do when a collision event is detected
		self.collisionHandler = CollisionHandlerEvent()
		#"In" event: when there is a collision in the current frame, but it didn't in the previous frame 
		self.collisionHandler.addInPattern('%fn-into-%in')
		#"Again" event: when there is a collision in the current frame, the same that happened in the previous frame
		self.collisionHandler.addAgainPattern('%fn-again-%in')
		#"Out" event: when there isn't a collision in the current frame, but there was in the previous frame
		self.collisionHandler.addOutPattern('%fn-out-%in')
		
		#self.collision3DPoint is the point where the collision occurs
		self.collision3DPoint = [0,0,0]
		
		self.addCollider(mousePicking.pickerNP)
		
		#############################
		#** Let's manage now the collision events:

		self.accept('mouseRay_cnode-again-terrain_cnode', self.collideMouseEventAgainTerrain,[mousePicking,player])
		#DO.accept('mouseRay_cnode-into-ClasseTorre_Rangecnode', collisionObj.collideEventIn)
		self.accept('mouseRay_cnode-into-ClasseTorre_cnode', self.collideMouseEventInTower,[mousePicking])
		self.accept('mouseRay_cnode-out-ClasseTorre_cnode', self.collideMouseEventOutTower,[mousePicking])
		
		#** This is how we interact with mouse clicks
		self.accept('mouse1', mousePicking.mouseClicked, [self,player])
		#self.accept('mouse1', self.printmouse2)
		#DO.accept('mouse1-up', mousePicking.mousePickCreateTower, ['up',collisionObj, towers])
		#############################
		
	def printmouse2(self):
		print "mouse2"
		
	def addCollider(self,nodePath):
		'''Setting a object (nodePath) to the self.collisionHandler
		'''  
		base.cTrav.addCollider(nodePath, self.collisionHandler)
		

	def collideMouseEventAgainTerrain(self, mousePick, player, entry):
		'''This function is called when the object (nodePath) is still colliding with another object 
		'''
		# here how we get the references of the two colliding objects to show their names ASA this happen
		np_from=entry.getFromNodePath()
		np_into=entry.getIntoNodePath()
		self.collision3DPoint = [entry.getSurfacePoint(np_into).getX(), entry.getSurfacePoint(np_into).getY(), entry.getSurfacePoint(np_into).getZ()]
		if mousePick.towerFollowMouse:
			player.getTower(-1).moveTower(self.collision3DPoint)

	def collideMouseEventInTower(self, mousePicking, entry):
		'''This function will be called by the CollisionHandlerEvent object as soon as the object (nodePath) collides with another object
		'''
		# here how we get the references of the two colliding objects to show their names ASA this happen
		np_from=entry.getFromNodePath()
		np_into=entry.getIntoNodePath()
		self.collision3DPoint = [entry.getSurfacePoint(np_into).getX(), entry.getSurfacePoint(np_into).getY(), entry.getSurfacePoint(np_into).getZ()]
		mousePicking.mousePickingOnTower = True
		mousePicking.collindingNode = entry.getIntoNode()
		print np_from, "started colliding with", np_into, "Ponto = ",self.collision3DPoint
		
	
	def collideMouseEventOutTower(self, mousePicking, entry):
		'''This function is called when the object (nodePath) stops colliding with another object.
		'''
		#np_from is the object that collides
		np_from=entry.getFromNodePath()
		#np_into is the object that is being collided by np_from
		np_into=entry.getIntoNodePath()
		mousePicking.mousePickingOnTower = False
		print np_from, "stopped colliding with", np_into



