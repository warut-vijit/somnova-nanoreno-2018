# This ensures that dynamic music can be used on the title screen.
init offset = -2

init python:
    import time
    import threading
    # Timers and threads are used here because the alternative method (renpy.music.play)
    # causes small skips in the music. The alternative method involves using the play command while
    # music is already playing, but specifying it to end at the next stop point. This is done
    # because Ren'Py does not provide any method to set a stopping-point for already-playing music.

    # This is the class which we can use for convenience.
    class DynamicMusic:
        def __init__(self, file_names, stop_points, loop_point):
            self.file_names = file_names
            self.stop_points = stop_points
            self.loop_point = loop_point

        def filename(self, index):
            if len(self.file_names) == 1:
                name = self.file_names[0]
            else:
                name = self.file_names[index]

            return "<loop {0}>{1}".format(self.loop_point, name)

    def queue_music(track):
        thread = threading.Thread(target = queue_music_async, args = [track])
        # Python exits a program when there are no non-daemonic threads left. Making this thread
        # daemonic ensures that the application can quit even if there's music that's been
        # queued and is waiting to be played. Without this, the program would wait until a stopping
        # point in a track before quitting while not actually being responsive.
        thread.daemon = True
        thread.start()

    def crossfade_music(volume_1, volume_2, time):
        thread = threading.Thread(target = crossfade_music_async, args = [volume_1, volume_2, time])
        thread.daemon = True
        thread.start()

    renpy.music.register_channel(
        name = "dynamic_1",
        mixer = "music",
        tight = True,
        loop = True,
        stop_on_mute = False)
    renpy.music.register_channel(
        name = "dynamic_2",
        mixer = "music",
        tight = True,
        loop = True,
        stop_on_mute = False)

    queued_music = None
    current_music = None
    def queue_music_async(track):
        global queued_music
        global current_music
        
        if current_music == track:
            return

        queued_music = track
        
        if current_music is not None:
            current_position = renpy.music.get_pos(channel = "dynamic_1")
            next_stop_points = [point for point in track.stop_points if point > current_position]
            stop_point = renpy.music.get_duration(channel = "dynamic_1") + track.stop_points[0]
            if len(next_stop_points) != 0:
                stop_point = next_stop_points[0]

            queued_music = track
            local_queued_music = track
            time.sleep(stop_point - current_position)
            if queued_music != local_queued_music:
                # Something has queued music while we were waiting.
                return

        renpy.music.set_volume(volume = 1.0, channel = "dynamic_1")
        renpy.music.set_volume(volume = 0.0, channel = "dynamic_2")
        renpy.music.play(
            filenames = track.filename(0),
            channel = "dynamic_1",
            synchro_start = True)
        renpy.music.play(
            filenames = track.filename(1),
            channel = "dynamic_2",
            synchro_start = True)

        current_music = track
        queued_music = None

    def crossfade_music_async(volume_1, volume_2, time):
        renpy.music.set_volume(volume = volume_1, delay = time, channel = "dynamic_1")
        renpy.music.set_volume(volume = volume_2, delay = time, channel = "dynamic_2")
        
