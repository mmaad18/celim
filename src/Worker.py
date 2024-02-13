
import os

from PySide6.QtCore import Slot, Signal, QObject
from ImageManipulations import *


class Worker(QObject):
    progressChanged = Signal(float)
    finished = Signal()

    def __init__(self):
        super().__init__()
        self.folderPath = ""
        self.edgeX = False
        self.edgeY = False

        self.filePath = ""

        self.lowerThreshold = 0.1
        self.upperThreshold = 0.2

    def setBatchParams(self, folderPath, edgeX, edgeY):
        self.folderPath = folderPath
        self.edgeX = edgeX
        self.edgeY = edgeY

    def setSegmentationParams(self, filePath, lowerThreshold, upperThreshold):
        self.filePath = filePath
        self.lowerThreshold = lowerThreshold
        self.upperThreshold = upperThreshold

    @Slot()
    def batchConvert(self):
        files = os.listdir(self.folderPath)
        tif_files = [file for file in files if file.endswith('.tif')]
        file_count = len(tif_files)

        print(self.edgeX, self.edgeY)

        progress = 0.0
        self.progressChanged.emit(progress)

        for i, file in enumerate(tif_files):
            file_name = file.split('.')[0]
            image_gray = load_image_gray(os.path.join(self.folderPath, file))
            save_image_gray(image_gray, f'out/{file_name}{i + 1}.png')

            if self.edgeX:
                image_conv = edge_detection_x(image_gray)
                save_image_gray(image_conv, f'out/{file_name}_edgeX_{i + 1}.png')

            if self.edgeY:
                image_conv = edge_detection_y(image_gray)
                save_image_gray(image_conv, f'out/{file_name}_edgeY_{i + 1}.png')

            progress = (i + 1) / file_count
            self.progressChanged.emit(progress)

        self.progressChanged.emit(1.0)
        self.finished.emit()


    @Slot()
    def segmentation(self):
        image_gray = load_image_gray(self.filePath)
        file_name = self.filePath.split('/')[-1].split('.')[0]
        image_threshold = thresholding(image_gray, (self.lowerThreshold, self.upperThreshold))
        save_image_gray(image_threshold, f'out/{file_name}_segmented.png')

        self.finished.emit()




