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
from Sequencial import *

if __name__ == '__main__':
    exp = Sequencial([Soma(Num(1), Var('x')), Soma(Num(1), Var('y'))])
    s = Estado()
    s.adicionar('y', 3)
    s.adicionar('x', 5)
    print(exp.toString())
    print(s.toString())
    exp = small_step(exp, s)
    while not isinstance(exp, Num) and not isinstance(exp, Skip):
        print(exp.toString())
        print(s.toString())
        exp = small_step(exp, s)

    print("Final")
    print(exp.toString())
    print(s.toString())

