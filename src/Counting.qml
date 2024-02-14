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

        Row {
            spacing: 10

            Label {
                text: qsTr("MIN Sigma:")
            }

            TextField {
                id: minSigma
                width: 50
                validator: RegularExpressionValidator { regularExpression: /^[0-9]*$/ }
            }

            Label {
                text: qsTr("MAX Sigma:")
            }

            TextField {
                id: maxSigma
                width: 50
                validator: RegularExpressionValidator { regularExpression: /^[0-9]*$/ }
            }

            Label {
                text: qsTr("NUM Sigma:")
            }

            TextField {
                id: numSigma
                width: 50
                validator: RegularExpressionValidator { regularExpression: /^[0-9]*$/ }
            }
        }

        Row {
            spacing: 10

            Label {
                text: qsTr("MIN Lokal Maxima:")
            }

            TextField {
                id: threshold
                width: 50
                validator: RegularExpressionValidator { regularExpression: /^[0-9.]*$/ }
            }

            Label {
                text: qsTr("Overlapp:")
            }

            TextField {
                id: overlap
                width: 50
                validator: RegularExpressionValidator { regularExpression: /^[0-9.]*$/ }
            }

            CheckBox {
                id: alive
                checked: true
                text: qsTr("Levende Celler")
            }
        }

        Row {
            spacing: 10

            Button {
                text: qsTr("Start")
                onClicked: {
                    let minSigmaValue = parseInt(minSigma.text);
                    let maxSigmaValue = parseInt(maxSigma.text);
                    let numSigmaValue = parseInt(numSigma.text);
                    let thresholdValue = parseFloat(threshold.text);
                    let overlapValue = parseFloat(overlap.text);
                    backend.detectBlobs(minSigmaValue, maxSigmaValue, numSigmaValue, thresholdValue, overlapValue, alive.checked);
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
    }

    FileDialog {
        id: fileDialog
        currentFolder: StandardPaths.standardLocations(StandardPaths.PicturesLocation)[0]
        onAccepted: {
            backend.setFilePath(fileDialog.selectedFile)
        }
    }
}
