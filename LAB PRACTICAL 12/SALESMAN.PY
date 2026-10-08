from itertools import permutations

def tsp_simple(graph, start=0):
    n = len(graph)
    # Get all cities except the starting city
    other_cities = [i for i in range(n) if i != start]
    
    min_cost = float('inf')
    best_path = []

    # Try every possible order of visiting the remaining cities
    for perm in permutations(other_cities):
        current_cost = 0
        current_city = start
        
        # Add distance from city to city in this permutation
        for next_city in perm:
            current_cost += graph[current_city][next_city]
            current_city = next_city
            
        # Add distance to return back to the starting city
        current_cost += graph[current_city][start]
        
        # Update minimum cost and best path found so far
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = [start] + list(perm) + [start]
            
    return min_cost, best_path

# Example Distance Matrix (4 cities: 0, 1, 2, 3)
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cost, path = tsp_simple(graph)
print(f"Minimum Cost: {cost}")
print(f"Best Route:   {' -> '.join(map(str, path))}")

# ---------------------------------------------------------
# COMPLEXITY ANALYSIS (Brute-Force Approach):
#
# Time Complexity: O(N!) 
# - Fixing the start city leaves (N - 1)! permutations to check.
# - Calculating the cost of each permutation takes O(N) time.
# - Total Time: O((N - 1)! * N) = O(N!)
#
# Space Complexity: O(N)
# - Storing the list of cities and current permutation takes O(N) space.
# ---------------------------------------------------------