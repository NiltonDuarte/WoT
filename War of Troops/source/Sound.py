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
		
	def setLoop(self, isLoop):
		self.sound.setLoop(isLoop)

#Getting the sound effects 
clickButtonSound = Sound("../sounds/buttonClick.wav")
clickButtonSound.setVolume(0.5)
turnPass_Sound = Sound("../sounds/changeTurn.wav")
turnPass_Sound.setVolume(0.5)
error_Sound = Sound("../sounds/Error.wav")
error_Sound.setVolume(0.5)
		
#Getting the main theme 
mainThemeSong = Sound("../sounds/mainTheme.wav")
mainThemeSong.setVolume(0.1)
mainThemeSong.setLoop(True)
#Getting the credits song
creditsSong = Sound("../sounds/creditsTheme.wav")
creditsSong.setVolume(0.1)
creditsSong.setLoop(True)
