from pandac.PandaModules import CollisionHandlerEvent, CollisionNode, CollisionTraverser, CollisionRay
from tower import *

class MousePicking:
	"""Class to handle mouse picking, receiving a collision object 
	   to add the mouse ray to the collision handler
	"""
	def __init__(self):
		self.pickerNode=CollisionNode('mouseRay_cnode')
		self.pickerNP=base.camera.attachNewNode(self.pickerNode)
		self.pickerRay=CollisionRay()
		self.pickerNode.addSolid(self.pickerRay)
		self.mpos = None
		self.pickingEnabled = True
		self.towerFollowMouse = False
		self.mousePickingOnTower = False
		self.mousePickingOnTroop = False
		self.collindingNode = None
        


	#** This is the function called each frame by a task defined below to syncronize the shooting ray position with the mouse moving pointer.
	def mouseRayUpdate(self,task):
		if base.mouseWatcherNode.hasMouse():
			self.mpos=base.mouseWatcherNode.getMouse()
			# this is what set our ray to shoot from the actual camera lenses off the 3d scene, passing by the mouse pointer position, making  magically hit in the 3d space what is pointed by it
			self.pickerRay.setFromLens(base.camNode, self.mpos.getX(),self.mpos.getY())
		return task.cont

	def mouseClicked(self,collisionObj, player):
		
		if self.mpos != None and self.towerFollowMouse == True:
			self.towerFollowMouse = False
			player.getTower(-1).towerModel.color =  [0.77,0,1, 0.5]
			player.getTower(-1).initTower()
			#player.getTower(-1).moveTower(collisionObj.collision3DPoint)
			#player.getTower(-1).initCollisionNode()
			#player.getTower(-1).towerInicialized = True
			print "mouseClicked", collisionObj.collision3DPoint
		elif self.mousePickingOnTower == True:
			print "mouseClicked on ", self.collindingNode.getParent(0).getChild(0)
		"""
		if status == 'up' and self.mpos != None:
			print "status up", collisionObj.collision3DPoint
		"""
