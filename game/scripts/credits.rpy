init python:
    credits_texts = [
        ("Game Director", "Christian Ines (Windreda)"),
        ("", ""),
        ("Writers", "Adam “Ultra_HR” Warren"),
        ("", "Guy “Gloom” Reisman "),
        ("", "Kuroe “Kuroe” Kuroe"),
        ("", "Windreda"),
        ("", "Hamadyne"),
        ("", ""),
        ("Editors", "Tristan “Cipher” Hallihan"),
        ("", "Logan “StuporSpoopy” Connolly"),
        ("", "Jamie “Swampie” Dunstan"),
        ("", ""),
        ("Art Director & Lead Artist", "Piotr “Morthiasik” Koszelak"),
        ("", ""),
        ("Artist", "godsavant"),
        ("", ""),
        ("Additional Concept Artists", "Eora"),
        ("", "Kuroe"),
        ("", "Likhos"),
        ("", ""),
        ("Music & Sound Director", "Sean “Flare” Gorter"),
        ("", ""),
        ("Musician", "Senzo"),
        ("", ""),
        ("Lead Programmer", "Arán"),
        ("", ""),
        ("Special Thanks", "Lemma Soft Forums"),
        ("", "Watercress Studios"),
        ("", "James Urbec "),
        ("", "K-PIN"),
        ("", "Latememes"),
        ("", "Zgred Baron")
    ]

init:
    image credits_text_left = Text(
        "\r\n".join(x[0] for x in credits_texts),
        color = gui.active_text_color,
        xanchor = 1.0,
        text_align = 1.0,
        xpos = 0.5,
        yoffset = 1200,
        xoffset = -20,
        size = 32)
    image credits_text_right = Text(
        "\r\n".join(x[1] for x in credits_texts),
        color = gui.text_color,
        xanchor = 0.0,
        text_align = 0.0,
        xpos = 0.5,
        yoffset = 1200,
        xcenter = 0.5,
        xoffset = 20,
        size = 32)
    image credits_text_end = Text(
        "And all of you! Thank you for playing through our first ever NaNoRenO game!\r\n\r\n© 2018\nSomnova Studios",
        color = gui.text_color,
        text_align = 0.5,
        xpos = 0.5,
        yoffset = 2950,
        xcenter = 0.5,
        size = 32)

label end_credits:
    scene bg_black
    $ config.skipping = False
    $ hide_quick_menu = True
    $ _game_menu_screen = None
    stop music fadeout 2
    stop dynamic_1 fadeout 2
    stop dynamic_2 fadeout 2
    show bg_black
    $ renpy.pause(2, hard = True)
    $ queue_music(music_nine2, False)
    show logo at credits_logo
    show credits_text_left at credits_text
    show credits_text_right at credits_text
    show credits_text_end at credits_text
    $ renpy.pause(38, hard = True)
    $ config.skipping = True
    $ hide_quick_menu = False
    $ _game_menu_screen = "save_screen"
    $ renpy.full_restart()
    return

transform credits_logo:
    on show:
        xcenter 0.5
        ycenter 0.5
        alpha 0.0
        linear 3.5 alpha 1.0
        linear 30 yoffset -2500

transform credits_text:
    on show:
        linear 3.5 alpha 1.0
        linear 30 yoffset -2500