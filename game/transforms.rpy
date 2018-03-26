transform common(x = 0):
    subpixel True
    transform_anchor True
    size (600 * 0.7, 1080 * 0.7)
    xcenter 1280 / 2
    yanchor 1080
    ypos 720
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
    common(200)

transform center_left:
    common(-200)

transform embiggen:
    ease 1 size (600 * 0.75, 1080 * 0.75)