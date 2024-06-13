from scipy.optimize import linprog

def solve_problem_1():
    # Coeficientes da função objetivo
    c = [5, 1]

    # Coeficientes das restrições de desigualdade
    A = [
        [-2, -1],
        [-1, -1],
        [-1, -5]
    ]

    # Termos constantes das restrições de desigualdade
    b = [-6, -4, -10]

    # Limites das variáveis (x1, x2 >= 0)
    x0_bounds = (0, None)
    x1_bounds = (0, None)

    # Resolvendo o problema de programação linear
    result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

    return result