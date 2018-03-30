init offset = -1

##########################################
##----------------STYLES----------------##
##########################################

style default:
    color gui.text_color
    font "fonts/Abel-Regular.ttf"
    language "western"

style vscrollbar:
    xysize (10, 520)
    selected_base_bar Frame("gui/scrollbar_border.png", 1, 1, tile = True)
    base_bar Frame("gui/scrollbar_border_idle.png", 1, 1, tile = True)
    selected_thumb Solid(gui.scrollbar_color)
    thumb Solid(gui.scrollbar_color_idle)

##########################################
##-----------------SAY------------------##
##########################################

# Reference: https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"
    
    frame:
        background Frame("gui/divider.png", 2, 0, tile = True)
        yoffset 1080
        pos (199, -262)
        xysize (1522, 2)

    window:
        id "window"
        add Solid(gui.border_edge, xalign = 1.0, xoffset = 1, xysize = (1, 160))
        
        text what id "what":
            xpos 37
            ypos 10
            xsize 1195
            line_spacing 4
            size 31

        window:
            style "namebox"
            add Solid(gui.border_edge, xpos = -1, xysize = (1, 60))
            if who is not None:
                text who + ":" id "who":
                    size 36
                    xpos 19
                    yalign 0.5

style say_window:
    yanchor 1.0
    pos (440, -80)
    xysize (1280, 160)
    yoffset 1080
    background Solid(gui.box_background_color)

style namebox:
    xpos -240
    xysize (220, 60)
    background Solid(gui.box_background_color)

##########################################
##---------SIMULTANEOUS DIALOGUE--------##
##########################################

style multiple2_say_window:
    xsize 500

style multiple2_namebox:
    xsize 200

style block2_multiple2_say_window:
    xpos 1220

##########################################
##---------------CHOICES----------------##
##########################################

# Reference: http://www.renpy.org/doc/html/screen_special.html#choice

define config.narrator_menu = True

screen choice(items):
    frame:
        style_prefix "choice"
        background "gui/choice_icon.png"
        xysize (80, 69)
        xalign 0.5
        yalign 0.4

        textbutton items[0].caption:
            action items[0].action
            xanchor 1.0
            xoffset -30
            background LiveComposite((734, 60), (0, 0), "gui/choice_button_left.png", (0, 0), "gui/choice_overlay_left_idle.png")
            hover_background LiveComposite((734, 60), (0, 0), "gui/choice_button_left.png", (0, 0), "gui/choice_overlay_left.png")
        textbutton items[1].caption:
            action items[1].action
            xanchor 0.0
            xoffset 30
            background LiveComposite((734, 60), (0, 0), "gui/choice_button_right.png", (0, 0), "gui/choice_overlay_right_idle.png")
            hover_background LiveComposite((734, 60), (0, 0), "gui/choice_button_right.png", (0, 0), "gui/choice_overlay_right.png")
            
style choice_button:
    xysize (734, 60)
    xpos 0.5
    ycenter 0.5

style choice_button_text:
    xfill True
    yfill True
    xcenter 0.5
    ycenter 0.5
    size 32

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
        
    hbox:
        style_prefix "quick_right"
        textbutton _("MENU") action ShowMenu("options")
        textbutton _("LOAD") action ShowMenu("load")
        textbutton _("SAVE") action ShowMenu("save")
        textbutton _("HISTORY") action ShowMenu("history")

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
    background Solid(gui.inactive_text_color, xysize = (3, 3), ypos = 37)
    hover_background Solid(gui.text_color, xysize = (3, 3), ypos = 37)
    selected_background Solid(gui.active_text_color, xysize = (3, 3), ypos = 37)

style quick_right_button:
    background Solid(gui.inactive_text_color, xysize = (3, 3), pos = (57, 37))
    hover_background Solid(gui.text_color, xysize = (3, 3), pos = (57, 37))
    selected_background Solid(gui.active_text_color, xysize = (3, 3), pos = (57, 37))

style quick_button_text:
    size 20
    color gui.inactive_text_color
    hover_color gui.text_color
    selected_color gui.active_text_color
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
        background Solid(gui.box_background_color)

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
                textbutton _("RETURN") action Return()
                textbutton _("HISTORY") action ShowMenu("history")
                textbutton _("SAVE GAME") action ShowMenu("save")
            
            textbutton _("LOAD GAME") action ShowMenu("load")
            textbutton _("OPTIONS") action ShowMenu("options")

            if main_menu:
                textbutton _("EXTRAS") sensitive False text_color gui.empty_text_color
                textbutton _("QUIT") action Quit(confirm = not main_menu)
            else:
                textbutton _("QUIT") action MainMenu()


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
        background Solid(gui.box_background_color)

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
            add Solid(gui.border_edge, xsize = 88)
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
    use file_slots(_("SAVE GAME"))

screen load():
    tag menu
    use file_slots(_("LOAD GAME"))


screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern = _("Page {}"), auto = _("Automatic saves"), quick = _("Quick saves"))
    use game_menu(title):
        fixed:
            # The grid of file slots.
            grid 4 3:
                yoffset -31
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                xspacing 20
                yspacing 60

                $ slot_hover = [False] * (4 * 3)
                for i in range(4 * 3):
                    $ slot = i + 1
                    if FileLoadable(slot):
                        button:
                            background Frame("gui/file_slot_button.png", 2, 2, tile = True)
                            xysize (240, 80)
                            action FileAction(slot)
                            add FileScreenshot(slot):
                                pos (20, 6)
                            text str(slot).rjust(3, str("0")):
                                pos (154, -1)
                                size 28
                            $ playtime_minutes = FileJson(slot, "playtime", empty = 0, missing = 0) / 60
                            text "{0}:{1}".format(str(int(playtime_minutes / 60)).rjust(2, str("0")), str(int(playtime_minutes % 60)).rjust(2, str("0"))):
                                pos (156, 33)
                                size 16
                            text FileTime(slot, format = _("{#file_time}%m-%d-%Y")):
                                pos (156, 58)
                                size 16
                            button:
                                anchor (0.0, 1.0)
                                pos (211, 21)
                                xysize (15, 15)
                                background "gui/x_idle.png"
                                hover_background "gui/x_focus.png"
                                action FileDelete(slot)
                    else:
                        button:
                            xysize (240, 80)
                            action FileAction(slot)
                            frame:
                                background Frame("gui/file_slot_empty.png", 2, 2, tile = True)
                                xysize (config.thumbnail_width, config.thumbnail_height)
                                pos (20, 6)
                            text _("Empty"):
                                color gui.empty_text_color
                                pos (154, -1)
                                size 28

            # Buttons to access other pages.
            hbox:
                style_prefix "page"
                xalign 1.0
                yalign 1.0
                offset (-20, -54)
                spacing 12
                textbutton _("Prev") action FilePagePrevious()

                # 1 (inclusive) to 6 (exclusive).
                for page in range(1, 6):
                    textbutton "[page]" action FilePage(page)

                textbutton _("Next") action FilePageNext()

style page_button_text:
    color gui.empty_text_color
    selected_color gui.text_color
    size 25

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
    color gui.inactive_text_color
    selected_color gui.active_text_color
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

    use game_menu(_("HISTORY")):
        viewport:
            pos (55, 60)
            xysize (965, 520)

            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            
            yinitial 1.0

            style_prefix "history"
            vbox:
                spacing 18
                for h in _history_list:
                    hbox:
                        spacing 5
                        if h.who:
                            text h.who + ":":
                                # Take the color of the who text from the Character, if set.
                                if "color" in h.who_args:
                                    color h.who_args["color"]

                        text h.what

style history_text:
    size 24

##########################################
##------------CONFIRM SCREEN------------##
##########################################

screen confirm(message, yes_action, no_action):
    # Ensure other screens do not get input while this screen is displayed.
    modal True
    zorder 200

    style_prefix "confirm"

    frame:
        xfill True
        yfill True
        background Solid(gui.confirm_background)
        frame:    
            xalign .5
            yalign .5
            xysize (660, 180)
            frame:
                background Frame("gui/divider.png", 2, 0, tile = True)
                ysize 2
                ypos -2
                xfill True
            frame:
                background Frame("gui/divider.png", 2, 0, tile = True)
                ysize 2
                ypos 180
                xfill True

            frame:
                ypos 20
                xysize (480, 140)
                frame:
                    background Solid(gui.border_edge)
                    xysize (2, 140)
                background Solid(gui.confirm_button_background)
                label _(message):
                    xcenter 0.5
                    ycenter 0.5
                    text_size 28
                    xsize 400
                    text_text_align 0.5
                vbox:
                    style_prefix "confirm"
                    xpos 500
                    spacing 20
                    textbutton _("Yes") action yes_action
                    textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

style confirm_button:
    xysize (160, 60)
    # Behold, a perfect example of Ren'Py's styling system being terrible:
    background LiveComposite((160, 60), (0, 0), Solid(gui.confirm_button_background), (158, 0), Solid(gui.border_edge, xysize = (2, 60)))
    hover_background LiveComposite((160, 60), (0, 0), Solid(gui.confirm_button_background), (158, 0), Solid(gui.active_text_color, xysize = (2, 60)))

style confirm_button_text:
    size 28
    xcenter 0.5
    ycenter 0.5
    color gui.confirm_text_color
    hover_color gui.text_color

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