import pytest

from lesson1.albums import Album


@pytest.fixture()
def album_queen():
    return Album('Queen', 'Killer Queen', [
        'Brighton rock',
        'Killer Queen',
        'Tenement Funster'
    ])

def test_init_(album_queen):
    assert album_queen.artist == 'Queen'
    assert album_queen.title == 'Killer Queen'
    assert album_queen.tracks == [
        'Brighton rock',
        'Killer Queen',
        'Tenement Funster'
    ]

@pytest.fixture()
def album_metallica():
    return Album('Metallica', 'Black Album', [
        'Enter Sandman',
        'Sad But True',
        'Holier Than Thou'
    ])

def test_init(album_metallica):
    assert album_metallica.artist == 'Metallica'
    assert album_metallica.title == 'Black Album'
    assert album_metallica.tracks == [
        'Enter Sandman',
        'Sad But True',
        'Holier Than Thou'
    ]