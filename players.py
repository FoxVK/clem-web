import dbus
import time


class Player:

    __d_ses = dbus.SessionBus()

    @staticmethod
    def get():

        lst = []

        try:
            lst.append(Player('clementine'))
        except Exception as e:
            if __name__ == "__main__":
                print(e)
            pass

        return lst

    def __init__(self, name):
        self.name = name

        self.d_player = Player.__d_ses.get_object('org.mpris.'+name, '/Player')
        self.d_if = dbus.Interface(self.d_player, dbus_interface='org.freedesktop.MediaPlayer')

        self.d_track_list = Player.__d_ses.get_object('org.mpris.'+name, '/TrackList')
        self.d_tracks_if = dbus.Interface(self.d_track_list, dbus_interface='org.freedesktop.MediaPlayer')

    def play(self):
        self.d_if.Play()

    def stop(self):
        self.d_if.Stop()

    def pause(self):
        self.d_if.Pause()

    def prev(self):
        self.d_if.Prev()

    def next(self):
        self.d_if.Next()

    @property
    def playing(self):
        m = self.d_if.GetMetadata()

        title = m["title"]
        artist = m["artist"]

        return artist + " - " + title

    @property
    def state(self):
        return str(self.d_if.GetStatus())

    @property
    def tracks(self):
        i = 0
        while True:
            d = self.d_tracks_if.GetMetadata(i)
            track = Track.from_metadata(i, d)

            if track is None:
                break

            yield track
            i += 1

    @property
    def current_track(self):
        i = self.d_tracks_if.GetCurrentTrack()
        return Track.from_metadata(i, self.d_tracks_if.GetMetadata(i))

    @current_track.setter
    def current_track(self, track):
        self.d_tracks_if.PlayTrack(int(track))

    def __str__(self):
        return self.name


class Track:

    @staticmethod
    def from_metadata(i, md):
        if 'title' not in md:
            return None

        time = -1
        if 'time' in md:
            time = int(md['time'])

        return Track(i, md['title'], time)

    def __init__(self, number, title, length):
        self.__length = int(length)
        self.__title = str(title)
        self.__number = int(number)

    def __int__(self):
        return self.__number

    def __str__(self):
        return self.__title

    def __len__(self):
        return self.__length

    def strlen(self, format="%H:%M:%S"):
        if self.__length < 0:
            return ""
        else:
            return time.strftime("%H:%M:%S", time.gmtime(self.__length))

if __name__ == "__main__":
    p = Player.get()[0]
    print(p.state)
    print(p.playing)

    for t in p.tracks:
        print (" ", t, t.strlen())

    print(p.current_track)