class Tabuleiro():
    def __init__(self, altura: int, largura: int):
        self.campo = []
        self.altura = altura
        self.largura = largura

        self.__montaTabuleiro()

    def __montaTabuleiro(self):
        for linha in range(self.altura):
            tabuleiroLinha = list()
            for coluna in range(self.largura):
                tabuleiroLinha.append("-")
            self.campo.append(tabuleiroLinha)

    def toString(self):
        # TODO: Tratar valores com 2 casas decimais
        tabuleiroString = "  "
        for coluna in range(self.largura):
            tabuleiroString += str(coluna + 1) + " "
        tabuleiroString += "\n"

        for linha in range(self.altura):
            colunas = " ".join(self.campo[linha])
            tabuleiroString += str(linha + 1) + " " + colunas + '\n'
        return tabuleiroString


