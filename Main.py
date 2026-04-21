"""
Nama    : Farid Nanda Syauqi
NIM     : F1D02310050
Kelas   : C
"""

import sys
from PySide6.QtWidgets import QApplication

# Import dari module
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

    # 2. Terapkan style qss eksternal
    stylesheet = load_stylesheet("Style.qss")
    app.setStyleSheet(stylesheet)
    
    # 3. Buat database manager
    db = DatabaseManager('Netflix.db')
    
    # 4. Buat window, kirim db sebagai parameter
    window = MainWindow(db)
    window.show()
    
    # 5. Jalankan
    sys.exit(app.exec())


if __name__ == "__main__":
    main()