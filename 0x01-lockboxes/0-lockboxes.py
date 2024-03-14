#!/usr/bin/env python3
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
    unlockedBoxes = [0]  # First box is always unlocked.
    index = 0

    while index < len(unlockedBoxes):
        currentIndex = unlockedBoxes[index]
        currentBox = boxes[currentIndex]
        for key in currentBox:
            if key not in unlockedBoxes:
                unlockedBoxes.append(key)
        index += 1

    if index == len(boxes):
        return True
    return False
