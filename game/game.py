import pygame

from config.assets import load_image
from config.settings import (
    BUTTON_SIZE,
    FPS,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    START_BUTTON_SIZE,
    WINDOW_TITLE,
)
from data.boats import boats
from entities.player import Player
from game.game_map import GameMap
from game.state import GameState
from systems.audio import AudioManager
from systems.collision import check_collisions
from ui.boat_menu import BoatMenu
from ui.controls_menu import ControlsMenu
from ui.credits_menu import CreditsMenu
from ui.hud import HUD
from ui.main_menu import MainMenu
from ui.pause_menu import PauseMenu
from ui.settings_menu import SettingsMenu


class BackgroundManager:
    """Handles all game backgrounds."""

    def __init__(self):
        self.main_original = load_image(
            "png",
            "background_main.png"
        )

        self.game_original = load_image(
            "png",
            "background_game.png"
        )

        self.spawn_original = load_image(
            "png",
            "background_spawn.png"
        )

        self.credits_original = load_image(
            "png",
            "background_credits.png"
        )

        self.controls_original = load_image(
            "png",
            "background_controls.png"
        )

        self.main = self.main_original
        self.game = self.game_original
        self.spawn = self.spawn_original
        self.credits = self.credits_original
        self.controls = self.controls_original

    def resize(
        self,
        width,
        height
    ):
        """Resize every background."""
        self.main = pygame.transform.scale(
            self.main_original,
            (width, height)
        )

        self.game = pygame.transform.scale(
            self.game_original,
            (width, height)
        )

        self.spawn = pygame.transform.scale(
            self.spawn_original,
            (width, height)
        )

        self.credits = pygame.transform.scale(
            self.credits_original,
            (width, height)
        )

        self.controls = pygame.transform.scale(
            self.controls_original,
            (width, height)
        )


class Game:
    """Main controller for Submarine Rush."""

    def __init__(self):
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT

        self.screen = pygame.display.set_mode(
            (
                self.screen_width,
                self.screen_height
            ),
            pygame.RESIZABLE
        )

        pygame.display.set_caption(
            WINDOW_TITLE
        )

        self.clock = pygame.time.Clock()
        self.running = True

        self.backgrounds = BackgroundManager()
        self.audio = AudioManager()

        self.coin_img = load_image(
            "png",
            "coin.png",
            (30, 30)
        )

        self.bomb_img = load_image(
            "png",
            "bomb.png",
            (50, 50)
        )

        self.title_img = load_image(
            "png",
            "title.png"
        )

        self.start_button_img = load_image(
            "png",
            "start.png",
            START_BUTTON_SIZE
        )

        self.boats_button_img = load_image(
            "png",
            "boat.png",
            BUTTON_SIZE
        )

        self.controls_button_img = load_image(
            "png",
            "controls.png",
            BUTTON_SIZE
        )

        self.credits_button_img = load_image(
            "png",
            "credits.png",
            BUTTON_SIZE
        )

        self.settings_button_img = load_image(
            "png",
            "settings.png",
            BUTTON_SIZE
        )

        self.backgrounds.resize(
            self.screen_width,
            self.screen_height
        )

        self.player = Player(
            self.screen_width,
            self.screen_height
        )

        self.map = GameMap(
            self.screen_width,
            self.screen_height,
            self.backgrounds
        )

        self.hud = HUD(
            self.screen,
            self.coin_img
        )

        self.main_menu = MainMenu(
            self.screen,
            self.title_img,
            self.coin_img,
            self.start_button_img,
            self.boats_button_img,
            self.controls_button_img,
            self.credits_button_img,
            self.settings_button_img
        )

        self.boat_menu = BoatMenu(
            self.screen,
            self.boats_button_img
        )

        self.controls_menu = ControlsMenu(
            self.screen,
            self.controls_button_img
        )

        self.credits_menu = CreditsMenu(
            self.screen,
            self.credits_button_img
        )

        self.settings_menu = SettingsMenu(
            self.screen,
            self.settings_button_img
        )

        self.pause_menu = PauseMenu(
            self.screen
        )

        self.camera_x = 0
        self.camera_y = 0

        self.in_menu = True
        self.paused = False

        self.current_screen = GameState.MAIN

        self.total_coins = 0
        self.highscore_coins = 0

        self.extreme_on = False

    def reset(self):
        """Reset the current run."""
        self.player = Player(
            self.screen_width,
            self.screen_height
        )

        self.map = GameMap(
            self.screen_width,
            self.screen_height,
            self.backgrounds
        )

        self.camera_x = 0
        self.camera_y = 0

    def start_game(self):
        """Start a new game."""
        self.reset()

        self.in_menu = False
        self.paused = False

    def return_to_menu(self):
        """Return to the main menu."""
        self.reset()

        self.in_menu = True
        self.paused = False
        self.current_screen = GameState.MAIN

    def equip_boat(self, index):
        """Equip an owned submarine."""
        if not boats[index].owned:
            return

        for boat in boats:
            boat.equipped = False

        boats[index].equipped = True

        self.player.update_boat()

    def handle_boat_click(
        self,
        mouse_pos
    ):
        """Handle submarine purchases and equipment."""
        for index, boat in enumerate(boats):
            y = 150 + index * 70

            name_box = pygame.Rect(
                self.screen_width // 2 - 200,
                y,
                250,
                70
            )

            price_box = pygame.Rect(
                name_box.right + 10,
                y,
                150,
                50
            )

            if (
                price_box.collidepoint(mouse_pos)
                and not boat.owned
            ):
                if self.total_coins >= boat.cost:
                    self.total_coins -= boat.cost
                    boat.owned = True

                return

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

                if equip_box.collidepoint(mouse_pos):
                    self.equip_boat(index)
                    return

    def handle_resize(self, event):
        """Handle window resizing."""
        self.screen_width = event.w
        self.screen_height = event.h

        self.screen = pygame.display.set_mode(
            (
                self.screen_width,
                self.screen_height
            ),
            pygame.RESIZABLE
        )

        self.backgrounds.resize(
            self.screen_width,
            self.screen_height
        )

        self.player.update_screen_size(
            self.screen_width,
            self.screen_height
        )

        self.map.update_screen_size(
            self.screen_width,
            self.screen_height
        )

        self.hud.screen = self.screen
        self.main_menu.screen = self.screen
        self.boat_menu.screen = self.screen
        self.controls_menu.screen = self.screen
        self.credits_menu.screen = self.screen
        self.settings_menu.screen = self.screen
        self.pause_menu.screen = self.screen

    def handle_keydown(self, event):
        """Handle keyboard input."""
        if event.key == pygame.K_ESCAPE:
            if not self.in_menu:
                self.paused = not self.paused

    def handle_mouse_click(
        self,
        mouse_pos
    ):
        """Handle mouse input."""
        if self.in_menu:
            self.handle_menu_click(
                mouse_pos
            )

        elif self.paused:
            self.handle_pause_click(
                mouse_pos
            )

    def handle_menu_click(
        self,
        mouse_pos
    ):
        """Handle menu interactions."""
        if self.current_screen == GameState.MAIN:
            buttons = self.main_menu.draw(self)

            if buttons["start"].collidepoint(mouse_pos):
                self.start_game()

            elif buttons["boats"].collidepoint(mouse_pos):
                self.current_screen = GameState.BOATS

            elif buttons["controls"].collidepoint(mouse_pos):
                self.current_screen = GameState.CONTROLS

            elif buttons["credits"].collidepoint(mouse_pos):
                self.current_screen = GameState.CREDITS

            elif buttons["extreme"].collidepoint(mouse_pos):
                self.extreme_on = not self.extreme_on

            elif buttons["settings"].collidepoint(mouse_pos):
                self.current_screen = GameState.SETTINGS

        elif self.current_screen == GameState.BOATS:
            back_button = self.boat_menu.draw(
                boats
            )

            if back_button.collidepoint(mouse_pos):
                self.current_screen = GameState.MAIN
            else:
                self.handle_boat_click(
                    mouse_pos
                )

        elif self.current_screen == GameState.CONTROLS:
            back_button = self.controls_menu.draw()

            if back_button.collidepoint(mouse_pos):
                self.current_screen = GameState.MAIN

        elif self.current_screen == GameState.CREDITS:
            back_button = self.credits_menu.draw()

            if back_button.collidepoint(mouse_pos):
                self.current_screen = GameState.MAIN

        elif self.current_screen == GameState.SETTINGS:
            (
                music_button,
                sound_button,
                back_button
            ) = self.settings_menu.draw(
                self.audio.music_on,
                self.audio.sound_on
            )

            if back_button.collidepoint(mouse_pos):
                self.current_screen = GameState.MAIN

            elif music_button.collidepoint(mouse_pos):
                self.audio.music_on = (
                    not self.audio.music_on
                )

            elif sound_button.collidepoint(mouse_pos):
                self.audio.sound_on = (
                    not self.audio.sound_on
                )

    def handle_pause_click(
        self,
        mouse_pos
    ):
        """Handle pause menu interactions."""
        buttons = self.pause_menu.draw()

        if buttons[0].collidepoint(mouse_pos):
            self.paused = False

        elif buttons[1].collidepoint(mouse_pos):
            self.return_to_menu()

        elif buttons[2].collidepoint(mouse_pos):
            self.running = False

    def update(self):
        """Update the active game."""
        if self.in_menu or self.paused:
            return

        keys = pygame.key.get_pressed()

        self.player.move(
            keys,
            self.extreme_on
        )

        self.camera_x = max(
            0,
            self.player.x
            - self.screen_width // 2
            + self.player.width // 2
        )

        self.camera_y = 0

        self.map.update(
            self.camera_x
        )

        check_collisions(self)

        if self.player.hp <= 0:
            if (
                self.player.current_coins
                > self.highscore_coins
            ):
                self.highscore_coins = (
                    self.player.current_coins
                )

            self.return_to_menu()

    def draw(self):
        """Draw the current game state."""
        if self.in_menu:

            if self.current_screen == GameState.MAIN:
                self.screen.blit(
                    self.backgrounds.main,
                    (0, 0)
                )

                self.main_menu.draw(self)

            elif self.current_screen == GameState.BOATS:
                self.screen.blit(
                    self.backgrounds.main,
                    (0, 0)
                )

                self.boat_menu.draw(
                    boats
                )

            elif self.current_screen == GameState.CONTROLS:
                self.screen.blit(
                    self.backgrounds.controls,
                    (0, 0)
                )

                self.controls_menu.draw()

            elif self.current_screen == GameState.CREDITS:
                self.screen.blit(
                    self.backgrounds.credits,
                    (0, 0)
                )

                self.credits_menu.draw()

            elif self.current_screen == GameState.SETTINGS:
                self.screen.blit(
                    self.backgrounds.main,
                    (0, 0)
                )

                self.settings_menu.draw(
                    self.audio.music_on,
                    self.audio.sound_on
                )

        elif self.paused:
            self.screen.blit(
                self.backgrounds.main,
                (0, 0)
            )

            self.pause_menu.draw()

        else:
            self.map.draw(
                self.screen,
                self.camera_x,
                self.camera_y
            )

            self.player.draw(
                self.screen,
                self.camera_x,
                self.camera_y
            )

            self.hud.draw_hp_bar(
                self.player.hp
            )

            self.hud.draw_stats(
                self.player.current_coins
            )

    def run(self):
        """Run the main game loop."""
        while self.running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.VIDEORESIZE:
                    self.handle_resize(event)

                elif event.type == pygame.KEYDOWN:
                    self.handle_keydown(event)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.handle_mouse_click(
                            event.pos
                        )

            self.audio.update_music()

            self.update()
            self.draw()

            pygame.display.flip()

            self.clock.tick(FPS)