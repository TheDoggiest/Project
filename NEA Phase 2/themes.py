# themes.py

# This file defines visual style configurations for various themes

THEMES = {
    "Normal": {
        "wall_color": "black",
        "path_color": "white",
        "entrance_color": "green",
        "exit_color": "red",
        "solution_color": "purple",
        "player1_color": "blue",
        "player2_color": "yellow",
        "decorations": None
    },
    "Christmas": {
        "wall_color": "#0B6623",  # Dark green
        "path_color": "#ffffff",  # White snow
        "entrance_color": "#00ff00",  # Bright green
        "exit_color": "#ff0000",      # Red
        "solution_color": "#cc33ff",  # Magenta
        "player1_color": "#0000ff",
        "player2_color": "#ffff00",
        "decorations": "tree"  # We'll draw tree icons on some walls
    },
    "Halloween": {
        "wall_color": "#FF7518",  # Pumpkin orange
        "path_color": "#1C1C1C",  # Very dark grey
        "entrance_color": "#FF6347",  # Tomato
        "exit_color": "#8B0000",      # Dark red
        "solution_color": "#9900cc",  # Deep purple
        "player1_color": "#0000ff",
        "player2_color": "#ffff00",
        "decorations": "pumpkin"  # Draw jack-o'-lanterns
    }
}
