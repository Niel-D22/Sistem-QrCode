from flask import Flask, request, jsonify
from pyzbar.pyzbar import decode
from PIL import Image
import numpy as np
import cv2
from flask_cors import CORS
import os

app = Flask(__name__, static_url_path='', static_folder='static')
CORS(app)

# Data Mahasiswa (Harus sama dengan generate.py agar terbaca)
data_mahasiswa = {
    "24013025": {"nama": "Daniel Riky Warouw", "nim": "24013025", "kelas": "A", "prodi": "TI"},
    "24013037": {"nama": "Marcois Soleman Benedictus Makalew", "nim": "24013037", "kelas": "B", "prodi": "TI"},
    "24013058": {"nama": "Reins Orlando Maindjanga", "nim": "24013058", "kelas": "B", "prodi": "TI"},
    "24013048": {"nama": "Selomitha Anastacia Nong", "nim": "24013048", "kelas": "B", "prodi": "TI"},
    "24013011": {"nama": "ANDRIANO DARINDING", "nim": "24013011", "kelas": "A", "prodi": "TI"},
    "24013031": {"nama": "YUSLI NGONGANO", "nim": "24013031", "kelas": "A", "prodi": "TI"},
    "24013023": {"nama": "KEVIN LIONEL SONDAKH", "nim": "24013023", "kelas": "A", "prodi": "TI"},
    "24013060": {"nama": "JOZIA ABRAHAM KOMALING", "nim": "24013060", "kelas": "B", "prodi": "TI"},
    "24013064": {"nama": "CLAY VALENTINO WALONI", "nim": "24013064", "kelas": "B", "prodi": "TI"},
    "24013057": {"nama": "ECKLEYSIO SASTRO ANTHONIO NANURU", "nim": "24013057", "kelas": "B", "prodi": "TI"},
}

@app.route("/scan", methods=["POST"])
def scan():
    print("--- Menerima request scan... ---") # Debug 1
    file = request.files.get("frame")
    if not file:
        print("Gagal: Tidak ada file gambar") # Debug 2
        return jsonify({"status": "gagal", "pesan": "Tidak ada gambar"})

    try:
        img = Image.open(file.stream)
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        barcodes = decode(img)
        
        # Debug 3: Lihat berapa barcode yang ditemukan
        print(f"Jumlah barcode ditemukan: {len(barcodes)}") 

        if len(barcodes) == 0:
            return jsonify({"status": "tidak ditemukan"})

        kode = barcodes[0].data.decode("utf-8")
        print(f"Isi Barcode: {kode}") # Debug 4

        mhs = data_mahasiswa.get(kode, None)

        if mhs:
            print(f"Data ditemukan: {mhs['nama']}") # Debug 5
            return jsonify({"status": "berhasil", "barcode": kode, "data": mhs})
        else:
            print("Data TIDAK ada di database") # Debug 6
            return jsonify({"status": "berhasil", "barcode": kode, "data": None}) 

    except Exception as e:
        print(f"ERROR SYSTEM: {e}") # Debug 7
        return jsonify({"status": "error", "pesan": str(e)})
@app.route("/")
def home():
    return app.send_static_file("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)