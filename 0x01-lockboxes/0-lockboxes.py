#!/usr/bin/python3
"""
Module: Boxes Unlocking

This module contains a function to determine if all boxes can be unlocked.

Functions:
- canUnlockAll(boxes: List[List[int]]) -> bool:
    Determine if all boxes can be unlocked.

    This function takes a list of boxes, where each box contains a list of keys that can unlock other boxes.
    The function uses a breadth-first search (BFS) approach to explore all possible paths of unlocking boxes.

    Parameters:
    boxes (List[List[int]]): A 2D list representing the boxes. Each inner list contains the keys that can unlock the corresponding box.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
"""


def createGraph(boxes):
    graph = __import__('graph').Graph()
    for i, box in enumerate(boxes):
        graph.addNode(i)
    for i, box in enumerate(boxes):
        for el in box:
            graph.addEdge(i, el)
    graph.printGraph()
    return graph


def canUnlockAll(boxes):
    graph = createGraph(boxes)
    graph.depthFirstSearch()
    graph.printGraph()
    for i in graph.getNodeList().keys():
        if graph.getNodeList()[i].parent == None:
            return False
    return True
