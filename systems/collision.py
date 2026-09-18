from config.settings import (
    BOMB_DAMAGE,
    COIN_VALUE,
)


def check_collisions(game):
    """Handle collisions between the player and game objects."""
    player = game.player
    player_rect = player.get_rect()

    for coin in game.map.coins[:]:
        if player_rect.colliderect(
            coin["rect"]
        ):
            game.map.coins.remove(coin)

            player.current_coins += COIN_VALUE
            game.total_coins += COIN_VALUE

            game.audio.play_coin()

    for bomb in game.map.bombs[:]:
        if player_rect.colliderect(
            bomb["rect"]
        ):
            game.map.bombs.remove(bomb)

            player.hp -= BOMB_DAMAGE

            game.audio.play_bomb()