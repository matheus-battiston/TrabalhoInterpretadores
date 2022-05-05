from Num import *
from Exp import *
from Skip import *
from Soma import *
from Bool import *


class Condicional(Exp):
    def __init__(self, a, b, c):
        self.cond = a
        self.entao = b
        self.senao = c

    def transicao(self, s):
        if isinstance(self.cond, Bool):
            if self.cond.valor:
                return self.entao.transicao(s)
            else:
                return self.senao.transicao(s)
        else:
            return Condicional(self.cond.transicao(s), self.entao, self.senao)

    def toString(self):
        return "if " + self.cond.toString() + " than ", self.entao.toString() + "; else " + self.senao.toString()
