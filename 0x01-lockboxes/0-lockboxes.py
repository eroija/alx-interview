#!/usr/bin/python3
"""Module for task 0."""


def canUnlockAll(boxes):
    """Function that determines if all the boxes are opened."""
    keys_seen = set()
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        keys_seen.add(current_box)

        for key in boxes[current_box]:
            if key not in keys_seen:
                queue.append(key)

    return len(keys_seen) == len(boxes)
