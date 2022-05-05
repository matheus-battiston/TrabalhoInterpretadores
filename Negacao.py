from Bool import *
from Exp import *


class Negacao(Exp):
    def __init__(self, b):
        self.exp = b

    def toString(self):

        return str("!(" + self.exp.toString()) + ")"

    def transicao(self, s):
        if not isinstance(self.exp, Bool):
            return Negacao(self.exp.transicao(s))
        else:
            return Bool(not self.exp.valor)