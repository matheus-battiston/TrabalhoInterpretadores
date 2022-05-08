from Any import *
from DoWhile import *
from Estado import *
from IfNoElse import *
from Interpretador import *
from Menor import *
from And import *
from Maior import *
from Igual import *
from Multiplicacao import *
from Inc import *

if __name__ == '__main__':
    exp = IfNoElse(And(Maior(Var('x'), Num(3)), Igual(Var('y'), Num(0))), Sequencial([Atribuicao(Var('y'), Multiplicacao(Var('x'), Num(3))), Inc(Var('x'))]))
    s = Estado()
    s.adicionar('y', 0)
    s.adicionar('x', 4)
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
