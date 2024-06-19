from scipy.optimize import linprog

def solve_problem_5():
    # Coeficientes da função objetivo (convertendo maximização para minimização)
    c = [5, 0, -3]  # Multiplicamos por -1 porque linprog faz minimização

    A_ub = [ #A_ub = coeficientes das restrições de desigualdade
        
        [1, -1, 0],  # x1 - x2 <= -1
        [0, 1, -1],  # x2 - x3 <= -1
    ]
    b_ub = [-1, -1] #b_ub = são os valores das restrições de desigualdade

    A_eq = [ #A_eq = Coeficientes das restrições de igualdade
        
        [1, 1, 1]  # x1 + x2 + x3 = 12
    ]
    
    b_eq = [12] #b_eq = são os valores das restrições de igualdade

    # Limites das variáveis (xj >= 0)
    x_bounds = [(0, None), (0, None), (0, None)]

    # Resolvendo o problema de programação linear
    result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=x_bounds, method='highs')
    
    return result