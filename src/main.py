import sys

from PySide6.QtCore import QUrl
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication

from Backend import Backend


def main():
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    backend = Backend()
    engine.rootContext().setContextProperty("backend", backend)

    # Load the QML file
    engine.load(QUrl.fromLocalFile('ImageProcessor.qml'))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())


main()

