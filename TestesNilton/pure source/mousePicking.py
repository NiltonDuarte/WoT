from pandac.PandaModules import CollisionHandlerEvent, CollisionNode, CollisionTraverser, CollisionRay
from tower import *
import collision
import player
import tower
import troop


"""File to handle mouse picking, receiving a collision object 
to add the mouse ray to the collision handler
"""

pickerNode=CollisionNode('mouseRay_cnode')
pickerNP=base.camera.attachNewNode(pickerNode)
pickerRay=CollisionRay()
pickerNode.addSolid(pickerRay)
collision.addCollider(pickerNP)

#A struct like to solve reference pass problems
class MousePicking:	
	mpos = None
	pickingEnabled = True
	towerFollowMouse = False
	mousePickingOnTower = False
	mousePickingOnTroop = False
	collindingNode = None
	gameHUD = None
	lastClickedTower = None
	

        
def collideMouseEventAgainTerrain(entry):
	'''This function is called when the object (nodePath) is still colliding with another object 
	'''
	# here how we get the references of the two colliding objects to show their names ASA this happen
	np_from=entry.getFromNodePath()
	np_into=entry.getIntoNodePath()
	collision.collision3DPoint = [entry.getSurfacePoint(np_into).getX(), entry.getSurfacePoint(np_into).getY(), entry.getSurfacePoint(np_into).getZ()]
	if MousePicking.towerFollowMouse:
		player.Player.currPlayer.getTower(-1).moveTower(collision.collision3DPoint)

def collideMouseEventAgainTower(entry):
	'''This function will be called by the CollisionHandlerEvent object as soon as the object (nodePath) collides with another object
	'''
	MousePicking.mousePickingOnTroop = False
	MousePicking.mousePickingOnTower = True
	MousePicking.collindingNode = entry.getIntoNode()
	#print "TowerDict = ", tower.Tower.towerDict[np_into.getTag("TowerID")].name

	

def collideMouseEventOutTower(entry):
	'''This function is called when the object (nodePath) stops colliding with another object.
	'''
	MousePicking.mousePickingOnTower = False


def collideMouseEventAgainTroop(entry):
	MousePicking.mousePickingOnTower = False
	MousePicking.mousePickingOnTroop = True
	MousePicking.collindingNode = entry.getIntoNode()
	
def collideMouseEventOutTroop(entry):
	MousePicking.mousePickingOnTroop = False
	
#** This is the function called each frame by a task defined below to syncronize the shooting ray position with the mouse moving pointer.
def mouseRayUpdate(task):
	if base.mouseWatcherNode.hasMouse():
		MousePicking.mpos=base.mouseWatcherNode.getMouse()
		# this is what set our ray to shoot from the actual camera lenses off the 3d scene, passing by the mouse pointer position, making  magically hit in the 3d space what is pointed by it
		pickerRay.setFromLens(base.camNode, MousePicking.mpos.getX(),MousePicking.mpos.getY())
	return task.cont

def mouseClicked():
	
	#posicioning tower
	if MousePicking.mpos != None and MousePicking.towerFollowMouse == True:
		MousePicking.towerFollowMouse = False
		player.Player.currPlayer.getTower(-1).towerModel.resetColor()
		player.Player.currPlayer.getTower(-1).initTower()
		#print "mouseClicked - tower inicialized in ", collision.collision3DPoint
	
	#picking tower	
	elif MousePicking.mousePickingOnTower and MousePicking.gameHUD != None:
		#print "TowerTag = ",MousePicking.collindingNode.getTag("TowerID")
		if MousePicking.lastClickedTower != None:
			MousePicking.lastClickedTower.towerModel.resetColor()
		towerObj = tower.Tower.towerDict[MousePicking.collindingNode.getTag("TowerID")]
		MousePicking.lastClickedTower = towerObj
		MousePicking.gameHUD.updateArtImage(towerObj.artPath)
		MousePicking.gameHUD.updateTowerAttributeTexts(towerObj)
		towerObj.towerModel.towerSelectedColor()
		
		#print "mouseClicked on tower ", MousePicking.collindingNode.getTag("TowerID")
	
	#picking troop	
	elif MousePicking.mousePickingOnTroop and MousePicking.gameHUD != None:
		if MousePicking.lastClickedTower != None:
			MousePicking.lastClickedTower.towerModel.resetColor()
		troopObj = troop.Troop.troopDict[MousePicking.collindingNode.getTag("TroopID")]
		MousePicking.lastClickedTower = troopObj.sourceTower
		troopObj.sourceTower.towerModel.towerSelectedColor()
		MousePicking.gameHUD.updateArtImage(troopObj.artPath)
		MousePicking.gameHUD.updateTroopAttributeTexts(troopObj)
		#print "TroopTag = ",MousePicking.collindingNode.getTag("TroopID")		
		
	elif MousePicking.gameHUD != None:
		if MousePicking.lastClickedTower != None:
			MousePicking.lastClickedTower.towerModel.resetColor()		
		MousePicking.gameHUD.updateArtImage()
		MousePicking.gameHUD.resetAttributeTexts()
	
collision.addMouseClickEvent(mouseClicked)
collision.addCollisionEventAgain("mouseRay_cnode","terrain_cnode", collideMouseEventAgainTerrain)
collision.addCollisionEventAgain("mouseRay_cnode","TowerClass_cnode",collideMouseEventAgainTower)
collision.addCollisionEventOut("mouseRay_cnode","TowerClass_cnode",collideMouseEventOutTower)
collision.addCollisionEventAgain("mouseRay_cnode","TroopClass_cnode",collideMouseEventAgainTroop)
collision.addCollisionEventOut("mouseRay_cnode","TroopClass_cnode",collideMouseEventOutTroop)
