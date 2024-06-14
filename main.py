from src.problems import solve_problem_1, solve_problem_2, solve_problem_4, solve_problem_7
# from problems.problem_4 import solve_problem_4 
# from problems.problem_7 import solve_problem_7
from src.results.plot_results import plot_results

def main():
    # Mapeando números de problemas para as funções de solução correspondentes
    problems_map = {
        1: solve_problem_1,
        2: solve_problem_2,
        4: solve_problem_4,
        7: solve_problem_7
    }

    # Solicitando a entrada de usuário para selecionar os problemas
    print('Selecione os problemas que deseja resolver (ex: 1, 4, 7): ')
    selected_problems = input()

    # Convertendo a entrada do usuário para uma lista de inteiros
    selected_problems = list(map(int, selected_problems.split(',')))

    # Lista para armazenar os resultados
    results = {}

    # Reoslvendo os problemas selecionados
    for problem in selected_problems:
        if problem in problems_map:
            result = problems_map[problem]()
            results[problem] = result
            print(f'Problema {problem} - Status: {result.message}')
            if result.success:
                print(f'Solução ótima: {result.x}')
                print(f'Valor da função obketivo na solução ótima: {result.fun}')
            else:
                print(f'Solução não encontrada')
        else:
            print(f'Problema {problem} não está definido.')

    # Plotando os resultados
    plot_results(results)

if __name__ == '__main__':
    main()

# result_1 = solve_problem_1()
# print(f'Problema 1 - Status: {result_1.message}')
# if result_1.success: 
#     print(f'Solução ótima: x* = {result_1.x[0]}, f(x) = {result_1.x[1]}')
#     print(f'Valor da função objetivo na solução ótima: {result_1.fun}')
# else:
#     print(f'Solução não encontrada')

# result_4 = solve_problem_4()
# print(f'Problema 4 - Status: {result_4.message}')
# if result_4.success: 
#     print(f'Solução ótima: x* = {result_4.x[0]}, f(x) = {result_4.x[1]}')
#     print(f'Valor da função objetivo na solução ótima: {result_4.fun}')
# else:
#     print(f'Solução não encontrada')

# result_7 = solve_problem_7()
# print(f'Problema 7 - Solução ótima: x* = {result_7[0][0]}, f(x) = {result_7[0][1]}')
# print(f'Valor da função objetivo na solução ótima: {result_7[1]}')
