from enum import Enum

from entidades.menu import Menu
from entidades.tabuleiro import Tabuleiro

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
        self.tabuleiro = None

    def iniciaJogo(self):
        self.menu.titulo = "CAMPO MINADO"
        self.dificuldade = self.selecionaDificuldade()

        self.alturaTabuleiro = self.menu.aguardaInteiro("Insira a altura do tabuleiro")
        self.larguraTabuleiro = self.menu.aguardaInteiro("Insira a largura do tabuleiro")

        self.tabuleiro = Tabuleiro(self.alturaTabuleiro, self.larguraTabuleiro, self.dificuldade.value)

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

    def mostraTabuleiro(self):
        self.menu.exibirMensagem(self.tabuleiro.toString())

jogo = Jogo()
jogo.iniciaJogo()
'''
- Apresentar menu de escolha para cada nível
- Montar o tabuleiro
- Sortear as bombas
- Dispersar pelo tabuleiro
- Aumentar valor dos campos ao redor das bombas
- Apresentar em tela as bombas

'''