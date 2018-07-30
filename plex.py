from plexapi.myplex import MyPlexAccount
from PySide2.QtCore import QObject, Slot, Signal, Property

class Plex(QObject):
    artistsChanged = Signal()
    currentAlbumsChanged = Signal()

    def __init__(self, username: str, password: str, server_name: str):
        QObject.__init__(self)
        self.account = MyPlexAccount(username, password)
        self.server = self.account.resource(server_name).connect()
        self._currentSection = None

        self._artists = []
        self._currentArtist = None
        self._currentAlbums = []

    @Slot()
    def refresh(self):
        #artists = ["Artic Monkey","X Ambassador"]
        #self.setArtists(artists)
        #return

        sections = [x for x in self.server.library.sections() if x.type == "artist"]

        if sections.__len__ != 0:
            self._currentSection = sections[0]
            artists = [x.title for x in self._currentSection.all()]
            self.setArtists(artists)

    @Slot(str)
    def loadAlbums(self, artist: str):
        #if artist == "Artic Monkey":
        #    albums = ["AM", "The other one"]
        #else:
        #    albums = ["VHS", "That one"]
        #return

        if self._currentSection == None:
            return

        artist = self._currentSection.get(artist)
        albums = [x.title for x in artist.albums()]
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
        