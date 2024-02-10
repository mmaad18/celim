from PySide6.QtCore import QObject, Signal, Slot

class Backend(QObject):
    folderPathChanged = Signal(str)  # Signal to emit when the folder path changes
    filePathChanged = Signal(str)    # Signal to emit when the file path changes

    def __init__(self):
        super().__init__()
        self._folderPath = ""
        self._filePath = ""

    @property
    def folderPath(self):
        return self._folderPath

    @folderPath.setter
    def folderPath(self, value):
        if self._folderPath != value:
            self._folderPath = value
            self.folderPathChanged.emit(self._folderPath)  # Emit signal with new value

    @property
    def filePath(self):
        return self._filePath

    @filePath.setter
    def filePath(self, value):
        if self._filePath != value:
            self._filePath = value
            self.filePathChanged.emit(self._filePath)  # Emit signal with new value

    @Slot(str)
    def setFolderPath(self, folderPath):
        # Convert URL to local file path
        if folderPath.startswith('file:///'):
            folderPath = folderPath[8:]
        print(f"Selected folder: {folderPath}")
        self.folderPath = folderPath  # Use the setter

    @Slot(str)
    def setFilePath(self, filePath):
        # Convert URL to local file path
        if filePath.startswith('file:///'):
            filePath = filePath[8:]
        print(f"Selected file: {filePath}")
        self.filePath = filePath  # Use the setter
