from Atribuicao import *
from Comando import *
from Estado import *
from Exp import *
from Interpretador import *
from Num import *
from Skip import *
from Soma import *
from Var import *
from Subtracao import *
from Multiplicacao import *

if __name__ == '__main__':
    exp = Multiplicacao(Num(1), Var('x'))
    s = Estado()
    s.adicionar('x', 1)
    exp = small_step(exp, s)
    print(exp.toString())
    print(s.toString())
    while not isinstance(exp, Num):
        print(exp.toString())
        print(s.toString())
        exp = small_step(exp, s)

    print("Final")
    print(exp.toString())
    print(s.toString())

