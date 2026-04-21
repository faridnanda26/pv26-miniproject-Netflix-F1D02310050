import sys
from PySide6.QtWidgets import QApplication

# Import dari module kita
from Database.DB_Manager import DatabaseManager
from UI.Main_Window import MainWindow

def load_stylesheet(filepath):
        """Load QSS dari file dan return sebagai string"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"QSS file not found: {filepath}")
            return ""

def main():
    # 1. Buat aplikasi
    app = QApplication(sys.argv)

    stylesheet = load_stylesheet("Style.qss")
    app.setStyleSheet(stylesheet)
    
    # 2. Buat database manager
    db = DatabaseManager('Netflix.db')
    
    # 3. Buat window, kirim db sebagai parameter
    window = MainWindow(db)
    window.show()
    
    # 4. Jalankan
    sys.exit(app.exec())


if __name__ == "__main__":
    main()