from src.problems import solve_problem_1, solve_problem_2, solve_problem_3, solve_problem_4, solve_problem_5, solve_problem_7
from src.problems import get_constraints_1, get_constraints_2, get_constraints_3, get_constraints_4, get_constraints_5, get_constraints_7
from src.results import plot_results

def main():

    # Mapeando números de problemas para as funções de solução correspondentes
    problems_map = {
        1: solve_problem_1,
        2: solve_problem_2,
        3: solve_problem_3,
        4: solve_problem_4,
        5: solve_problem_5,
        7: solve_problem_7
    }

    constraints_map = {
        1: get_constraints_1,
        2: get_constraints_2,
        3: get_constraints_3,
        4: get_constraints_4,
        5: get_constraints_5,
        7: get_constraints_7
    }

    # Solicitando a entrada de usuário para selecionar os problemas
    print('Selecione os problemas que deseja resolver (ex: 1, 2, 3, 4, 5, 7): ')
    selected_problems = input()

    # Convertendo a entrada do usuário para uma lista de inteiros
    selected_problems = list(map(int, selected_problems.split(',')))

    # Lista para armazenar os resultados
    results = {}
    constraints = {}

    # Reoslvendo os problemas selecionados
    for problem in selected_problems:
        if problem in problems_map:
            result = problems_map[problem]()
            results[problem] = result
            constraints[problem] = constraints_map[problem]()
            print(f'Problema {problem} - Status: {result.message}')
            if result.success:
                print(f'Solução ótima: {result.x}')
                print(f'Valor da função objetivo na solução ótima: {result.fun}')
            else:
                print(f'Solução não encontrada')
        else:
            print(f'Problema {problem} não está definido.')

    # Plotando os resultados
    plot_results(results, constraints)

if __name__ == '__main__':
    main()
