init python:
    # define images using Python API to use in the gallery
    renpy.image("bg_black", Solid("#000"))
    renpy.image("bg_club_1_off_work", "backgrounds/club-1-off-work.webp")
    renpy.image("bg_club_2_after_work", "backgrounds/club-2-after-work.webp")
    renpy.image("bg_club_2_before_work", "backgrounds/club-2-before-work.webp")
    renpy.image("bg_club_2_during_work", "backgrounds/club-2-during-work.webp")
    renpy.image("bg_back_alley", "backgrounds/back-alley.webp")
    renpy.image("bg_club_lounge", "backgrounds/club-lounge.webp")
    renpy.image("bg_credits", "backgrounds/credits.webp")

    # bg_gallery is shown in the Extras menu
    bg_gallery = (Gallery(), ["bg_club_1_off_work", "bg_club_2_after_work", "bg_back_alley", "bg_club_lounge"])
    bg_gallery[0].button("bg_club_1_off_work")
    bg_gallery[0].unlock_image("bg_club_1_off_work")

    bg_gallery[0].button("bg_club_2_after_work")
    bg_gallery[0].unlock_image("bg_club_2_after_work")
    bg_gallery[0].unlock_image("bg_club_2_during_work")
    bg_gallery[0].unlock_image("bg_club_2_before_work")

    bg_gallery[0].button("bg_back_alley")
    bg_gallery[0].unlock_image("bg_back_alley")

    bg_gallery[0].button("bg_club_lounge")
    bg_gallery[0].unlock_image("bg_club_lounge")

    bg_gallery[0].transition = dissolve
