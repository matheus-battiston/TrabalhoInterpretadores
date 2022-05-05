from Exp import *


class Bool(Exp):
    def __init__(self, valor):
        self.valor = valor

    def get_valor(self):
        return self.valor

    def transicao(self, s):
        return self

    def toString(self):
        return str(self.valor)
