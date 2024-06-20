import matplotlib.pyplot as plt
import numpy as np

def plot_results(results, constraints):
    fig, ax = plt.subplots()

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    markers = ['o', 's', 'D', '^', 'v', 'p', '*']

    for idx, (problem, result) in enumerate(results.items()):
        A_ub, b_ub, A_eq, b_eq = constraints[problem]

        x_vals = np.linspace(0, 10, 400)
        
        if A_ub is not None:
             for i in range(len(A_ub)):
                a1 = A_ub[i][0]
                if len(A_ub[i]) > 1:
                    a2 = A_ub[i][1]
                    if a2 != 0:
                        y_vals = (b_ub[i] - a1 * x_vals) / a2
                        ax.plot(x_vals, y_vals, label=f'Restrição {i+1} do Problema {problem}', color=colors[idx % len(colors)])
                else:
                    # Casos especiais para uma única variável
                    ax.axvline(x=b_ub[i] / a1, label=f'Restrição {i+1} do Problema {problem}', color=colors[idx % len(colors)])


        if A_eq is not None:
             for i in range(len(A_eq)):
                a1 = A_eq[i][0]
                if len(A_eq[i]) > 1:
                    a2 = A_eq[i][1]
                    if a2 != 0:
                        y_vals = (b_eq[i] - a1 * x_vals) / a2
                        ax.plot(x_vals, y_vals, label=f'Restrição de igualdade {i+1} do Problema {problem}', linestyle='--', color=colors[idx % len(colors)])
                else:
                    # Casos especiais para uma única variável
                    ax.axvline(x=b_eq[i] / a1, label=f'Restrição de igualdade {i+1} do Problema {problem}', linestyle='--', color=colors[idx % len(colors)])

        if len(result.x) > 1:
            ax.plot(result.x[0], result.x[1], markers[idx % len(markers)], label=f'Solução Ótima do Problema {problem}', markersize=10, color=colors[idx % len(colors)])
        else:
            # Caso especial para uma única variável
            ax.axvline(x=result.x[0], label=f'Solução Ótima do Problema {problem}', markersize=10, color=colors[idx % len(colors)])

    # ax.set_xlim((0, 10))
    # ax.set_ylim((0, 10)) 
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.legend()
    plt.title('Resultados dos Problemas')
    plt.grid(True)
    plt.show()