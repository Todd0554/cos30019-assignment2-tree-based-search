import sys

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
                    print(self.nodes[dest[0]], " ", len(path))
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
        
        return
        
    # Greedy Best-First Search
    def GBFS(self):
        
        return
        
        
    # A*
    def Astar(self):
        
        return
        
        
    def CUS1(self):
        
        return
        
        
    def CUS2(self):
        
        return
        
    
    
    
       
        








                