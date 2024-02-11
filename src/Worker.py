import os

from PySide6.QtCore import QThread, Slot, Signal, QObject
from src.ImageManipulations import *


class Worker(QObject):
    progressChanged = Signal(float)
    finished = Signal()

    def __init__(self):
        super().__init__()
        self.folderPath = ""
        self.edgeX = False
        self.edgeY = False

    def setBatchParams(self, folderPath, edgeX, edgeY):
        self.folderPath = folderPath
        self.edgeX = edgeX
        self.edgeY = edgeY

    @Slot()
    def batchConvert(self):
        files = os.listdir(self.folderPath)
        tif_files = [file for file in files if file.endswith('.tif')]
        file_count = len(tif_files)

        print(self.edgeX, self.edgeY)

        progress = 0.0
        self.progressChanged.emit(progress)

        for i, file in enumerate(tif_files):
            image_gray = load_image_gray(os.path.join(self.folderPath, file))
            save_image_gray(image_gray, f'out/{file}{i + 1}.png')

            image_conv = edge_detection_x(image_gray)
            save_image_gray(image_conv, '../out/conv.png')

            progress = (i + 1) / file_count
            self.progressChanged.emit(progress)

        self.progressChanged.emit(1.0)
        self.finished.emit()



