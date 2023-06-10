from enum import Enum

from entidades.menu import Menu
from entidades.tabuleiro import Tabuleiro
from entidades.tabuleiro import TipoCampo

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

        self.alturaTabuleiro = self.menu.aguardaInteiro("", "Insira a altura do tabuleiro")
        self.larguraTabuleiro = self.menu.aguardaInteiro("", "Insira a largura do tabuleiro")

        self.tabuleiro = Tabuleiro(self.alturaTabuleiro, self.larguraTabuleiro, self.dificuldade.value)

    def selecionaDificuldade(self):
        self.menu.insereOpcoes([
            "Fácil",
            "Médio",
            "Difícil"
        ])

        dificuldades = [Dificuldade.FACIL, Dificuldade.MEDIO, Dificuldade.DIFICIL]
        opcao = self.menu.aguardaInteiro(None, "Insira a dificuldade")
        
        while(True):
            if (opcao <= 0 or opcao > len(dificuldades)):
                self.menu.exibirErro("Não existe opção para o valor inserido")
                opcao = self.menu.aguardaInteiro(None, "Insira a dificuldade")
            else:
                break
        self.menu.limpaCorpo()
        return dificuldades[opcao - 1]

    def mostraTabuleiro(self):
        self.menu.exibirMenu(self.tabuleiro.toString(), None)

    def solicitaCoordenada(self):
        linha = 0
        coluna = 0

        while(linha <= 0 or linha > self.tabuleiro.altura):
            linha = self.menu.aguardaInteiro(None, "Insira a linha")

            if (linha <= 0):
                self.menu.exibirErro("Insira um valor maior que 0")
            elif (linha > self.tabuleiro.altura):
                self.menu.exibirErro("Insira um valor menor que " + str(self.tabuleiro.altura))
            else:
                self.menu.retorno = "Linha: " + str(linha)

        while(coluna <= 0 or coluna > self.tabuleiro.largura):
            coluna = self.menu.aguardaInteiro(None, "Insira a coluna")

            if (coluna <= 0):
                self.menu.exibirErro("Insira um valor maior que 0")
            elif (coluna > self.tabuleiro.largura):
                self.menu.exibirErro("Insira um valor menor que " + str(self.tabuleiro.largura))
            else:
                self.menu.retorno = "Linha: " + str(linha) + " | Coluna: " + str(coluna)        

        return linha, coluna

    def solicitaConfirmacao(self):
        self.menu.aguardaConfirmacao()

    def insereCoordenada(self, linha: int, coluna: int):
        jogo.mostraTabuleiro()
        tipoCampo = self.tabuleiro.verificaCampo(linha, coluna)

        if (tipoCampo == TipoCampo.BOMBA):
            self.menu.exibirErro("Você perdeu!!")
            return False
        
        if (tipoCampo == TipoCampo.DICA):
            self.tabuleiro.abreCampo(linha, coluna)
            
        jogo.mostraTabuleiro()

        if jogo.tabuleiro.camposDescobertos == (jogo.tabuleiro.altura * jogo.tabuleiro.largura - len(jogo.tabuleiro.bombas)):
            jogo.menu.exibirMensagem("Você venceu!!!")
            jogo.solicitaConfirmacao()
            return False
        return True

tentarNovamente = True
while (tentarNovamente):
    jogo = Jogo()
    jogo.iniciaJogo()

    tentarNovamente = False
    emPartida = True

    while(emPartida):
        jogo.mostraTabuleiro()
        
        entradaInvalida = True
        while (entradaInvalida):
            linha, coluna = jogo.solicitaCoordenada()

            if jogo.tabuleiro.campo[linha - 1][coluna - 1] != "■":
                jogo.menu.exibirErro("Campo já descoberto! Insira outra coordenada")
            else:
                entradaInvalida = False

        emPartida = jogo.insereCoordenada(linha, coluna)

        if (emPartida):
            jogo.solicitaConfirmacao()
            jogo.menu.limpaMenu()
        else:
            jogo.menu.insereOpcoes(["Sim", "Não"])
            tentarNovamente = jogo.menu.aguardaInteiro(None, "Deseja continuar jogando?") == 1
            jogo.menu.limpaConsole()