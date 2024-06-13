import matplotlib.pyplot as plt

def plot_results(results):
    for problem, result in results.items():
        if result.success:
            plt.scatter(result.x[0], result.x[1], label=f'Problema {problem}')
    
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.legend()
    plt.title('Resultados dos Problemas')
    plt.show()

