import QtQuick 2.0
import QtQuick.Layouts 1.11

Component {
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