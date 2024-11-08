//  Function to handle jumping (only if on the ground)
//  Player is now in the air
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    if (on_ground) {
        //  Only allow jumping if on the ground
        mySprite.vy = -120
        //  Jump upwards when 'A' is pressed
        on_ground = false
    }
    
})
/** Initialize global variables */
let on_ground = false
let score = 0
let mySprite : Sprite = null
//  Set background color to pink
scene.setBackgroundColor(3)
//  Create the player's sprite
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
//  Apply gravity to the sprite (so it falls back down after jumping)
mySprite.ay = 200
//  Player's gravity
//  Add controller movement for the sprite to move left and right
controller.moveSprite(mySprite, 100, 0)
//  Set the camera to follow the sprite
scene.cameraFollowSprite(mySprite)
//  Create the floor (platform) tilemap
tiles.setCurrentTilemap(tilemap`
    level8
`)
tiles.placeOnTile(mySprite, tiles.getTileLocation(0, 13))
//  Create the bomb sprite (enemy that causes game over)
let bomb = sprites.create(img`
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
//  Create the cake sprite (food to be collected)
let cake = sprites.create(assets.image`
    Cake Sprite
`, SpriteKind.Food)
//  Set cake and bomb initial positions at the top
cake.setPosition(randint(0, scene.screenWidth()), 0)
bomb.setPosition(randint(0, scene.screenWidth()), 0)
//  Apply gravity to the cake and bomb
cake.ay = 15
//  Cake falls faster
bomb.ay = 10
//  Bomb falls continuously with gravity
bomb.setFlag(SpriteFlag.GhostThroughWalls, true)
//  Initialize score
info.setScore(score)
//  Function to update falling objects (cake and bomb)
game.onUpdateInterval(500, function on_update_interval() {
    
    //  If the player catches the cake, increase the score
    if (mySprite.overlapsWith(cake)) {
        score += 1
        info.changeScoreBy(1)
        //  Reset the cake position after collection
        cake.setPosition(randint(0, scene.screenWidth()), 0)
    }
    
    //  If the player collides with the bomb, game over
    if (mySprite.overlapsWith(bomb)) {
        game.gameOver(false)
    }
    
    //  Check if the player is on the ground (to allow jumping)
    if (mySprite.y >= tiles.getTileLocation(0, 13).y) {
        //  Player touches the ground
        on_ground = true
        mySprite.vy = 0
        //  Stop downward velocity
        mySprite.y = tiles.getTileLocation(0, 13).y
    } else {
        //  If the player is in the air
        on_ground = false
    }
    
})
