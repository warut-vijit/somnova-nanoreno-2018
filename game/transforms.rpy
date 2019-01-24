transform common(x = 0):
    subpixel True
    transform_anchor True
    xcenter 0.5
    yanchor 1.0
    ypos 1080
    on show:
        # This block is called when the image is first shown.
        alpha 0
        xoffset x
        linear 0.25 alpha 1
    on replaced:
        alpha 1
        linear 0.25 alpha 0
        ease 0.75 xoffset x

# This is so that characters don't blip out of existence.
transform transform_hide:
    on hide:
        linear 0.25 alpha 0

transform centered:
    common()

transform center_right:
    common(300)

transform center_left:
    common(-300)

transform embiggen:
    size (600, 1080)
    ease 1 size (600 * 1.1, 1080 * 1.1)

# =============
# UI Transforms
# =============

init -2:
    
    # Use a variable for universal animation speed
    define gui.animspeed = 0.75

    # Used for standard element dissolve in/old. Takes order argument for staggering the effect.
    transform mmfade(order):
        alpha 1.0
        on show:
            alpha 0.0
            pause (order * 0.1)
            ease gui.animspeed alpha 1.0
    
    # Same as above but with less difference between ordered elements (used on save/load)
    transform mmqfade(order):
        alpha 0.0
        pause (order * 0.05)
        ease gui.animspeed alpha 1.0

    # Same as mmfade but without the on show - this caused bugs with some elements
    transform mmsfade(order):
        alpha 0.0
        pause (order * 0.1)
        ease gui.animspeed alpha 1.0

    # Used for efficiently fading the screen to black where necessary - use with black.webp
    # TODO: Use a generate matte in future instead of an image.
    transform blackfade:
        alpha 0.0
        on show:
            alpha 1.0
            ease gui.animspeed alpha 0.0
    
    # Used to fade in the titles at the top of game menu screens
    transform menutitlefade:
        alpha 0.0
        ease gui.animspeed alpha 1.0
    
    # Used to give the game menu background a cool effect.
    # Takes child argument - this takes the special argument "child" so that the element to which the transform is applied can be used within the ImageDissolve.
    # TODO: Find a way to make more performant. Might remove completely in future.
    # NOTE: This is currently not used. Too slow.
    transform gmbgimdissolve(child):
        on show:
            Null(height=1080, width=1220)
            xpos 500
            child with ImageDissolve("images/fx/pixelcloud.png", gui.animspeed*2)

    # Used to crop in the divider 
    transform dividercrop:
        crop_relative True
        on hide:
            crop (0, 0, 1, 1) alpha 1.0
            ease gui.animspeed crop (0, 0, 0, 1) alpha 1.0
        on show:
            crop (0, 0, 0, 1) alpha 1.0
            ease gui.animspeed crop (0, 0, 1, 1) alpha 1.0
    
    # Used to fade and crop in the history screen
    transform historyfade:
        crop_relative True
        crop (0, 0, 1, 0) alpha 0.0
        ease gui.animspeed crop (0, 0, 1, 1) alpha 1.0

    # Used to fade in the notification ("Are you sure you want to quit?" etc.)
    transform notify_appear:
        on show:
            alpha 0
            linear .25 alpha 1.0
        on hide:
            linear .5 alpha 0.0