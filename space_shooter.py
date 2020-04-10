# Imports
import arcade
import random

# Constants
SCALING = 2.0


# Refernece:
# https://realpython.com/arcade-python-game-framework/
# https://arcade.academy/examples/sprite_collect_coins_background.html
# classes
class SapceShooter(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # set up the empty sprite list
        self.enemies_list = arcade.SpriteList()
        self.clouds_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()

        # set the background color
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # set up the player
        self.player = arcade.Sprite("images/sprite1.png")
        self.player.center_y = self.height / 2
        self.player.left = 10
        self.all_sprites.append(self.player)

        self.background = arcade.load_texture("images/universe-wallpaper.png")

        # spawn a new enemy every 0.25 seconds
        arcade.schedule(self.add_enemy, 0.5)

    def on_draw(self):
        arcade.start_render()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)

        # Draw all sprites
        arcade.SpriteList.draw(self.all_sprites)

    def on_update(self, delta_time):
        # Update all sprites
        arcade.SpriteList.update(self.all_sprites)

    def add_enemy(self, delta_time: float):
        # first create the new enemy sprite
        enemy = arcade.Sprite("images/missle.png")

        # set its position to a random height and off screen right
        enemy.left = random.randint(self.width, self.width + 80)
        enemy.top = random.randint(10, self.height - 10)

        # Set its speed to a random speed heading left
        enemy.velocity = (random.randint(-15, -3), 0)

        self.enemies_list.append(enemy)
        self.all_sprites.append(enemy)


# Main code entry point
if __name__ == "__main__":
    app = SapceShooter(960, 600, "Space Shooter")
    arcade.run()
