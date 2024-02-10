import QtQuick
import QtQuick.Controls
import QtQuick.Dialogs
import QtCore

Rectangle {
    width: 640
    height: 480
    color: "lightgreen"

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

            FileDialog {
                id: fileDialog
                currentFolder: StandardPaths.standardLocations(StandardPaths.PicturesLocation)[0]
                onAccepted: backend.setFilePath(fileDialog.fileUrl)
            }

            Button {
                text: qsTr("Choose Image")
                onClicked: {
                    fileDialog.open()
                }
            }
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
