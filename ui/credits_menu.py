import pygame

from config.settings import (
    BLACK,
    WHITE,
)


class CreditsMenu:
    """Handles the credits page."""

    def __init__(
        self,
        screen,
        credits_button_img
    ):
        self.screen = screen
        self.credits_button_img = credits_button_img

    def draw_back_button(self):
        """Draw and return the back button."""
        button = pygame.Rect(
            10,
            10,
            100,
            40
        )

        pygame.draw.rect(
            self.screen,
            BLACK,
            button
        )

        font = pygame.font.Font(
            None,
            48
        )

        text = font.render(
            "Back",
            True,
            WHITE
        )

        self.screen.blit(
            text,
            (20, 15)
        )

        return button

    def draw(self):
        """Draw credits page."""
        scaled_image = pygame.transform.scale(
            self.credits_button_img,
            (
                int(
                    self.credits_button_img.get_width()
                    * 1.3
                ),
                int(
                    self.credits_button_img.get_height()
                    * 1.3
                )
            )
        )

        self.screen.blit(
            scaled_image,
            (
                self.screen.get_width() // 2
                - scaled_image.get_width() // 2,
                50
            )
        )

        font = pygame.font.Font(
            None,
            48
        )

        text = font.render(
            "Alex, Robbe, Ruben, Lars, Bjarne",
            True,
            BLACK
        )

        self.screen.blit(
            text,
            (
                self.screen.get_width() // 2
                - text.get_width() // 2,
                self.screen.get_height() // 2
            )
        )

        return self.draw_back_button()