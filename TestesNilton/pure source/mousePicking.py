from pandac.PandaModules import CollisionHandlerEvent, CollisionNode, CollisionTraverser, CollisionRay
from tower import *
import collision
import player


"""File to handle mouse picking, receiving a collision object 
to add the mouse ray to the collision handler
"""

pickerNode=CollisionNode('mouseRay_cnode')
pickerNP=base.camera.attachNewNode(pickerNode)
pickerRay=CollisionRay()
pickerNode.addSolid(pickerRay)
mpos = None
pickingEnabled = True
towerFollowMouse = False
mousePickingOnTower = False
mousePickingOnTroop = False
collindingNode = None
collision.addCollider(pickerNP)
        


#** This is the function called each frame by a task defined below to syncronize the shooting ray position with the mouse moving pointer.
def mouseRayUpdate(task):
	if base.mouseWatcherNode.hasMouse():
		mpos=base.mouseWatcherNode.getMouse()
		# this is what set our ray to shoot from the actual camera lenses off the 3d scene, passing by the mouse pointer position, making  magically hit in the 3d space what is pointed by it
		pickerRay.setFromLens(base.camNode, mpos.getX(),mpos.getY())
	return task.cont

def mouseClicked():
	
	if mpos != None and towerFollowMouse == True:
		towerFollowMouse = False
		player.currPlayer.getTower(-1).towerModel.color =  [0.77,0,1, 0.5]
		player.currPlayer.getTower(-1).initTower()

		print "mouseClicked", collision.collision3DPoint
	elif mousePickingOnTower == True:
		print "mouseClicked on ", collindingNode.getParent(0).getChild(0)
	"""
	if status == 'up' and self.mpos != None:
		print "status up", collisionObj.collision3DPoint
	"""
