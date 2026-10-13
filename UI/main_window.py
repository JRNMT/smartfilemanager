
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Smart File Manager")
        self.resize(1000, 650)

        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        self.folder_label = QLabel("No folder selected")
        self.browse_button = QPushButton("Browse Folder")

        layout.addWidget(self.folder_label)
        layout.addWidget(self.browse_button)
        layout.addStretch()

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.browse_button.clicked.connect(self.select_folder)

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(
            self,
            "Select a Folder",
            ""
        )

        if folder_path:
            self.folder_label.setText(folder_path)
            print(f"Selected folder: {folder_path}")
