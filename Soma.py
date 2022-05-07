from Exp import *
from Num import *


class Soma(Exp):
    def __init__(self, e, d):
        self.expEsq = e
        self.expDir = d

    def toString(self):

        return str(self.expEsq.toString() + " + " + self.expDir.toString())

    def transicao(self, s):
        if not isinstance(self.expEsq, Num):
            return Soma(self.expEsq.transicao(s), self.expDir)
        elif not isinstance(self.expDir, Num):
            return Soma(self.expEsq, self.expDir.transicao(s))
        else:
            return Num(self.expEsq.valor + self.expDir.valor)
