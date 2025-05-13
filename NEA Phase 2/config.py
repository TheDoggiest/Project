# config.py
from themes import THEMES

# Maze size limits
MIN_SIZE = 4
MAX_SIZE = 64

# Square size in pixels
SQUARE_SIZE = 20

# Colours
COLOR_ENTRANCE = "green"
COLOR_EXIT = "red"
COLOR_PATH = "white"
COLOR_WALL = "black"
COLOR_SOLUTION = "purple"
COLOR_PLAYER1 = "blue"
COLOR_PLAYER2 = "yellow"

# Difficulty thresholds
DIFFICULTY_THRESHOLDS = {
    "Easy": (0.1, 0.3),
    "Medium": (0.3, 0.6),
    "Hard": (0.6, 1.0),
}


# Set default theme
CURRENT_THEME_NAME = "Normal"
CURRENT_THEME = THEMES[CURRENT_THEME_NAME]
