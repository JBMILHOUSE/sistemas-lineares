import numpy as np
from scipy.optimize import linprog
import math

def solve_problem_7():
    # Coeficientes da função objetivo (negativos para maximização)
    c = [-9, -5]

    # Matriz de coeficientes das restrições
    A = []
    b = []

    # Adicionando as restrições para k = 1 a 13
    for k in range(1, 14):
       theta = [math.sin(k / 13), math.cos(k / 13)]
       A.append(theta)
       b.append(7)

    # Adicionando restrições de não negatividade
    bounds = [(0, None), (0, None)]

    # Resolver o problema de programação linear
    result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return result

def get_constraints_7():
    A_ub = []
    b_ub = []
    for k in range(1, 14):
        A_ub.append([np.sin(k / 13.0), np.cos(k / 13.0)])
        b_ub.append(7)
    return A_ub, b_ub, None, None