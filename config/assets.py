from pathlib import Path

import pygame


BASE_DIR = Path(__file__).resolve().parent.parent


def asset_path(folder, filename):
    return str(
        BASE_DIR / "assets" / folder / filename
    )


def load_image(folder, filename, size=None):
    image = pygame.image.load(
        asset_path(folder, filename)
    ).convert_alpha()

    if size is not None:
        image = pygame.transform.scale(
            image,
            size
        )

    return image