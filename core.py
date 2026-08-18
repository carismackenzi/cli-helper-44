import random
import os
from typing import List

def get_random_game_title(games: List[str]) -> str:
    """Select a random game title from a list."""
    if not games:
        return 'No games available'
    return random.choice(games)


def save_game_progress(game_name: str, progress: dict, save_dir: str = 'saves') -> None:
    """Save the game progress to a file."""
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    file_path = os.path.join(save_dir, f'{game_name}_progress.json')
    with open(file_path, 'w') as save_file:
        json.dump(progress, save_file)


def load_game_progress(game_name: str, save_dir: str = 'saves') -> dict:
    """Load the game progress from a file."""
    file_path = os.path.join(save_dir, f'{game_name}_progress.json')
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r') as save_file:
        return json.load(save_file)


def list_available_games(games: List[str]) -> None:
    """Print all available game titles."""
    if not games:
        print('No games available')
        return
    for game in games:
        print(f'- {game}')