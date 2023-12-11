from dfs import DFS
from bfs import BFS
from astar import aStar
from pymaze import maze, agent, textLabel

def run_test_case(maze_rows, maze_cols, loop_percent):
    m = maze(maze_rows, maze_cols)
    m.CreateMaze(loopPercent=loop_percent)

    
    path_dfs = DFS(m)
    steps_dfs = len(path_dfs) + 1

    
    path_bfs = BFS(m)
    steps_bfs = len(path_bfs) + 1

    
    path_astar = aStar(m)
    steps_astar = len(path_astar) + 1

    print(f"\nMaze {maze_rows}x{maze_cols} with {loop_percent}% loops:")
    print(f"DFS steps: {steps_dfs}, BFS steps: {steps_bfs}, A* steps: {steps_astar}")

    
    if steps_dfs <= steps_bfs and steps_dfs <= steps_astar:
        efficient_algorithm = "DFS"
        efficient_path = path_dfs
    elif steps_bfs <= steps_dfs and steps_bfs <= steps_astar:
        efficient_algorithm = "BFS"
        efficient_path = path_bfs
    else:
        efficient_algorithm = "A*"
        efficient_path = path_astar

    
    a = agent(m, footprints=True)
    m.tracePath({a: efficient_path})
    l = textLabel(m, 'Length of Shortest Path', len(efficient_path) + 1)
    m.run()

    return efficient_algorithm, steps_dfs, steps_bfs, steps_astar

if __name__ == '__main__':
    test_cases = [
        (15, 15, 60),
        
    ]

    for maze_rows, maze_cols, loop_percent in test_cases:
        efficient_algorithm, steps_dfs, steps_bfs, steps_astar = run_test_case(maze_rows, maze_cols, loop_percent)
        print(f"\nMost Efficient Algorithm: {efficient_algorithm}")
        
