"""Here we store functions that are going to be used by some objects"""

from random import randint
from math import *

VALUE = 0
MAX = 1
MIN = 2
NUM_IT = 100



def startRandomAttributes(attrList, points):
	'''This function distributes random values to the different attributes
	   of attrList of an object
	'''
        currentList = [x[:] for x in attrList]
        currentPoints = 2*points
        dist = abs(currentPoints - points)
	index_NUM_IT = 0
        for i in range(NUM_IT):
                currentPoints = 0
                for index in range(len(currentList)):
                        currentList[index][VALUE] = randint(currentList[index][MIN], currentList[index][MAX])
                        currentPoints += currentList[index][VALUE]
                current_dist = abs(currentPoints - points)
                if current_dist < dist:
                        for index in range(len(attrList)):
                                attrList[index][VALUE] = currentList[index][VALUE]
                        dist = current_dist
                        finalPoints = currentPoints
			if dist == 0: return
        #print attrList, finalPoints, index_NUM_IT
    
def vector3Sub(vector1, vector2):
	retVector = [0,0,0]
	retVector[0] = vector1[0] - vector2[0]
	retVector[1] = vector1[1] - vector2[1]
	retVector[2] = vector1[2] - vector2[2]
	return retVector
	
def vector2Module(vector1):
	retModule = 0
	retModule = (vector1[0]**2 + vector1[1]**2)**0.5
	return retModule

def vector3Module(vector):
	retModule = 0
	retModule = (vector[0]**2 + vector[1]**2 + vector[2]**2)**0.5
	return retModule
	
def thetaCalc(velocity, gravity, distanceModule, z):
	termSqrt = velocity**4 + gravity*((-gravity*(distanceModule**2)) + 2*z*(velocity**2))
	numerador = (velocity**2) - sqrt(termSqrt)
	denominador = -gravity*distanceModule
	thetaAngle = atan(numerador/denominador)
	return thetaAngle
	
