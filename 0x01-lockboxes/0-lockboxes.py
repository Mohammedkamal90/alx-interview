#!/usr/bin/python3
'''Lockboxes problem
'''

def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    # Keep track of boxes that have been visited
    visited = set()

    # Initialize a queue with the first box
    queue = [0]

    # Iterate through the queue until it's empty
    while queue:
        box = queue.pop(0)
        visited.add(box)  # Mark the box as visited

        # Check the keys in the current box
        for key in boxes[box]:
            if key not in visited:
                queue.append(key)

    # Check if all boxes have been visited
    return len(visited) == len(boxes)
