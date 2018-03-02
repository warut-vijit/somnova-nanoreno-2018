# This ensures that dynamic music can be used on the title screen.
init offset -2

init python:
    import time
    import threading
    # Timers and threads are used here because the alternative method (renpy.music.play)
    # causes small skips in the music. The alternative method involves using the play command while
    # music is already playing, but specifying it to end at the next stop point. This is done
    # because Ren'Py does not provide any method to set a stopping-point for already-playing music.

    # This is the class which we can use for convenience.
    class DynamicMusic:
        def __init__(self, file_name, stop_points, loop_point):
            self.file_name = file_name
            self.stop_points = stop_points
            self.loop_point = loop_point

    def queue_music(track):
        thread = threading.Thread(target = queue_music_async, args = [track])
        # Python exits a program when there are no non-daemonic threads left. Making this thread
        # daemonic ensures that the application can quit even if there's music that's been
        # queued and is waiting to be played. Without this, the program would wait until a stopping
        # point in a track before quitting while not actually being responsive. 
        thread.daemon = True
        thread.start()

    current_music = None
    queued_music = None
    def queue_music_async(track):
        global current_music
        global queued_music
        if renpy.music.get_playing() is None:
            current_music = track
            renpy.music.play("<loop {0}>{1}".format(track.loop_point, track.file_name))
        else:
            current_time = renpy.music.get_pos()
            # This is a list of every stopping point which comes after the current position.
            next_times = [x for x in current_music.stop_points if x > current_time]

            if len(next_times) == 0:
                # There are no stopping points left, so just loop and use the first stopping point.
                next_time = renpy.music.get_duration() + current_music.stop_points[0]
            else:
                next_time = next_times[0]
            
            queued_music = track
            local_queued_music = track

            # Wait until the specified stopping point is reached.
            time.sleep(next_time - current_time)

            # This check ensures that new music hasn't been queued while we were waiting to change
            # the music. This could occur if someone decides to speed through a scene so fast that
            # a scheduled music change doesn't even get a chance to happen and another one is
            # already scheduled afterwards.
            if local_queued_music.file_name == queued_music.file_name:
                # This ensures that it doesn't seem like music is restarted unnecessarily.
                if renpy.music.get_playing() != queued_music.file_name:
                    current_music = queued_music
                    renpy.music.play("<loop {0}>{1}".format(queued_music.loop_point, queued_music.file_name))
                queued_music = None