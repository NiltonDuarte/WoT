from pandaImports import *
from camera import *

#Creating AI World
AIworld = AIWorld(render)

def AIUpdate(task):
	AIworld.update()       
	return Task.cont
#Updating the World
taskMgr.add(AIUpdate,"AIUpdate")


class AI:
	def __init__(self):
		self.AIcharList = []
		self.AIBehaviorsList = []
		pass
		
	def addCharAI(self, charNP, name, param, pathFollowList):

		self.AIcharList.append(AICharacter(name,charNP, 10, 0.05, 5))
		AIworld.addAiChar(self.AIcharList[-1])
		self.AIBehaviorsList.append(self.AIcharList[-1].getAiBehaviors())

		self.AIBehaviorsList[-1].pathFollow(1)

		for pathPoint in reversed(pathFollowList):
			self.AIBehaviorsList[-1].addToPath(Vec3(pathPoint[0], pathPoint[1], 0))

		self.AIBehaviorsList[-1].startFollow()

Ai = AI()
