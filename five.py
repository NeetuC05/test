# hill climbing
import random

def hill_climbing(graph, start, goal):
    # Initialize the current city and the path taken
    current_city = start
    path = [current_city]
    total_distance = 0
    visited = set()  # Set to keep track of visited cities
    
    while current_city != goal:
        visited.add(current_city)  # Mark current city as visited
        
        # Get the neighbors of the current city with their distances
        neighbors = graph.get(current_city, [])
        
        # Find the neighbor with the shortest distance that hasn't been visited yet
        next_city = None
        min_distance = float('inf')
        
        for neighbor, distance in neighbors:
            if neighbor not in visited and distance < min_distance:
                next_city = neighbor
                min_distance = distance
        
        # If no next city is found, the goal is unreachable, break
        if next_city is None:
            print("No path found to the goal.")
            return None, None
        
        # Update the path and total distance
        path.append(next_city)
        total_distance += min_distance
        current_city = next_city
    
    return path, total_distance

# Graph with cities and distances (the given structure)
graph = {
    'Mh': [('G', 500), ('Mp', 700), ('Rj', 800)],
    'G': [('Mh', 500), ('Rj', 600)],
    'Mp': [('Mh', 700)],
    'Rj': [('Mh', 800), ('G', 600), ('D', 400)],
    'D': [('Rj', 400), ('Up', 200)],
    'Up': [('D', 200), ('J&K', 600)],
    'J&K': [('Up', 600), ('L', 300)],
    'L': [('J&K', 300)]
}

# Run the Hill Climbing algorithm
path, total_distance = hill_climbing(graph, 'Mh', 'L')

# Print the result
if path is not None:
    print(f"Shortest path from Maharashtra to Ladakh: {' -> '.join(path)}")
    print(f"Total distance: {total_distance} km")



#Beam Search algorithm
# define a simple function to optimize (maximize)
def objective_function(x):
    return -(x**2) + 10 * x   #a simple quadratic function

#beam search algorithm
def beam_search(start, objective_function, beam_width=3, iterations=10):
    open_list = [start]
    for _ in range(iterations):
        
        #generate neighbors by adjusting the current points
        neighbors = [x + 1 for x in open_list] + [x - 1 for x in open_list]
        
        #evaluate the neighbors based on the objective function
        scored_neighbors = [(neighbor, objective_function(neighbor)) for neighbor in neighbors]
        
        #sort by the objective function value and keep the top 'beam_width' nodes
        open_list = [x[0] for x in sorted(scored_neighbors, key=lambda x: x[1], reverse=True)[:beam_width]]
        
    return open_list[0]  #return the best node found

#example usage
start = 0  #starting position
best_position = beam_search(start, objective_function, beam_width=3)

print("Best position found:", best_position)
print("Objective value at this position:", objective_function(best_position))
