# resource_allocation.py

import numpy as np

POPULATION_SIZE = 100
MAX_GENERATIONS = 100
MUTATION_RATE = 0.1

def fitness_function(allocation):
    # Função de aptidão que calcula o lucro e o tempo de espera
    profit = 2 * allocation[0] + 3 * allocation[1]
    wait_time = allocation[0] + 2 * allocation[1]
    return profit, -wait_time  # Maximizar o lucro e minimizar o tempo de espera

def mutate(individual):
    for i in range(len(individual)):
        if np.random.rand() < MUTATION_RATE:
            individual[i] += np.random.randint(-1, 2)  # Pequenas alterações aleatórias
            individual[i] = max(0, individual[i])  # Garante que os valores sejam não negativos

def crossover(parent1, parent2):
    # Combina os genes dos pais para criar filhos usando um ponto de corte
    crossover_point = np.random.randint(1, len(parent1))
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2

def tournament_selection(population, fitness, tournament_size=5):
    # Seleciona os indivíduos para reprodução por meio de torneio
    selected_parents = []
    for _ in range(POPULATION_SIZE):
        indices = np.random.choice(len(population), size=tournament_size, replace=False)
        tournament = population[indices]
        tournament_fitness = fitness[indices]
        best_idx = np.argmax(tournament_fitness[:, 0])
        selected_parents.append(tournament[best_idx])
    return np.array(selected_parents)

def main():
    np.random.seed(42)

    # Inicialização da população
    population = np.random.randint(10, size=(POPULATION_SIZE, 2))  # Suponha que temos 2 atividades

    for generation in range(MAX_GENERATIONS):
        # Avaliar a aptidão de cada indivíduo na população
        fitness = np.array([fitness_function(allocation) for allocation in population])

        # Encontrar os índices dos indivíduos com as melhores aptidões (Pareto não dominado)
        best_indices = []
        for i in range(POPULATION_SIZE):
            if all(np.all(fitness[i] >= fitness[j]) for j in range(POPULATION_SIZE) if j != i):
                best_indices.append(i)

        best_solutions = population[best_indices]
        best_fitness = fitness[best_indices]

        print(f"Generation {generation + 1} - Best Fitness:")
        for solution, fitness in zip(best_solutions, best_fitness):
            print(f"  Allocation: {solution} | Profit: {fitness[0]} | Wait Time: {-fitness[1]}")

        # Seleção por torneio
        selected_parents = tournament_selection(population, fitness)

        # Recombinação e criação de novos indivíduos (filhos)
        children = []
        for i in range(0, POPULATION_SIZE, 2):
            child1, child2 = crossover(selected_parents[i], selected_parents[i+1])
            children.append(child1)
            children.append(child2)

        children = np.array(children)

        # Mutação dos filhos
        for child in children:
            mutate(child)

        # Substituir a população pela nova geração
        population = children

    print("\nMelhores soluções encontradas:")
    for solution, fitness in zip(best_solutions, best_fitness):
        print(f"  Allocation: {solution} | Profit: {fitness[0]} | Wait Time: {-fitness[1]}")

if __name__ == "__main__":
    main()
