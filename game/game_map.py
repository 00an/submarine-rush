import random

import pygame

from config.assets import load_image
from config.settings import (
    BOMB_SPAWN_CHANCE,
    COIN_SPAWN_CHANCE,
    OBJECTS_PER_GENERATION,
)


class GameMap:
    """Handles object spawning, cleanup and rendering."""

    def __init__(
        self,
        screen_width,
        screen_height,
        backgrounds
    ):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.backgrounds = backgrounds

        self.bombs = []
        self.coins = []

        self.last_generated_x = 0

        self.bomb_image = load_image(
            "png",
            "bomb.png",
            (50, 50)
        )

        self.coin_image = load_image(
            "png",
            "coin.png",
            (30, 30)
        )

    def update_screen_size(
        self,
        width,
        height
    ):
        """Update the current screen dimensions."""
        self.screen_width = width
        self.screen_height = height

    def object_overlaps(self, rect):
        """Return True when the rectangle overlaps another object."""
        for bomb in self.bombs:
            if rect.colliderect(bomb["rect"]):
                return True

        for coin in self.coins:
            if rect.colliderect(coin["rect"]):
                return True

        return False

    def generate_random_objects(
        self,
        start_x,
        end_x
    ):
        """Generate a new group of random objects."""
        for _ in range(OBJECTS_PER_GENERATION):

            if random.random() < BOMB_SPAWN_CHANCE:
                bomb_x = random.randint(
                    start_x,
                    end_x
                )

                bomb_y = random.randint(
                    0,
                    max(
                        0,
                        self.screen_height
                        - self.bomb_image.get_height()
                    )
                )

                bomb_rect = pygame.Rect(
                    bomb_x,
                    bomb_y,
                    self.bomb_image.get_width(),
                    self.bomb_image.get_height()
                )

                if not self.object_overlaps(
                    bomb_rect
                ):
                    self.bombs.append(
                        {
                            "rect": bomb_rect,
                            "image": self.bomb_image
                        }
                    )

            if random.random() < COIN_SPAWN_CHANCE:
                coin_x = random.randint(
                    start_x,
                    end_x
                )

                coin_y = random.randint(
                    0,
                    max(
                        0,
                        self.screen_height
                        - self.coin_image.get_height()
                    )
                )

                coin_rect = pygame.Rect(
                    coin_x,
                    coin_y,
                    self.coin_image.get_width(),
                    self.coin_image.get_height()
                )

                if not self.object_overlaps(
                    coin_rect
                ):
                    self.coins.append(
                        {
                            "rect": coin_rect,
                            "image": self.coin_image
                        }
                    )

    def update(self, camera_x):
        """Generate new objects and remove objects behind the camera."""
        if camera_x > self.last_generated_x + 50:
            start_x = camera_x + (
                self.screen_width * 75 // 100
            )

            end_x = (
                start_x
                + self.screen_width
            )

            self.last_generated_x = camera_x

            self.generate_random_objects(
                start_x,
                end_x
            )

        minimum_x = (
            camera_x
            - self.screen_width
        )

        self.bombs = [
            bomb
            for bomb in self.bombs
            if bomb["rect"].right > minimum_x
        ]

        self.coins = [
            coin
            for coin in self.coins
            if coin["rect"].right > minimum_x
        ]

    def draw(
        self,
        screen,
        camera_x,
        camera_y
    ):
        """Draw the correct background and all active objects."""
        if camera_x <= 0:
            background = self.backgrounds.spawn
        else:
            background = self.backgrounds.game

        screen.blit(
            background,
            (0, 0)
        )

        for bomb in self.bombs:
            rect = bomb["rect"]

            screen.blit(
                bomb["image"],
                (
                    rect.x - camera_x,
                    rect.y - camera_y
                )
            )

        for coin in self.coins:
            rect = coin["rect"]

            screen.blit(
                coin["image"],
                (
                    rect.x - camera_x,
                    rect.y - camera_y
                )
            )