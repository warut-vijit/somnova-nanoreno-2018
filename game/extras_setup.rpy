init python:

    # Note: this shouldn't be here, needs to be in the game folder

    def MaxScale(img, minwidth=config.screen_width, minheight=config.screen_height):
        currwidth, currheight = renpy.image_size(img)
        xscale = float(minwidth) / currwidth
        yscale = float(minheight) / currheight

        if xscale > yscale:
            MaxScale = xscale
        else:
            MaxScale = yscale

        return im.FactorScale(img, MaxScale, MaxScale);

    def MinScale(img, maxwidth=config.screen_width, maxheight=config.screen_height):
        currwidth, currheight = renpy.image_size(img)
        xscale = float(maxwidth) / currwidth
        yscale = float(maxheight) / currheight

        if xscale < yscale:
            MinScale = xscale
        else:
            MinScale = yscale
        
        return im.FactorScale(img, MinScale, MinScale)

maxnumx = 2
maxnumy = 2
maxthumbx = config.screen_width / (maxnumx + 1)
maxthumby = config.screen_height / (maxnumy + 1)
maxperpage = maxnumx * maxnumy

class GalleryItem:
    def __init__(self, name, images, thumb, locked="lockedthumb"):
        self.name = name
        self.images = images
        self.thumb = thumb
        self.locked = locked
        self.refresh_lock()
    
    def num_images(self):
        return len(self.images)
    
    def refresh_lock(self):
        self.num_unlocked = 0
        lockme = False
        for img in self.images:
            if not renpy.seen_image(img):
                lockme = True
            else:
                self.num_unlocked += 1
        self.is_locked = lockme

    