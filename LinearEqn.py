from sympy import *
from sympy import symbols
from sympy.solvers import solve
from sympy import Function
from sympy.abc import a,b,d,x

#x, y = symbols('x y')


def solve_expression(expr, var="x"):
    expr = expr.replace(var, "1j")
    left, right = map(eval, expr.split("="))

    return (right.real - left.real) / (left.imag - right.imag)


eqn = input()

print(solve_expression(eqn))
