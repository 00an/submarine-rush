import pygame

from config.settings import (
    BLACK,
    WHITE,
)


class ControlsMenu:
    """Handles the controls page."""

    def __init__(
        self,
        screen,
        controls_button_img
    ):
        self.screen = screen
        self.controls_button_img = controls_button_img

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
        """Draw controls page."""
        scaled_image = pygame.transform.scale(
            self.controls_button_img,
            (
                int(
                    self.controls_button_img.get_width()
                    * 1.3
                ),
                int(
                    self.controls_button_img.get_height()
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

        controls = [
            "Arrow right: Move Right",
            "Arrow up: Move Up",
            "Arrow down: Move Down",
            "Arrow left: Move Left",
            "ESC: Pause Menu",
        ]

        y = (
            self.screen.get_height() // 2
            - 100
        )

        for line in controls:
            text = font.render(
                line,
                True,
                BLACK
            )

            self.screen.blit(
                text,
                (
                    self.screen.get_width() // 2
                    - text.get_width() // 2,
                    y
                )
            )

            y += 50

        return self.draw_back_button()