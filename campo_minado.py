from enum import Enum
import random
import math

from entidades.menu import Menu

class Dificuldade(Enum):
    FACIL = 0.15
    MEDIO = 0.4
    DIFICIL = 0.6

class Jogo():
    def __init__(self):
        self.menu = Menu()
        self.dificuldade = 0
        self.alturaTabuleiro = 0
        self.larguraTabuleiro = 0
        self.tabuleiro = list()
        self.bombas = list()

        self.iniciaJogo()

    def iniciaJogo(self):
        self.menu.titulo = "CAMPO MINADO"
        self.dificuldade = self.selecionaDificuldade()

        self.alturaTabuleiro = self.menu.aguardaInteiro("Insira a altura do tabuleiro")
        self.larguraTabuleiro = self.menu.aguardaInteiro("Insira a largura do tabuleiro")

        self.sorteiaBombas()
        print(self.bombas)
        self.montaTabuleiro()
        for linha in self.tabuleiro:
            print(linha)

    def selecionaDificuldade(self):
        self.menu.insereOpcoes([
            "Fácil",
            "Médio",
            "Difícil"
        ])

        dificuldades = [Dificuldade.FACIL, Dificuldade.MEDIO, Dificuldade.DIFICIL]
        opcao = self.menu.aguardaInteiro("Insira a dificuldade")
        
        while(True):
            if (opcao <= 0 or opcao > len(dificuldades)):
                self.menu.exibirErro("Não existe opção para o valor inserido")
                opcao = self.menu.aguardaInteiro("Insira a dificuldade")
            else:
                break
        self.menu.limpaCorpo()
        return dificuldades[opcao - 1]

    def sorteiaBombas(self):
        quantidadeBombas = math.ceil((self.larguraTabuleiro * self.alturaTabuleiro) * self.dificuldade.value)
        bombasInseridas = 0

        while(bombasInseridas < quantidadeBombas):
            novaBomba = [random.randint(1, self.larguraTabuleiro), random.randint(1, self.alturaTabuleiro)]

            if (not self.__existeBomba(novaBomba)):
                self.bombas.append(novaBomba)
                bombasInseridas += 1

    def __existeBomba(self, novaBomba: list[int]):
        for bomba in self.bombas:
            if (bomba[0] == novaBomba[0] and bomba[1] == novaBomba[1]):
                return True
        return False        

    def montaTabuleiro(self):
        for linha in range(self.alturaTabuleiro):
            tabuleiroLinha = list()
            for coluna in range(self.larguraTabuleiro):
                for bomba in self.bombas:
                    if (bomba[0] == (coluna + 1) and bomba[1] == (linha + 1)):
                        tabuleiroLinha.append(" 0 ")
                        continue
                tabuleiroLinha.append(" - ")
            self.tabuleiro.append(tabuleiroLinha)

jogo = Jogo()
'''
- Apresentar menu de escolha para cada nível
- Montar o tabuleiro
- Sortear as bombas
- Dispersar pelo tabuleiro
- Aumentar valor dos campos ao redor das bombas
- Apresentar em tela as bombas

'''