# maze_solver.py

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze

    def solve(self, start, end):
        visited = set()
        path = []
        self._dfs(start, end, visited, path)
        return path

    def _dfs(self, current, end, visited, path):
        if current == end:
            path.append(current)
            return True

        if current not in visited:
            visited.add(current)
            row, col = current
            if self.maze[row][col] == 1:
                return False

            neighbors = [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1)
            ]

            for neighbor in neighbors:
                if self._dfs(neighbor, end, visited, path):
                    path.append(current)
                    return True

        return False

# main(para o problema do labirinto)
maze = [
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0]
]

solver = MazeSolver(maze)
start = (0, 0)
end = (4, 4)
path = solver.solve(start, end)
print("Caminho mais curto:", path[::-1])  # Inverte o caminho para obter a ordem correta
