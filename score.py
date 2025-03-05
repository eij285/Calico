import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from collections import deque

from Errors import InvalidTokenError


# Scores button tile by verifying valid placement through breadth search
def is_valid_button(g, node, button_color):

    # Check that the node given is the same color as the button
    if button_color != g.nodes[node]['color']:
        return False

    # Create queue with neighbors of given node and initialise a visited np array with array values
    queue = deque(g.neighbors(node))
    visited = np.full((15,), False)

    valid_nodes = 0

    # While queue still has elements, pop the first node number
    while queue:
        node = queue.popleft()
        
        # If node has already been visited, skip this in the queue
        if visited[node - 1]:
            continue

        # Check that the button color matches and increment valid_nodes
        if button_color == g.nodes[node]['color']:
            valid_nodes += 1

            # If there are 3 valid nodes adjacent, check has been satisfied
            if valid_nodes == 3:
                return True
            
            # Add new neighbors of current node to queue if they have not been visited
            for neighbor in g.neighbors(node):
                if not visited[neighbor - 1]:
                    queue.append(neighbor)

        # Mark node as visited
        visited[node - 1] = True    
    
    # If there were not at least 3 valid_nodes, reject the check
    return False

# Scores button tile by verifying valid placement through breadth search
def score_button():
    return 3

# Scores cat tile through breadth search
def score_cat(graph, value, type, design):
    return value

# Scores design tile by checking neighbouring nodes and seeing if its satisfied
def score_design_tile(graph, value1, value2):
    return 0


if __name__ == '__main__':
    G = nx.Graph()
    G.add_nodes_from([(1, {"color": "pink"}), (2, {"color": "yellow"}), (3, {"color": "light-blue"})])
    G.add_nodes_from([(8, {"color": "green"})])
    G.add_nodes_from([(15, {"color": "dark-blue"})])

    G.add_edges_from([(1, 2), (2, 3), (1, 8), (2, 8), (8, 15)])

    G.add_nodes_from([(9, {"color": "light-blue"}), (10, {"color": "light-blue"})])
    G.add_edges_from([(2, 9), (3, 9), (3, 10), (8, 9), (9, 10)])

    nx.draw(G, with_labels=True)  
    plt.show()
    print(G.edges())

    is_valid_button(G, 10, 'light-blue')