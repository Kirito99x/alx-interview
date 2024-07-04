#!/usr/bin/python3
""" unlock Lockboxes """
def canUnlockAll(boxes):
    """unlock Lockboxes"""
    if not boxes:
        """if boxes is empty return false"""
        return False
    
    n = len(boxes) # number of boxes
    opended = [False] * n # list of boxes that are opend 
    opended[0] = True # first box is always open
    queue = [0] # list of boxes to open

    while queue:
        """queue of boxes to open"""
        current_box = queue.pop(0) # current box to open 
        for key in boxes[current_box]: # loop through keys in the current box
            if key < n and not opended[key]: # check if key is valid and not opened
                opended[key] = True # open the box
                queue.append(key) # add the box to the queue
    
    return all(opended)
