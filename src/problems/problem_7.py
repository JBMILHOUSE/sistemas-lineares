import numpy as np
from scipy.optimize import linprog

def solve_problem_7():
    # Coeficientes da função objetivo (negativos para maximização)
    c = [-9, -5]

    # Matriz de coeficientes das restrições
    A = []
    b = []

    # Adicionando as restrições para k = 1 a 13
    for k in range(1, 14):
       A.append([np.sin(k / 13.0), np.cos(k / 13.0)])
       b.append(7)

    # Adicionando restrições de não negatividade
    x_bounds = (0, None)
    bounds = [x_bounds, x_bounds]

    # Resolver o problema de programação linear
    result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

   #  x_star = result_problem_7.x
   #  f_x_star = -result_problem_7.fun

    return result