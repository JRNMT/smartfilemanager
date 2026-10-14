
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from Core.scanner import scan_folder

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BEAF")
        self.resize(1000, 500)

        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        self.folderlabel = QLabel("No folder selected")
        self.searchfolderbutton = QPushButton("Open folder")

        layout.addWidget(self.folderlabel)
        layout.addWidget(self.searchfolderbutton)
        layout.addStretch()

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.searchfolderbutton.clicked.connect(self.select_folder)

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "select a folder", "")
        if folder_path:
            self.folderlabel.setText(folder_path)
            scan_folder(folder_path)
