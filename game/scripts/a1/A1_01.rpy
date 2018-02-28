label A1_01:
    scene bg_elonmusk_office
    show elonmusk smile
    elonmusk "Alright, well..."
    elonmusk "I've got a rocket to catch."
    show cg_elonmusk_liftoff
    window hide # Hide dialogue box
    $ renpy.pause() # Wait for click
    window show # Show dialogue box
    "Smiling, I wipe a tear from my eye as I watch the rocket take off."
    "I will miss Elon dearly, but his sacrifice was for the greater good."
    return