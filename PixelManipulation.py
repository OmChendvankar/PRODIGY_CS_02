import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel,
    QLineEdit, QRadioButton, QFileDialog, QMessageBox, QHBoxLayout, QSpacerItem, QSizePolicy
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PIL import Image
import numpy as np


class ImageEncryptionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Pixel Manipulation Tool')

        layout = QVBoxLayout()

        self.key_label = QLabel('Enter Key (Integer 0-255):')
        layout.addWidget(self.key_label)

        self.key_entry = QLineEdit(self)
        layout.addWidget(self.key_entry)

        self.method_label = QLabel('Encryption Method:')
        layout.addWidget(self.method_label)

        self.add_method = QRadioButton('Add Value')
        self.add_method.setChecked(True)
        layout.addWidget(self.add_method)

        self.swap_method = QRadioButton('Swap Pixels')
        layout.addWidget(self.swap_method)

        # Input Image selection
        input_layout = QHBoxLayout()
        self.input_button = QPushButton('Select Input Image', self)
        self.input_button.clicked.connect(self.select_file)
        input_layout.addWidget(self.input_button)

        self.input_path_label = QLabel("No file selected")
        input_layout.addWidget(self.input_path_label)
        layout.addLayout(input_layout)

        # Output Image selection
        output_layout = QHBoxLayout()
        self.output_button = QPushButton('Select Output Image', self)
        self.output_button.clicked.connect(self.save_file)
        output_layout.addWidget(self.output_button)

        self.output_path_label = QLabel("No file selected")
        output_layout.addWidget(self.output_path_label)
        layout.addLayout(output_layout)

        self.encrypt_button = QPushButton('Encrypt Image', self)
        self.encrypt_button.clicked.connect(self.encrypt_image)
        layout.addWidget(self.encrypt_button)

        self.decrypt_button = QPushButton('Decrypt Image', self)
        self.decrypt_button.clicked.connect(self.decrypt_image)
        layout.addWidget(self.decrypt_button)

        # Spacer to center the image
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Center the image label
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(500, 400)  # Set a larger fixed size for QLabel
        layout.addWidget(self.image_label, alignment=Qt.AlignCenter)

        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(layout)
        self.setGeometry(100, 100, 500, 600)  # Adjust window size to accommodate larger QLabel

        # Store file paths
        self.input_path = None
        self.output_path = None

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg)"
        )
        if file_path:
            self.input_path = file_path
            self.input_path_label.setText(file_path)
            self.load_image(self.input_path)

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Image", "", "PNG files (*.png)"
        )
        if file_path:
            self.output_path = file_path
            self.output_path_label.setText(file_path)

    def load_image(self, path):
        pixmap = QPixmap(path)
        # Scale the pixmap to fit within the QLabel while preserving aspect ratio
        scaled_pixmap = pixmap.scaled(
            self.image_label.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.image_label.setPixmap(scaled_pixmap)

    def swap_pixels(self, pixels):
        height, width, _ = pixels.shape
        for i in range(0, height - 1, 2):
            for j in range(0, width - 1, 2):
                if i + 1 < height and j + 1 < width:
                    pixels[i, j], pixels[i + 1, j + 1] = pixels[i + 1, j + 1], pixels[i, j]
        return pixels

    def add_value(self, pixels, value):
        return np.clip(pixels + value, 0, 255)

    def subtract_value(self, pixels, value):
        return np.clip(pixels - value, 0, 255)

    def encrypt_image(self):
        if not self.input_path:
            QMessageBox.warning(self, "Warning", "Please select an input image first.")
            return
        if not self.output_path:
            QMessageBox.warning(self, "Warning", "Please select an output file first.")
            return
        try:
            key = int(self.key_entry.text())
            method = "add" if self.add_method.isChecked() else "swap"
            self.process_image(self.input_path, self.output_path, key, method, True)
            self.load_image(self.output_path)
            QMessageBox.information(self, "Success", "Image encrypted successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def decrypt_image(self):
        if not self.input_path:
            QMessageBox.warning(self, "Warning", "Please select an input image first.")
            return
        if not self.output_path:
            QMessageBox.warning(self, "Warning", "Please select an output file first.")
            return
        try:
            key = int(self.key_entry.text())
            method = "add" if self.add_method.isChecked() else "swap"
            self.process_image(self.input_path, self.output_path, key, method, False)
            self.load_image(self.output_path)
            QMessageBox.information(self, "Success", "Image decrypted successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def process_image(self, input_path, output_path, key, method, encrypt):
        image = Image.open(input_path)
        pixels = np.array(image)
        if method == "swap":
            if encrypt:
                pixels = self.swap_pixels(pixels)
                pixels = self.add_value(pixels, key)
            else:
                pixels = self.subtract_value(pixels, key)
                pixels = self.swap_pixels(pixels)
        elif method == "add":
            if encrypt:
                pixels = self.add_value(pixels, key)
            else:
                pixels = self.subtract_value(pixels, key)
        processed_image = Image.fromarray(pixels.astype(np.uint8))
        processed_image.save(output_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageEncryptionApp()
    ex.show()
    sys.exit(app.exec())