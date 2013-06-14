"""Everything related to Troop is here"""
from random import randint

from pandaImports import *

class Troop:
    """This class defines all attributes and functions
	   of a troop
    """

    def __init__self(initTroopFunc = False, points=0, listOfParameters=[]):
        #Life of a troop
        self.life = 0
        self.lifeMin = 100
        self.lifeMax = 250
        self.listLife = [self.life, self.lifeMax, self.lifeMin]

        #Speed of a troop
        self.speed = 0
        self.speedMin = 10
        self.speedMax = 30
        self.listSpeed = [self.speed, self.speedMax, self.speedMin]

        #Resistence of a troop
        self.resistence = 0
        self.resistenceMin = 10
        self.resistenceMax = 25
        self.listResistence = [self.resistence, self.resistenceMax, self.resistenceMin]

        self.listAttributes = [self.listLife, self.listSpeed, self.listResistence]


        #Position of the troop
        self.position = [0,0,0]
        self.positionBefore = [0,0,0]
    
        self.initialPoints = 230
        
        #Graphical part------------------
        
        self.troopModel = None
        
        #----------------------------------

    def defineParameters(self, listParam):
        """Gets the values of listParam and puts them in this order
                [@lifeMin, @lifeMax, 
                @speedMin, @speedMax,
                @resistenceMin, @resistenceMax]
        """
        if len(listParam) != 6: print "Error with the parameters of listParam of the troop"; return
        self.lifeMin = listParam[0]
        self.lifeMax = listParam[1]
        self.speedMin = listParam[2]
        self.speedMax = listParam[3]
        self.resistenceMin = listParam[4]
        self.resistenceMax = listParam[5]

    def initTroop(self):
        """Initialize the troop with random values inside a interval, **based on tower's attributes**"""
        if (self.initialPoints >= \
            (self.lifeMin + self.speedMin + self.resistenceMin) \
            and self.initialPoints <= \
            (self.lifeMax + self.speedMax + self.resistenceMax)):  
          
            #Attributing the minimum values
            self.listLife[MIN] = self.lifeMin
            self.listSpeed[MIN] = self.speedMin
            self.listResistence[MIN] = self.resistenceMin

            
            #Attributing the maximum values
            self.listLife[MAX] = self.lifeMax
            self.listSpeed[MAX] = self.speedMax
            self.listResistence[MAX] = self.resistenceMax
            
            #Attributing random values
            startRandomAttributes(self.listAttributes, self.initialPoints)
        else:
            print "Error with the number of initial points of the tower" 
            
    def setInitialPoints(self, points):
        self.initialPoints = points
        
    def initModel(self, position, color):
        self.position = position
        troopModel = None
 



