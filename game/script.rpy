# Game entrypoint.
$ config.developer = True

label start:
    # First, initialize story-progression variables. There's no real reason to do this, but it's
    # cool and good.
    python:
        cooperation = 0
        rivalry = 0 

        scene_5_rivalry = True
        scene_5_cooperation = True

    if config.developer:
        $ renpy.watch("cooperation")
        $ renpy.watch("rivalry")
        $ renpy.watch("scene_5_rivalry")
        $ renpy.watch("scene_5_cooperation")
        $ renpy.watch("current_music")
        $ renpy.watch("queued_music")
        $ renpy.watch("renpy.music.get_pos(channel = 'dynamic_1')")
        $ renpy.watch("renpy.music.get_pos(channel = 'dynamic_2')")

    call A1_01
    call A1_02
    call A1_03
    call A1_04
    call A1_05

    # No scene 6 because 6 is an unlucky number in Javanese.
    # I made that up, but that's okay.
    
    if cooperation > rivalry:
        call A1_07c
        call A1_08c
        call A1_09c
    else:
        call A1_07r
        call A1_08r
        call A1_09r

    return
