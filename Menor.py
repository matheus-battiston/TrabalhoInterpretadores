from Num import *
from Bool import *


class Menor(Exp):
    def __init__(self, e, d):
        self.expEsq = e
        self.expDir = d

    def toString(self):

        return str(self.expEsq.toString() + " < " + self.expDir.toString())

    def transicao(self, s):
        if not isinstance(self.expEsq, Num):
            return Menor(self.expEsq.transicao(s), self.expDir)
        elif not isinstance(self.expDir, Num):
            return Menor(self.expEsq, self.expDir.transicao(s))
        else:
            return Bool(self.expEsq.valor < self.expDir.valor)
