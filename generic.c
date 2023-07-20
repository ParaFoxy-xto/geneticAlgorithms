#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define POPULATION_SIZE 100
#define MAX_GENERATIONS 1000
#define MUTATION_RATE 0.01

typedef struct {
    int genes[10]; // Supondo um problema com 10 genes (bits) em cada indivíduo
    int fitness;
} Individual;

int fitness_function(const Individual *individual) {
    int fitness = 0;
    for (int i = 0; i < 10; i++) {
        fitness += individual->genes[i];
    }
    return fitness;
}

void mutate(Individual *individual) {
    for (int i = 0; i < 10; i++) {
        if (rand() / (double)RAND_MAX < MUTATION_RATE) {
            individual->genes[i] = !individual->genes[i];
        }
    }
}

int main() {
    srand(time(NULL));

    Individual population[POPULATION_SIZE];
    for (int i = 0; i < POPULATION_SIZE; i++) {
        for (int j = 0; j < 10; j++) {
            population[i].genes[j] = rand() % 2;
        }
        population[i].fitness = fitness_function(&population[i]);
    }

    for (int generation = 0; generation < MAX_GENERATIONS; generation++) {
        // Seleção, recombinação e nova geração aqui (não incluído neste exemplo)
        // ...

        // Mutação
        for (int i = 0; i < POPULATION_SIZE; i++) {
            mutate(&population[i]);
            population[i].fitness = fitness_function(&population[i]);
        }
    }

    // Encontrar a melhor solução após as iterações
    Individual best_solution = population[0];
    for (int i = 1; i < POPULATION_SIZE; i++) {
        if (population[i].fitness > best_solution.fitness) {
            best_solution = population[i];
        }
    }

    printf("Melhor solução encontrada: ");
    for (int i = 0; i < 10; i++) {
        printf("%d ", best_solution.genes[i]);
    }
    printf("\nFitness: %d\n", best_solution.fitness);

    return 0;
}
