from pandaImports import *

class Sound(DirectObject):
	'''This class handles the songs and sound effects of the game
	'''
	def __init__(self, sound):
		#Loading the sound
		self.sound = base.loader.loadSfx(sound)  #returns type AudioSound

	def play(self):
		self.sound.play()
	
	def stop(self):
		self.sound.stop()
	
	def setVolume(self, volume):
		self.sound.setVolume(volume)
		
	def getSoundStatus(self):
		return self.sound.status()
		

