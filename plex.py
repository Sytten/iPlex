from plexapi.myplex import MyPlexAccount
from PySide2.QtCore import QObject, Slot, Signal, Property
from models import Album, Artist

class Plex(QObject):
    artistsChanged = Signal()
    currentArtistChanged = Signal()
    currentAlbumsChanged = Signal()

    def __init__(self, username: str, password: str, server_name: str):
        QObject.__init__(self)
        #self.account = MyPlexAccount(username, password)
        #self.server = self.account.resource(server_name).connect()
        self._currentSection = None

        self._artists = []
        self._currentArtist = None
        self._currentAlbums = []

    @Slot()
    def refresh(self):
        artists = [Artist("Artic Monkey", []), Artist("X Ambassador", [])]
        self.setArtists(artists)
        return

        sections = [x for x in self.server.library.sections() if x.type == "artist"]

        if sections.__len__ != 0:
            self._currentSection = sections[0]
            # Load artists, but not albums
            artists = [Artist(x.title, []) for x in self._currentSection.all()]
            self.setArtists(artists)

    @Slot(str)
    def loadAlbums(self, artist: str):
        albums = [Album("AM", ["Song 1", "Song 2"]), Album("The other one", ["Song 3", "Song4"])]
        self.setCurrentAlbums(albums)
        return

        if self._currentSection == None:
            return

        artist = self._currentSection.get(artist)
        albums = [Album(a.title, [t.title for t in a.tracks()]) for a in artist.albums()]
        self.setCurrentAlbums(albums)

    @Property('QVariantList', notify=currentAlbumsChanged)
    def currentAlbums(self):
        return self._currentAlbums

    def setCurrentAlbums(self, albums):
        if albums != self._currentAlbums:
            self._currentAlbums = albums
            self.currentAlbumsChanged.emit()

    @Property('QVariantList', notify=artistsChanged)
    def artists(self):
        return self._artists

    @artists.setter
    def setArtists(self, artists):
        if artists != self._artists:
            self._artists = artists
            self.artistsChanged.emit()
        