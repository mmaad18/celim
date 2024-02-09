from PySide6.QtCore import QObject, Slot


class Backend(QObject):

    def __init__(self):
        super().__init__()
        self.folderPath = ""
        self.filePath = ""

    @Slot(str)
    def getFolderPath(self):
        # This method will be called from QML
        return self.folderPath

    @Slot(str)
    def getFilePath(self):
        # This method will be called from QML
        return self.filePath

    @Slot(str)
    def setFolderPath(self, folderPath):
        # Convert URL to local file path
        if folderPath.startswith('file:///'):
            folderPath = folderPath[8:]
        print(f"Selected folder: {folderPath}")
        self.folderPath = folderPath


    @Slot(str)
    def setFilePath(self, filePath):
        # Convert URL to local file path
        if filePath.startswith('file:///'):
            filePath = filePath[8:]
        print(f"Selected file: {filePath}")
        self.filePath = filePath
