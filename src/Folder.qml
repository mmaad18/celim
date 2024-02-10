import QtQuick
import QtQuick.Controls
import QtQuick.Dialogs
import QtCore

Rectangle {
    width: 640
    height: 480
    color: "lightblue"

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
                    backend.setFolderPath(folderDialog.selectedFolder)
                    targetPath.text = backend.getFolderPath()
                }
            }

            Button {
                text: qsTr("Choose Folder")
                onClicked: {
                    folderDialog.open()
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
        }
    }
}
