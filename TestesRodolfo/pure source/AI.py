
class AI:
	def __init__:
		self.AIworld = AIWorld(render)
		self.AIchar = AICharacter("ralph",self.ralph, 60, 0.05, 15)
		
	def setAI(self):
		#Creating AI World
		self.AIchar = AICharacter("ralph",self.ralph, 60, 0.05, 15)
		self.AIworld.addAiChar(self.AIchar)
		self.AIbehaviors = self.AIchar.getAiBehaviors()
        
		self.AIbehaviors.initPathFind("models/navmesh.csv")
        
		#AI World update        
		taskMgr.add(self.AIUpdate,"AIUpdate")
		
