import requests
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QMessageBox, QTextEdit
)
from PyQt5.QtGui import QFont
import sys

# API Configuration
API_KEY = "AIzaSyCsIn3X8MsQb1eI_8EfFT10dsjFrlIp2J4"
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"

headers = {
    "Content-Type": "application/json"
}

class APIGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Generative Language API")
        self.setGeometry(100, 100, 600, 400)

        # Main container
        container = QWidget()
        self.setCentralWidget(container)

        # Layouts
        main_layout = QVBoxLayout()
        input_layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        # Header
        header_label = QLabel("Generative Language API")
        header_label.setFont(QFont("Helvetica", 16))
        header_label.setStyleSheet("color: #333;")
        main_layout.addWidget(header_label)

        # Input Field
        input_label = QLabel("\u0e1b\u0e49\u0e2d\u0e19\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21:\n")
        input_label.setFont(QFont("Helvetica", 12))
        input_layout.addWidget(input_label)
        self.input_field = QLineEdit()
        self.input_field.setFont(QFont("Helvetica", 12))
        self.input_field.setStyleSheet(
            "border: 1px solid #ccc; padding: 8px; border-radius: 5px;"
        )
        input_layout.addWidget(self.input_field)

        # Generate Button
        generate_button = QPushButton("Generate")
        generate_button.setFont(QFont("Helvetica", 12))
        generate_button.setStyleSheet(
            "background-color: #4CAF50; color: white; padding: 8px 16px; border: none; border-radius: 5px;"
        )
        generate_button.clicked.connect(self.generate_content)
        button_layout.addWidget(generate_button)

        # Output Field
        output_label = QLabel("\u0e1c\u0e25\u0e25\u0e31\u0e1e:\n")
        output_label.setFont(QFont("Helvetica", 12))
        input_layout.addWidget(output_label)
        self.output_text = QTextEdit()
        self.output_text.setFont(QFont("Helvetica", 12))
        self.output_text.setReadOnly(True)
        self.output_text.setStyleSheet(
            "border: 1px solid #ccc; padding: 8px; border-radius: 5px; background-color: #f9f9f9;"
        )
        input_layout.addWidget(self.output_text)

        # Add layouts to main layout
        main_layout.addLayout(input_layout)
        main_layout.addLayout(button_layout)

        # Set main layout
        container.setLayout(main_layout)

    def generate_content(self):
        user_input = self.input_field.text()
        if not user_input.strip():
            QMessageBox.critical(self, "Error", "\u0e01\u0e23\u0e38\u0e13\u0e32\u0e1b\u0e49\u0e2d\u0e19\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21")
            return

        data = {
            "contents": [
                {
                    "parts": [
                        {"text": user_input}
                    ]
                }
            ]
        }

        try:
            response = requests.post(f"{url}?key={API_KEY}", headers=headers, json=data)

            if response.status_code == 200:
                result = response.json()
                self.output_text.setText(str(result))
            else:
                QMessageBox.critical(
                    self,
                    "Error",
                    f"API Request Failed: {response.status_code}\n{response.text}"
                )
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request failed: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = APIGeneratorApp()
    window.show()
    sys.exit(app.exec_())
