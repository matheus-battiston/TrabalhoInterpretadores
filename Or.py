from Bool import *
from Num import *
from Exp import *


class Or(Exp):
    def __init__(self, e, d):
        self.expEsq = e
        self.expDir = d

    def toString(self):

        return str(self.expEsq.toString() + " & " + self.expDir.toString())

    def transicao(self, s):
        if not isinstance(self.expEsq, Bool):
            return Or(self.expEsq.transicao(s), self.expDir)
        elif not isinstance(self.expDir, Bool):
            return Or(self.expEsq, self.expDir.transicao(s))
        else:
            return Bool(self.expEsq.valor or self.expDir.valor)
