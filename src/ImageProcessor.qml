import QtQuick
import QtQuick.Controls
import QtQuick.Dialogs
import QtQuick.Layouts
import QtCore

ApplicationWindow {
    title: "Image Processing App"
    width: 640
    height: 480
    visible: true

    TabBar {
        id: tabBar
        width: parent.width
        currentIndex: stackView.currentIndex
        TabButton {
            text: qsTr("Single File")
        }
        TabButton {
            text: qsTr("Mappe")
        }
    }

    StackLayout {
        id: stackView
        anchors.fill: parent
        anchors.topMargin: tabBar.height
        currentIndex: tabBar.currentIndex

        Item {
            id: singleFile
            Loader { source: "SingleFile.qml" }
        }

        Item {
            id: folder
            Loader { source: "Folder.qml" }
        }
    }
}
