# Uniform cost search
def uniform_cost_search(graph, start, goal):
    frontier = [(0, start)]   # (cost, node)
    came_from = {}
    cost_so_far = {start: 0}
    
    while frontier:
        current_cost, current_node = heapq.heappop(frontier)
        
        if current_node == goal:
            break
            
        for neighbor, cost in graph[current_node]:
            new_cost = current_cost + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                heapq.heappush(frontier, (new_cost, neighbor))
                came_from[neighbor] = current_node
            
            
    # Reconstruct path

    path = []
    node = goal
    while node != start:
        path.append(node)
        node = came_from[node]
    path.append(start)
    path.reverse()
    return path, cost_so_far[goal]

#Example graph: adjacency list (node, cost): Bengaluru to kolkata distance:

graph = {
    "B": [("Hy", 700), ("Ch", 350), ("M", 1500)],
    "Hy": [("M", 700)],
    "Ch" : [("K", 1700)],
    "M" : [("K", 1800)]
}

start = "B"
end = "K"

path, cost = uniform_cost_search(graph, start, end)
print(f"The total distance to travel from {start} to {end} is {cost}km")
