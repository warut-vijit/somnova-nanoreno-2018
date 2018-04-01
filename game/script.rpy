# Game entrypoint.
$ config.developer = True

label start:
    # First, initialize story-progression variables. There's no real reason to do this, but it's
    # cool and good.
    python:
        cooperation = 0
        rivalry = 0 

    # $ _game_menu_screen = "game_menu"
    if config.developer:
        $ renpy.watch("cooperation")
        $ renpy.watch("rivalry")

    call A1_01
    call A1_02
    # call A1_03
    return
