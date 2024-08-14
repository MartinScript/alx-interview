#!/usr/bin/python3
class Graph:
    """
    A class representing a graph data structure.

    Attributes:
    graph (dict): A dictionary to store nodes and their adjacent nodes.

    Methods:
    get_graph(): Prints the graph in the format of node and its attributes.
    add_node(node): Adds a node to the graph.
    add_adj_nodes(node, adj): Adds adjacent nodes to a given node.
    """

    graph = {}

    def add_node(self, node):
        """
        Adds a node to the graph.

        Parameters:
        node (Node): The node to be added to the graph. If the node already exists,
            it will be replaced with the new node.
        """
        if node in self.graph.values():
            node = self.graph[node.el]
        self.graph[node.el] = node

    def add_adj_nodes(self, node, adj):
        """
        Adds adjacent nodes to a given node.

        Parameters:
        node (Node): The node to which adjacent nodes will be added.
        adj (list): A list of integers representing the indices of adjacent nodes.
        """
        if node is not None:
            for i in adj:
                node.adj_nodes.append(self.graph[i])


class Node:
    """
    A class representing a node in a graph.

    Attributes:
    el (int): The element stored in the node.
    adj_nodes (dict): A dictionary to store adjacent nodes.
    color (str): The color of the node during graph traversal.
    distance (int): The distance of the node from the starting node during graph traversal.
    parent (Node): The parent node in the traversal path.

    Methods:
    __init__(self, el): Initializes a new node with the given element.
    __str__(self): Returns a string representation of the node.
    """

    def __init__(self, el):
        self.el = el
        self.adj_nodes = []
        self.color = 'white'
        self.distance = 0
        self.parent = None

    def __str__(self):
        return "{}".format(self.__dict__)

def create_graph(boxes):
    """
    This function creates a graph representation of the given boxes.

    Parameters:
    boxes (list of lists): A list of boxes, where each box is represented by a list of integers.
        Each integer in the box represents an adjacent node.

    Returns:
    graph (Graph): A graph object representing the boxes. The graph contains nodes and their adjacent nodes.
    """
    graph = Graph()
    for i in range(len(boxes)):
        node = Node(i)
        graph.add_node(node)

    for key, value in graph.graph.items():
        for i, box in enumerate(boxes):
            if i == key:
                graph.add_adj_nodes(value, box)
    return graph


count = 0

def depth_visit(node):
    """
    Performs a depth-first search traversal on a graph starting from a given node.

    Parameters:
    node (Node): The starting node for the depth-first search.

    Returns:
    None. The function modifies the attributes of the nodes during the traversal.
    """
    global count
    count += 1
    node.distance = count
    node.color = 'gray'
    for adj in node.adj_nodes:
        if adj.color == 'white':
            adj.parent = node
            depth_visit(adj)
    node.color = 'black'
    count += 1
    node.f = count


def depth_first_search(graph):
    """
    Performs a depth-first search traversal on a given graph.

    Parameters:
    graph (Graph): The graph object to be traversed. The graph should contain nodes and their adjacent nodes.

    Returns:
    None. The function modifies the attributes of the nodes during the traversal.
    Specifically, it sets the 'color', 'distance', 'parent', and 'f' attributes of each node.
    """
    for value in graph.graph.values():
        if value.color == 'white':
            depth_visit(value)


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    This function creates a graph representation of the given boxes, performs a depth-first search traversal,
    and checks if all boxes can be unlocked. A box can be unlocked if it is adjacent to an already unlocked box.

    Parameters:
    boxes (list of lists): A list of boxes, where each box is represented by a list of integers.
        Each integer in the box represents an adjacent node.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
    """
    graph = create_graph(boxes)
    depth_first_search(graph)
    for i in range(1,len(graph.graph)):
        if graph.graph[i].parent == None:
            return False
    return True

