transform common(x = 0):
    subpixel True
    transform_anchor True
    xcenter 0.5
    yanchor 1.0
    ypos 1080
    on show:
        # This block is called when the image is first shown.
        alpha 0
        xoffset x
        linear 0.25 alpha 1
    on replace:
        # This block is called when the image replaces another instance of itself.
        alpha 1
        ease 0.75 xoffset x

# This is so that characters don't blip out of existence.
transform transform_hide:
    on hide:
        linear 0.25 alpha 0

transform centered:
    common()

transform center_right:
    common(300)

transform center_left:
    common(-300)

transform embiggen:
    size (600, 1080)
    ease 1 size (600 * 1.1, 1080 * 1.1)