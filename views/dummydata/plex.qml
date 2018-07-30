import QtQuick 2.11
import QtQml.Models 2.11

Item {
    property variant artists: ListModel {
        ListElement { modelData: "Artist 1" }
        ListElement { modelData: "Artist 2" }
    }
    
    property variant currentAlbums: ListModel {
        ListElement { modelData: "Album 1" }
        ListElement { modelData: "Album 2" }
    }
}
