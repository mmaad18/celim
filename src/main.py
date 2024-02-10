import sys

from PySide6.QtCore import QUrl
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication

from Backend import Backend

from PySide6.QtCore import __version__ as PYSIDE_VERSION
from PySide6.QtCore import qVersion

print("Qt version:", qVersion())
print("PySide version:", PYSIDE_VERSION)



def main():
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    backend = Backend()
    engine.rootContext().setContextProperty("backend", backend)
    engine.load(QUrl.fromLocalFile('src/ImageProcessor.qml'))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())


main()

