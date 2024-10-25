// define the action when the A button is PRESSED
// combine the vertical velocity function to the button 'A'
// apply a vertical velocity to the sprite to make it jump up and down
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.vy = -120
})
let projectile: Sprite = null
let mySprite: Sprite = null
// set background colour to pink
scene.setBackgroundColor(3)
// create game sprite (human), and add features to move this sprite around
// sprite must use camelCase
// assign the sprite to the player kind
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
// create tile map for sprite to jump on to (different platform levels)
tiles.setCurrentTilemap(tilemap`level8`)
tiles.placeOnTile(mySprite, tiles.getTileLocation(0, 13))
// create gravity for the sprite, set acceleration in y axis direction
// set speed of acceleration to 200 downards
mySprite.ay = 200
// move sprite 100 pixels horizontally
controller.moveSprite(mySprite, 100, 0)
// make in game camera follow and focus on the sprite
scene.cameraFollowSprite(mySprite)
tiles.placeOnTile(projectile, tiles.getTileLocation(0, 0))
game.onUpdateInterval(5000, function () {
    projectile = sprites.create(img`
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
        `, SpriteKind.Enemy)
    projectile.setPosition(randint(0, scene.screenWidth()), scene.screenHeight())
    projectile.setVelocity(0, 80)
})
