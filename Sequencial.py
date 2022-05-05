from Num import *
from Exp import *
from Skip import *
from Soma import *


class Sequencial(Exp):
    def __init__(self, a):
        self.expEsq = a.pop(0)
        self.expDir = a


    def transicao(self, s):
        if isinstance(self.expEsq, Soma):
            self.expDir.insert(0, self.expEsq.transicao(s))
            return Sequencial(self.expDir)
        elif isinstance(self.expEsq, Num):
            self.expDir.insert(0, Skip())
            return Sequencial(self.expDir)
        elif isinstance(self.expEsq, Skip) and len(self.expDir) > 0:
            return Sequencial(self.expDir)
        else:
            return self.expEsq

    def toString(self):
        if isinstance(self.expEsq, Skip):
            string = self.expEsq.toString() + " ; "
            for x in self.expDir:
                string = string + x.toString()
            return string
        else:
            string = self.expEsq.toString()
            for x in self.expDir:
                string = string + " ; " + x.toString()
            return string
