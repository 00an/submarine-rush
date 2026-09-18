import pygame

from config.settings import (
    GREEN,
    RED,
    WHITE,
)


class SettingsMenu:
    """Handles the settings page."""

    def __init__(
        self,
        screen,
        settings_button_img
    ):
        self.screen = screen
        self.settings_button_img = settings_button_img

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
            (0, 0, 0),
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

    def draw(
        self,
        music_on,
        sound_on
    ):
        """Draw settings page."""
        scaled_image = pygame.transform.scale(
            self.settings_button_img,
            (
                int(
                    self.settings_button_img.get_width()
                    * 1.3
                ),
                int(
                    self.settings_button_img.get_height()
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

        music_button = pygame.Rect(
            self.screen.get_width() // 2 - 100,
            200,
            200,
            50
        )

        pygame.draw.rect(
            self.screen,
            GREEN if music_on else RED,
            music_button
        )

        music_text = font.render(
            "Music: ON"
            if music_on
            else "Music: OFF",
            True,
            WHITE
        )

        self.screen.blit(
            music_text,
            (
                music_button.x + 10,
                music_button.y + 10
            )
        )

        sound_button = pygame.Rect(
            self.screen.get_width() // 2 - 160,
            300,
            325,
            50
        )

        pygame.draw.rect(
            self.screen,
            GREEN if sound_on else RED,
            sound_button
        )

        sound_text = font.render(
            "Sound Effects: ON"
            if sound_on
            else "Sound Effects: OFF",
            True,
            WHITE
        )

        self.screen.blit(
            sound_text,
            (
                sound_button.x + 10,
                sound_button.y + 10
            )
        )

        back_button = self.draw_back_button()

        return (
            music_button,
            sound_button,
            back_button
        )