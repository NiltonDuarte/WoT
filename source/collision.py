
from pandac.PandaModules import CollisionHandlerEvent, CollisionNode, CollisionTraverser, CollisionRay

class CollisionWoT():
		def __init__(self):
			self.pickingEnabled = False
			base.cTrav=CollisionTraverser()
			self.collisionHandler = CollisionHandlerEvent()
			self.collisionHandler.addInPattern('%fn-into-%in')
			self.collisionHandler.addOutPattern('%fn-out-%in')
			self.collisionHandler.addAgainPattern('%fn-again-%in')
			self.collision3DPoint = [0,0,0]
			
	
		def addCollider(self,nodePath):
			base.cTrav.addCollider(nodePath, self.collisionHandler)
			

		#** This function will be called by the CollisionHandlerEvent object as soon as the ray will collide with  (the FROM ray pierce INTO)
		def collideEventIn(self,entry):
			# here how we get the references of the two colliding objects to show their names ASA this happen
			np_from=entry.getFromNodePath()
			np_into=entry.getIntoNodePath()
			self.collision3DPoint = [entry.getSurfacePoint(np_into).getX(), entry.getSurfacePoint(np_into).getY(), entry.getSurfacePoint(np_into).getZ()]
			print np_into, "collideIN", np_into, "Ponto = ",self.collision3DPoint
			
		#** This function will be called by the CollisionHandlerEvent object as the ray will collide again with  (the FROM ray pierce INTO)
		def collideEventAgain(self,entry):
			# here how we get the references of the two colliding objects to show their names ASA this happen
			np_from=entry.getFromNodePath()
			np_into=entry.getIntoNodePath()
			self.collision3DPoint = [entry.getSurfacePoint(np_into).getX(), entry.getSurfacePoint(np_into).getY(), entry.getSurfacePoint(np_into).getZ()]
			#print np_into, "collideAGAIN", np_into, "Ponto = ",self.collision3DPoint


		#** This function will be called as the ray will leave (the FROM ray goes OUT)
		def collideEventOut(self,entry):


			np_from=entry.getFromNodePath()
			np_into=entry.getIntoNodePath()
			print np_into, "collideOUT", np_into
    


