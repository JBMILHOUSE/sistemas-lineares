from scipy.optimize import linprog

def solve_problem_3():
    # Coeficientes da função objetivo (convertendo maximização para minimização)
    c = [-15, -30, -11]  # Multiplicamos por -1 porque linprog faz minimização

    # Coeficientes das restrições de desigualdade
    A = [[-2, 1, 1]]  # 2x1 - x2 - x3 >= 0

    # Termos constantes das restrições de desigualdade
    b = [0]

    # Limites das variáveis (0 <= xj <= 1)
    x_bounds = [(0, 1), (0, 1), (0, 1)]

    # Resolvendo o problema de programação linear usando o método 'highs'
    result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')
    
    return result