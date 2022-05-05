from Bool import *
from Exp import *
from Var import *
import random
from Atribuicao import *


class Any(Exp):
    def __init__(self, b):
        self.var = b

    def toString(self):
        return str("Any (" + self.var.toString()) + ")"

    def transicao(self, s):
        if isinstance(self.var, Var):
            return Atribuicao(self.var, Num(random.randint(0,1000)))