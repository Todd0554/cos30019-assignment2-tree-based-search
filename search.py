import sys
import math
import heapq
from collections import deque
from queue import PriorityQueue

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
        

        while path:
            current = path[-1]
            visited.add(current)

            if current in dest:
                find_path = True
                print(self.nodes[dest[0]], " ", len(path))
                print(", ".join(map(str, path)))
                path = [self.origin]
                visited = set()
                dest.remove(current)
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
        
        return   
        

        
    # breadth-first search 
    def BFS(self):
        # Initialize a queue with the origin node and its path
        queue = deque([(self.origin, [self.origin])])
        visited = set()

        while queue:
            # Dequeue the first element
            current, path = queue.popleft()

            # If the current node is a destination, print the path and return
            if current in self.destinations:
                print(" ".join(map(str, path)))
                return

            # Mark the current node as visited
            visited.add(current)

            # Add all unvisited neighbors to the queue
            for (from_node, to_node), cost in self.edges.items():
                if from_node == current and to_node not in visited:
                    queue.append((to_node, path + [to_node]))

        # If no path is found
        print("No path found")
        return
        
    def heuristic(self, node, goal):
        """Euclidean distance between node and goal."""
        (x1, y1) = self.nodes[node]
        (x2, y2) = self.nodes[goal]
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    # Greedy Best-First Search

    def GBFS(self):
        """Greedy Best-First Search using only the heuristic."""
        frontier = []
        # Use the minimum heuristic value among all destinations as the initial value.
        init_h = min(self.heuristic(self.origin, goal) for goal in self.destinations)
        heapq.heappush(frontier, (init_h, self.origin, [self.origin]))
        visited = set()
        while frontier:
            h_val, current, path = heapq.heappop(frontier)
            if current in visited:
                continue
            visited.add(current)
            if current in self.destinations:
                print(" ".join(map(str, path)))
                return
            # Expand neighbors.
            for (from_node, to_node), cost in self.edges.items():
                if from_node == current and to_node not in visited:
                    new_h = min(self.heuristic(to_node, goal) for goal in self.destinations)
                    heapq.heappush(frontier, (new_h, to_node, path + [to_node]))
        print("No path found")
        
        
        
    # A*
    def Astar(self):
        def euclidean_heuristic(node, goals, coordinates):
            x1, y1 = coordinates[node]
            return min(math.sqrt((x1 - coordinates[g][0])2 + (y1 - coordinates[g][1])2) for g in goals)

            # Build graph in form: node -> list of (neighbor, cost)
        graph = {}
        for (from_node, to_node), cost in self.edges.items():
            if from_node not in graph:
                graph[from_node] = []
            graph[from_node].append((to_node, cost))

        frontier = []
        heapq.heappush(frontier, (0, self.origin))

        came_from = {self.origin: None}
        cost_so_far = {self.origin: 0}
        nodesexpanded = 0

        while frontier:
            _, current = heapq.heappop(frontier)
            nodes_expanded += 1

            if current in self.destinations:
                # Reconstruct path
                path = []
                node = current
                while current is not None:
                    path.append(current)
                    current = came_from[current]
                path.reverse()

                # Print in required format
                print(f"{sys.argv[1]} AS")
                print(f"{node} {nodes_expanded}")
                print(" -> ".join(map(str, path)))
                return

            for neighbor, cost in graph.get(current, []):
                new_cost = cost_so_far[current] + cost
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + euclidean_heuristic(neighbor, self.destinations, self.nodes)
                    heapq.heappush(frontier, (priority, neighbor))
                    came_from[neighbor] = current

        # If no goal was reached
        print("No path found.")

        
        
    def CUS1(self):

        return
        
        
    def CUS2(self):
        
        return
        
    
    
    
       
        








                