# display/tile.py

WALL = 0
PATH = 1
ENTRANCE = 2
EXIT = 3

def get_tile_color(tile_type):
    from display.config import COLOR_WALL, COLOR_PATH, COLOR_ENTRANCE, COLOR_EXIT
    if tile_type == WALL:
        return COLOR_WALL
    elif tile_type == PATH:
        return COLOR_PATH
    elif tile_type == ENTRANCE:
        return COLOR_ENTRANCE
    elif tile_type == EXIT:
        return COLOR_EXIT
    else:
        return (200, 200, 200)  # Unknown tile
