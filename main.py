from file_manager import FileManager
from photo_snapper import PhotoSnapper
from song_player import SongPlayer


def main():
    photosnapper = PhotoSnapper()
    file_namanger = FileManager()
    song_player = SongPlayer()

    imgstr = photosnapper.snap()
    response = photosnapper.dispatch_to_rekognition(imgstr)

    name = photosnapper.get_name(response)
    if not name:
        return
    filepath = file_namanger.get_filepath(name)
    if not filepath:
        return
    song_player.play(filepath)


if __name__ == "__main__":
    main()
