import pygame

from config.settings import (
    BLACK,
    GREEN,
    ORANGE,
    RED,
    WHITE,
)


class BoatMenu:
    """Handles the submarine selection menu."""

    def __init__(
        self,
        screen,
        boats_button_img
    ):
        self.screen = screen
        self.boats_button_img = boats_button_img

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

    def draw(self, boats):
        """Draw submarine selection menu."""
        scaled_image = pygame.transform.scale(
            self.boats_button_img,
            (
                int(
                    self.boats_button_img.get_width()
                    * 1.3
                ),
                int(
                    self.boats_button_img.get_height()
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

        back_button = self.draw_back_button()

        font = pygame.font.Font(
            None,
            36
        )

        for index, boat in enumerate(boats):
            y = 150 + index * 70

            name_box = pygame.Rect(
                self.screen.get_width() // 2 - 200,
                y,
                250,
                70
            )

            pygame.draw.rect(
                self.screen,
                BLACK,
                name_box
            )

            name_text = font.render(
                boat.name,
                True,
                WHITE
            )

            self.screen.blit(
                name_text,
                (
                    name_box.x + 10,
                    name_box.y + 10
                )
            )

            price_box = pygame.Rect(
                name_box.right + 10,
                y,
                150,
                50
            )

            pygame.draw.rect(
                self.screen,
                (
                    GREEN
                    if boat.owned
                    else RED
                ),
                price_box
            )

            price_text = (
                "Owned"
                if boat.owned
                else f"{boat.cost} Coins"
            )

            self.screen.blit(
                font.render(
                    price_text,
                    True,
                    WHITE
                ),
                (
                    price_box.x + 10,
                    price_box.y + 10
                )
            )

            if boat.owned:
                equip_width = (
                    130
                    if boat.equipped
                    else 100
                )

                equip_box = pygame.Rect(
                    price_box.right + 10,
                    y,
                    equip_width,
                    50
                )

                pygame.draw.rect(
                    self.screen,
                    (
                        GREEN
                        if boat.equipped
                        else ORANGE
                    ),
                    equip_box
                )

                equip_text = (
                    "Equipped"
                    if boat.equipped
                    else "Equip"
                )

                self.screen.blit(
                    font.render(
                        equip_text,
                        True,
                        WHITE
                    ),
                    (
                        equip_box.x + 10,
                        equip_box.y + 10
                    )
                )

        return back_button