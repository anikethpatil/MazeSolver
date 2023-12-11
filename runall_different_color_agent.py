from pymaze import maze, agent, textLabel
from astar import aStar
from bfs import BFS
from dfs import DFS

m = maze(20,20)
m.CreateMaze(loopPercent=60)

# A* 
path1 = aStar(m)
a = agent(m, footprints=True, color='blue')
steps_astar = len(path1) + 1
# BFS 
path2 = BFS(m)
b = agent(m, footprints=True, color='red')
steps_bfs = len(path2) + 1
# DFS
path3 = DFS(m)
c = agent(m, footprints=True, color='green')
steps_dfs = len(path3) + 1

m.tracePath({a: path1})
m.tracePath({b: path2})
m.tracePath({c: path3})

if steps_dfs <= steps_bfs and steps_dfs <= steps_astar:
        efficient_algorithm = "DFS"
        efficient_path = path1
elif steps_bfs <= steps_dfs and steps_bfs <= steps_astar:
        efficient_algorithm = "BFS"
        efficient_path = path2
else:
        efficient_algorithm = "A*"
        efficient_path = path3

l = textLabel(m, 'A*[blue agent] Path Length', len(path1))
l = textLabel(m, 'BFS[red agent] Path Length', len(path2))
l = textLabel(m, 'DFS[green agent] Path Length', len(path3))

m.run()
print(f"DFS steps: {steps_dfs}\nBFS steps: {steps_bfs}\nA* steps: {steps_astar}")
print(f"Most Efficient Algorithm: {efficient_algorithm}")