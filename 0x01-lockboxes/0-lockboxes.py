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


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.

    This function takes a list of boxes, where each box contains a list of keys that can unlock other boxes.
    The function uses a breadth-first search (BFS) approach to explore all possible paths of unlocking boxes.

    Parameters:
    boxes (List[List[int]]): A 2D list representing the boxes. Each inner list contains the keys that can unlock the corresponding box.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)
    unlocked = [False] * n  # Track which boxes have been unlocked
    unlocked[0] = True  # Box 0 is initially unlocked
    keys = [0]  # Start with the key to the first box

    while keys:
        current_key = keys.pop(0)
        for key in boxes[current_key]:
            if key < n and not unlocked[key]:  # Check if the key unlocks a box
                unlocked[key] = True
                # Add the new key to the list to explore further
                keys.append(key)

    return all(unlocked)  # Check if all boxes were unlocked
