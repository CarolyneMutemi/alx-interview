#!/usr/bin/python3
"""
Solving lockboxes challenge.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    Args:
        boxes - a list of lists containing keys.
    Return: True or False
    """
    boxesList = [x for x in range(len(boxes))]
    unlockedBoxes = [0]  # First box is always unlocked.
    index = 0

    while index < len(unlockedBoxes):
        currentIndex = unlockedBoxes[index]
        currentBox = boxes[currentIndex]
        for key in currentBox:
            if key not in unlockedBoxes and key in range(len(boxes)):
                unlockedBoxes.append(key)
        index += 1

    if boxesList == sorted(unlockedBoxes):
        return True
    return False
