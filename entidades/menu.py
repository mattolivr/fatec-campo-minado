import os

class Menu:
    def __init__(self):
        self.titulo = None
        self.corpo = None
        self.retorno = None

    def exibirMenu(self):
        self.limpaConsole()
        
        if (self.titulo != None):
            titulo = ("=" * 6) + self.titulo + ("=" * 6)
            print(titulo)
        
        if (self.corpo != None):
            print(self.corpo)
            if (self.titulo != None):
                print("=" * len(titulo))
        
        if (self.retorno != None):
            print(self.retorno)

    def exibirErro(self, erro: str):
        self.retorno = erro

        self.exibirMensagem()
        self.aguardaConfirmacao()

        self.limpaRetorno()

    def exibirMensagem(self, mensagem: str):
        self.limpaConsole()
        
        if (self.titulo != None):
            titulo = ("=" * 6) + self.titulo + ("=" * 6)
            print(titulo)

        if (mensagem != None):
            print(mensagem)

    def aguardaDado(self, mensagem: str):
        self.exibirMenu()

        dado = input(mensagem + ": ")
        return dado

    def aguardaConfirmacao(self):
        print(os.linesep)
        input("Insira qualquer coisa para continuar: ")

    def aguardaInteiro(self, mensagem: str):
        dado = self.aguardaDado(mensagem)

        # Validar ESC
        while(not dado.isnumeric()):
            self.exibirErro("Entrada inválida. Por favor, insira um número inteiro: ")
            dado = input()

        return int(dado)

    def limpaConsole(self):
        windows = os.name == "Windows"

        if (windows):
            os.system("cls")
        else:
            os.system("clear")

    def limpaTitulo(self):
        self.titulo = None

    def limpaCorpo(self):
        self.corpo = None

    def limpaRetorno(self):
        self.retorno = None

    def limpaMenu(self):
        self.limpaCorpo()
        self.limpaRetorno()

    def insereOpcoes(self, opcoes: list[str]):
        if (opcoes != None):
            self.corpo = ""
            indice = 1

            for opcao in opcoes:
                separador = ""
                if (indice != len(opcoes)):
                    separador = os.linesep

                self.corpo += str(indice) + " - " + opcao + separador
                indice += 1