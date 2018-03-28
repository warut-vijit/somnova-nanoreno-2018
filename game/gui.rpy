##########################################
##-----------INIITIALIZATION------------##
##########################################

init offset = -2

init python:
    gui.init(1920, 1080)

##########################################
##----------------COLORS----------------##
##########################################

# An accent color used throughout the interface to label and highlight text.
define gui.accent_color = '#ccc'

# The color used for a text button when it is neither selected nor hovered.
define gui.idle_color = '#555555'

# The small color is used for small text, which needs to be stronger to achieve the same effect.
define gui.idle_small_color = '#aaaaaa'

# The color that is used for buttons and bars that are hovered.
define gui.hover_color = '#fff'

# The color used for a text button when it is selected but not focused. A button is selected if it
# is the current screen or preference value.
define gui.selected_color = '#ffffff'

# The color used for a text button when it cannot be selected.
define gui.insensitive_color = '#666'

# Colors used for the portions of bars that are not filled in. These are not used directly, but
# are used when re-generating bar image files.
define gui.muted_color = '#888'
define gui.hover_muted_color = '#aaa'

# The colors used for dialogue and menu choice text.
define gui.text_color = '#fff'
define gui.interface_text_color = '#fff'

##########################################
##----------------FONTS-----------------##
##########################################

# The font used for in-game text.
define gui.text_font = "fonts/Lato-Light.ttf"

# The font used for character names.
define gui.name_text_font = "fonts/Lato-Light.ttf"

# The font used for out-of-game text.
define gui.interface_text_font = "fonts/Lato-Light.ttf"

# The size of normal dialogue text.
define gui.text_size = 22

# The size of character names.
define gui.name_text_size = 30

# The size of text in the game's user interface.
define gui.interface_text_size = 30

# The size of labels in the game's user interface.
define gui.label_text_size = 30

# The size of text on the notify screen.
define gui.notify_text_size = 16

##########################################
##----------------BUTTONS---------------##
##########################################

# The width and height of a button, in pixels. If None, Ren'Py computes a size.
define gui.button_width = None
define gui.button_height = 36

# The borders on each side of the button. (left, top, right, bottom)
define gui.button_borders = Borders(4, 4, 4, 4)

# If True, the background image will be tiled. If False, the background image will be linearly
# scaled.
define gui.button_tile = False

# The font used by the button.
define gui.button_text_font = gui.interface_text_font

# The size of the text used by the button.
define gui.button_text_size = gui.interface_text_size

# The color of button text in various states.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

# The horizontal alignment of the button text. (0.0 is left, 0.5 is center, 1.0 is right).
define gui.button_text_xalign = 0.0

##########################################
##-----------BUTTONS OVERRIDES----------##
##########################################

define gui.radio_button_borders = Borders(25, 4, 4, 4)

define gui.check_button_borders = Borders(25, 4, 4, 4)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(10, 4, 10, 4)

define gui.quick_button_borders = Borders(10, 4, 10, 0)
define gui.quick_button_text_size = 14
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

##########################################
##--------IN-GAME CHOICE BUTTONS--------##
##########################################

define gui.choice_button_width = 500
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(10, 5, 10, 5)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#cccccc"
define gui.choice_button_text_hover_color = "#ffffff"

##########################################
##----------FILE SAVE BUTTONS-----------##
##########################################

# The save slot button.
define gui.slot_button_width = 276
define gui.slot_button_height = 206
define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 14
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color

# The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 256
define config.thumbnail_height = 144

# The number of columns and rows in the grid of save slots.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2

##########################################
##-------------POSITIONING--------------##
##########################################

# The vertical position of the skip indicator.
define gui.skip_ypos = 10

# The vertical position of the notify screen.
define gui.notify_ypos = 45

# The spacing between menu choices.
define gui.choice_spacing = 22

# Controls the amount of spacing between preferences.
define gui.pref_spacing = 10

# Controls the amount of spacing between preference buttons.
define gui.pref_button_spacing = 0

# The spacing between file page buttons.
define gui.page_spacing = 0

# The spacing between file slots.
define gui.slot_spacing = 10

##########################################
##----------------FRAMES----------------##
##########################################

# Generic frames that are introduced by player code.
define gui.frame_borders = Borders(4, 4, 4, 4)

# The frame that is used as part of the confirm screen.
define gui.confirm_frame_borders = Borders(40, 40, 40, 40)

# The frame that is used as part of the skip screen.
define gui.skip_frame_borders = Borders(16, 5, 50, 5)

# The frame that is used as part of the notify screen.
define gui.notify_frame_borders = Borders(16, 5, 40, 5)

# Should frame backgrounds be tiled?
define gui.frame_tile = False

##########################################
##--------SCROLLBARS AND SLIDERS--------##
##########################################

# The height of horizontal bars, scrollbars, and sliders. The width of vertical bars, scrollbars,
# and sliders.
define gui.bar_size = 36
define gui.scrollbar_size = 12
define gui.slider_size = 30

# True if bar images should be tiled. False if they should be linearly scaled.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

# Horizontal borders.
define gui.bar_borders = Borders(4, 4, 4, 4)
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(4, 4, 4, 4)

# Vertical borders.
define gui.vbar_borders = Borders(4, 4, 4, 4)
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define gui.vslider_borders = Borders(4, 4, 4, 4)

# What to do with unscrollable scrollbars in the gui. "hide" hides them, while None shows them.
define gui.unscrollable = "hide"

##########################################
##----------------HISTORY---------------##
##########################################

# The number of blocks of dialogue history Ren'Py will keep.
define config.history_length = 250

# The height of a history screen entry, or None to make the height variable at the cost of
# performance.
define gui.history_height = 140

# The position, width, and alignment of the label giving the name of the speaking character.
define gui.history_name_xpos = 150
define gui.history_name_ypos = 0
define gui.history_name_width = 150
define gui.history_name_xalign = 1.0

# The position, width, and alignment of the dialogue text.
define gui.history_text_xpos = 170
define gui.history_text_ypos = 5
define gui.history_text_width = 740
define gui.history_text_xalign = 0.0

##########################################
##-------------LOCALIZATION-------------##
##########################################

# This controls where a line break is permitted. The default is suitable for most languages. A
# list of available values can be found here:
# https://www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"