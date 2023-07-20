# tic_tac_toe.py

import random

def check_winner(board):
    # Verifica se algum jogador venceu o jogo
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '-':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '-':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return board[0][2]

    return None

def evaluate_fitness(strategy):
    # Joga várias partidas com a estratégia e calcula a taxa de vitórias
    wins = 0
    for _ in range(100):
        board = [['-' for _ in range(3)] for _ in range(3)]
        current_player = 'X'
        for move in strategy:
            row, col = move
            board[row][col] = current_player
            winner = check_winner(board)
            if winner:
                if winner == 'X':
                    wins += 1
                break
            current_player = 'X' if current_player == 'O' else 'O'
    return wins

def crossover(parent1, parent2):
    # Combina os movimentos dos pais para criar um filho
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(strategy):
    # Realiza uma mutação em um movimento aleatório
    row, col = random.randint(0, 2), random.randint(0, 2)
    strategy[random.randint(0, len(strategy) - 1)] = (row, col)

def main():
    random.seed(42)

    # População inicial de estratégias aleatórias
    population = [[(random.randint(0, 2), random.randint(0, 2)) for _ in range(5)] for _ in range(100)]

    for generation in range(100):
        # Avalia a aptidão de cada estratégia
        fitness = [evaluate_fitness(strategy) for strategy in population]

        # Encontra o índice da estratégia com a melhor aptidão
        best_strategy_idx = fitness.index(max(fitness))
        best_strategy = population[best_strategy_idx]

        print(f"Generation {generation + 1} - Win Rate: {fitness[best_strategy_idx] / 100:.2f}")

        # Seleção dos pais para reprodução (usando método da roleta viciada)
        probabilities = [f / sum(fitness) for f in fitness]
        parents_indices = random.choices(range(100), weights=probabilities, k=98)
        parents = [population[idx] for idx in parents_indices]

        # Recombinação e criação de novos indivíduos (filhos)
        children = [crossover(parent1, parent2) for parent1, parent2 in zip(parents[::2], parents[1::2])]

        # Mutação dos filhos
        for child in children:
            mutate(child)

        # Substituir as estratégias menos aptas pelos filhos
        population[best_strategy_idx] = best_strategy
        for i, idx in enumerate(parents_indices):
            population[idx] = children[i]

    print("\nMelhor estratégia encontrada:")
    print(best_strategy)

if __name__ == "__main__":
    main()
