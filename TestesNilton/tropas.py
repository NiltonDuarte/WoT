"""Arquivo da classe tropa"""
from random import randint

class Tropa:
    """Classe que define os atributos e funcoes de uma tropa"""

    def __init__(self):
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

        def definirParametros(self, lista):
            """Atribui os valores da lista nos respectivos parametros
                    [@vida, @velocidade, @resistencia]
            """
            if len(lista) != 3: print "Erro com tamanho da lista de parametros da tropa"; return
            self.vida = lista[0]
            self.velocidade = lista[1]
            self.resistencia = lista[2]

        def iniciarTropa(self):
            """Inicia a tropa com valores semi aleatorios, baseados em atributos da torre"""
