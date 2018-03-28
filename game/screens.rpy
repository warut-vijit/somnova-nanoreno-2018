init offset = -1

##########################################
##----------------STYLES----------------##
##########################################

style default:
    color "#fff"
    font "fonts/Abel-Regular.ttf"
    language "western"

##########################################
##-----------------SAY------------------##
##########################################

# Reference: https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        yanchor 1.0
        pos (460, -80)
        xysize (1260, 160)
        yoffset 1080
        background Solid("#0005") # TODO
        add Solid("#fff", xpos = 1260, xysize = (1, 160))
        
        text what id "what":
            xpos 37
            ypos 10
            xsize 1175
            line_spacing 4
            size 31

    #if who is not None:
    window:
        yanchor 1.0
        pos (199, -180)
        xysize (241, 60)
        yoffset 1080
        background Solid("#0005") # TODO
        add Solid("#fff", xpos = 0, xysize = (1, 60))

        text who + ":" id "who":
            size 36
            xpos 19
            yalign 0.5

##########################################
##---------SIMULTANEOUS DIALOGUE--------##
##########################################

# TODO: Design and implement.
style block1_multiple2_say_window:
    xalign 0.0

style block2_multiple2_say_window:
    xalign 1.0

##########################################
##---------------CHOICES----------------##
##########################################

# Reference: http://www.renpy.org/doc/html/screen_special.html#choice

define config.narrator_menu = True

screen choice(items):
    style_prefix "choice"
    hbox:
        for i in items:
            textbutton i.caption action i.action

style choice_hbox is hbox
style choice_button is button
style choice_button_text is button_text

style choice_hbox:
    xalign 0.5
    ycenter 0.5
    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    ycenter 0.5

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")

##########################################
##--------------QUICK MENU--------------##
##########################################

screen quick_menu():
    # The quick menu lords over other puny screens.
    zorder 100
    frame:
        background LiveTile("gui/quick_menu_bar.png")
        ysize 80
        xfill True
        yanchor 1.0
        yoffset 1080

    hbox:
        style_prefix "quick_left"
        textbutton _("AUTO") action Preference("auto-forward", "toggle")
        textbutton _("SKIP") action Skip() alternate Skip(fast = True, confirm = True)
        textbutton _("MUTE") action Preference("all mute", "toggle")
        textbutton _("HISTORY") action ShowMenu("history")
        
    hbox:
        style_prefix "quick_right"
        textbutton _("MENU") action ShowMenu("options")
        textbutton _("LOAD") action ShowMenu("load")
        textbutton _("SAVE") action ShowMenu("save")

init python:
    config.overlay_screens.append("quick_menu")

style quick_hbox:
    yanchor 1.0
    ypos -20
    yoffset 1080
    spacing 20

style quick_left_hbox is quick_hbox
style quick_left_hbox:
    xoffset 200
    xalign 0.0

style quick_right_hbox is quick_hbox
style quick_right_hbox:
    xoffset -200
    xalign 1.0
    box_reverse True

style quick_button:
    xysize (60, 40)

style quick_left_button is quick_button
style quick_right_button is quick_button

style quick_left_button:
    background Solid("#fff6", xysize = (3, 3), ypos = 37)

style quick_right_button:
    background Solid("#fff6", xysize = (3, 3), pos = (57, 37))

style quick_button_text:
    size 20
    color "#fff6"
    ycenter 0.5

style quick_left_button_text is quick_button_text
style quick_right_button_text is quick_button_text
style quick_right_button_text:
    xalign 1.0

##########################################
##-------------NAVIVGATION--------------##
##########################################

# Navigation is used in both the main (title) menu and on the in-game menu screen.
screen navigation():
    style_prefix "navigation"
    frame:
        xpos 200
        xsize 280
        background Solid("#0006") # TODO: Transparency?

        label _("MENU"):
            text_ycenter 0.73 # This aligns the text to the bottom of the container. Ack.
            text_size 90
            xcenter 0.5
            yanchor 1.0
            ypos 180
        
        vbox:
            yoffset 340
            spacing 20

            if main_menu:
                textbutton _("NEW GAME") action Start()
            else:
                textbutton _("HISTORY") action ShowMenu("history")
                textbutton _("SAVE GAME") action ShowMenu("save")
            
            textbutton _("LOAD GAME") action ShowMenu("load")
            textbutton _("OPTIONS") action ShowMenu("options")

            if not main_menu:
                textbutton _("MAIN MENU") action MainMenu()

            textbutton _("EXTRAS") action ShowMenu("extras")

            textbutton _("QUIT") action Quit(confirm = not main_menu)

style navigation_button:
    xysize (280, 60)
    hover_background Frame("gui/main_menu_button.png", 2, 2, tile = True)
    selected_background Frame("gui/main_menu_button.png", 2, 2, tile = True)
    
style navigation_button_text:
    font "fonts/Lato-Light.ttf"
    xcenter 0.5
    ycenter 0.5
    size 30

##########################################
##--------------MAIN MENU---------------##
##########################################
# Reference: http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    tag menu # This ensures that any other menu screen is replaced.
    style_prefix "main_menu"
    add "gui/main_menu.png" # TODO

    frame:
        pass

    use navigation # This pulls all the navigation code and includes it here.

##########################################
##--------------GAME MENU---------------##
##########################################

# This includes a bunch of different menu types.
screen game_menu(title):
    style_prefix "game_menu"

    if main_menu:
        add "gui/main_menu.png" # TODO
    
    frame:
        xpadding 80
        xpos 500
        xsize 1220
        yfill True
        background Solid("#0006") # TODO

        label title:
            text_ycenter 0.73 # Align to bottom. Ack.
            text_size 90
            text_first_indent -8 # Align to left. Ack.
            yanchor 1.0
            ypos 180
        frame: # Top divider.
            background Frame("gui/divider.png", 2, 0, tile = True)
            yoffset 200
            ysize 2
        frame: # Bottom divider.
            background Frame("gui/divider.png", 2, 0, tile = True)
            xfill True
            add Solid("#fff", xsize = 88)
            yoffset 858
            ysize 2
        textbutton _("BACK"):
            text_size 45
            text_ycenter 0.29 # Align to top. Ack.
            text_first_indent -6 # Align to left. Ack.
            yoffset 880
            action Return()
        frame:
            yoffset 200
            ysize 660
            transclude # Include whatever content is necessary.

    use navigation
    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

##########################################
##-----------LOAD/SAVE SCREEN-----------##
##########################################
# Reference: www.renpy.org/doc/html/screen_special.html#load

screen save():
    tag menu
    use file_slots(_("Save"))

screen load():
    tag menu
    use file_slots(_("Load"))


screen file_slots():
    default page_name_value = FilePageNameInputValue(pattern = _("Page {}"), auto = _("Automatic saves"), quick = _("Quick saves"))
    use game_menu():
        fixed:
            # This ensures the input will get the enter event before any of the buttons do.
            order_reverse True
            # The page name, which can be edited by clicking on a button.
            button:
                style "page_label"
                key_events True
                xalign 0.5
                action page_name_value.Toggle()
                input:
                    style "page_label_text"
                    value page_name_value

            # The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        has vbox
                        add FileScreenshot(slot) xalign 0.5
                        text FileTime(slot, format = _("{#file_time}%A, %B %d %Y, %H:%M"), empty = _("empty slot")):
                            style "slot_time_text"
                        text FileSaveName(slot):
                            style "slot_name_text"
                        key "save_delete" action FileDelete(slot)

            # Buttons to access other pages.
            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0
                spacing gui.page_spacing
                textbutton _("<") action FilePagePrevious()

                # 1 (inclusive) to 10 (exclusive).
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")

##########################################
##---------------OPTIONS----------------##
##########################################
# Reference: https://www.renpy.org/doc/html/screen_special.html#preferences

screen options():
    tag menu
    style_prefix "options"
    use game_menu(_("OPTIONS")):
        $ position_offset = 21 + 10
        hbox:
            ypos 130 - position_offset
            label _("Display")
            textbutton _("FULLSCREEN") action Preference("display", "fullscreen")
            textbutton _("WINDOWED") action Preference("display", "window")
        hbox:
            ypos 190 - position_offset
            label _("Skip unseen text")
            textbutton _("ON") action Preference("skip", "all")
            textbutton _("OFF") action Preference("skip", "seen")
        hbox:
            ypos 250 - position_offset
            label _("Skip after choices")
            textbutton _("ON") action Preference("after choices", "skip")
            textbutton _("OFF") action Preference("after choices", "stop")
        hbox:
            ypos 360 - position_offset
            label _("Text Speed")
            bar value Preference("text speed")
        hbox:
            ypos 420 - position_offset
            label _("Auto-Forward Time")
            bar value Preference("auto-forward time")
        hbox:
            ypos 480 - position_offset
            label _("Music Volume")
            bar value Preference("music volume")
        hbox:
            ypos 540 - position_offset
            label _("SFX Volume")
            bar value Preference("sound volume")
        frame:
            yanchor 0.5
            offset (810, 499)
            xysize (12, 80)
            background "gui/mute_frame.png"
            textbutton _("MUTE") action Preference("all mute", "toggle"):
                style "mute_all_button"

style options_label:
    xysize (380, 40)
    right_padding 20
    
style options_label_text:
    font "fonts/Lato-Light.ttf"
    size 30
    xalign 1.0

style options_button:
    xysize (180, 40)
    background Frame("gui/options_button.png", 2, 2, tile = True)

style options_button_text:
    xcenter 0.5
    ycenter 0.5
    color "#898885"
    selected_color "#59ff9b"
    size 20

style options_slider:
    left_bar Frame("gui/bar_left.png", 2, 2, tile = True)
    right_bar Frame("gui/bar_right.png", 2, 2, tile = True)
    left_gutter 2
    right_gutter 2
    yalign 0.5
    xysize (380, 20)

style mute_all_button:
    size 8
    ycenter 0.5
    xoffset 10

style options_hbox:
    spacing 20

##########################################
##----------------HISTORY---------------##
##########################################
# Reference https://www.renpy.org/doc/html/history.html

screen history():
    tag menu

    # Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll = ("vpgrid" if gui.history_height else "viewport")):
        style_prefix "history"
        for h in _history_list:
            window:
                # This lays things out properly if history_height is None.
                has fixed:
                    yfit True
                if h.who:
                    label h.who:
                        style "history_name"
                        # Take the color of the who text from the Character, if set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what
        if not _history_list:
            label _("The dialogue history is empty.")

style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

##########################################
##------------CONFIRM SCREEN------------##
##########################################

screen confirm(message, yes_action, no_action):
    # Ensure other screens do not get input while this screen is displayed.
    modal True
    zorder 200

    style_prefix "confirm"

    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 30
            label _(message):
                style "confirm_prompt"
                xalign 0.5
            hbox:
                xalign 0.5
                spacing 100
                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile = gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")

##########################################
##------------SKIP INDICATOR------------##
##########################################
# Reference https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():
    zorder 100
    style_prefix "skip"

    frame:
        hbox:
            spacing 6
            text _("Skipping")
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

# This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5
    pause delay
    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat

style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile = gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    # We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE glyph in it.
    font "DejaVuSans.ttf"

##########################################
##-------------NOTIFY POPUP-------------##
##########################################

screen notify(message):
    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Solid("#0006") # TODO
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")