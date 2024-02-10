import QtQuick
import QtQuick.Controls
import QtQuick.Dialogs
import QtCore
import QtQml

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
                placeholderText: qsTr("Velg sti til mappe...")
                text: backend.folderPath
            }

            Connections {
                target: backend
                function onFolderPathChanged (path) {
                    targetPath.text = path
                }
            }

            FolderDialog {
                id: folderDialog
                currentFolder: StandardPaths.standardLocations(StandardPaths.PicturesLocation)[0]
                onAccepted: {
                    backend.setFolderPath(folderDialog.selectedFolder)
                }
            }

            Button {
                text: qsTr("Velg mappe")
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
