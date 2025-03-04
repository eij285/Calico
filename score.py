import networkx as nx
from Errors import InvalidTokenError


# Scores button tile by verifying valid placement through breadth search
def score_button(g, node, button_color):
    # Check neighouring tiles until we find 3 that have the same color
    queue = g.neighbors(node)
    
    # Write a visited 

    valid_nodes = 0

    for elem in queue:
        if button_color == elem['color']:
            valid_nodes += 1

            # Need to stop duplicate elements
            queue.append(elem.neighbors(node))
        
    

# Scores cat tile through breadth search
def score_cat(graph, value, type, design):
    return value

# Scores design tile by checking neighbouring nodes and seeing if its satisfied
def score_design_tile(graph, value1, value2):
    return 0


# if __name__ == '__main__':
#     graph = nx.Graph()