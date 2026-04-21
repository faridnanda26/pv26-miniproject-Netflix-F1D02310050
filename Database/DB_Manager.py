import sqlite3

class DatabaseManager:
    def __init__(self, db_name='Netflix.db'):
        self.db_name = db_name
        self.create_table()
    
    # Membuat koneksi ke database
    def get_connection(self):
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        return conn
    
    # Membuat tabel yang diperlukan
    def create_table(self):
        with self.get_connection() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS movie (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL UNIQUE,
                    duration INTEGER NOT NULL,
                    genre TEXT NOT NULL,
                    year INTEGER NOT NULL
                )
            ''')
    
    # Query add data
    def add(self, title, duration, genre, year):
        with self.get_connection() as conn:
            conn.execute(
                'INSERT INTO movie (title, duration, genre, year) VALUES (?, ?, ?, ?)', # Prepared Statement
                (title, duration, genre, year)
            )
    
    # Mengambil semua data pada tabel movie
    def get_all(self):
        with self.get_connection() as conn:
            return conn.execute(
                'SELECT * FROM movie ORDER BY title'
            ).fetchall()
    
    # Mencari data by title/id
    def find(self, key):
        with self.get_connection() as conn:
            return conn.execute(
                'SELECT * FROM movie WHERE title LIKE ? OR id LIKE ?',
                (f'%{key}%', f'%{key}%') # karena menggunakan LIKE harus mengikuti format
            ).fetchall()
    
    # Update data berdasarkan id
    def update(self, id, title, duration, genre, year):
        with self.get_connection() as conn:
            conn.execute(
                'UPDATE movie SET title=?, duration=?, genre=?, year=? WHERE id=?',
                (title, duration, genre, year, id)
            )
    
    # Hapus data berdasarkan id
    def delete(self, id):
        with self.get_connection() as conn:
            conn.execute(
                'DELETE FROM movie WHERE id = ?', (id,) # jika satu statement, berikan tanda ',' pada akhir
            )