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
define music_five = DynamicMusic(["music/five-1.ogg", "music/five-2.ogg"], stop_points = [3.133, 06.467, 9.800, 13.133, 16.467, 19.800, 23.133, 26.467, 29.800, 33.133, 36.467, 39.800, 43.133, 46.667, 49.800, 53.133, 56.467, 59.800, 63.133, 66.467, 66.467, 73.133, 76.467, 79.800, 83.133, 86.467, 89.800, 93.133, 96.467, 99.800, 103.133, 106.467, 109.800, 113.133, 116.467, 119.800, 123.133, 126.467, 129.800, 133.133, 136.467, 139.800, 143.133, 146.667, 149.800, 153.133, 156.467, 159.800, 163.133, 166.467, 169.800, 173.133, 176.467, 179.800, 183.133, 186.467, 189.800, 193.133, 196.467, 199.800, 203.133, 206.467, 209.800, 213.133, 216.467, 219.800], loop_point = 48.333) # "music/five-1-reverb.ogg" and "music/five-2-reverb.ogg" are on standby until crossfade allows for four simultaneous tracks
define music_test = DynamicMusic(["music/test1.ogg", "music/test2.ogg"], stop_points = [0], loop_point = 0)