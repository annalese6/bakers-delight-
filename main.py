# define the action when the A button is PRESSED
# combine the vertical velocity function to the button 'A'
# apply a vertical velocity to the sprite to make it jump up and down

def on_a_pressed():
    mySprite.vy = -120
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

projectile: Sprite = None
mySprite: Sprite = None
# set background colour to pink
scene.set_background_color(3)
# create game sprite (human), and add features to move this sprite around
# sprite must use camelCase
# assign the sprite to the player kind
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
# create tile map for sprite to jump on to (different platform levels)
tiles.set_current_tilemap(tilemap("""
    level8
"""))
tiles.place_on_tile(mySprite, tiles.get_tile_location(0, 13))
# create gravity for the sprite, set acceleration in y axis direction
# set speed of acceleration to 200 downards
mySprite.ay = 200
# move sprite 100 pixels horizontally
controller.move_sprite(mySprite, 100, 0)
# make in game camera follow and focus on the sprite
scene.camera_follow_sprite(mySprite)
tiles.place_on_tile(projectile, tiles.get_tile_location(0, 0))

def on_update_interval():
    global projectile
    projectile = sprites.create(img("""
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
    projectile.set_position(randint(0, scene.screen_width()), scene.screen_height())
    projectile.set_velocity(0, 80)
game.on_update_interval(5000, on_update_interval)
