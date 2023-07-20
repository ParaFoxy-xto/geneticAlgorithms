import numpy as np

POPULATION_SIZE = 100
GENE_SIZE = 2
MAX_GENERATIONS = 100
MUTATION_RATE = 0.1

# Função de Rosenbrock
def rosenbrock(x, y):
    a, b = 1, 100
    return (a - x)**2 + b * (y - x**2)**2

def mutate(individual):
    for i in range(len(individual)):
        if np.random.rand() < MUTATION_RATE:
            individual[i] += np.random.normal(0, 0.1)  # Pequenas perturbações aleatórias

def main():
    np.random.seed(42)

    population = np.random.uniform(-2, 2, size=(POPULATION_SIZE, GENE_SIZE)) # Inicialização aleatória da população

    for generation in range(MAX_GENERATIONS):
        # Avaliar a aptidão de cada indivíduo na população
        fitness = np.array([rosenbrock(x, y) for x, y in population])

        # Encontrar o índice do indivíduo com a melhor aptidão
        best_solution_idx = np.argmin(fitness)
        best_solution = population[best_solution_idx]

        print(f"Generation {generation + 1} - Best Fitness: {fitness[best_solution_idx]}")

        # Seleção dos pais para reprodução (apenas os 2 melhores indivíduos)
        parents = population[np.argsort(fitness)[:2]]

        # Recombinação e criação de novos indivíduos (filhos)
        child1 = (parents[0] + parents[1]) / 2
        child2 = (parents[0] + parents[1]) / 2

        # Mutação dos filhos
        mutate(child1)
        mutate(child2)

        # Substituir os 2 piores indivíduos pelos filhos
        worst_solution_idx = np.argmax(fitness)
        population[worst_solution_idx] = child1
        second_worst_solution_idx = np.argpartition(fitness, -2)[-2:]
        population[second_worst_solution_idx] = child2

    print("\nMelhor solução encontrada:")
    print(f"Coordenadas (x, y): {best_solution}")
    print(f"Fitness: {rosenbrock(*best_solution)}")

if __name__ == "__main__":
    main()
