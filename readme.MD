# Scanner Absensi Mahasiswa Berbasis Web (Flask + OpenCV)

Aplikasi ini adalah sistem absensi sederhana yang menggunakan **QR Code**. Sistem dibangun menggunakan **Python (Flask)** sebagai backend untuk pemrosesan citra dan **HTML/JS** sebagai frontend untuk antarmuka kamera.

## 📋 Fitur Utama
1.  **Real-time Scanning**: Membaca QR Code langsung dari webcam laptop/PC.
2.  **Upload Image**: Fitur alternatif untuk mengunggah foto QR Code jika webcam tidak tersedia.
3.  **Verifikasi Data**: Mencocokkan data QR Code dengan database mahasiswa (hardcoded dummy data).
4.  **QR Generator**: Script utilitas untuk membuat kartu mahasiswa berisi QR Code secara otomatis.

## 🛠️ Prasyarat (Requirements)
Pastikan komputer Anda sudah terinstal:
* **Python 3.8** atau versi lebih baru.
* **Pip** (Package installer for Python).
* **Webcam** yang aktif (untuk fitur scan).

## 🚀 Cara Instalasi

1.  **Ekstrak Kode Sumber**
    Ekstrak file `.zip` atau `.rar` proyek ini ke dalam satu folder.

2.  **Siapkan Virtual Environment (Opsional tapi Disarankan)**
    Buka terminal/CMD di dalam folder proyek, lalu jalankan:
    ```bash
    python -m venv .venv
    # Untuk Windows:
    .venv\Scripts\activate
    # Untuk Mac/Linux:
    source .venv/bin/activate
    ```

3.  **Install Library Pendukung**
    Install semua library yang dibutuhkan (Flask, OpenCV, Pyzbar, Pillow, dll) dengan perintah:
    ```bash
    pip install -r requirements.txt
    ```

    *> Catatan: Jika terjadi error pada instalasi `pyzbar` di Windows, pastikan "Visual C++ Redistributable" sudah terinstal.*

## ⚙️ Cara Menjalankan Aplikasi

### Langkah 1: Generate QR Code Mahasiswa (Opsional)
Jika belum memiliki gambar QR Code untuk dites, jalankan script ini:
```bash
python generate.py