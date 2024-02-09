from PySide6.QtCore import QObject, Slot

class Backend(QObject):

    def __init__(self):
        super().__init__()
        self.folderPath = ""

    @Slot(result=str)
    def getFolderPath(self):
        # This method will be called from QML
        return self.folderPath


    @Slot(str)
    def processFolderPath(self, folderPath):
        # Do something with the folder_path
        print(folderPath)
