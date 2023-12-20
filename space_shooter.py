# Imports
import arcade
import random

# Constants
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 800
SCREEN_TITLE = "SpaceShooter"
SCALING = 2.0


# Refernece:
# https://realpython.com/arcade-python-game-framework/
# https://arcade.academy/examples/sprite_collect_coins_background.html
# classes
class SapceShooter(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Our Scene Object
        self.scene = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Background image will be stored in this variable
        self.background = None
        # self.background = arcade.load_texture("images/universe-wallpaper.png")
        # self.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")
        # set the background color
        arcade.set_background_color(arcade.color.SKY_BLUE)
    
    def setup(self):
        # Initialize Scene
        self.scene = arcade.Scene()

        # Create the Sprite lists
        self.scene.add_sprite_list("Player")

        # Create the Sprite lists
        self.scene.add_sprite_list("Enemies")

        # set up the player
        self.player_sprite = arcade.Sprite("images/sprite1.png")
        # self.player_sprite.center_y = SCREEN_HEIGHT / 2
        # self.player_sprite.left = 10
        self.player_sprite.left = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 80)
        self.player_sprite.top = random.randint(10, SCREEN_HEIGHT - 10)
        self.player_sprite.velocity = (random.randint(-15, -3), 0)
        self.scene.add_sprite("Player", self.player_sprite)

        # # first create the new enemy sprite
        # enemy = arcade.Sprite("images/missle.png")
        # # set its position to a random height and off screen right
        # enemy.left = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 80)
        # enemy.top = random.randint(10, SCREEN_HEIGHT - 10)

        # # Set its speed to a random speed heading left
        # enemy.velocity = (random.randint(-15, -3), 0)
        # self.scene.add_sprite("Enemies", enemy)

        # spawn a new enemy every 0.25 seconds
        # arcade.schedule(self.add_enemy, 0.5)

    def on_draw(self):
        # Clear the screen to the background color
        self.clear()

        # Draw the background texture
        # arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # Draw our Scene
        self.scene.draw()

    def on_update(self):
        # Draw our Scene
        self.

    def add_enemy(self, delta_time: float):
        # first create the new enemy sprite
        enemy = arcade.Sprite("images/missle.png")
        # set its position to a random height and off screen right
        enemy.left = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 80)
        enemy.top = random.randint(10, SCREEN_HEIGHT - 10)

        # Set its speed to a random speed heading left
        enemy.velocity = (random.randint(-15, -3), 0)
        self.scene.add_sprite("Enemies", enemy)


def main():
    """Main function"""
    window = SapceShooter()
    window.setup()
    arcade.run()

# Main code entry point
if __name__ == "__main__":
    main()
