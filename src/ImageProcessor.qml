import QtQuick
import QtQuick.Controls
import QtQuick.Dialogs
import QtCore

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: "Image Processing App"

    Rectangle {
        anchors.fill: parent
        color: "white"

        Column {
            spacing: 10
            anchors.centerIn: parent

            Row {
                spacing: 10

                Label {
                    text: qsTr("Plassering:")
                }

                TextField {
                    id: targetPath
                    width: 200
                    placeholderText: qsTr("Velg sti til mappe eller fil...")
                }

                FolderDialog {
                    id: folderDialog
                    currentFolder: StandardPaths.standardLocations(StandardPaths.PicturesLocation)[0]
                    onAccepted: {
                        backend.setFolderPath(folderDialog.folderUrl)
                        targetPath.text = backend.getFilePath()
                    }
                }

                FileDialog {
                    id: fileDialog
                    currentFolder: StandardPaths.standardLocations(StandardPaths.PicturesLocation)[0]
                    onAccepted: backend.setFilePath(fileDialog.fileUrl)
                }

                Button {
                    text: qsTr("Velg Mappe")
                    onClicked: {
                        folderDialog.open()
                    }
                }

                Button {
                    text: qsTr("Velg Bilde")
                    onClicked: {
                        fileDialog.open()
                    }
                }
            }

            // Value goes from 0 to 1, unless specified using "from" and "to"
            ProgressBar {
                id: progressBar
                width: 300
                value: 0
            }

            Row {
                Button {
                    text: qsTr("Start")
                    onClicked: {
                        // Start processing logic
                    }
                }

                Button {
                    text: qsTr("Avslutt")
                    onClicked: {
                        Qt.quit()
                    }
                }

                Button {
                    text: "Process Folder"
                    onClicked: {
                        // Send the folderPath value to Python
                        backend.processFolderPath(targetPath.text)
                    }
                }

            }
        }
    }
}
