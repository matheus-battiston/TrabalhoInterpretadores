from Atribuicao import *
from Soma import *
from Var import *

class Inc(Exp):
    def __init__(self, b):
        self.var = b

    def toString(self):
        return str("Inc (" + self.var.toString()) + ")"

    def transicao(self, s):
        if isinstance(self.var, Var):
            return Atribuicao(self.var, Soma(self.var, Num(1)))
