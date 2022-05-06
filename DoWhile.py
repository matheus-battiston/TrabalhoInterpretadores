from Num import *
from Exp import *
from Skip import *
from Soma import *
from Bool import *
from Condicional import *
from Sequencial import *


class DoWhile(Exp):
    def __init__(self, a, c):
        self.comando = a
        self.cond = c

    def transicao(self, s):
        if not isinstance(self.cond, Skip):
            return Sequencial([self.comando, Condicional(self.cond, Sequencial([self]), Skip())])
        else:
            return Skip()

    def toString(self):
        return "Do " + self.comando.toString() + " While " + self.cond.toString()
