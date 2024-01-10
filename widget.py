import sys
from PySide6.QtWidgets import QApplication, QWidget, QDialog, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from ui_form import Ui_Widget
import pyshorteners
import pyperclip

BITLY_API_KEY = '9e0f4161d322843e355785bc26f68b392b2212e8'

class CustomDialog(QDialog):
    def __init__(self, message, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Error")
        self.setMinimumWidth(150)
        self.setMinimumHeight(100)

        layout = QVBoxLayout()
        label = QLabel(message)
        font = QFont("Arial", 10)
        label.setFont(font)
        label.setAlignment(Qt.AlignCenter)

        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)

        layout.addWidget(label)
        layout.addWidget(ok_button)
        self.setLayout(layout)

class URLShortener:
    @staticmethod
    def shorten_url(long_url):
        type_bitly = pyshorteners.Shortener(api_key=BITLY_API_KEY)
        return type_bitly.bitly.short(long_url)

class Widget(QWidget, Ui_Widget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Connect the clicked signal of the generateButton to the convertUrl method
        self.ui.generateButton.clicked.connect(self.convert_url)

        # Connect the clicked signal of the copyButton to the copy_url method
        self.ui.copyButton.clicked.connect(self.copy_url)

    def convert_url(self):
        """Converts a long URL to a short URL."""
        long_url = self.ui.longUrlBox.toPlainText()

        if long_url:
            short_url = URLShortener.shorten_url(long_url)

            # Set the short URL to the shortUrlBox
            self.ui.shortUrlBox.setPlainText(short_url)

            # Log the short URL for debugging
            print("Short URL:", short_url)
        else:
            # Show an error message in a custom QDialog
            self.show_error_message("Invalid URL")

    def copy_url(self):
        """Copies the short URL to the clipboard."""
        # Use pyperclip to copy the text in shortUrlBox to the clipboard
        pyperclip.copy(self.ui.shortUrlBox.toPlainText())

    def show_error_message(self, message):
        """Shows an error message in a custom QDialog."""
        custom_dialog = CustomDialog(message, self)
        custom_dialog.exec()

if __name__ == "__main__":
    # Create the Qt application
    app = QApplication([])

    # Create an instance of the Widget class
    widget = Widget()

    # Show the widget
    widget.show()

    # Run the application event loop
    sys.exit(app.exec())
