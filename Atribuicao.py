from Comando import *
from Num import *
from Skip import *


class Atribuicao(Comando):
    def __init__(self, variavel, expressao):
        self.variavel = variavel
        self.expressao = expressao

    def toString(self):
        return self.variavel.toString() + ' :=  ' + self.expressao.toString()

    def transicao(self, s):
        if isinstance(self.expressao, Num):
            s.atualizar(self.variavel.nome, self.expressao.valor)
            return Skip()
        else:
            exp = self.expressao.transicao(s)
            return Atribuicao(self.variavel, exp)
