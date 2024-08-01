#!/usr/bin/python3
"""Module for task 0."""


def canUnlockAll(boxes):
    """Function that determines if all the boxes are opened.

    Args:
        boxes (List[List[int]]): list of lists of integers.

    Returns:
        boolean: True if all boxes can be unlocked, by using all the keys
        available in all the reachable boxes, and False otherwise.
    """
    visited = {0}
    queue = [boxes[0]]
    while queue:
        box = queue.pop(0)
        for key in box:
            if key not in visited and key < len(boxes):
                visited.add(key)
                queue.append(boxes[key])
    return len(visited) == len(boxes)
