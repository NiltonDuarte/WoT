from pandac.PandaModules import CollisionHandlerEvent, CollisionNode, CollisionTraverser, CollisionRay



class MousePicking:
    def __init__(self):
        self.pickerNode=CollisionNode('mouseRaycnode')
        self.pickerNP=base.camera.attachNewNode(self.pickerNode)
        self.pickerRay=CollisionRay()
        self.pickerNode.addSolid(self.pickerRay)
        
    #** This is the function called each frame by a task defined below to syncronize the shooting ray position with the mouse moving pointer.
    def mouseRayUpdate(self,task):
      if base.mouseWatcherNode.hasMouse():
        mpos=base.mouseWatcherNode.getMouse()
        # this is what set our ray to shoot from the actual camera lenses off the 3d scene, passing by the mouse pointer position, making  magically hit in the 3d space what is pointed by it
        self.pickerRay.setFromLens(base.camNode, mpos.getX(),mpos.getY())
      return task.cont


