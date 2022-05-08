from Num import *


class Multiplicacao(Exp):
    def __init__(self, e, d):
        self.expEsq = e
        self.expDir = d

    def toString(self):
        return str(self.expEsq.toString()) + " * " + str(self.expDir.toString())

    def transicao(self, s):
        if not isinstance(self.expEsq, Num):
            return Multiplicacao(self.expEsq.transicao(s), self.expDir)
        elif not isinstance(self.expDir, Num):
            return Multiplicacao(self.expEsq, self.expDir.transicao(s))
        else:
            return Num(self.expEsq.valor * self.expDir.valor)
