import inspect
import logging

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QDialog, QApplication, QStyleFactory, QGroupBox, QVBoxLayout, QLabel, QGridLayout,
                             QFileDialog, QTextEdit, QPushButton)

class DataMigrationTool(QDialog):
    def __init__(self, parent=None):
        super(DataMigrationTool, self).__init__(parent)
        QApplication.setStyle(QStyleFactory.create('Fusion'))
        #print(QStyleFactory.keys())
        self.sourcePath = ""
        self.destinationPath = ""

        self.sourceLbl = None
        self.destinationLbL = None
        self.output = None

        self.createTopGroup()
        self.createBottomGroup()

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.topGroupBox, 1, 0)
        mainLayout.addWidget(self.bottomGroupBox, 2, 0)
        self.setLayout(mainLayout)

        self.setWindowTitle("Data Migration Tool")
        self.setGeometry(1000, 100, 1000, 800)

    def createTopGroup(self):
        self.topGroupBox = QGroupBox("Inputs")

        self.sourceLbl = QLabel("Source:")
        source = QPushButton("Browse Source")
        source.clicked.connect(lambda: self.browse_path("source"))

        self.destinationLbL = QLabel("Destination:")
        destination = QPushButton("Browse Destination")
        destination.clicked.connect(lambda: self.browse_path("destination"))

        transfer = QPushButton("Transfer")
        transfer.clicked.connect((lambda: self.transfer_data()))

        layout = QGridLayout()
        layout.addWidget(self.sourceLbl,1,0)
        layout.addWidget(source, 0,0)
        layout.addWidget(destination,0,1)
        layout.addWidget(self.destinationLbL,1,1)

        self.topGroupBox.setLayout(layout)

    def createBottomGroup(self):
        self.bottomGroupBox = QGroupBox("Output")
        self.output = QTextEdit()
        self.output.setDisabled(True)
        self.output.setPlainText("Some Text Here")
        layout = QGridLayout()
        layout.addWidget(self.output)
        self.bottomGroupBox.setLayout(layout)

    def browse_path(self, location):
        path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if location == "source":
            self.sourceLbl.setText(path)
            self.sourcePath = path
        elif location == "destination":
            self.destinationLbL.setText(path)
            self.destinationPath = path
           #temp for testing
        self.transfer_data()

    def transfer_data(self):
        print("Source Path: " + self.sourcePath)
        print("Destination Path: " + self.destinationPath)

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    gallery = DataMigrationTool()
    gallery.show()
    sys.exit(app.exec_())


