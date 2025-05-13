# maze_solver.py
"""
Implements Bidirectional BFS for shortest path finding.
"""

from collections import deque

def bidirectional_bfs(maze, start, end):
    """Find shortest path using bidirectional BFS."""
    width, height = len(maze[0]), len(maze)
    visited_start = {}
    visited_end = {}

    queue_start = deque([start])
    queue_end = deque([end])
    visited_start[start] = None
    visited_end[end] = None

    def neighbors(pos):
        x, y = pos
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 0:
                yield (nx, ny)

    while queue_start and queue_end:
        intersect = search_step(queue_start, visited_start, visited_end, neighbors)
        if intersect: return reconstruct_path(visited_start, visited_end, intersect)

        intersect = search_step(queue_end, visited_end, visited_start, neighbors)
        if intersect: return reconstruct_path(visited_start, visited_end, intersect)

    return None  # No path found

def search_step(queue, visited_this, visited_other, neighbors):
    """Performs one step of BFS."""
    current = queue.popleft()
    for neighbor in neighbors(current):
        if neighbor not in visited_this:
            visited_this[neighbor] = current
            queue.append(neighbor)
        if neighbor in visited_other:
            return neighbor
    return None

def reconstruct_path(visited_start, visited_end, meet_point):
    """Reconstructs path from start to end."""
    path = []
    node = meet_point
    while node:
        path.append(node)
        node = visited_start[node]
    path.reverse()
    node = visited_end[meet_point]
    while node:
        path.append(node)
        node = visited_end[node]
    return path
