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
from Menor import *
from Maior import *
from Igual import *
from Or import *
from And import *
from Negacao import *
from Any import *
from Condicional import *
from While import *
from DoWhile import *

if __name__ == '__main__':
    exp = DoWhile(Atribuicao(Var('x'), Soma(Var('x'), Num(1))), Menor(Var('x'), Num(2)))
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

