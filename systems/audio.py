import pygame

from config.assets import asset_path


class AudioManager:
    """Handles background music and sound effects."""

    def __init__(self):
        pygame.mixer.init()

        self.music_on = True
        self.sound_on = True

        self.coin_sound = pygame.mixer.Sound(
            asset_path(
                "mp3",
                "coin_sound.mp3"
            )
        )

        self.bomb_sound = pygame.mixer.Sound(
            asset_path(
                "mp3",
                "bomb_sound.mp3"
            )
        )

        self.background_music = asset_path(
            "mp3",
            "background_music.mp3"
        )

        self.play_music()

    def play_music(self):
        """Start looping background music."""
        if not self.music_on:
            return

        pygame.mixer.music.load(
            self.background_music
        )

        pygame.mixer.music.play(-1)

    def update_music(self):
        """Keep music state synchronized with the setting."""
        if self.music_on:
            if not pygame.mixer.music.get_busy():
                self.play_music()
        else:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()

    def stop_music(self):
        """Stop background music."""
        pygame.mixer.music.stop()

    def play_coin(self):
        """Play the coin collection sound."""
        if self.sound_on:
            self.coin_sound.play()

    def play_bomb(self):
        """Play the bomb collision sound."""
        if self.sound_on:
            self.bomb_sound.play()