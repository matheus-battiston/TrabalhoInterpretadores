from Exp import *
from Num import *

class Var(Exp):
    def __init__(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def transicao(self, s):
        return Num(s.ler(self.nome))

    def toString(self):
        return self.nome
