from scipy.optimize import linprog

def solve_problem_4():
    # Coeficientes da função objetivo
    c = [0, 0, 10, 10]

    # Coeficientes das restrições de desigualdade
    A = [
        [-1, 2, 0, 0],
        [0, -1, 2, 0],
        [0, 0, -1, 2]
    ]

    # Termos constantes das restrições de desigualdade
    b = [0, 0, 0]

    # Coeficientes das restrições de igualdade
    A_eq = [[1, 1, 1, 1]]

    # Termos constantes das restrições de igualdade
    b_eq = [400]

    # Limites das variáveis (x1, x2, x3, x4 >= 0)
    x_bounds = [(0, None), (0, None), (0, None), (0, None)]

    # Resolvendo o problema de programação linear
    result = linprog(c, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, bounds=x_bounds, method='highs')

    return result

def get_constraints_4():
    A_ub = [
        [-1, 2, 0, 0],
        [0, -1, 2, 0],
        [0, 0, -1, 2]
    ]
    b_ub = [0, 0, 0]
    return A_ub, b_ub, None, None