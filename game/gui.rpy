##########################################
##-----------INIITIALIZATION------------##
##########################################

init offset = -2

init python:
    gui.init(1920, 1080)

    def save_time(save):
        save["playtime"] = renpy.get_game_runtime()

    config.save_json_callbacks = [save_time]
    config.main_menu_music = music_one.file_names[0]

##########################################
##----------------COLORS----------------##
##########################################

define gui.box_background_color = "#0000004C" # Black (30% opacity)
define gui.text_color = "#fff" # White
define gui.empty_text_color = "#ffffff80" # White (50% opacity)
define gui.inactive_text_color = "#fff3" # White (20% opacity)
define gui.active_text_color = "#59ff9b"
define gui.border_edge = "#fff" # White
define gui.border_center = "#fff3" # White (20% opacity)
define gui.confirm_text_color = "#ffffff4c" # White (30% opacity)
define gui.confirm_background = "#00000080" # Black (50% opacity)
define gui.confirm_button_background = "#000000B2" # Black (70% opacity)
define gui.scrollbar_color = "#fff" # White
define gui.scrollbar_color_idle = "#ffffff4c" # White (30% opacity)

##########################################
##--------------FILE SLOTS--------------##
##########################################

define config.thumbnail_width = 120
define config.thumbnail_height = 68

##########################################
##--------SCROLLBARS AND SLIDERS--------##
##########################################

# What to do with unscrollable scrollbars in the gui. "hide" hides them, while None shows them.
define gui.unscrollable = "hide"

##########################################
##----------------HISTORY---------------##
##########################################

# The number of blocks of dialogue history Ren'Py will keep.
define config.history_length = 250

##########################################
##---------------SPLASH-----------------##
##########################################

image logo = "gui/logo.png"
image splash_movie = Movie(play = "gui/intro.webm")

label splashscreen:
    show bg_black
    show splash_movie at splash_movie with Pause(6)
    hide splash_movie
    show logo at splash_centered with Pause(4)
    return

transform splash_movie:
    alpha 1.0
    on show:
        linear 5 alpha 1.0
        linear 1 alpha 0.0

transform splash_centered:
    xcenter 0.5
    ycenter 0.5
    alpha 0.0
    on show:
        linear 1 alpha 1.0
        linear 2 alpha 1.0
        linear 1 alpha 0.0
