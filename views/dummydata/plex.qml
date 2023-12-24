import QtQuick 2.11
import QtQml.Models 2.11

Item {
    property variant artists: ListModel {
        ListElement { 
            modelData: Item {
                property variant name: "Artist 1" 
            }
        }
        ListElement { 
            modelData: Item {
                property variant name: "Artist 2" 
            }
        }
    }
    
    property variant currentAlbums: ListModel {
        ListElement { modelData: "Album 1" }
        ListElement { modelData: "Album 2" }
    }
}
