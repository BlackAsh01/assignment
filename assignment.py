from sympy import *
import numpy as np

x, a, d, b = symbols('x a d b')
e = input("Equation: \n")

solvefor = input("Solve for what?")

if solvefor == 'x':
    eqn1 = Eq(a * x - d * x * x - d * x * b, 0)
    solution = solve(eqn1, x)
    print(solution)
    n = solution(x)
    print(n)
elif solvefor == 'a':
    eqn1 = Eq(a, d(x+b))
    solution = solve(eqn1, a)
    print(solution)
    n = solution(a)
    print(n)
elif solvefor == 'd':
    eqn1 = Eq(a/(x+b), d)
    solution = solve(eqn1, d)
    print(solution)
    n = solution(d)
    print(n)
elif solvefor == 'b':
    eqn1 = Eq(a/d - x, b)
    solution = solve(eqn1, b)
    print(solution)
    n = solution(b)
    print(n)
else:
    print("enter valid entry")
