"""Arquivo da classe tropa"""
from random import randint

class Tropa:
    """Classe que define os atributos e funcoes de uma tropa"""

    def __init__self, iniciarTorreFunc = False, pontos=0, lista=[]):
        #Vida da tropa
        self.vida = 0
        self.vidaMin = 100
        self.vidaMax = 250
        self.listaVida = [self.vida, self.vidaMax, self.vidaMin]

        #Velocidade da tropa
        self.velocidade = 0
        self.velocidadeMin = 10
        self.velocidadeMax = 30
        self.listaVelocidade = [self.velocidade, self.velocidadeMax, self.velocidadeMin]

        #Resistencia da tropa
        self.resistencia = 0
        self.resistenciaMin = 10
        self.resistenciaMax = 25
        self.listaResistencia = [self.resistencia, self.resistenciaMax, self.resistenciaMin]

        self.listaAtributos = [self.listaVida, self.listaVelocidade, self.listaResistencia]


        self.pontosIniciais = 230

    def definirParametros(self, lista):
        """Atribui os valores da lista nos respectivos parametros
                [@vidaMin, @vidaMax, 
                @velocidadeMin, @velocidadeMax,
                @resistenciaMin, @resistenciaMax]
        """
        if len(lista) != 6: print "Erro com tamanho da lista de parametros da tropa"; return
        self.vidaMin = lista[0]
        self.vidaMax = lista[1]
        self.velocidadeMin = lista[2]
        self.velocidadeMax = lista[3]
        self.resistenciaMin = lista[4]
        self.resistenciaMax = lista[5]

    def iniciarTropa(self):
        """Inicia a tropa com valores semi aleatorios, **baseados em atributos da torre**"""
        if (self.pontosIniciais >= \
            (self.vidaMin + self.velocidadeMin + self.resistenciaMin) \
            and self.pontosIniciais <= \
            (self.vidaMax + self.velocidadeMax + self.resistenciaMax)):  
          
            #Atribuindo valores minimos
            self.listaVida[MIN] = self.vidaMin
            self.listaVelocidade[MIN] = self.velocidadeMin
            self.listaResistencia[MIN] = self.resistenciaMin

            
            #Atribuindo valores maximos
            self.listaVida[MAX] = self.vidaMax
            self.listaVelocidade[MAX] = self.velocidadeMax
            self.listaResistencia[MAX] = self.resistenciaMax
            
            #Atribuindo pontos aleatorios
            iniciarAtributosAleatorios(self.listaAtributos, self.pontosIniciais)
        else:
            print "Erro com quantidade de pontos iniciais da torre" 
            
    def setPontosIniciais(self, pontos):
        self.pontosIniciais = pontos
 



