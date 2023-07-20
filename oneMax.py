import numpy as np

POPULATION_SIZE = 100
GENE_SIZE = 10
MAX_GENERATIONS = 100
MUTATION_RATE = 0.01

def fitness_function(individual):
    return np.sum(individual)

def mutate(individual):
    for i in range(len(individual)):
        if np.random.rand() < MUTATION_RATE:
            individual[i] = 1 - individual[i]

def crossover(parent1, parent2):
    crossover_point = np.random.randint(1, GENE_SIZE)  # Ponto de corte para a recombinação
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2

def tournament_selection(population, tournament_size):
    selected_parents = []
    for _ in range(2):  # Selecionar dois pais
        tournament_indices = np.random.choice(len(population), tournament_size, replace=False)
        tournament_fitness = [fitness_function(population[i]) for i in tournament_indices]
        selected_parents.append(population[tournament_indices[np.argmax(tournament_fitness)]])
    return selected_parents[0], selected_parents[1]

def main():
    np.random.seed(42)

    population = np.random.randint(2, size=(POPULATION_SIZE, GENE_SIZE))

    for generation in range(MAX_GENERATIONS):
        new_population = []

        # Criar a nova geração por meio de seleção, recombinação e mutação
        while len(new_population) < POPULATION_SIZE:
            parent1, parent2 = tournament_selection(population, tournament_size=5)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.append(child1)
            new_population.append(child2)

        population = np.array(new_population)

    # Encontrar a melhor solução após as iterações
    best_solution_idx = np.argmax([fitness_function(individual) for individual in population])
    best_solution = population[best_solution_idx]

    print("Melhor solução encontrada:", best_solution)
    print("Fitness:", fitness_function(best_solution))

if __name__ == "__main__":
    main()
