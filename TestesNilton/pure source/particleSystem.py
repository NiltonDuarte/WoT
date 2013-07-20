'''This file creates a ParticleSystem for any object we want'''
from pandaImports import *
from pandac.PandaModules import LVecBase3f

class ParticleSystem(DirectObject):
	def __init__(self, position, model):
		#Enabling particle effects
		self.ps = ParticleEffect()
		self.position = position
		self.model = model
		self.loadParticleConfig('fire.ptf')
	
	def loadParticleConfig(self, file):
		#Loading the file with the particle configurations
		self.ps.loadConfig(Filename(file))
		#Sets particles to birth where the troop is      
		self.ps.start(self.model)

	
	
