
from pandac.PandaModules import CollisionHandlerEvent, CollisionNode, CollisionTraverser, CollisionRay

class CollisionWoT():
    def __init__(self):
        self.pickingEnabled = False
        base.cTrav=CollisionTraverser()
        self.collisionHandler = CollisionHandlerEvent()
	self.collisionHandler.addInPattern('%fn-into-%in')
	self.collisionHandler.addOutPattern('%fn-out-%in')
        
	
    def addCollider(self,nodePath):
	base.cTrav.addCollider(nodePath, self.collisionHandler)

    #** This function will be called by the CollisionHandlerEvent object as soon as the ray will collide with  (the FROM ray pierce INTO)
    def pickingCollideEventIn(self,entry):
      # here how we get the references of the two colliding objects to show their names ASA this happen
      np_from=entry.getFromNodePath()
      np_into=entry.getIntoNodePath()

      print "collideIN"

      # we need also to raise a flag to inform the mousePick routine that the picking is now active
      self.pickingEnabled=True

    #** This function will be called as the ray will leave (the FROM ray goes OUT)
    def pickingCollideEventOut(self,entry):
      # now we update the flag to inform mousePick routine that the picking is actually no more
      self.pickingEnabled=False

      np_into=entry.getIntoNodePath()
      print "collideOUT"
    


