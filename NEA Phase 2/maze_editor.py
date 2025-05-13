# maze_editor.py
"""
This module handles logic for manually editing a maze.
Includes toggling walls/paths and managing entrance/exit squares.
"""

def toggle_cell(maze: list, x: int, y: int):
    """
    Toggles cell from wall (1) to path (0) or vice versa.
    Includes defensive checks.
    """
    if not (0 <= y < len(maze) and 0 <= x < len(maze[0])):
        return  # Invalid coordinates, do nothing

    maze[y][x] = 1 - maze[y][x]  # Toggle

def set_entrance(maze: list, x: int, y: int):
    """Sets entrance cell (ensures it's a path)."""
    toggle_cell(maze, x, y)
    return (x, y)

def set_exit(maze: list, x: int, y: int):
    """Sets exit cell (ensures it's a path)."""
    toggle_cell(maze, x, y)
    return (x, y)
