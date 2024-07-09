import heapq

def a_star(start, goal, graph, heuristic):
    # Initialize the open set with the start node, using a heap queue for efficient retrieval
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    # g stores the cost from the start node to each node
    g = {start: 0}
    # parents keeps track of the path
    parents = {start: None}
    
    while open_set:
        # Get the node in open_set with the lowest cost
        current_cost, current = heapq.heappop(open_set)
        
        # If we reached the goal, reconstruct the path
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            return path[::-1]  # Return reversed path
        
        # Explore the neighbors of the current node
        for neighbor, weight in graph[current]:
            tentative_g = g[current] + weight  # Calculate the cost to the neighbor
            
            # If this path to neighbor is better, update g and parent, and add to open_set
            if tentative_g < g.get(neighbor, float('inf')):
                g[neighbor] = tentative_g
                f = tentative_g + heuristic[neighbor]
                heapq.heappush(open_set, (f, neighbor))
                parents[neighbor] = current
    
    return None  # Return None if no path is found

# Graph representation as adjacency list
graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1), ('H', 7)],
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)],
    'J': []
}

# Heuristic values for each node (estimated cost to reach goal)
heuristic = {
    'A': 10, 'B': 8, 'C': 5, 'D': 7,
    'E': 3, 'F': 6, 'G': 5, 'H': 3,
    'I': 1, 'J': 0
}

# Call the A* algorithm with start and goal nodes
path = a_star('A', 'J', graph, heuristic)
print('Path found:', path)
