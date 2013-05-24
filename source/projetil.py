"""Arquivo da classe projetil"""
from Models import ProjectileModel


class Projetil:
	"""Classe que define os atributos e funcoes de um projetil"""

	def __init__(self):
		#Massa do projetil
		self.massa = 100
		#self.massaMin = 5
		#self.massaMax = 40
		#self.listaMassa = [self.massa, self.massaMax]
	
		#Raio de espalho do projetil
		self.raioEspalho = 0 
		#self.raioEspalhoMin = 5
		#self.raioEspalhoMax = 10
		#self.listaRaioEspalho = [self.raioEspalho, self.raioEspalhoMax]
	
		#Porcentagem do dano que sera espalhada
		self.porcentagemEspalho = 0
		#self.porcentagemEspalhoMin = 10
		#self.porcentagemEspalhoMax = 40
		#self.listaPorcentagemEspalho = [self.porcentagemEspalho, self.porcentagemEspalhoMax]
	
		#Dano com o tempo do projetil
		self.dot = 0
		self.dotDuracao = 100
	
		#Lentidao causada pelo projetil
		self.lentidao = 0
		self.lentidaoDuracao = 70
	
		#Chance de critico
		self.chanceCritico = 0

		#Posicao do projetil
		self.posicao = [0,0,0]
		self.posicaoAnterior = [0,0,0]
        
		#Parte grafica---------------------
        
		self.projectileModel = None
		#----------------------------------
		#Parte fisica----------------------
		
		self.forcaImpulso = [0,0,0]
        #ActorNode is the component of the physics system that tracks interactions and applies them to the projectile model 
		self.actorNode = None
 		#self.actorNodePath will be attached to the physicsNode
		self.actorNodePath = None 
		

		#----------------------------------
               
	def iniciarProjetil(self,fisicaObj):
		self.iniciarModelo(self.posicao)
		self.actorNode, self.actorNodePath = fisicaObj.iniciarPhysicNodes("ProjetilTorre", self.projectileModel.projectile)
		fisicaObj.setForcaImpulso(self.actorNode,self.forcaImpulso)
		fisicaObj.setMassa(self.actorNode,self.massa)
	
	def definirParametros(self,lista):
		"""Atribui os valores da lista nos recpectivos parametros
			[@massa, @raioEspalho, @porcentagemEspalho,
			@dot, @dotDuracao,
			@lentidao, @lentidaoDuracao,
			@chanceCritico]
		"""
		if len(lista) != 8: print "Erro com tamanho da lista de parametros do projetil"; return
		
		self.massa = lista[0]
		self.raioEspalho = lista[1]
		self.porcentagemEspalho = lista[2]
		self.dot = lista[3]
		self.dotDuracao = lista[4]
		self.lentidao = lista[5]
		self.lentidaoDuracao = lista[6]
		self.chanceCritico = lista[7]

	def iniciarModelo(self, posicao):
		self.posicao = posicao
		self.projectileModel = ProjectileModel(posicao)
        




