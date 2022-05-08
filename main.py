from Any import *
from DoWhile import *
from Estado import *
from IfNoElse import *
from Interpretador import *
from Menor import *
from Multiplicacao import *

if __name__ == '__main__':
    exp = Multiplicacao(Var('y'), Num(10))
    s = Estado()
    s.adicionar('y', 3)
    s.adicionar('x', 0)
    print(exp.toString())
    print(s.toString())
    exp = small_step(exp, s)
    while exp.toString() != 'skip' and not isinstance(exp, Num) and not isinstance(exp, Bool):
        print(exp.toString())
        print(s.toString())
        exp = small_step(exp, s)

    print("Final")
    print(exp.toString())
    print(s.toString())
