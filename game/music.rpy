# DynamicMusic is a custom class I defined in dynamicmusic.rpy.
# stop_points is a list of points at which the song can be stopped (in seconds).
# loop_point is a point at which the song can be looped (in seconds).
#
# To use this in a script, use the following command:
# $ queue_music(music_jazz_tune)

define music_one = DynamicMusic("music/one.ogg", stop_points = [0], loop_point = 61.0807)