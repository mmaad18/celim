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
                width: 300
                placeholderText: qsTr("Velg sti til bilde...")
                text: backend.filePath
                readOnly: true
            }

            FileDialog {
                id: fileDialog
                currentFolder: StandardPaths.standardLocations(StandardPaths.PicturesLocation)[0]
                onAccepted: backend.setFilePath(fileDialog.fileUrl)
            }

            Button {
                text: qsTr("Velg Bilde")
                onClicked: {
                    fileDialog.open()
                }
            }
        }

        Row {
            spacing: 10

            Label {
                text: qsTr("Nedre Grense:")
            }

            TextField {
                id: lowerBound
                width: 90
                validator: DoubleValidator { bottom: 0.0; top: 1.0; decimals: 10 }
            }

            Label {
                text: qsTr("Øvre Grense:")
            }

            TextField {
                id: upperBound
                width: 90
                validator: DoubleValidator { bottom: 0.0; top: 1.0; decimals: 10 }
            }
        }

        Row {
            spacing: 10

            Button {
                text: qsTr("Segmenter")
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
