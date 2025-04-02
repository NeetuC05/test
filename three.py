# A* Search

from queue import PriorityQueue

def a_star(graph, start, goal, heuristics):
    open_set = PriorityQueue()
    open_set.put((0,start)) # cost,node
    came_from = {}
    g_score = {node: float("inf") for node in graph}
    g_score[start] = 0
    f_score = {node: float("inf") for node in graph}
    f_score[start] = heuristic[start]
    
    while not open_set.empty():
        _, current = open_set.get()
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1],f_score[goal]
        
        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current]+cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic[neighbor]
                open_set.put((f_score[neighbor], neighbor))
    return None, float("inf")

# example

graph = {
    "A":{"B":1,"C":2},
    "B":{"D":4,"E":2},
    "C":{"F":1,"G":3},
    "D":{},
    "E":{},
    "F":{},
    "G":{}
}

# Heuristic values
heuristic = {"A":6,"B":5,"C":4,"D":7,"E":3,"F":2,"G":0}

#Run A_star search

start ="A"
goal = "G"

path, cost = a_star(graph, start, goal, heuristic)
print(f"Path:{path},Cost:{cost}")


# Greedy Best First Search
import heapq

class Node:
    def __init__(self, position, h_value, parent=None):
        self.position=position
        self.h_value=h_value
        self.parent=parent
        
    def __lt__(self, other):
        return self.h_value < other.h_value
    
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def greedy_best_first_search(start, goal, gird):
    open_list=[]
    closed_list=set()
    
    start_node=Node(start, heuristic(start, goal))
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current_node=heapq.heappop(open_list)
        
        if current_node.position == goal:
            path=[]
            while current_node:
                path.append(current_node.position)
                current_node=current_node.parent
            return path[::-1]
        
        closed_list.add(current_node.position)
    
        for neighbor in get_neighbors(current_node.position, grid):
            if neighbor not in closed_list:
                neighbor_node=Node(neighbor, heuristic(neighbor, goal), current_node)
                heapq.heappush(open_list, neighbor_node)
    
    return None

def get_neighbors(position, grid):
    x, y = position
    neighbors=[]
    directions=[(-1,0),(1,0),(0,-1),(0,1)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny]!=1:
            neighbors.append((nx,ny))
            
    return neighbors

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start=(0, 0)
goal=(4, 4)

path=greedy_best_first_search(start, goal, grid)

if path:
    print("Path Found:", path)
else:
    print("No Path Found")
