import time

import vlc


class SongPlayer:
    def __init__(self):
        self.vlcInst = vlc.Instance()
        self.player = self.vlcInst.media_player_new()

    def play(self, filepath):
        Media = self.vlcInst.media_new_path(filepath)
        self.player.set_media(Media)
        self.player.play()
        time.sleep(10)


if __name__ == "__main__":
    player = SongPlayer()
    player.play("/Users/mac/Documents/bigbrother/Sandstorm.mp3")
