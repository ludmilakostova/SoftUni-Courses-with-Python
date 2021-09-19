from project.song import Song


class Album:
    def __init__(self, name: str, songs):
        self.name = name
        self.songs = []
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f'Cannot add {song.name}. It\'s a single'

        if self.published:
            return 'Cannot add songs. Album is published.'

        if song not in self.songs:
            self.songs.append(song)
            return f'Song {song.name} has been added to the album {self.name}.'
        return 'Song is already in the album.'

    def remove_song(self, song_name: str):
        for song_object in self.songs:
            if song_object.name == song_name:
                if self.published:
                    return 'Cannot remove songs. Album is published.'
                self.songs.remove(song_object)
                return f'Removed song {song_name} from album {self.name}.'

        return 'Song is not in the album.'

    def publish(self):
        if self.published:
            return f'Album {self.name} is already published.'

        self.published = True
        return f'Album {self.name} has been published.'

    def details(self):
        result = ""
        result += f'Album {self.name}\n'
        for song_object in self.songs:
            result += f'== {song_object.get_info()}\n'
        return result








