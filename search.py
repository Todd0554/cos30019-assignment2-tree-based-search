import sys

class Search:

    nodes = {}
    edges = {}
    origin = {}
    destinations = {}
    
    
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
                
    def DFS(self):
        # path = []
        # numOfNodes = len(path)
        # for
        
        # for node in self.nodes:
            
            
        return
        
    def BFS(self):
        
        return
        
        
        
    def GBFS(self):
        
        return
        
        
    
    def Astar(self):
        
        return
        
        
    def CUS1(self):
        
        return
        
        
    def CUS2(self):
        
        return
        
    
    
    
       
        








                