#!/usr/bin/python3
class Node:
    """
    A class to represent a node in a graph.

    Attributes
    ----------
    el : str
        The element or value of the node.
    color : str
        The color of the node during graph traversal.
    distance : int
        The distance of the node from the source node in a graph traversal.
    parent : Node
        The parent node in the traversal tree.

    Methods
    -------
    __str__() -> str
        Returns a string representation of the node.
    """

    def __init__(self, el):
        """
        Constructs all the necessary attributes for the node object.

        Parameters
        ----------
        el : str
            The element or value of the node.
        """
        self.el = el
        self.color = "white"
        self.distance = 0
        self.parent = None

    def __str__(self) -> str:
        """
        Returns a string representation of the node.

        Returns
        -------
        str
            The string representation of the node.
        """
        return "{}".format(self.__dict__)


class Graph:
    __nodeList = {}
    __adjacencyList = {}
    tree = []
    count = 0

    def addNode(self, el):
        """
        Adds a new node to the graph.

        Parameters:
        el (str): The element or value of the node.

        Returns:
        None
        """
        node = Node(el)
        self.__nodeList.setdefault(el, node)
        self.__adjacencyList.setdefault(node, [])

    def getNode(self, node):
        """
        Retrieves a node from the graph based on its element.

        Parameters:
        node (str): The element of the node.

        Returns:
        Node: The node object with the given element.
        """
        node = self.__nodeList[node]
        return node

    def addEdge(self, nodeSource, nodeDest):
        nodeSource = self.getNode(nodeSource)
        nodeDest = self.getNode(nodeDest)

        if nodeSource and nodeDest:
            self.__adjacencyList[nodeSource].append(nodeDest)

        self.__adjacencyList[nodeSource].append(nodeDest)
        # For undirected graph
        # self.adjacencyList[nodeDest].append(nodeSource)

    def getNodeList(self):
        """
        Retrieves all nodes in the graph.

        Parameters:
        None

        Returns:
        dict: A dictionary containing all nodes in the graph.
        """
        return self.__nodeList

    def printGraph(self):
        """
        Prints the graph in adjacency list format.

        Parameters:
        None

        Returns:
        None
        """
        for key, value in self.__adjacencyList.items():
            if value:
                print("{} is connected to {}".format(key.el, [v.el for v in value]))

    def removeNode(self, node):
        """
        Removes a node from the graph.

        Parameters:
        node (str): The element of the node to be removed.

        Returns:
        None
        """
        if node:
            for value in self.__adjacencyList.values():
                value.remove(node)
            del self.__adjacencyList[node]
            self.__nodeList.remove(node)

    def removeEdge(self, nodeSource, nodeDest):
        """
        Removes a directed edge from nodeSource to nodeDest.

        Parameters:
        nodeSource (str): The element of the source node.
        nodeDest (str): The element of the destination node.

        Returns:
        None
        """
        nodeSource = self.__nodeList(nodeSource)
        nodeDest = self.__nodeList(nodeDest)
        if not nodeSource or not nodeDest:
            return
        self.__adjacencyList[nodeSource].remove(nodeDest)

    def getEdges(self, node):
        """
        Retrieves all edges connected to a given node.

        Parameters:
        node (str): The element of the node.

        Returns:
        list: A list of nodes connected to the given node.
        """
        edges = self.__adjacencyList[node]
        return edges

    def breadthFirstSearch(self, source):
        """
        Performs a breadth-first search traversal on the graph starting from the given source node.

        Parameters:
        source (str): The element of the source node.

        Returns:
        None
        """
        source = self.getNode(source)
        self.tree.append(source)
        while self.tree != []:
            u = self.tree.pop()
            for v in self.getEdges(u):
                if v.color == "white":
                    v.color = "gray"
                    v.distance = u.distance + 1
                    v.parent = u
                    self.tree.append(v)
            u.color == "black"

    def depthVisit(self, node):
        """
        Performs a depth-first search traversal on the graph starting from the given node.

        Parameters:
        node (Node): The node to start the traversal from.

        Returns:
        None
        """
        # topologicalSort = __import__('linked_list').LinkedList()
        self.count += 1
        node.distance = self.count
        node.color = "gray"
        for adj in self.getEdges(node):
            if adj.color == "white":
                adj.parent = node
                self.depthVisit(adj)
        node.color = "black"
        self.count += 1
        node.f = self.count
        # topologicalSort.addNode(node.el)
        # topologicalSort.printList()

    def depthFirstSearch(self):
        """
        Performs a depth-first search traversal on the entire graph.

        Parameters:
        None

        Returns:
        None
        """
        for value in self.__nodeList.values():
                if value.color == "white":
                    self.depthVisit(value)
