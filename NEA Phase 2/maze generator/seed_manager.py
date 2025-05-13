# maze_generator/seed_manager.py
import random

class SeedManager:
    MIN_SIZE = 3
    MAX_SIZE = 64

    @staticmethod
    def validate_seed(seed_str):
        try:
            return int(seed_str)
        except ValueError:
            raise ValueError("Seed must be an integer.")

    @staticmethod
    def generate_seed():
        return random.randint(10000, 99999999)  # or use time, UUID if needed

    @staticmethod
    def apply_seed(seed):
        random.seed(seed)

    @staticmethod
    def validate_dimensions(width, height):
        if not (SeedManager.MIN_SIZE <= width <= SeedManager.MAX_SIZE) or \
           not (SeedManager.MIN_SIZE <= height <= SeedManager.MAX_SIZE):
            raise ValueError(f"Width and height must be between {SeedManager.MIN_SIZE} and {SeedManager.MAX_SIZE}.")
