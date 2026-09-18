import pygame

from config.settings import (
    BUTTON_SIZE,
    GREEN,
    RED,
    PURPLE,
    START_BUTTON_SIZE,
    WHITE,
)


class MainMenu:
    """Handles the main menu."""

    def __init__(
        self,
        screen,
        title_img,
        coin_img,
        start_button_img,
        boats_button_img,
        controls_button_img,
        credits_button_img,
        settings_button_img
    ):
        self.screen = screen

        self.title_img = title_img
        self.coin_img = coin_img

        self.start_button_img = start_button_img
        self.boats_button_img = boats_button_img
        self.controls_button_img = controls_button_img
        self.credits_button_img = credits_button_img
        self.settings_button_img = settings_button_img

    def draw(self, game):
        """Draw main menu and return button rectangles."""
        width = game.screen_width
        height = game.screen_height

        title_width = int(
            self.title_img.get_width() * 0.30
        )

        title_height = int(
            self.title_img.get_height() * 0.22
        )

        scaled_title = pygame.transform.scale(
            self.title_img,
            (
                title_width,
                title_height
            )
        )

        self.screen.blit(
            scaled_title,
            (
                width // 2
                - scaled_title.get_width() // 2
                + 22,
                45
            )
        )

        font_coin = pygame.font.Font(
            None,
            36
        )

        coin_text = font_coin.render(
            str(game.total_coins),
            True,
            PURPLE
        )

        coin_x = (
            width
            - self.coin_img.get_width()
            - 77
        )

        text_x = (
            coin_x
            + self.coin_img.get_width()
            + 10
        )

        self.screen.blit(
            self.coin_img,
            (coin_x, 11)
        )

        self.screen.blit(
            coin_text,
            (text_x, 15)
        )

        highscore_font = pygame.font.Font(
            None,
            36
        )

        highscore_text = highscore_font.render(
            f"Highscore: {game.highscore_coins}",
            True,
            RED
        )

        self.screen.blit(
            highscore_text,
            (
                (
                    width
                    - highscore_text.get_width()
                ) // 2,
                15
            )
        )

        start_button = pygame.Rect(
            width * 0.5
            - START_BUTTON_SIZE[0] * 0.5,
            height * 0.29,
            *START_BUTTON_SIZE
        )

        boats_button = pygame.Rect(
            width * 0.5
            - BUTTON_SIZE[0] * 0.5,
            height * 0.47,
            *BUTTON_SIZE
        )

        controls_button = pygame.Rect(
            width * 0.5
            - BUTTON_SIZE[0] * 0.5,
            height * 0.61,
            *BUTTON_SIZE
        )

        credits_button = pygame.Rect(
            20,
            height - BUTTON_SIZE[1] - 20,
            *BUTTON_SIZE
        )

        settings_button = pygame.Rect(
            width - BUTTON_SIZE[0] - 20,
            height - BUTTON_SIZE[1] - 20,
            *BUTTON_SIZE
        )

        font_large = pygame.font.Font(
            None,
            48
        )

        extreme_text = font_large.render(
            (
                "Extreme: ON"
                if game.extreme_on
                else "Extreme: OFF"
            ),
            True,
            WHITE
        )

        extreme_button = pygame.Rect(
            width // 2
            - (
                extreme_text.get_width()
                + 20
            ) // 2,
            height * 0.77,
            extreme_text.get_width() + 20,
            extreme_text.get_height() + 20
        )

        pygame.draw.rect(
            self.screen,
            (
                GREEN
                if game.extreme_on
                else RED
            ),
            extreme_button
        )

        self.screen.blit(
            extreme_text,
            (
                extreme_button.x + 10,
                extreme_button.y + 10
            )
        )

        self.screen.blit(
            self.start_button_img,
            start_button.topleft
        )

        self.screen.blit(
            self.boats_button_img,
            boats_button.topleft
        )

        self.screen.blit(
            self.controls_button_img,
            controls_button.topleft
        )

        self.screen.blit(
            self.credits_button_img,
            credits_button.topleft
        )

        self.screen.blit(
            self.settings_button_img,
            settings_button.topleft
        )

        return {
            "start": start_button,
            "boats": boats_button,
            "controls": controls_button,
            "credits": credits_button,
            "extreme": extreme_button,
            "settings": settings_button,
        }