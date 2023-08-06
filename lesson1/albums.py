"""
Создай класс Album у которого есть поля

- Исполнитель (artist) - строка
- Название (title) - строка
- Треки (tracks) - это **список**

**Создай два экземпляра album_1 и album_2**

Исполнитель: Queen

Название: Killer Queen

Треки: Brighton rock, Killer Queen, Tenement Funster

Исполнитель: Metallica

Название: Black Album

Треки: Enter Sandman, Sad But True, Holier Than Thou
"""


class Album:

    def __init__(self, artist, title, tracks):
        self.tracks = tracks
        self.artist = artist
        self.title = title




album_1 = Album('Queen', 'Killer Queen', ['Brighton rock', 'Killer Queen', 'Tenement Funster'])

album_2 = Album('Metallica', 'Black Album', ['Enter Sandman', 'Sad But True', 'Holier Than Thou'])


print(album_1.artist, album_1.title, len(album_1.tracks), "треков")  # Queen Killer Queen 3 треков
print(album_2.artist, album_2.title, len(album_2.tracks), "треков")  # Metallica Black Album 3 треков