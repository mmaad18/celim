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
                width: 300
                placeholderText: qsTr("Velg sti til mappe...")
                text: backend.folderPath
                readOnly: true
            }

            Button {
                text: qsTr("Velg mappe")
                onClicked: {
                    folderDialog.open()
                }
            }
        }

        Row {
            spacing: 10

            CheckBox {
                id: edgeX
                checked: true
                text: qsTr("Kantdeteksjon Horisontal")
            }
            CheckBox {
                id: edgeY
                checked: false
                text: qsTr("Kantdeteksjon Vertikal")
            }
        }

        // Value goes from 0 to 1, unless specified using "from" and "to"
        ProgressBar {
            id: progressBar
            width: 445
            value: backend.progress
        }

        Row {
            spacing: 10

            Button {
                text: qsTr("Start")
                onClicked: {
                    //backend.batchConvert(edgeX.checked, edgeY.checked)
                    backend.startProcessing()
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
        function onFolderPathChanged (path) {
            targetPath.text = path
        }
        function onProgressChanged (progress) {
            progressBar.value = progress
        }
    }

    FolderDialog {
        id: folderDialog
        currentFolder: StandardPaths.standardLocations(StandardPaths.PicturesLocation)[0]
        onAccepted: {
            backend.setFolderPath(folderDialog.selectedFolder)
        }
    }
}
