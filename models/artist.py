from PySide2.QtCore import QObject, Property

class Artist(QObject):
    def __init__(self, name: str, albums):
        QObject.__init__(self)
        self._name = name
        self._albums = albums

    @Property('QVariantList')
    def albums(self):
        return self._albums

    @Property('QString', constant=True)
    def name(self):
        return self._name
