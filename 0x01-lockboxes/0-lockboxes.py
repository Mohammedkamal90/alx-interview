#!/usr/bin/python3
'''Lockboxes problem
'''

def canUnlockAll(boxes):
    if not boxes:
        return False

    keys = set([0])  # Start with keys to the first box
    opened = set()   # Set to keep track of opened boxes

    while keys:
        box_idx = keys.pop()  # Get a box index from keys
        opened.add(box_idx)   # Mark the box as opened

        # Add keys from the current box to keys set
        for key in boxes[box_idx]:
            if key not in opened:
                keys.add(key)

    # Check if all boxes are opened
    return len(opened) == len(boxes)


# Test cases
if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # False
