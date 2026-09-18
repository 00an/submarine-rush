import pygame

from config.settings import (
    BLACK,
    GREEN,
    RED,
    WHITE,
)


class HUD:
    """Handles gameplay HUD elements."""

    def __init__(self, screen, coin_img):
        self.screen = screen
        self.coin_img = coin_img

    def draw_hp_bar(self, hp):
        """Draw the player's HP bar."""
        bar_width = 200
        bar_height = 20

        pygame.draw.rect(
            self.screen,
            BLACK,
            (
                10,
                10,
                bar_width,
                bar_height
            )
        )

        pygame.draw.rect(
            self.screen,
            GREEN,
            (
                10,
                10,
                min(
                    bar_width,
                    max(0, hp) * 2
                ),
                bar_height
            )
        )

        font = pygame.font.Font(
            None,
            24
        )

        text = font.render(
            f"HP: {max(0, hp)}",
            True,
            RED
        )

        self.screen.blit(
            text,
            (
                110 - text.get_width() // 2,
                10
            )
        )

    def draw_stats(self, coins):
        """Draw current coin count."""
        font = pygame.font.Font(
            None,
            36
        )

        text = font.render(
            str(coins),
            True,
            WHITE
        )

        self.screen.blit(
            text,
            (10, 40)
        )

        self.screen.blit(
            self.coin_img,
            (
                text.get_width() + 15,
                35
            )
        )