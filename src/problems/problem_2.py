from scipy.optimize import linprog

def solve_problem_2():
    # Coeficientes da função objetivo (negados para maximização)
    c = [-2, 3]

    # Coeficientes das restrições de desigualdade
    A = [
        [1, 2],  # coeficientes da primeira restrição
        [2, -1]  # coeficientes da segunda restrição
    ]

    # Termos constantes das restrições de desigualdade
    b = [6, 8]

    # Limites das variáveis (x1, x2 >= 0)
    x0_bounds = (0, None)
    x1_bounds = (0, None)

    # Resolvendo o problema de programação linear
    result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

    return result

def get_constraints_2():
    A_ub = [
        [1, 2],  # x1 + 2*x2 <= 6
        [2, -1]  # 2*x1 - x2 <= 8
    ]
    b_ub = [6, 8]  # Termos constantes das restrições de desigualdade

    return A_ub, b_ub, None, None