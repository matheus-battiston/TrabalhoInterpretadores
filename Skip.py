from Exp import *


class Skip(Exp):
    def transicao(self, s):
        return self

    def toString(self):
        return 'skip'
