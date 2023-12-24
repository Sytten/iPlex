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
                            text: modelData.name
                        }
                        MouseArea {
                            anchors.fill: parent
                            onClicked: {
                                artistsView.currentIndex = index
                                plex.loadAlbums(modelData.name)
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
                delegate: Component {
  ColumnLayout {
    width: parent.width

    Text {
      Layout.preferredHeight: 20
      text: modelData.title
    }

    ListView {
      Layout.fillHeight: true
      model: modelData.songs
      delegate: Row {
        Text {
            text: modelData
        }
      }
    }
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
