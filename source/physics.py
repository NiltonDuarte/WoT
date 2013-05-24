################################################################
#This file will have all classes related to the Physics of our game
################################################################
from pandac.PandaModules import *
from direct.showbase.DirectObject import DirectObject

class Physics:
	def __init__(self):
		#physicsNode is a child node of render that will be responsible for the basic physics calculations
		self.physicsNode = NodePath("PhysicsNode")
		self.physicsNode.reparentTo(render)
		#Enabling the physics engine
		base.enableParticles()
		self.setGravity()  #Now our world have gravitty
		
		
	def setGravity(self):
		'''This function sets the gravity force to our world
		'''
		self.gravityForceNode = ForceNode('gravity_Force')
	#	self.gravityForceNodePath = self.projectile.attachNewNode(self.gravityForceNode)
		#creating the gravity acceleration
		self.gravityForce = LinearVectorForce(0,0,-9.81) 
		#Now self.gravityForceNode will be transformed by the gravity
		self.gravityForceNode.addForce(self.gravityForce)
		base.physicsMgr.addLinearForce(self.gravityForce)
		
		
	def iniciarPhysicNodes(self, actorNodeName, model):
		'''This function sets the projectile to be a child of physicsNode and 
		   a child of physicsManager.
		'''
		#ActorNode is the component of the physics system that tracks interactions and applies them to the projectile model 
		actorNode = ActorNode(actorNodeName)
		#self.actorNodePath is now attached to the physicsNode
		actorNodePath = self.physicsNode.attachNewNode(actorNode)
		base.physicsMgr.attachPhysicalNode(actorNode)
		model.reparentTo(actorNodePath)
		return (actorNode, actorNodePath)
			
	def setForcaImpulso(self,actorNode,forcaImpulso):
		'''This function sets the direcional force to our projectile
		'''
		actorNode.getPhysicsObject().addImpulse(Vec3(*forcaImpulso))

	def setMassa(self, actorNode, massa):
		actorNode.getPhysicsObject().setMass(massa)
