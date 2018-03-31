# DynamicMusic is a custom class I defined in dynamicmusic.rpy.
# file_names is an array of up to two files which have identical timing (i.e. can be crossfaded between).
# stop_points is a list of points at which the song can be stopped (in seconds).
# loop_point is the point from which a song can be looped (from the beginning).
#
# To use this in a script, use the following command:
# $ queue_music(music_jazz_tune)
#
# To crossfade, use the following command:
# $ crossfade_music(0.0, 1.0, 5.0)
# This sets the first track's volume to 0.0 and the second track's volume to 1.0 over the course
# of five seconds.

define music_one = DynamicMusic(["music/one.ogg", "music/one-reverb.ogg"], stop_points = [0], loop_point = 61.324)
define music_test = DynamicMusic(["music/test1.ogg", "music/test2.ogg"], stop_points = [0], loop_point = 0)