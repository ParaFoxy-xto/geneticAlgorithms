import numpy as np
import random

# Dados do problema (coordenadas das cidades)
cities = {
    'A': (0, 0),
    'B': (1, 5),
    'C': (3, 1),
    'D': (4, 4),
    'E': (2, 3)
}

# Parâmetros do Algoritmo Genético
POPULATION_SIZE = 100
MAX_GENERATIONS = 1000
MUTATION_RATE = 0.1

def distance(city1, city2):
    # Distância euclidiana entre duas cidades
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def fitness_function(path):
    # Calcula o comprimento total do caminho
    total_distance = sum(distance(path[i], path[i+1]) for i in range(len(path) - 1))
    total_distance += distance(path[-1], path[0])  # Voltar ao ponto de partida
    return total_distance

def mutate(individual):
    for i in range(len(individual)):
        if np.random.rand() < MUTATION_RATE:
            j = random.randint(0, len(individual) - 1)
            individual[i], individual[j] = individual[j], individual[i]  # Swap de duas cidades

def main():
    np.random.seed(42)

    # Inicialização da população
    population = [list(cities.keys()) for _ in range(POPULATION_SIZE)]

    for generation in range(MAX_GENERATIONS):
        # Avaliar a aptidão de cada indivíduo na população
        fitness = np.array([fitness_function(path) for path in population])

        # Encontrar o índice do indivíduo com a melhor aptidão
        best_solution_idx = np.argmin(fitness)
        best_solution = population[best_solution_idx]

        print(f"Generation {generation + 1} - Best Fitness: {fitness[best_solution_idx]}")

        # Seleção dos pais para reprodução (usando método da roleta viciada)
        probabilities = 1 / fitness
        probabilities /= probabilities.sum()
        parents_indices = np.random.choice(len(population), size=POPULATION_SIZE - 2, p=probabilities, replace=True)
        parents = [population[idx] for idx in parents_indices]

        # Recombinação e criação de novos indivíduos (filhos)
        children = []
        for i in range(0, len(parents), 2):
            parent1, parent2 = parents[i], parents[i + 1]
            crossover_point = random.randint(1, len(parent1) - 2)
            child1 = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[:crossover_point]]
            child2 = parent2[:crossover_point] + [city for city in parent1 if city not in parent2[:crossover_point]]
            children.extend([child1, child2])

        # Mutação dos filhos
        for child in children:
            mutate(child)

        # Substituir os indivíduos menos aptos pelos filhos
        population[best_solution_idx] = best_solution
        population[parents_indices] = parents
        population[-2:] = children

    print("\nMelhor solução encontrada:")
    print(f"Caminho: {best_solution}")
    print(f"Distância total: {fitness_function(best_solution)}")

if __name__ == "__main__":
    main()
