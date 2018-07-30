import sys
import os
from os.path import abspath, dirname, join
from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine
from plex import Plex

def main():
    app = QApplication([])
    engine = QQmlApplicationEngine()

    # Instances of Objects
    plex = Plex(os.environ['USERNAME'], os.environ['PASSWORD'], os.environ['SERVER_NAME'])

    # Expose instances
    context = engine.rootContext()
    context.setContextProperty("plex", plex)

    # Load the view
    view_path = join(dirname(__file__), 'views/view.qml')
    engine.load(abspath(view_path))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
