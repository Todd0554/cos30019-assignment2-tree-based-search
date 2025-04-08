import sys
import math
import heapq
from collections import deque

class Search:

    nodes = {}
    edges = {}
    origin = None
    destinations = []

    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.origin = None
        self.destinations = []
        
    def algoritm_selection(self, method):
        match method:
            case 'DFS':
                self.DFS()
            case 'BFS':
                self.BFS()
            case 'GBFS':
                self.GBFS()
            case 'A*':
                self.Astar()
            case 'CUS1': 
                self.CUS1()
            case 'CUS2':
                self.CUS2()
            case _:
                print("Invalid method selected.")
                
    # Depth-First-Search
    def DFS(self):
        
        # to record the path
        path = [self.origin]
        
        # a list to keep track of destinations, the destinations path is found, that destination will be removed from dest not from the destinations list
        dest = self.destinations
        
        # a set to keep track of visited nodes
        visited = set()
        
        # a boolean to check if a path is found
        find_path = False
        
        # a boolean to control the loop
        loop = True
        
        while loop:
            loop = False 
            while path:
                current = path[-1]
                visited.add(current)

                if current in dest:
                    find_path = True
                    print(f"{current} {len(path)}")
                    print(" ".join(map(str, path)))
                    path = [self.origin]
                    visited = set()
                    dest.remove(current)
                    loop = True 
                    break

                # find all neighbors of the current node
                candidate_neighbors = []
                for key in self.edges:
                    from_node, to_node = key
                    if from_node == current and to_node not in visited:
                        candidate_neighbors.append(to_node)

                candidate_neighbors = sorted(candidate_neighbors)

                # try the first neighbor found
                found_neighbor = False
                for neighbor in candidate_neighbors:
                    path.append(neighbor)
                    found_neighbor = True
                    break

                if not found_neighbor:
                    path.pop()
            
            # if all destinations are checked but no path is found
            if  not find_path:
                print("No path found")
                break
        return   
        

        
    # breadth-first search 
    def BFS(self):
        # to record the path
        path = [self.origin]
        
        # a list to keep track of destinations, the destinations path is found, that destination will be removed from dest not from the destinations list
        dest = self.destinations
        
        # a set to keep track of visited nodes
        visited = set()
        
        # a boolean to check if a path is found
        find_path = False
        
        # a boolean to control the loop
        loop = True
        
        while loop:
            loop = False 
            while path:
                current = path[-1]
                visited.add(current)
                # print(visited)
                # print(self.destinations)
                if current in dest:
                    find_path = True
                    print(f"{current} {len(path)}")
                    print(" ".join(map(str, path)))
                    path = [self.origin]
                    visited = set()
                    dest.remove(current)
                    loop = True 
                    break

                # find all neighbors of the current node
                candidate_neighbors = []
                for key in self.edges:
                    from_node, to_node = key
                    if from_node == current and to_node not in visited:
                        candidate_neighbors.append(to_node)

                candidate_neighbors = sorted(candidate_neighbors)

                # try the first neighbor found
                found_neighbor = False
                for neighbor in candidate_neighbors:
                    path.append(neighbor)
                    found_neighbor = True
                    break

                if not found_neighbor:
                    path.pop()
            
            # if all destinations are checked but no path is found
            if  not find_path:
                print("No path found")
                break
        return

    # Greedy Best-First Search

    def GBFS(self):
        def heuristic(self, node, goal):
            """Euclidean distance between node and goal."""
            (x1, y1) = self.nodes[node]
            (x2, y2) = self.nodes[goal]
            return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        
        remaining_dest = set(self.destinations)
        overall_explored = 0  # Global count across searches 
    
        # Continue until all destinations have been reached.
        while remaining_dest:
            # Initialize the frontier with a new search from the origin.
            frontier = []
            init_h = min(heuristic(self.origin, goal) for goal in remaining_dest)
            heapq.heappush(frontier, (init_h, self.origin, [self.origin]))
            visited = set()
            found = False
            
            while frontier:
                h_val, current, path = heapq.heappop(frontier)
                if current in visited:
                    continue
                visited.add(current)
                overall_explored += 1  # Count each expanded node
                
                if current in remaining_dest:
                    print(f"{current} {len(path)}")
                    print(" ".join(map(str, path)))
                    remaining_dest.remove(current)
                    found = True
                    break

                # Expand neighbors: collect them first to enforce tie-breaking
                neighbors = []
                for (from_node, to_node), cost in self.edges.items():
                    if from_node == current and to_node not in visited:
                        # Compute new heuristic value using remaining destinations.
                        new_h = min(heuristic(to_node, goal) for goal in remaining_dest)
                        neighbors.append((new_h, to_node, path + [to_node]))
                # Sort neighbors: primary by heuristic, then by node ID (ascending)
                neighbors.sort(key=lambda x: (x[0], x[1]))
                for item in neighbors:
                    heapq.heappush(frontier, item)
            
            if not found:
                # If no destination was reached in this run, then the remaining ones are unreachable.
                print("No path found.")
                break
        return

        
    # A*
    def Astar(self):
        
        return
        
        
    def CUS1(self):
        
        return
        
        
    def CUS2(self):
        
        return
        
    
    
    
       
        








                