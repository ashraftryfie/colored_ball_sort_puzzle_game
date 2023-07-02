from game import Game
from state import States

if __name__ == '__main__':
    print('\n' + '-' * 19)
    print('| Ball Sort Puzzle |')
    print('-' * 19)

    g = Game()

    g.new_game()

    start_node = States(g.tubes, None, 0)

    g.display_tubes()
    # print(g.heuristic(start_node.tubes))

    print("Algorithms: ")
    print("1. BFS")
    print("2. DFS")
    print("3. UCS (Dijkstra)")
    print("4. Hill Climbing")
    print("5. A*")
    choice = int(input("choose algorithm, want to play game with: "))

    if choice == 1:
        g.bfs(start_node)
        if int(input("(1) to print path, (0) to exit:")):
            g.print_path()
    elif choice == 2:
        g.dfs(start_node)
    elif choice == 3:
        g.ucs(start_node)
        if int(input("(1) to print path, (0) to exit:")):
            g.print_path()
    elif choice == 4:
        g.hill_climbing(start_node)
        if int(input("(1) to print path, (0) to exit:")):
            g.print_path()
    elif choice == 5:
        g.a_star(start_node)
        if int(input("(1) to print path, (0) to exit:")):
            g.print_path()
    else:
        pass
