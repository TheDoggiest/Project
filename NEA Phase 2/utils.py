# utils.py
"""
Utility functions used across multiple modules.
"""

import random
import string

def generate_seed(length=8):
    """Generate a random alphanumeric seed."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def classify_difficulty(maze, path_length):
    """
    Classifies difficulty based on path length and wall density.
    """
    total_cells = len(maze) * len(maze[0])
    wall_count = sum(row.count(1) for row in maze)
    density = wall_count / total_cells

    if path_length < 20 and density < 0.3:
        return "Easy"
    elif path_length < 50 and density < 0.6:
        return "Medium"
    else:
        return "Hard"
