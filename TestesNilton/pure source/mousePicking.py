from pandac.PandaModules import CollisionHandlerEvent, CollisionNode, CollisionTraverser, CollisionRay
from tower import *
import collision
import player
import tower


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
        
def collideMouseEventAgainTerrain(entry):
	'''This function is called when the object (nodePath) is still colliding with another object 
	'''
	global towerFollowMouse
	# here how we get the references of the two colliding objects to show their names ASA this happen
	np_from=entry.getFromNodePath()
	np_into=entry.getIntoNodePath()
	collision.collision3DPoint = [entry.getSurfacePoint(np_into).getX(), entry.getSurfacePoint(np_into).getY(), entry.getSurfacePoint(np_into).getZ()]
	if towerFollowMouse:
		player.Player.currPlayer.getTower(-1).moveTower(collision.collision3DPoint)

def collideMouseEventInTower(entry):
	'''This function will be called by the CollisionHandlerEvent object as soon as the object (nodePath) collides with another object
	'''
	global mousePickingOnTower, collindingNode
	# here how we get the references of the two colliding objects to show their names ASA this happen
	np_from=entry.getFromNodePath()
	np_into=entry.getIntoNodePath()
	collision3DPoint = [entry.getSurfacePoint(np_into).getX(), entry.getSurfacePoint(np_into).getY(), entry.getSurfacePoint(np_into).getZ()]
	mousePickingOnTower = True
	collindingNode = entry.getIntoNode()
	print "TowerDict = ", tower.Tower.towerDict[np_into.getTag("TowerID")].name
	print np_from, "started colliding with", np_into
	

def collideMouseEventOutTower(entry):
	'''This function is called when the object (nodePath) stops colliding with another object.
	'''
	global mousePickingOnTower
	#np_from is the object that collides
	np_from=entry.getFromNodePath()
	#np_into is the object that is being collided by np_from
	np_into=entry.getIntoNodePath()
	mousePickingOnTower = False
	print np_from, "stopped colliding with", np_into

#** This is the function called each frame by a task defined below to syncronize the shooting ray position with the mouse moving pointer.
def mouseRayUpdate(task):
	if base.mouseWatcherNode.hasMouse():
		global mpos
		mpos=base.mouseWatcherNode.getMouse()
		# this is what set our ray to shoot from the actual camera lenses off the 3d scene, passing by the mouse pointer position, making  magically hit in the 3d space what is pointed by it
		pickerRay.setFromLens(base.camNode, mpos.getX(),mpos.getY())
	return task.cont

def mouseClicked():
	global towerFollowMouse
	if mpos != None and towerFollowMouse == True:
		towerFollowMouse = False
		player.Player.currPlayer.getTower(-1).towerModel.color =  [0.77,0,1, 0.5]
		player.Player.currPlayer.getTower(-1).initTower()

		print "mouseClicked", collision.collision3DPoint
	elif mousePickingOnTower == True:
		print "mouseClicked on ", collindingNode.getParent(0).getChild(0)

	
collision.addMouseClickEvent(mouseClicked)
collision.addCollisionEventAgain("mouseRay_cnode","terrain_cnode", collideMouseEventAgainTerrain)
collision.addCollisionEventInto("mouseRay_cnode","TowerClass_cnode",collideMouseEventInTower)
collision.addCollisionEventOut("mouseRay_cnode","TowerClass_cnode",collideMouseEventOutTower)
