# Game entrypoint.
$ config.developer = true

label start:
    # First, initialize story-progression variables.
    python:
        cooperation = 0
        rivalry = 0 

    # $ _game_menu_screen = "game_menu"
    # call A1_01
    # call A1_02
    call A1_03
    return
