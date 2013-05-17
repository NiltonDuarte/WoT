
from pandac.PandaModules import CollisionHandlerEvent, CollisionNode, CollisionTraverser, CollisionRay

class CollisionWoT():
    def __init__(self):
        self.pickingEnabled = False
        base.cTrav=CollisionTraverser()
        self.collisionHandler = CollisionHandlerEvent()
        
        

    def pickingCollideEventIn(self,entry):
      # here how we get the references of the two colliding objects to show their names ASA this happen
      np_from=entry.getFromNodePath()
      np_into=entry.getIntoNodePath()

      np_into.getParent().setColor(.6, 0.5, 1.0, 1)

      # we need also to raise a flag to inform the mousePick routine that the picking is now active
      self.pickingEnabled=True

    def pickingCollideEventOut(self,entry):
      # now we update the flag to inform mousePick routine that the picking is actually no more
      self.pickingEnabled=False

      np_into=entry.getIntoNodePath()
      np_into.getParent().setColor(1.0, 1.0, 1.0, 1)
    

    def mousePick(self,status):
      if self.pickingEnabled:
        if status == 'down':
          print "status down"

        if status == 'up':
            print "status up"
