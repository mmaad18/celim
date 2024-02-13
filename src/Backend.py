
from PySide6.QtCore import QObject, Signal, Slot, QThread

from Worker import Worker


class Backend(QObject):
    folderPathChanged = Signal(str)
    filePathChanged = Signal(str)
    progressChanged = Signal(float)

    def __init__(self):
        super().__init__()
        self._folderPath = ""
        self._filePath = ""
        self._progress = 0.0

        self.setupWorkerAndThread()

    def setupWorkerAndThread(self):
        self.thread = QThread()
        self.worker = Worker()  # Make sure Worker is properly defined elsewhere
        self.worker.moveToThread(self.thread)

        # Connect signals
        self.worker.progressChanged.connect(self.setProgress)
        self.worker.finished.connect(self.thread.quit)  # Request thread to quit when worker is done
        self.thread.finished.connect(self.cleanUp)  # Cleanup when thread finishes

        self.worker.finished.connect(self.worker.deleteLater)  # Ensure worker is deleted safely
        self.thread.finished.connect(self.thread.deleteLater)  # Ensure thread is deleted safely

    def cleanUp(self):
        # Cleanup has been simplified as deletion and quit requests are handled via signals
        print("Cleanup completed")

        # Optionally, reinitialize the worker and thread for the next use if needed
        self.thread = None
        self.worker = None


    '''
    # Folder path setup
    '''
    @property
    def folderPath(self):
        return self._folderPath

    @folderPath.setter
    def folderPath(self, value):
        if self._folderPath != value:
            self._folderPath = value
            self.folderPathChanged.emit(self._folderPath)

    @Slot(str)
    def setFolderPath(self, folderPath):
        if folderPath.startswith('file:///'):
            folderPath = folderPath[8:]
        print(f"Selected folder: {folderPath}")
        self.folderPath = folderPath

    '''
    # File path setup
    '''
    @property
    def filePath(self):
        return self._filePath

    @filePath.setter
    def filePath(self, value):
        if self._filePath != value:
            self._filePath = value
            self.filePathChanged.emit(self._filePath)

    @Slot(str)
    def setFilePath(self, filePath):
        if filePath.startswith('file:///'):
            filePath = filePath[8:]
        print(f"Selected file: {filePath}")
        self.filePath = filePath

    '''
    # Progress setup
    '''
    @property
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self, value):
        if self._progress != value:
            self._progress = value
            self.progressChanged.emit(self._progress)

    @Slot(float)
    def setProgress(self, progress):
        print(f"Progress: {progress}")
        self.progress = progress

    '''
    # Batch processing
    '''
    @Slot(bool, bool)
    def batchConvert(self, edgeX, edgeY):
        if not self.thread or not self.thread.isRunning():
            self.setupWorkerAndThread()

            self.worker.setBatchParams(self.folderPath, edgeX, edgeY)
            self.thread.started.connect(self.worker.batchConvert)
            self.thread.start()
        else:
            print("A batch conversion is already running.")

    '''
    # Segmentation
    '''
    @Slot(float, float)
    def segmentation(self, lowerThreshold, upperThreshold):
        if not self.thread or not self.thread.isRunning():
            self.setupWorkerAndThread()

            self.worker.setSegmentationParams(self.filePath, lowerThreshold, upperThreshold)
            self.thread.started.connect(self.worker.segmentation)
            self.thread.start()
        else:
            print("A segmentation is already running.")



