from pandac.PandaModules import CollisionHandlerEvent, CollisionNode, CollisionTraverser, CollisionRay
from pandaImports import DirectObject
from tower import *



'''This file handles all the collision events 
   of our game
'''
#base.cTrav maintains a list of colliders of all solid objects in the world to check collisions (runs every frame)
base.cTrav=CollisionTraverser()

#collisionHandler specifies what to do when a collision event is detected
collisionHandler = CollisionHandlerEvent()
#"In" event: when there is a collision in the current frame, but it didn't in the previous frame 
collisionHandler.addInPattern('%fn-into-%in')
#"Again" event: when there is a collision in the current frame, the same that happened in the previous frame
collisionHandler.addAgainPattern('%fn-again-%in')
#"Out" event: when there isn't a collision in the current frame, but there was in the previous frame
collisionHandler.addOutPattern('%fn-out-%in')

#self.collision3DPoint is the point where the collision occurs
collision3DPoint = [0,0,0]

#self.addCollider(mousePicking.pickerNP)
#self.addCollider(player.getTower(-1).troop.troopModel.troopColliderNP)


DO = DirectObject()

	
def addCollisionEventAgain(fromName, intoName, function, extraArgs = []):
	#Let's manage now the collision events:
	DO.accept(fromName+"-again-"+intoName, function, extraArgs)

def addCollisionEventInto(fromName, intoName, function, extraArgs = []):
	#Let's manage now the collision events:
	DO.accept(fromName+"-into-"+intoName, function, extraArgs)

def addCollisionEventOut(fromName, intoName, function, extraArgs = []):
	#Let's manage now the collision events:
	DO.accept(fromName+"-out-"+intoName, function, extraArgs)

def addMouseClickEvent(function, extraArgs = []):
	#** This is how we interact with mouse clicks
	DO.accept('mouse1', function, extraArgs)

	#self.accept('mouse1', self.printmouse2)
	#DO.accept('mouse1-up', mousePicking.mousePickCreateTower, ['up',collisionObj, towers])
	#############################

	
	
def addCollider(nodePath):
	base.cTrav.addCollider(nodePath, collisionHandler)
	








