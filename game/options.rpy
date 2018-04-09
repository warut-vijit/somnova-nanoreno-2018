##########################################
##----------------BASICS----------------##
##########################################

# The _() marks the string as translatable, should we want that in the future.
define config.name = _("Arcadia")

define config.version = "1.1.0"

# Text that is placed on the game's about screen. To insert a blank line
# between paragraphs, write \n\n.
define gui.about = _("")

define build.name = "Arcadia"

##########################################
##----------------AUDIO-----------------##
##########################################

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

##########################################
##-------------TRANSITIONS--------------##
##########################################

# Entering or exiting the game menu.
define config.enter_transition = dissolve
define config.exit_transition = dissolve

# A transition that is used after a game has been loaded.
define config.after_load_transition = dissolve

# Used when entering the main menu after the game has ended.
define config.end_game_transition = dissolve

##########################################
##-----------DIALOGUE WINDOW------------##
##########################################

# show: always show
# hide: hide unless there's dialogue
# auto: hidden before scene statement, shown with dialogue
define config.window = "hide"

# Transitions.
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

define config.rollback_enabled = False

##########################################
##---------DEFAULT PREFERENCES----------##
##########################################

# How many characters to display per second. 0 = instantaneous display
default preferences.text_cps = 24

# How long to wait until auto-forward advances (in seconds).
default preferences.afm_time = 15

##########################################
##------------SAVE DIRECTORY------------##
##########################################

# Windows: %APPDATA\RenPy\<config.save_directory>
# Macintosh: $HOME/Library/RenPy/<config.save_directory>
# Linux: $HOME/.renpy/<config.save_directory>

# This probably should't be changed.
define config.save_directory = "arcadia-218-1519786094"

##########################################
##-----------------ICON-----------------##
##########################################

#define config.window_icon = "images/emblem_icon.png"
# This icon should be used for non-final builds.
define config.window_icon = "images/emblem_icon.png"

##########################################
##--------BUILDING/DISTRIBUTION---------##
##########################################

init python:
    # Glob patterns, case insensitive.
    # / - directory separator
    # * - all characters, except directory separator
    # ** - all characters, including directory separator

    # Classifying as None means files will be excluded from the build.
    # Classifying as "archive" means files will be archived. Huh.
    build.classify("**~", None)
    build.classify("**.bak", None)
    build.classify("**/.**", None)
    build.classify("**/#**", None)
    build.classify("**/thumbs.db", None)

    build.documentation('*.html')
    build.documentation('*.txt')
    
    # If we intend to upload this to itch.io, we can set the project name here.
    # build.itch_project = "renpytom/test-project"
    
    def replace_text(s):
        # This is the em dash. —
        s = s.replace('--', u'\u2014')
        # This is the ellipsis.
        s = s.replace('...', u'\u2026')
        return s
    config.replace_text = replace_text