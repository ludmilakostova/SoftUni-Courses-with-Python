from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album not in self.albums:
            self.albums.append(album)
            return f'Band {self.name} has added their newest album {album.name}.'
        return f'Band {self.name} already has {album.name} in their library.'

    def remove_album(self, album_name: str):
        for album_object in self.albums:
            if album_object.published:
                return f'Album has been published. It cannot be removed.'

            if album_object.name == album_name:
                return f'Album {album_object.name} has been removed.'
            else:
                return f'Album {album_object.name} is not found.'

    def details(self):
        album_details = "\n".join(album.details() for album in self.albums)
        return f'Band {self.name}\n' + album_details


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())


