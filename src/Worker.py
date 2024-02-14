
import os

from PySide6.QtCore import Slot, Signal, QObject
from ImageManipulations import *
from skimage import feature


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

        self.minSigma = 10
        self.maxSigma = 30
        self.numSigma = 1
        self.threshold = 0.1
        self.overlap = 0.9
        self.alive = True

    def setBatchParams(self, folderPath, edgeX, edgeY):
        self.folderPath = folderPath
        self.edgeX = edgeX
        self.edgeY = edgeY

    def setSegmentationParams(self, filePath, lowerThreshold, upperThreshold):
        self.filePath = filePath
        self.lowerThreshold = lowerThreshold
        self.upperThreshold = upperThreshold

    def setDetectBlobsParams(self, filePath, minSigma, maxSigma, numSigma, threshold, overlap, alive):
        self.filePath = filePath
        self.minSigma = minSigma
        self.maxSigma = maxSigma
        self.numSigma = numSigma
        self.threshold = threshold
        self.overlap = overlap
        self.alive = alive

    @Slot()
    def batchConvert(self):
        files = os.listdir(self.folderPath)
        tif_files = [file for file in files if file.endswith('.tif')]
        file_count = len(tif_files)

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

        image_height, image_width = image_gray.shape
        output = np.zeros((image_height, image_width))

        progress = 0.0
        modulo = np.ceil(image_height / 10)
        self.progressChanged.emit(progress)

        for i in range(image_height):
            if i % modulo == 0:
                progress = i / image_height
                self.progressChanged.emit(progress)

            for j in range(image_width):
                if self.lowerThreshold < image_gray[i, j] < self.upperThreshold:
                    output[i, j] = 1.0

        save_image_gray(output, f'out/{file_name}_segmented.png')

        self.progressChanged.emit(1.0)
        self.finished.emit()


    @Slot()
    def detectBlobs(self):
        image_gray = load_image_gray(self.filePath)
        file_name = self.filePath.split('/')[-1].split('.')[0]

        blobs_log = feature.blob_log(
            image=image_gray,
            min_sigma=self.minSigma,
            max_sigma=self.maxSigma,
            num_sigma=self.numSigma,
            threshold=self.threshold,
            overlap=self.overlap,
        )

        dpi = 300
        width, height = image_gray.shape
        inches = np.ceil(height / dpi), np.ceil(width / dpi)

        fig, ax = plt.subplots(1, 1, figsize=inches)
        ax.imshow(image_gray, cmap='gray')

        color = 'green' if self.alive else 'red'

        for blob in blobs_log:
            y, x, r = blob
            c = plt.Circle((x, y), r, color=color, linewidth=1, fill=False)
            ax.add_patch(c)

        plt.axis('off')
        plt.savefig(f'out/{file_name}_count.png', dpi=dpi, bbox_inches='tight', pad_inches=0.0)
        plt.close()

        self.finished.emit()




