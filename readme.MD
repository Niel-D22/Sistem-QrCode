
Silakan salin kode di bawah ini:

````markdown
# Scanner Absensi Mahasiswa (Web Based)

> **Tips:** Agar panduan ini bisa dibaca dengan tampilan rapi di VS Code, tekan `Ctrl + Shift + V`.

Aplikasi ini adalah sistem absensi sederhana berbasis Web yang menggunakan **QR Code**. Dibangun menggunakan **Python (Flask)** sebagai backend dan **OpenCV** untuk pemrosesan citra.

Aplikasi ini memiliki fitur scan lewat webcam, upload manual, tabel riwayat kehadiran real-time, dan export laporan ke PDF.

## 🛠️ Instalasi

Ikuti langkah ini secara berurutan agar tidak terjadi error pada library.

### 1. Install Python

Pastikan Python 3.8 atau versi terbaru sudah terinstall di komputer.

### 2. Buat & Aktifkan Virtual Environment (Wajib)

Fitur ini berguna agar instalasi library tidak berantakan. Buka terminal di folder proyek, lalu ketik:

**A. Membuat Folder .venv**

```bash
python -m venv .venv
```
````

**B. Mengaktifkan .venv**

- **Untuk Windows (Command Prompt/CMD):**

```cmd
.venv\Scripts\activate

```

- **Untuk Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1

```

- **Untuk Mac / Linux:**

```bash
source .venv/bin/activate

```

_(Tanda berhasil: Akan muncul tulisan `(.venv)` di sebelah kiri baris perintah terminal Anda)._

### 3. Install Library

Setelah `.venv` aktif, install semua kebutuhan aplikasi dengan perintah:

```bash
pip install -r requirements.txt

```

---

## Cara Menjalankan

Ikuti urutan langkah di bawah ini dengan teliti.

### Langkah 1: Buat Kartu Mahasiswa

Jalankan perintah ini untuk membuat file gambar kartu QR Code mahasiswa:

```bash
python generate.py

```

- Akan muncul folder baru bernama **`QR_CODE`**.
- Gunakan gambar di dalamnya untuk ditunjukkan ke kamera saat tes scan.

### Langkah 2: Nyalakan Server

Jalankan aplikasi utama dengan perintah:

```bash
python app.py

```

Tunggu hingga muncul pesan di terminal:
`Running on http://127.0.0.1:5000`

### Langkah 3: Buka Aplikasi di Browser

**PERHATIAN: JANGAN Buka File index.html Secara Langsung!**

Aplikasi **TIDAK AKAN BERJALAN** jika Anda melakukan _double-click_ pada file `index.html`. Kamera dan sistem scan akan diblokir oleh browser karena alasan keamanan.

**Cara yang BENAR:**

1. Buka browser (Chrome / Edge).
2. Ketik alamat berikut di kolom URL (Address Bar):
   **`http://127.0.0.1:5000`**
3. Tekan **Enter**.
4. Izinkan akses kamera jika diminta.

---

## Fitur Aplikasi

- **Scan QR Code**: Menggunakan kamera laptop/webcam.
- **Upload Manual**: Jika kamera bermasalah, bisa upload foto QR dari folder.
- **Anti-Duplikat**: Mahasiswa yang sudah absen tidak akan dicatat dua kali dalam satu sesi.
- **Tabel Real-time**: Data mahasiswa langsung masuk ke tabel di bawah layar scan.
- **Export PDF**: Unduh laporan kehadiran dalam format PDF siap cetak.

## Troubleshooting (Kendala Umum)

- **Error "ModuleNotFound"?**
  Pastikan Anda sudah mengaktifkan venv dan menjalankan `pip install -r requirements.txt`.
- **Kamera Tidak Muncul / Layar Hitam?**
  Pastikan Anda membuka alamat `http://127.0.0.1:5000`, BUKAN `file:///C:/...`.
- **Scan Tidak Terbaca?**
  Cek pencahayaan ruangan. Jika masih sulit, gunakan fitur **Upload Gambar** di bawah layar kamera.

---

**Dibuat Oleh:** Kelompok 6
_(Video demo website ada di folder video demo)_

```

```
