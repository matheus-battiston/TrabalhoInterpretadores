from Bool import *
from Sequencial import *


class IfNoElse(Exp):
    def __init__(self, a, b):
        self.cond = a
        self.entao = b

    def transicao(self, s):
        if isinstance(self.cond, Bool):
            if self.cond.valor:
                return Sequencial([self.entao])
            else:
                return Skip()
        else:
            return IfNoElse(self.cond.transicao(s), self.entao)

    def toString(self):
        return "if " + self.cond.toString() + " than " + self.entao.toString()
