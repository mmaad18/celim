import QtQuick
import QtQuick.Controls
import QtQuick.Dialogs
import QtCore

Rectangle {
    width: 1280
    height: 960
    color: "lightgreen"

    Column {
        spacing: 20
        anchors.centerIn: parent

        Row {
            spacing: 20

            Label {
                text: qsTr("Plassering:")
            }

            TextField {
                id: targetPath
                width: 600
                placeholderText: qsTr("Velg sti til bilde...")
                text: backend.filePath
                readOnly: true
            }

            Button {
                text: qsTr(" Velg Bilde ")
                onClicked: {
                    fileDialog.open();
                }
            }
        }

        Row {
            spacing: 20

            Label {
                text: qsTr("Nedre Grense:")
            }

            TextField {
                id: lowerBound
                width: 170
                validator: RegularExpressionValidator { regularExpression: /^[0-9.]*$/ }
            }

            Label {
                text: qsTr("Øvre Grense:")
            }

            TextField {
                id: upperBound
                width: 170
                validator: RegularExpressionValidator { regularExpression: /^[0-9.]*$/ }
            }

            CheckBox {
                id: histogram
                checked: false
                text: qsTr("Histogram")
            }
        }

        ProgressBar {
            id: progressBar
            width: 880
            value: backend.progress
        }

        Row {
            spacing: 20

            Button {
                text: qsTr(" Start ")
                onClicked: {
                    let lower = parseFloat(lowerBound.text);
                    let upper = parseFloat(upperBound.text);
                    backend.segmentation(lower, upper, histogram.checked);
                }
            }

            Button {
                text: qsTr(" Avslutt ")
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
