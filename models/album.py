from PySide2.QtCore import QObject, Property

class Album(QObject):
    def __init__(self, title: str, songs):
        QObject.__init__(self)
        self._title = title
        self._songs = songs

    @Property('QVariantList', constant=True)
    def songs(self):
        return self._songs

    @Property('QString', constant=True)
    def title(self):
        return self._title
