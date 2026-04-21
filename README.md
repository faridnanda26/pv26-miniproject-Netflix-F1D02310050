# Netflix - Movie Manager

Aplikasi manajemen daftar film sederhana yang memungkinkan pengguna untuk menambah, mencari, memperbarui, dan menghapus (CRUD) data film. Aplikasi ini dibangun dengan antarmuka grafis (GUI) yang modern dan terintegrasi dengan database lokal.

---

## Deskripsi Singkat
Netflix Movie Manager dirancang untuk memudahkan pecinta film dalam mengorganisir koleksi tontonan mereka. Pengguna dapat mencatat detail film seperti judul, durasi (jam & menit), genre, dan tahun rilis. Aplikasi ini dilengkapi dengan validasi input untuk memastikan data yang tersimpan akurat dan konsisten.

## Fitur Utama
- **Manajemen Data (CRUD):** Tambah, Lihat, Edit, dan Hapus data film.
- **Pencarian Cepat:** Mencari film berdasarkan ID atau judul secara *real-time*.
- **UI Modern:** Antarmuka berbasis PySide6 dengan kustomisasi gaya (QSS) yang bersih.
- **Penyimpanan Lokal:** Menggunakan SQLite yang ringan dan tidak memerlukan instalasi server tambahan.
- **CSV Export:** Menggunakan fungsi operasi file dan library CSV untuk menuliskan data ke dalam CSV.

## Teknologi yang Digunakan
- **Bahasa Pemrograman:** [Python 3.x](https://www.python.org/)
- **GUI Framework:** [PySide6](https://doc.qt.io/qtforpython/) (Qt for Python)
- **Database:** [SQLite3](https://www.sqlite.org/index.html)
- **Styling:** Qt Style Sheets (QSS)

## Cara Menjalankan Aplikasi

### 1. Setup environtment
download bahasa pemrogramman Python dan Library PySide6
### 2. Klik Run File
Pastikan file berjalan dan tidak terjadi error
### 3. Fitur-fitur Netflix
- **Add:** Menambahkan movie baru ke database menggunakan custom dialog
- **Delete:** Menghapus movie dari database dengan dialog konfirmasi
- **Update:** Memperbarui data yang dipilih dengan custom dialog
- **Help Menubar:** Menampilkan spesifikasi aplikasi netflix
- **Export csv:** Menulis data pada tabel kedalam bentuk csv file