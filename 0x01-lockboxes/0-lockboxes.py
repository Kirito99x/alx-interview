#!/usr/bin/python3
"""lockboxes module"""
def can_unlock_all(boxes):
    """Unlock Lockboxes"""
    if not boxes:
        """If boxes is empty, return False"""
        return False
    
    n = len(boxes)  # Number of boxes
    opened = [False] * n  # List of boxes that are opened 
    opened[0] = True  # First box is always open
    queue = [0]  # List of boxes to open

    while queue:
        """Queue of boxes to open"""
        current_box = queue.pop(0)  # Current box to open 
        for key in boxes[current_box]:  # Loop through keys in the current box
            if key < n and not opened[key]:  # Check if key is valid and not opened
                opened[key] = True  # Open the box
                queue.append(key)  # Add the box to the queue

    return all(opened)
