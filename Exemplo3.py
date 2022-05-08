from Any import *
from DoWhile import *
from Estado import *
from IfNoElse import *
from Interpretador import *
from Menor import *
from DoWhile import *
from Inc import *
from Subtracao import *

if __name__ == '__main__':
    exp = DoWhile(Inc(Var('x')), Menor(Var('x'), Subtracao(Var('y'), Num(5))))
    s = Estado()
    s.adicionar('y', 10)
    s.adicionar('x', 1)
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
