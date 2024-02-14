import QtQuick
import QtQuick.Controls
import QtQuick.Dialogs
import QtCore

Rectangle {
    width: 1280
    height: 960
    color: "salmon"

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
                    fileDialog.open()
                }
            }
        }

        Row {
            spacing: 20

            Label {
                text: qsTr("MIN Sigma:")
            }

            TextField {
                id: minSigma
                width: 100
                validator: RegularExpressionValidator { regularExpression: /^[0-9]*$/ }
            }

            Label {
                text: qsTr("MAX Sigma:")
            }

            TextField {
                id: maxSigma
                width: 100
                validator: RegularExpressionValidator { regularExpression: /^[0-9]*$/ }
            }

            Label {
                text: qsTr("NUM Sigma:")
            }

            TextField {
                id: numSigma
                width: 100
                validator: RegularExpressionValidator { regularExpression: /^[0-9]*$/ }
            }
        }

        Row {
            spacing: 20

            Label {
                text: qsTr("MIN Lokal Maxima:")
            }

            TextField {
                id: threshold
                width: 100
                validator: RegularExpressionValidator { regularExpression: /^[0-9.]*$/ }
            }

            Label {
                text: qsTr("Overlapp:")
            }

            TextField {
                id: overlap
                width: 100
                validator: RegularExpressionValidator { regularExpression: /^[0-9.]*$/ }
            }

            CheckBox {
                id: dead
                checked: false
                text: qsTr("Døde Celler")
            }
        }

        Row {
            Column {
                Row {
                    width: 400
                    spacing: 20

                    Button {
                        text: qsTr(" Start ")
                        onClicked: {
                            let minSigmaValue = parseInt(minSigma.text);
                            let maxSigmaValue = parseInt(maxSigma.text);
                            let numSigmaValue = parseInt(numSigma.text);
                            let thresholdValue = parseFloat(threshold.text);
                            let overlapValue = parseFloat(overlap.text);
                            backend.detectBlobs(minSigmaValue, maxSigmaValue, numSigmaValue, thresholdValue, overlapValue, dead.checked);
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

            Column {
                Row {
                    width: 470
                    spacing: 20
                    layoutDirection: Qt.RightToLeft

                    TextField {
                        id: count
                        width: 100
                        placeholderText: qsTr("0")
                        text: backend.count
                        readOnly: true
                    }

                    Label {
                        text: qsTr("Antall:")
                    }
                }
            }
        }
    }

    Connections {
        target: backend
        function onFilePathChanged (path) {
            targetPath.text = path
        }
        function onCountChanged (value) {
            count.text = value
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
