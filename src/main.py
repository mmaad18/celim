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

    engine.load(QUrl.fromLocalFile('src/main.qml'))
    engine.warnings.connect(lambda warnings: print(warnings))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())


main()

