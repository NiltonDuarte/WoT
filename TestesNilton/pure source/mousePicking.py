from pandac.PandaModules import CollisionHandlerEvent, CollisionNode, CollisionTraverser, CollisionRay


class MousePicking:
	"""Class to handle mouse picking, receiving a collision object 
	   to add the mouse ray to the collision handler
	"""
	def __init__(self, collisionObj):
		self.pickerNode=CollisionNode('mouseRay_cnode')
		self.pickerNP=base.camera.attachNewNode(self.pickerNode)
		self.pickerRay=CollisionRay()
		self.pickerNode.addSolid(self.pickerRay)
		collisionObj.addCollider(self.pickerNP)
		self.mpos = None
		self.pickingEnabled = True
		self.picked3DPoint = [0,0,0]
		self.towerFollowMouse = False
        


	#** This is the function called each frame by a task defined below to syncronize the shooting ray position with the mouse moving pointer.
	def mouseRayUpdate(self,task):
		if base.mouseWatcherNode.hasMouse():
			self.mpos=base.mouseWatcherNode.getMouse()
			# this is what set our ray to shoot from the actual camera lenses off the 3d scene, passing by the mouse pointer position, making  magically hit in the 3d space what is pointed by it
			self.pickerRay.setFromLens(base.camNode, self.mpos.getX(),self.mpos.getY())
		return task.cont

	def mousePickCreateTower(self,status,collisionObj, towerList):
		if self.pickingEnabled:
			if status == 'down' and self.mpos != None and self.towerFollowMouse == True:
				self.towerFollowMouse = False
				self.picked3DPoint = collisionObj.collision3DPoint
				towerList[-1].towerModel.color = [.0,1.0,.0, .5]
				towerList[-1].moveTower(self.picked3DPoint)
				print "status down", self.picked3DPoint 

			if status == 'up' and self.mpos != None:
				self.picked3DPoint = collisionObj.collision3DPoint
				print "status up", self.picked3DPoint
