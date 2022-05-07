from Bool import *
from Exp import *
from Num import *


class Maior(Exp):
    def __init__(self, e, d):
        self.expEsq = e
        self.expDir = d

    def toString(self):

        return str(self.expEsq.toString() + " > " + self.expDir.toString())

    def transicao(self, s):
        if not isinstance(self.expEsq, Num):
            return Maior(self.expEsq.transicao(s), self.expDir)
        elif not isinstance(self.expDir, Num):
            return Maior(self.expEsq, self.expDir.transicao(s))
        else:
            return Bool(self.expEsq.valor > self.expDir.valor)