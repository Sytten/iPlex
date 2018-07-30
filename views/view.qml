import QtQuick 2.0
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.1
import QtQuick.Window 2.1

ApplicationWindow {
    id: page
    width: 800
    height: 400
    visible: true

    ColumnLayout {
        id: mainLayout
        anchors.fill: parent

        RowLayout {
            id: centralLayout
            Layout.fillWidth: true

            ListView {
                id: artistsView
                Layout.minimumWidth: 200
                Layout.fillHeight: true
                model: plex.artists
                delegate: Component {
                    Item {
                        width: parent.width
                        height: 40
                        Text {
                            text: modelData
                        }
                        MouseArea {
                            anchors.fill: parent
                            onClicked: {
                                artistsView.currentIndex = index
                                plex.loadAlbums(modelData)
                            }
                        }
                    }
                }
                highlight: Rectangle {
                    color: 'grey'
                }
            }

            ListView {
                id: albumsView
                Layout.fillWidth: true
                Layout.fillHeight: true
                model: plex.currentAlbums
                delegate: Row {
                    Text {
                        text: modelData
                    }
                }
            }
        }

        Button {
            text: "Get artists"
            Layout.fillWidth: true
            onClicked: plex.refresh()
        }

    }
}
/*##^## Designer {
    D{i:16;anchors_height:400;anchors_width:800;anchors_x:0;anchors_y:0}
}
 ##^##*/
