# Function to handle jumping (only if on the ground)
# Player is now in the air

def on_a_pressed():
    global on_ground
    if on_ground:
        # Only allow jumping if on the ground
        mySprite.vy = -120
        # Jump upwards when 'A' is pressed
        on_ground = False
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

"""

Initialize global variables

"""
on_ground = False
score = 0
mySprite: Sprite = None
# Set background color to pink
scene.set_background_color(3)
# Create the player's sprite
mySprite = sprites.create(img("""
        . . . . . e e e e e . . . . . . 
            . . . . e e e e e e e . . . . . 
            . . . . e e e e e e e . . . . . 
            . . . . e e d d d e e . . . . . 
            . . . . . e f d f e . . . . . . 
            . . . . . . d 2 d . . . . . . . 
            . . . . . d . d . d . . . . . . 
            . . . . . d d d d d . . . . . . 
            . . . . . . d d d . . . . . . . 
            . . . . . . . d . . . . . . . . 
            . . . . . . d d d . . . . . . . 
            . . . . . . d . d . . . . . . . 
            . . . . . . d . d . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
# Apply gravity to the sprite (so it falls back down after jumping)
mySprite.ay = 200
# Player's gravity
# Add controller movement for the sprite to move left and right
controller.move_sprite(mySprite, 100, 0)
# Set the camera to follow the sprite
scene.camera_follow_sprite(mySprite)
# Create the floor (platform) tilemap
tiles.set_current_tilemap(tilemap("""
    level8
"""))
tiles.place_on_tile(mySprite, tiles.get_tile_location(0, 13))
# Create the bomb sprite (enemy that causes game over)
bomb = sprites.create(img("""
        . . . . . . . . . f f . 2 . 5 . 
            . . . . . . . . f . . f . 4 . 4 
            . . . . . . . . f . . . f . . 5 
            . . . . . f f f f f f f . f f . 
            . . . . . f f f f f f f 5 . . . 
            . . . . . f f f f f f f . 4 . 2 
            . . . . . f f f f f f f . . . . 
            . . . f f f f f f f f f f f . . 
            . . f f 1 f f f f f f f f f f . 
            . f f f f f f f f f f f f f f f 
            . f f 1 f f f f f f f f f f f f 
            . f f 1 f f f f f f f f f f f f 
            . f f 1 f f f f f f f f f f f f 
            . . f f f 1 f f f f f f f f f . 
            . . . f f f f f f f f f f f . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.enemy)
# Create the cake sprite (food to be collected)
cake = sprites.create(assets.image("""
    Cake Sprite
"""), SpriteKind.food)
# Set cake and bomb initial positions at the top
cake.set_position(randint(0, scene.screen_width()), 0)
bomb.set_position(randint(0, scene.screen_width()), 0)
# Apply gravity to the cake and bomb
cake.ay = 15
# Cake falls faster
bomb.ay = 10
# Bomb falls continuously with gravity
bomb.set_flag(SpriteFlag.GHOST_THROUGH_WALLS, True)
# Initialize score
info.set_score(score)
# Function to update falling objects (cake and bomb)

def on_update_interval():
    global score, on_ground
    # If the player catches the cake, increase the score
    if mySprite.overlaps_with(cake):
        score += 1
        info.change_score_by(1)
        # Reset the cake position after collection
        cake.set_position(randint(0, scene.screen_width()), 0)
    # If the player collides with the bomb, game over
    if mySprite.overlaps_with(bomb):
        game.game_over(False)
    # Check if the player is on the ground (to allow jumping)
    if mySprite.y >= tiles.get_tile_location(0, 13).y:
        # Player touches the ground
        on_ground = True
        mySprite.vy = 0
        # Stop downward velocity
        mySprite.y = tiles.get_tile_location(0, 13).y
    else:
        # If the player is in the air
        on_ground = False
game.on_update_interval(500, on_update_interval)
