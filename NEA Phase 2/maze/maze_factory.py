# maze/maze_factory.py
from maze.square_maze import SquareMaze
from maze.triangle_maze import TriangleMaze
from maze.pentagon_maze import PentagonMaze
from maze.hexagon_maze import HexagonMaze
from maze.circular_maze import CircularMaze

def create_maze(shape: str, width: int, height: int):
    shape = shape.lower()
    if shape == "square":
        return SquareMaze(width, height)
    elif shape == "triangular":
        return TriangleMaze(width, height)
    elif shape == "pentagonal":
        return PentagonMaze(width, height)
    elif shape == "hexagonal":
        return HexagonMaze(width, height)
    elif shape == "circular":
        return CircularMaze(width, height)
    else:
        raise ValueError(f"Unknown maze shape: {shape}")
