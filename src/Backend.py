import os

from PySide6.QtCore import QObject, Signal, Slot, QThread

from src.ImageManipulations import *
from src.Worker import Worker


class Backend(QObject):
    folderPathChanged = Signal(str)
    filePathChanged = Signal(str)
    progressChanged = Signal(float)

    def __init__(self):
        super().__init__()
        self._folderPath = ""
        self._filePath = ""
        self._progress = 0.0

        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)

        # Connect signals
        self.worker.progressChanged.connect(self.setProgress)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.thread.quit)

        # Connect the thread's started signal to the worker's testRun slot
        self.thread.started.connect(self.worker.testRun)

        # Clean up
        self.thread.finished.connect(self.thread.deleteLater)

    def onWorkerFinished(self):
        self.worker.deleteLater()  # Clean up the worker when finished
        self.thread.quit()  # Quit the thread


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
        self.progressChanged.emit(progress)

    '''
    # Batch processing
    '''
    @Slot(bool, bool)
    def batchConvert(self, edgeX, edgeY):
        if not self.thread.isRunning():
            try:
                self.thread.started.disconnect()
            except RuntimeError:
                pass

            #self.thread.started.connect(lambda: self.worker.batchConvert(self.folderPath, edgeX, edgeY))
            self.thread.started.connect(lambda: self.worker.testRun())
            self.thread.start()
        else:
            print("A batch conversion is already running.")


    @Slot()
    def startProcessing(self):
        if not self.thread.isRunning():
            self.thread.start()
        else:
            print("Already running.")



