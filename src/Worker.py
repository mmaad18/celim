import os

from PySide6.QtCore import QThread, Slot, Signal, QObject
from src.ImageManipulations import *


class Worker(QObject):
    progressChanged = Signal(float)
    finished = Signal()

    def __init__(self):
        super().__init__()

    @Slot()
    def testRun(self):
        for i in range(1, 11):
            QThread.sleep(1)  # Simulate work with a delay
            self.progressChanged.emit(i * 0.1)  # Emit a test progress value
        self.finished.emit()

    @Slot(str, bool, bool)
    def batchConvert(self, folderPath, edgeX, edgeY):
        files = os.listdir(folderPath)
        tif_files = [file for file in files if file.endswith('.tif')]
        file_count = len(tif_files)

        print(edgeX, edgeY)

        progress = 0.0
        self.progressChanged.emit(progress)

        for i, file in enumerate(tif_files):
            image_gray = load_image_gray(os.path.join(folderPath, file))
            save_image_gray(image_gray, f'out/conv{i + 1}.png')
            progress = (i + 1) / file_count
            self.progressChanged.emit(progress)

        self.progressChanged.emit(1.0)
        self.finished.emit()
