from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl

def main():
    app = QApplication([])
    view = QQuickView()
    url = QUrl("views/view.qml")

    view.setSource(url)
    view.setResizeMode(QQuickView.SizeRootObjectToView)
    view.show()
    app.exec_()

if __name__ == '__main__':
    main()
