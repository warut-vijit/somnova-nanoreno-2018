# extras.rpy
# loads images and thumbnails used in extras menus

init python:
    # Gallery
    g_size = 9
    g_gallery = Gallery()
    g_gallery.transition = dissolve
    g_thumbs = []
    for i in range(1, g_size+1):
        filename = "g{:02}".format(i)
        renpy.image(filename, "extras/gallery/{}.png".format(filename))
        renpy.image(filename+"_thumb", "extras/gallery-thumbs/{}.png".format(filename))
        g_gallery.button(filename)
        g_gallery.unlock_image(filename)
        g_thumbs.append(filename+"_thumb")
    extras_gallery = (g_gallery, g_thumbs)

    # Concept Art
    ca_size = 13
    ca_gallery = Gallery()
    ca_gallery.transition = dissolve
    ca_thumbs = []
    for i in range(1, ca_size+1):
        filename = "ca{:02}".format(i)
        renpy.image(filename, "extras/conceptart/{}.png".format(filename))
        renpy.image(filename+"_thumb", "extras/conceptart-thumbs/{}.png".format(filename))
        ca_gallery.button(filename)
        ca_gallery.unlock_image(filename)
        ca_thumbs.append(filename+"_thumb")
    extras_ca = (ca_gallery, ca_thumbs)
