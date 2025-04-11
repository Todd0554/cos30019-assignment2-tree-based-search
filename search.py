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
            case 'Astar':
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
        
        # while the length of path is noy 0
        while path:
            # the current node we are at is the last node in the path[]
            currentNode = path[-1]
            # add the current node to the visited set
            visited.add(currentNode)

            # if the current node is in the dest now is [5, 4]
            if currentNode in dest:
                # set the find_path to True, which means we found a path to one of the destinations
                find_path = True
                # print the current node (destination node) and the length of the path
                print(f"{currentNode} {len(path)}")
                # print the path in the required format
                print(" ".join(map(str, path)))
                # the code below is for the next destination, but I found that we don't need to do this, DFS will stop when we find first destination
                # path = [self.origin]
                # visited = set()
                # dest.remove(currentNode)
                break

            # find all neighbors (the nodes the current node can reach) of the current node
            candidate_neighbors = []
            # key of edges is made from (node1, node2), node 1 is the from_node, node 2 is the next to_node
            for key in self.edges:
                # get the from_node and to_node
                from_node, to_node = key
                # if the current node(from_node) can reach the next node(to_node), append to_node to the candidate_neighbors list
                if from_node == currentNode and to_node not in visited:
                    candidate_neighbors.append(to_node)
            
            # try the first neighbor found
            # if the candidate_neighbors list is empty, 
            found_neighbor = False
            for neighbor in candidate_neighbors:
                path.append(neighbor)
                found_neighbor = True
                break

            # if the candidate_neighbors list is empty, delete the last node in the path[], then continue the loop to check other reachable nodes of the previous node(now is the lat node in path[])
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

    #   Greedy Best-First Search
    def GBFS(self):
        def heuristic(node, goal):
            """Euclidean distance between node and goal."""
            (x1, y1) = self.nodes[node]
            (x2, y2) = self.nodes[goal]
            return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        """Greedy Best-First Search using only the heuristic."""
        frontier = []
        init_h = min(heuristic(self.origin, goal) for goal in self.destinations)
        heapq.heappush(frontier, (init_h, self.origin, [self.origin]))
        visited = set()

        while frontier:
            h_val, current, path = heapq.heappop(frontier)
            if current in visited:
                continue
            visited.add(current)

            if current in self.destinations:
                print(f"{current} {len(path)}")
                print(" ".join(map(str, path)))
                return

            for (from_node, to_node), cost in self.edges.items():
                if from_node == current and to_node not in visited:
                    new_h = min(heuristic(to_node, goal) for goal in self.destinations)
                    heapq.heappush(frontier, (new_h, to_node, path + [to_node]))

        print("No path found")
        return
        
   # A*
    def Astar(self):
        
        def euclidean_heuristic(node, goals, coordinates):
            x1, y1 = coordinates[node]
            return min(math.sqrt((x1 - coordinates[g][0])**2 + (y1 - coordinates[g][1])**2) for g in goals)

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

        while frontier:
            _, current = heapq.heappop(frontier)

            if current in self.destinations:
                # Reconstruct path
                path = []
                node = current
                while current is not None:
                    path.append(current)
                    current = came_from[current]
                path.reverse()

                # Print in required format
                print(f"{node} {len(path)}")
                print(" ".join(map(str, path)))
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
  
    # Dijkstra
    def CUS1(self):
        start = self.origin
        dest = set(self.destinations)
        # from origin to each node, the lowest cost of each node, the cost can be updated in the loop 
        # the data structure is like (node: cost)
        min_cost = {start: 0}
        
        # (to node, from_node) pairs
        came_from = {}
        
        # (0, start) means (cost, node), it will append more cost and node pairs
        frontier = [(0, start)]
        
        visited = set()

        while frontier:
            # for checking the min cost dictionary
            # print("######", min_cost, "######")
            
            # get the node we are at now in current
            cost, currentNode = frontier.pop(0)
            # if the node we loop now is already visited, we use continue to skip to next
            if currentNode in visited:
                continue
            # if the node we loop now is not visited, we add it to the visited set
            visited.add(currentNode)

            # if the current node is a goal, we record the path
            if currentNode in dest:
                # set the path array
                path = []
                while currentNode is not None:
                    # add the current node to the path[]
                    path.append(currentNode)
                    # change the current node to the previous node
                    currentNode = came_from.get(currentNode)
                # print("currentNode", currentNode)
                # print("came_from", came_from)
                # print("+currentNode", currentNode)
                # reverse the path[] element squence
                path.reverse()
                print(f"{path[-1]} {len(path)}")
                print(" ".join(map(str, path)))
                return

            # loop the edges dictionary and check the cost from origin to each node
            for (from_node, to_node), edge_cost in self.edges.items():
                # check if the from_node is the current node we are at now
                if from_node == currentNode:
                    # if it is, add the previous cost with the cost to the next node
                    new_cost = cost + edge_cost
                    # if the next node is not in min_cost dictionary or the new cost is lower than the cost before
                    if to_node not in min_cost or new_cost < min_cost[to_node]:
                        # add a new pair or update the previous pair in min_cost dictionary with "node: cost"
                        min_cost[to_node] = new_cost
                        # print("-came_from", came_from)
                        # add or update the pair in came_from dictionary with "node: previous node"
                        came_from[to_node] = currentNode
                        # print("+came_from", came_from)
                        # print("-frontier", frontier)
                        # add the new cost and new next node or update lowest cost for node already exsit in frontier[]
                        frontier.append((new_cost, to_node))
                        # print("+frontier", frontier)

        print("No path found.")

        
        # Recursive Best-First Search
    def CUS2(self):
            def euclidean_heuristic(node, goal):
                x1, y1 = self.nodes[node]
                x2, y2 = self.nodes[goal]
                return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        
            def rbfs(current, goal, path, g, f_limit):
                if current == goal:
                    return path, g, True
        
                successors = []
                for (from_node, to_node), cost in self.edges.items():
                    if from_node == current and to_node not in path:
                        h = euclidean_heuristic(to_node, goal)
                        f = g + cost + h
                        successors.append((f, to_node, cost))
        
                if not successors:
                    return None, float('inf'), False
        
                successors.sort()
                
                while successors:
                    best_f, best_node, best_cost = successors[0]
                    alt_f = successors[1][0] if len(successors) > 1 else float('inf')
        
                    result, new_f, found = rbfs(best_node, goal, path + [best_node], g + best_cost, min(f_limit, alt_f))
                    if found:
                        return result, new_f, True
        
                    successors[0] = (new_f, best_node, best_cost)
                    successors.sort()
        
                return None, float('inf'), False
        
            for goal in self.destinations:
                path, _, found = rbfs(self.origin, goal, [self.origin], 0, float('inf'))
                if found:
                    print(f"{goal} {len(path)}")
                    print(" ".join(map(str, path)))
                    return
        
            print("No path found.")
