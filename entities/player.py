import pygame

from config.assets import asset_path
from config.settings import (
    EXTREME_SPEED,
    PLAYER_BASE_SPEED,
)
from data.boats import boats


class Player:
    """Handles player movement, health and submarine."""

    def __init__(
        self,
        screen_width,
        screen_height
    ):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.base_speed = PLAYER_BASE_SPEED
        self.speed = PLAYER_BASE_SPEED

        self.current_coins = 0

        self.width = 100
        self.height = 60

        self.x = 0

        self.y = (
            screen_height // 2
            - self.height // 2
        )

        self.hp = 0
        self.image = None

        self.update_boat()

    def update_screen_size(
        self,
        screen_width,
        screen_height
    ):
        """Update the screen dimensions."""
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.y = max(
            0,
            min(
                self.y,
                self.screen_height - self.height
            )
        )

    def get_equipped_boat(self):
        """Return the currently equipped submarine."""
        return next(
            (
                boat
                for boat in boats
                if boat.equipped
            ),
            None
        )

    def update_boat(self):
        """Update the submarine image, size and HP."""
        boat = self.get_equipped_boat()

        if boat is None:
            self.hp = 0
            self.image = None
            return

        boat_index = boats.index(boat)

        scale_factor = (
            150
            - (15 * boat_index)
        )

        self.image = pygame.image.load(
            asset_path(
                "png",
                boat.image
            )
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (
                scale_factor,
                scale_factor // 2
            )
        )

        self.width = scale_factor
        self.height = scale_factor // 2
        self.hp = boat.hp

    def move(
        self,
        keys,
        extreme_mode
    ):
        """Move the submarine according to player input."""
        base_speed = (
            EXTREME_SPEED
            if extreme_mode
            else PLAYER_BASE_SPEED
        )

        speed_multiplier = (
            self.screen_width / 800
        )

        self.speed = max(
            1,
            round(
                base_speed * speed_multiplier
            )
        )

        if extreme_mode:
            self.x += self.speed

        if keys[pygame.K_LEFT]:
            self.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        if keys[pygame.K_UP]:
            self.y -= self.speed

        if keys[pygame.K_DOWN]:
            self.y += self.speed

        self.x = max(
            0,
            self.x
        )

        self.y = max(
            0,
            min(
                self.y,
                self.screen_height - self.height
            )
        )

    def get_rect(self):
        """Return the player's collision rectangle."""
        return pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )

    def draw(
        self,
        screen,
        camera_x,
        camera_y
    ):
        """Draw the submarine relative to the camera."""
        if self.image is None:
            return

        screen.blit(
            self.image,
            (
                self.x - camera_x,
                self.y - camera_y
            )
        )