import QtQuick
import QtQuick.Controls
import QtQuick.Dialogs
import QtCore

Rectangle {
    width: 640
    height: 480
    color: "salmon"

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
                width: 300
                placeholderText: qsTr("Velg sti til bilde...")
                text: backend.filePath
                readOnly: true
            }

            Button {
                text: qsTr("Velg Bilde")
                onClicked: {
                    fileDialog.open()
                }
            }
        }

        ProgressBar {
            id: progressBar
            width: 435
            value: backend.progress
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

    Connections {
        target: backend
        function onFilePathChanged (path) {
            targetPath.text = path
        }
        function onProgressChanged (progress) {
            progressBar.value = progress
        }
    }

    FileDialog {
        id: fileDialog
        currentFolder: StandardPaths.standardLocations(StandardPaths.PicturesLocation)[0]
        onAccepted: {
            backend.setFilePath(fileDialog.selectedFile)
        }
    }
}
