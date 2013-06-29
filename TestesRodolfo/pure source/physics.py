#####################################################################
#This file will have all classes related to the Physics of our game
#####################################################################
from pandac.PandaModules import *
from direct.showbase.DirectObject import DirectObject


#physicsNode is a child node of render that will be responsible for the basic physics calculations
physicsNode = NodePath("PhysicsNode")
physicsNode.reparentTo(render)
#Enabling the physics engine
base.enableParticles()

	
	
def setGravity():
	'''This function sets the gravity force to our world
	'''
	gravityForceNode = ForceNode('gravity_Force')
	#self.gravityForceNodePath = self.projectile.attachNewNode(self.gravityForceNode)
	#creating the gravity acceleration
	gravityForce = LinearVectorForce(0,0,-9.81) 
	#Now self.gravityForceNode will be transformed by the gravity
	gravityForceNode.addForce(gravityForce)
	base.physicsMgr.addLinearForce(gravityForce)

setGravity()  #Now our world have gravity	
	
def setPhysicNodes(actorNodeName, model):
	'''This function sets the projectile to be a child of physicsNode and 
	   a child of physicsManager.
	'''
	#ActorNode is the component of the physics system that tracks interactions and applies them to the model 
	actorNode = ActorNode(actorNodeName)
	#self.actorNodePath is now attached to the physicsNode
	actorNodePath = physicsNode.attachNewNode(actorNode)
	base.physicsMgr.attachPhysicalNode(actorNode)
	model.reparentTo(actorNodePath)
	return (actorNode, actorNodePath)
		
def setImpulseForce(actorNode,impulseForce):
	'''This function sets the direcional force to our projectile
	'''
	actorNode.getPhysicsObject().addImpulse(Vec3(*impulseForce))

def setMass(actorNode, mass):
	actorNode.getPhysicsObject().setMass(mass)
	

