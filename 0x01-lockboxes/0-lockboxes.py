#!usr/bin/python3

"""
This module contains functions to create a graph representation of boxes and determine if it is possible to unlock all boxes.

Functions:
createGraph(boxes): Creates a graph representation of the given boxes.
canUnlockAll(boxes): Determines if it is possible to unlock all boxes in the given configuration.
"""


def createGraph(boxes):
    """
    Creates a graph representation of the given boxes.

    Parameters:
    boxes (list of lists): A list where the index represents box IDs (strings) and the values are lists of box IDs that can unlock the corresponding box.

    Returns:
    graph (Graph): A graph object representing the boxes and their unlocking relationships.
    """
    graph = __import__("graph").Graph()
    for i, box in enumerate(boxes):
        graph.addNode(i)
    for i, box in enumerate(boxes):
        for el in box:
            graph.addEdge(i, el)
    return graph


def canUnlockAll(boxes):
    """
    Determines if it is possible to unlock all boxes in the given configuration.

    Parameters:
    boxes (list of lists): A List where the index are box IDs (strings) and the values are lists of box IDs that can unlock the corresponding box.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
    """
    graph = createGraph(boxes)
    graph.depthFirstSearch()
    graph.printGraph()
    for i in range(1, len(graph.getNodeList())):
        if graph.getNodeList()[i].parent == None:
            return False
    return True
