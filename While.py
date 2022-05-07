from Condicional import *
from Sequencial import *


class While(Exp):
    def __init__(self, a, c):
        self.cond = a
        self.comando = c

    def transicao(self, s):
        if not isinstance(self.cond, Skip):
            return Condicional(self.cond, Sequencial([self.comando, self]), Skip())
        else:
            return Skip()

    def toString(self):
        return "while " + self.cond.toString() + " do ", self.comando.toString()
