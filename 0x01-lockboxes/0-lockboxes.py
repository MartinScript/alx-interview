def createGraph(boxes):
    """
    Creates a graph representation of the given boxes.

    Parameters:
    boxes (dict): A dictionary where the keys are box IDs (strings) and the values are lists of box IDs that can unlock the corresponding box.

    Returns:
    Graph: A graph object representing the boxes and their unlocking relationships.
    """
    graph = __import__('graphs').Graph()
    for i in boxes.keys():
        graph.addNode(i)
    for i, box in boxes.items():
        for el in box:
            graph.addEdge(i, el)
    return graph


def canUnlockAll(boxes):
    """
    Determines if it is possible to unlock all boxes in the given configuration.

    Parameters:
    boxes (dict): A dictionary where the keys are box IDs (strings) and the values are lists of box IDs that can unlock the corresponding box.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
    """
    graph = createGraph(boxes)
    graph.depthFirstSearch()
    for i in graph.getNodeList().keys():
        if graph.getNodeList()[i].parent == None:
            return False
    return True