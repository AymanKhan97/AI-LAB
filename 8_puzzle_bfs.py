from collections import deque


def is_goal(state, goal_state):
    return state == goal_state


def get_neighbors(state):
    neighbors = []
    index = state.index(0)  
    row, col = divmod(index, 3)

    
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for move in moves:
        new_row, new_col = row + move[0], col + move[1]

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append(tuple(new_state))
    return neighbors

def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()  


def bfs(start, goal):
    visited = set()
    queue = deque([(start, [])])

    while queue:
        current_state, path = queue.popleft()

        if current_state in visited:
            continue

        visited.add(current_state)

        if is_goal(current_state, goal):
            return path + [current_state]

        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                queue.append((neighbor, path + [current_state]))

    return None  


def input_puzzle(prompt):
    print(prompt)
    puzzle = []
    for i in range(3):
        row = input(f"Enter row {i+1} (3 numbers separated by spaces): ").split()
        puzzle.extend([int(x) for x in row])
    return tuple(puzzle)

start_state = input_puzzle("Enter the start state (use 0 for the blank space):")
goal_state = input_puzzle("Enter the goal state (use 0 for the blank space):")

bfs_solution = bfs(start_state, goal_state)

if bfs_solution:
    print("BFS Solution found! Steps:")
    for i, step in enumerate(bfs_solution):
        print(f"Step {i + 1}:")
        print_state(step)
else:
    print("No solution found using BFS.")