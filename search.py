import sys

class Search:

    nodes = {}
    edges = {}
    origin = None
    destinations = None
    
    
    def __init__(self, nodes, edges, origin, destination):
        self.nodes = nodes
        self.edges = edges
        self.origin = origin
        self.destination = destination
        
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
        # path = []
        # numOfNodes = len(path)
        # for
        
        # for node in self.nodes:
            
            
        return
    
    # Breadth-First-Search
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
        
    
    
    
       
        








                