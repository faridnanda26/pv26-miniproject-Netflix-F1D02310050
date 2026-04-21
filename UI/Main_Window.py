import csv
import sqlite3
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QLineEdit, QPushButton, QLabel, QSpinBox,
    QTimeEdit, QTableWidget, QTableWidgetItem, QMessageBox,
    QStyle, QDialog, QFormLayout, QFileDialog
)

from PySide6.QtGui import QAction, QKeySequence, QIcon
from PySide6.QtCore import Qt

from CustomDialogs.Dialogs import MovieInputDialog, MovieUpdateDialog

class MainWindow(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.setWindowTitle("Netflix")
        self.resize(700,500)
        self.center_on_screen()

        self.db = db
        self.selected_id = None

        self.setup_ui()
        self.load_data()
        self.create_actions()
        self.create_menus()
        self.create_toolbars()

    def setup_ui(self):
        self.central = QWidget()
        self.setCentralWidget(self.central)

        layout = QVBoxLayout(self.central)

        # Form Input
        container_search = QWidget()
        container_search.setObjectName("container")
        form = QHBoxLayout(container_search)
        self.search_label = QLabel("Search:")
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Enter Movie Title...")
        self.search_input.textChanged.connect(self.find_movie)
        form.addWidget(self.search_label)
        form.addWidget(self.search_input)

        layout.addWidget(container_search)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Title", "Duration", "Genre", "Year"])
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.clicked.connect(self.id_selection)

        layout.addWidget(self.table)


    def create_actions(self):
        style = self.style()

        # About
        self.about_action = QAction("About", self)
        self.about_action.setIcon(style.standardIcon(QStyle.SP_MessageBoxInformation))
        self.about_action.setStatusTip("About")
        self.about_action.triggered.connect(self.show_version)

        # Add
        self.add_action = QAction("Add", self)
        self.add_action.setIcon(QIcon("Icons/add.png"))
        self.add_action.setStatusTip("Add New Movie")
        self.add_action.triggered.connect(self.add_movie)

        # Delete
        self.delete_action = QAction("Delete", self)
        self.delete_action.setIcon(QIcon("Icons/delete.png"))
        self.delete_action.setStatusTip("Delete Movie Now")
        self.delete_action.triggered.connect(self.delete_movie)

        # Update
        self.update_action = QAction("Update", self)
        self.update_action.setIcon(QIcon("Icons/update.png"))
        self.update_action.setStatusTip("update New Movie")
        self.update_action.triggered.connect(self.update_movie)

        # Export
        self.export_action = QAction("Export CSV", self)
        self.export_action.setIcon(QIcon("Icons/export.png"))
        self.export_action.setStatusTip("Export to CSV")
        self.export_action.triggered.connect(self.export_csv)

    def create_menus(self):
        menu_bar = self.menuBar()

        help_menu = menu_bar.addMenu("Help")
        help_menu.addAction(self.about_action)

    def create_toolbars(self):
        file_toolbar = self.addToolBar("File")
        file_toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        file_toolbar.addAction(self.add_action)
        file_toolbar.addAction(self.delete_action)
        file_toolbar.addAction(self.update_action)
        file_toolbar.addAction(self.export_action)

    def center_on_screen(self):
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)

    def load_data(self):
        data = self.db.get_all()
        self.show_to_table(data)

    def show_to_table(self, data):
        self.table.setRowCount(0)
        for row_data in data:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(str(row_data['id'])))
            self.table.setItem(row, 1, QTableWidgetItem(row_data['title']))
            self.table.setItem(row, 2, QTableWidgetItem(row_data['duration']))
            self.table.setItem(row, 3, QTableWidgetItem(row_data['genre']))
            self.table.setItem(row, 4, QTableWidgetItem(str(row_data['year'])))

    def add_movie(self):
        dialog = MovieInputDialog(self)
        
        if dialog.exec() == QDialog.Accepted:
            data = dialog.get_data()
            try:
                self.db.add(data["title"], data["duration"], data["genre"], data["year"])
                QMessageBox.information(self, "Success", "Movie added!")
                
                self.load_data()
            
            except sqlite3.IntegrityError:
                QMessageBox.warning(self, "Error", "The movie has been registered!")

    def id_selection(self):
        row = self.table.currentRow()
        if row >= 0:
            self.selected_id = int(self.table.item(row, 0).text())

    def delete_movie(self):
        if not self.selected_id:
            QMessageBox.warning(
                self, 
                "Warning",
                "Please select a movie"
            )
            return
        
        reply = QMessageBox.question(self, "Confirmation", "Are you sure you want to delete this movie?")
        if reply == QMessageBox.Yes:
            self.db.delete(self.selected_id)
            self.load_data()

    def update_movie(self):
        if not self.selected_id:
            QMessageBox.warning(
                self, 
                "Warning",
                "Please select a movie"
            )
            return
        
        data = self.db.find(self.selected_id)
        data_dict = data[0]

        dialog = MovieUpdateDialog(self, data_dict)
        
        if dialog.exec() == QDialog.Accepted:
            data_dialog = dialog.get_data()
            try:
                self.db.update(data_dict["id"], data_dialog["title"], data_dialog["duration"], data_dialog["genre"], data_dialog["year"])
                QMessageBox.information(self, "Success", "Movie updated!")
                
                self.load_data()
            
            except Exception as e:
                QMessageBox.critical(self, "System Error", f"An unexpected error occurred: {str(e)}")
        
    def find_movie(self, text):
        searched_movie = self.db.find(text) if text else self.db.get_all()
        self.show_to_table(searched_movie)

    def show_version(self):
        version_info = (
            "Netflix Movie Manager\n"
            "Version: 1.0.4\n\n"
            "Developed with: PySide6 & SQLite\n"
            "Build Date: April 2026\n"
            "© 2026 Farid Dev."
        )
        
        QMessageBox.information(
            self,
            "App Version", 
            version_info
        )

    def export_csv(self):
        filepath, _ = QFileDialog.getSaveFileName(
            self, "Export CSV", "Netflix.csv", "CSV Files (*.csv)"
        )
        if not filepath:
            return
        
        try:
            data = self.db.get_all()
            with open(filepath, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Title", "Duration", "Genre", "Year"])
                for r in data:
                    writer.writerow([r['id'], r['title'], r['duration'], r['genre'], r['year']])
            QMessageBox.information(self, "Success", f"Export Success!\n{filepath}")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
