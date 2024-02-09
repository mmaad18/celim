import QtQuick
import QtQuick.Controls

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
                    text: "Mappe plassering:"
                }

                TextField {
                    id: folderPath
                    width: 200
                    placeholderText: qsTr("Path to folder containing files")
                }

                Button {
                    text: "Get Folder Path"
                    onClicked: {
                        // Call the Python method from QML
                        var path = backend.getFolderPath()
                        console.log("The folder path is: " + path)
                    }
                }

            }

            ProgressBar {
                id: progressBar
                width: 200
                value: 0 // This will be updated dynamically
            }

            Row {
                Button {
                    text: "Start"
                    onClicked: {
                        // Start processing logic
                    }
                }

                Button {
                    text: "Avslutt"
                    onClicked: {
                        Qt.quit()
                    }
                }

                Button {
                    text: "Process Folder"
                    onClicked: {
                        // Send the folderPath value to Python
                        backend.processFolderPath(folderPath.text)
                    }
                }

            }
        }
    }
}
