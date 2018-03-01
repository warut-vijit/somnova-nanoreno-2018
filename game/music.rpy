# DynamicMusic is a custom class I defined in dynamicmusic.rpy.
# stop_points is a list of points at which the song can be stopped (in seconds).
# loop_point is a point at which the song can be looped (in seconds).
#
# To use this in a script, use the following command:
# $ queue_music(music_jazz_tune)

define music_jazz_tune = DynamicMusic("music/jazz-tune.ogg", stop_points = [0, 12.002, 17.455], loop_point = 12.002)
define music_funeral_march = DynamicMusic("music/funeral-march.ogg", stop_points = [0, 12.75, 36.75, 48.75], loop_point = 0.75)