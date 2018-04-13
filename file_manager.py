from config import NAME_SONG_DICT


class FileManager:
    def __init__(self):
        pass

    def save(self, song):
        pass

    def get_filepath(self, name):
        if name not in NAME_SONG_DICT:
            return None
        return NAME_SONG_DICT["name"]
