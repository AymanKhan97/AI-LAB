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


def dfs(start, goal):
    visited = set()
    stack = [(start, [])]

    while stack:
        current_state, path = stack.pop()

        if current_state in visited:
            continue

        visited.add(current_state)

        if is_goal(current_state, goal):
            return path + [current_state]

        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                stack.append((neighbor, path + [current_state]))

    return None  


def input_puzzle(prompt):
    print(prompt)
    puzzle = []
    for i in range(3):
        row = input(f"Enter row {i+1} (3 numbers separated by spaces): ").split()
        puzzle.extend([int(x) for x in row])
    return tuple(puzzle)


def select_goal_state():
    print("Select a goal state:")
    print("1. Goal State:")
    print("   0 1 2")
    print("   3 4 5")
    print("   6 7 8")
    print("2. Goal State:")
    print("   1 2 3")
    print("   4 5 6")
    print("   7 8 0")
    choice = input("Enter 1 or 2: ")
    if choice == '1':
        return (0, 1, 2, 3, 4, 5, 6, 7, 8)
    else:
        return (1, 2, 3, 4, 5, 6, 7, 8, 0)


def solve_puzzle():
    start_state = input_puzzle("Enter the start state (use 0 for the blank space):")
    goal_state = select_goal_state()

    print("Choose the algorithm to solve the puzzle:")
    print("1. BFS (Breadth-First Search)")
    print("2. DFS (Depth-First Search)")
    algorithm_choice = input("Enter 1 or 2: ")

    if algorithm_choice == '1':
        print("\nSolving using BFS...")
        solution = bfs(start_state, goal_state)
    elif algorithm_choice == '2':
        print("\nSolving using DFS...")
        solution = dfs(start_state, goal_state)
    else:
        print("Invalid choice!")
        return

    if solution:
        print("Solution found! Steps:")
        for i, step in enumerate(solution):
            print(f"Step {i + 1}:")
            print_state(step)
    else:
        print("No solution found.")

solve_puzzle()
