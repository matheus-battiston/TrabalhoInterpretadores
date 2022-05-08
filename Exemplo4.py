from Any import *
from DoWhile import *
from Estado import *
from IfNoElse import *
from Interpretador import *
from Menor import *
from Or import *
from Igual import *
from Maior import *


if __name__ == '__main__':
    exp = Sequencial([IfNoElse(Or(Igual(Var('x'), Num(4)), Maior(Var('y'), Num(10))), Atribuicao(Var('y'), Num(5))), Any(Var('x'))])
    s = Estado()
    s.adicionar('y', 0)
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
