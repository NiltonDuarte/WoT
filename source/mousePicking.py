from pandac.PandaModules import CollisionHandlerEvent, CollisionNode, CollisionTraverser, CollisionRay


class MousePicking:
    def __init__(self):
        self.pickerNode=CollisionNode('mouseRay_cnode')
        self.pickerNP=base.camera.attachNewNode(self.pickerNode)
        self.pickerRay=CollisionRay()
        self.pickerNode.addSolid(self.pickerRay)
	self.mpos = None
        


    #** This is the function called each frame by a task defined below to syncronize the shooting ray position with the mouse moving pointer.
    def mouseRayUpdate(self,task):
      if base.mouseWatcherNode.hasMouse():
        self.mpos=base.mouseWatcherNode.getMouse()
        # this is what set our ray to shoot from the actual camera lenses off the 3d scene, passing by the mouse pointer position, making  magically hit in the 3d space what is pointed by it
        self.pickerRay.setFromLens(base.camNode, self.mpos.getX(),self.mpos.getY())
      return task.cont

    def mousePick(self,status):
      #if pickingEnabled:
        if status == 'down' and self.mpos != None:
          print "status down", self.mpos.getX(), self.mpos.getY()

        if status == 'up' and self.mpos != None:
            print "status up", self.mpos.getX(), self.mpos.getY()
