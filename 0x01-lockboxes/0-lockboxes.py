#!/usr/bin/python3
"""
Module: Boxes Unlocking

This module contains a function to determine if all boxes can be unlocked.

Functions:
- canUnlockAll(boxes: List[List[int]]) -> bool:
    Determine if all boxes can be unlocked.
    This function takes a list of boxes, where each box contains a list of
    keys that can unlock other boxes.
    The function uses a breadth-first search (BFS) approach to
    explore all possible paths of unlocking boxes.

    Parameters:
    boxes (List[List[int]]): A 2D list representing the boxes.
    Each inner list contains the keys that can unlock the corresponding box.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.

- createGraph(boxes: List[List[int]]) -> graph:
    Create a graph representation of the boxes and their unlocking
    relationships.
    This function takes a list of boxes, where each box contains a 
    list of keys that can unlock other boxes.
    It creates a graph using the provided 'graph' module, 
    where each node represents a box and each edge represents
    an unlocking relationship between two boxes.

    Parameters:
    boxes (List[List[int]]): A 2D list representing the boxes. Each inner list
    contains the keys that can unlock the corresponding box.

    Returns:
    graph: A graph object representing the boxes and their unlocking 
    relationships.
"""


def createGraph(boxes):
    """
    Create a graph representation of the boxes and their unlocking 
    relationships.

    This function takes a list of boxes, where each box contains
    a list of keys that can unlock other boxes.
    It creates a graph using the provided 'graph' module, where each node
    represents a box and each edge represents
    an unlocking relationship between two boxes.

    Parameters:
    boxes (List[List[int]]): A 2D list representing the boxes.
    Each inner list contains
    the keys that can unlock the corresponding box.

    Returns:
    graph: A graph object representing the boxes and their
    unlocking relationships.
    """
    graph = __import__('graph').Graph()
    for i, box in enumerate(boxes):
        graph.addNode(i)
    for i, box in enumerate(boxes):
        for el in box:
            graph.addEdge(i, el)
    return graph


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.

    This function takes a list of boxes, where each box contains
    a list of keys that can unlock other boxes.
    It uses a depth-first search (DFS) approach to explore all
    possible paths of unlocking boxes.

    Parameters:
    boxes (List[List[int]]): A 2D list representing the boxes.
    Each inner list contains the keys that can unlock the corresponding box.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
    The function creates a graph representation of the boxes
    and their unlocking relationships using the 'createGraph' function.
    It then performs a depth-first search (DFS) on the graph
    to determine if all boxes can be unlocked.
    """
    graph = createGraph(boxes)
    graph.depthFirstSearch()
    graph.printGraph()
    for i in range(1, len(graph.getNodeList().keys())):
        if graph.getNodeList()[i].parent == None:
            return False
    return True
