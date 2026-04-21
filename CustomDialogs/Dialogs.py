from PySide6.QtWidgets import (
    QVBoxLayout, QDialog, QDialogButtonBox,
    QLineEdit, QComboBox, QSpinBox, QFormLayout,
    QTimeEdit, QMessageBox
)

from PySide6.QtCore import QTime

from Logic.Validator import Validator

class MovieInputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add A Movie")
        self.setMinimumWidth(400)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        form_layout = QFormLayout()
        
        # Title
        self.title_input = QLineEdit()
        form_layout.addRow("Title:", self.title_input)
        
        # Duration
        self.duration_input = QTimeEdit()
        self.duration_input.setDisplayFormat("h 'Hours' m 'Minutes'") 
        self.duration_input.setTime(QTime(1, 30))
        form_layout.addRow("Duration:", self.duration_input)

        # Genre
        self.genre_input = QComboBox()
        self.genre_input.addItems([
            "Action", "Adventure", "Comedy", "Drama", "Horror",
            "Animation", "Romance", "Sci-Fi", "Thriller"
        ])
        form_layout.addRow("Genre", self.genre_input)

        # Year
        self.year_input = QSpinBox()
        self.year_input.setRange(1888, 2030) 
        self.year_input.setValue(2026)
        self.year_input.setGroupSeparatorShown(False)
        form_layout.addRow("Year", self.year_input)

        layout.addLayout(form_layout)
        
        button_box = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        button_box.accepted.connect(self.validate_and_accept)
        button_box.rejected.connect(self.reject)
        
        layout.addWidget(button_box)

    def validate_and_accept(self):
        valid, error = Validator.title_validation(self.title_input.text())

        if not valid:
            QMessageBox.warning(
                self,
                "Warning",
                error
            )
            self.title_input.setFocus()
            return
        
        self.accept()

    def get_data(self):
        return {
            "title": self.title_input.text().strip(),
            "duration": self.duration_input.time().toString("HH:mm"),
            "genre": self.genre_input.currentText(),
            "year": self.year_input.value()
        }
    
class MovieUpdateDialog(QDialog):
    def __init__(self, parent=None, data=None):
        super().__init__(parent)
        self.setWindowTitle("Update A Movie")
        self.setMinimumWidth(400)

        self.data = data

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        form_layout = QFormLayout()
        
        # Title
        self.title_input = QLineEdit()
        self.title_input.setText(self.data["title"])
        form_layout.addRow("Title:", self.title_input)
        
        # Duration
        self.duration_input = QTimeEdit()
        self.duration_input.setDisplayFormat("h 'Hours' m 'Minutes'") 
        duration_object = QTime.fromString(self.data["duration"], "HH:mm")
        if duration_object.isValid():
            self.duration_input.setTime(duration_object)
        else:
            self.duration_input.setTime(QTime(1, 0)) 
        form_layout.addRow("Duration:", self.duration_input)

        # Genre
        self.genre_input = QComboBox()
        self.genre_input.addItems([
            "Action", "Adventure", "Comedy", "Drama", "Horror",
            "Animation", "Romance", "Sci-Fi", "Thriller"
        ])
        self.genre_input.setCurrentText(self.data["genre"])
        form_layout.addRow("Genre", self.genre_input)

        # Year
        self.year_input = QSpinBox()
        self.year_input.setRange(1888, 2030) 
        self.year_input.setValue(2026)
        self.year_input.setGroupSeparatorShown(False)
        self.year_input.setValue(self.data["year"])
        form_layout.addRow("Year", self.year_input)

        layout.addLayout(form_layout)
        
        button_box = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        button_box.accepted.connect(self.validate_and_accept)
        button_box.rejected.connect(self.reject)
        
        layout.addWidget(button_box)

    def validate_and_accept(self):
        valid, error = Validator.title_validation(self.title_input.text())

        if not valid:
            QMessageBox.warning(
                self,
                "Warning",
                error
            )
            self.title_input.setFocus()
            return
        
        self.accept()

    def get_data(self):
        return {
            "title": self.title_input.text().strip(),
            "duration": self.duration_input.time().toString("HH:mm"),
            "genre": self.genre_input.currentText(),
            "year": self.year_input.value()
        }