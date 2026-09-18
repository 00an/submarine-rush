import pygame

from config.settings import (
    BLACK,
    WHITE,
)


class PauseMenu:
    """Handles the pause menu."""

    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        """Draw pause menu."""
        font_large = pygame.font.Font(
            None,
            48
        )

        pause_text = font_large.render(
            "PAUSED",
            True,
            WHITE
        )

        self.screen.blit(
            pause_text,
            (
                self.screen.get_width() // 2
                - pause_text.get_width() // 2,
                self.screen.get_height() // 2 - 120
            )
        )

        buttons = []

        labels = [
            "Resume",
            "Home",
            "Exit"
        ]

        for index, label in enumerate(labels):
            button = pygame.Rect(
                self.screen.get_width() // 2 - 75,
                self.screen.get_height() // 2
                - 60
                + index * 70,
                150,
                50
            )

            pygame.draw.rect(
                self.screen,
                BLACK,
                button
            )

            text = pygame.font.Font(
                None,
                36
            ).render(
                label,
                True,
                WHITE
            )

            self.screen.blit(
                text,
                (
                    button.x
                    + (
                        button.width
                        - text.get_width()
                    ) // 2,
                    button.y + 10
                )
            )

            buttons.append(button)

        return buttons