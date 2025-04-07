import sys
import os
from search import Search 

# initialize the dictionary for each different data
nodes = {}
edges = {}
origin = None
destinations = []

# read the file path and algorithm method from command line argument

if len(sys.argv) == 3 :
    path = sys.argv[1]
    algorithMethod = sys.argv[2]
    goal = None
    if os.path.isfile(path):
        with open(path, "r") as file:
            section = None
        # read line by line
            for line in file:
                line = line.strip()
                if not line:
                    continue

                # check what session the data below belongs to
                if line.startswith("Nodes:"):
                    section = "nodes"
                    continue
                elif line.startswith("Edges:"):
                    section = "edges"
                    continue
                elif line.startswith("Origin:"):
                    section = "origin"
                    continue
                elif line.startswith("Destinations:"):
                    section = "destinations"
                    continue

                # read data under each section
                if section == "nodes":
                    node_id, coords = line.split(": ")
                    x, y = coords.strip("()").split(",")
                    nodes[int(node_id.strip())] = (int(x), int(y))
                elif section == "edges":
                    edge_part, weight = line.split(": ")
                    from_to = edge_part.strip("()").split(",")
                    from_node = int(from_to[0])
                    to_node = int(from_to[1])
                    edges[(from_node, to_node)] = int(weight)
                elif section == "origin":
                    origin_id = int(line.strip())
                    origin = origin_id
                elif section == "destinations":
                    dest_list = line.strip().split(";")
                    destinations = [int(x.strip()) for x in dest_list]
                    goal = len(destinations)
        
        print(path, " ", algorithMethod)

        
        
        # need to be commented out
        # print("Nodes:", nodes)
        # print("Edges:", edges)
        # print("Origin:", origin)
        # print("Destinations:", destinations)

        
        if origin is None:
            print("Origin not found.")
            sys.exit(1)
        # instantiate the Search class  
        search = Search()
        search.nodes = nodes
        search.edges = edges
        search.origin = origin
        search.destinations = destinations
        search.algoritm_selection(algorithMethod)
    else:
        print("File not found.")
        sys.exit(1)
else:
    print("Please provide the file path and algorithm method as command line arguments.")
    sys.exit(1)