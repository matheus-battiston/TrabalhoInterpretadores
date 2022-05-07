from Bool import *
from Sequencial import *

class Condicional(Exp):
    def __init__(self, a, b, c):
        self.cond = a
        self.entao = b
        self.senao = c

    def transicao(self, s):
        if isinstance(self.cond, Bool):
            if self.cond.valor:
                return Sequencial([self.entao])
            else:
                return Sequencial([self.senao])
        else:
            return Condicional(self.cond.transicao(s), self.entao, self.senao)

    def toString(self):
        return "if " + self.cond.toString() + " than " + self.entao.toString() + "; else " + self.senao.toString()
