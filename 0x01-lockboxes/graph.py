#!/usr/bin/python3
class Node:
    def __init__(self, el):
        self.el = el
        self.color = 'white'
        self.distance = 0
        self.parent = None

    def __str__(self) -> str:
        return "{}".format(self.__dict__)


class Graph:

    def __init__(self):
        self.__nodeList = {}
        self.__adjacencyList = {}
        self.tree = []
        self.count = 0

    def addNode(self, el):
        node = Node(el)
        self.__nodeList.setdefault(el, node)
        self.__adjacencyList.setdefault(node, [])

    def getNode(self, node):
        node = self.__nodeList[node]
        return node

    def addEdge(self, nodeSource, nodeDest):
        nodeSource = self.getNode(nodeSource)
        nodeDest = self.getNode(nodeDest)

        self.__adjacencyList[nodeSource].append(nodeDest)
        # for undirected graph
        # self.adjacencyList[nodeDest].append(nodeSource)

    def getNodeList(self):
        return self.__nodeList

    def printGraph(self):
        for key, value in self.__adjacencyList.items():
            if value is not []:
                print("{} is connected to {}".format(key, value))

    def removeNode(self, node):
        if node:
            for value in self.__adjacencyList.values():
                value.remove(node)
            del self.__adjacencyList[node]
            self.__nodeList.remove(node)

    def removeEdge(self, nodeSource, nodeDest):
        nodeSource = self.__nodeList(nodeSource)
        nodeDest = self.__nodeList(nodeDest)
        if not nodeSource or not nodeDest:
            return
        self.__adjacencyList[nodeSource].remove(nodeDest)

    def getEdges(self, node):
        """
        Retrieve the edges (neighboring nodes) of a given node in the graph.

        Parameters:
        node (Node): The node for which to retrieve the edges. The node must be an instance of the Node class.

        Returns:
        list: A list of nodes that are adjacent to the given node. If the given node has no edges, an empty list is returned.
        """
        edges = self.__adjacencyList[node]
        return edges

    def breadthFirstSearch(self, source):
        """
        Perform a breadth-first search on the graph starting from the given source node.

        Parameters:
        source (str): The label of the source node from which to start the search.

        Returns:
        None. The function modifies the graph by updating the color, distance, and parent attributes of each node.
        """
        source = self.getNode(source)
        self.tree.append(source)
        while self.tree != []:
            u = self.tree.pop()
            for v in self.getEdges(u):
                if v.color == 'white':
                    v.color = 'gray'
                    v.distance = u.distance + 1
                    v.parent = u
                    self.tree.append(v)
            u.color == 'black'

    def depthVisit(self, node):
        # topologicalSort = __import__('linked_list').LinkedList()
        self.count += 1
        node.distance = self.count
        node.color = 'gray'
        for adj in self.getEdges(node):
            if adj.color == 'white':
                adj.parent = node
                self.depthVisit(adj)
        node.color = 'black'
        self.count += 1
        node.f = self.count
        # topologicalSort.addNode(node.el)
        # topologicalSort.printList()

    def depthFirstSearch(self):
        for value in self.__nodeList.values():
            if value.color == 'white':
                self.depthVisit(value)
