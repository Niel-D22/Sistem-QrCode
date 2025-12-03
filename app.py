from flask import Flask, request, jsonify
from pyzbar.pyzbar import decode
from PIL import Image
import numpy as np
import cv2
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Contoh database sederhana
data_mahasiswa = {
    "24013025": {"nama": "Daniel Riky Warouw", "nim": "24013025", "kelas": "A", "prodi": "Teknik Informatika"},
    "24013037": {"nama": "Marcois Soleman Benedictus Makalew", "nim": "24013037", "kelas": "B", "prodi": "Teknik Informatika"},
    "24013058": {"nama": "Reins Orlando Maindjanga", "nim": "24013058", "kelas": "B", "prodi": "Teknik Informatika"},
    "24013048": {"nama": "Selomitha Anastacia Nong", "nim": "24013048", "kelas": "B", "prodi": "Teknik Informatika"},
    "24013011": {"nama": "ANDRIANO DARINDING", "nim": "24013011", "kelas": "A", "prodi": "Teknik Informatika"},

    "24013031": {"nama": "YUSLI NGONGANO", "nim":"24013031", "kelas": "A", "prodi": "Teknik Informatika"},
    "24013023": {"nama": "KEVIN LIONEL SONDAKH", "nim": "24013023", "kelas": "A", "prodi": "Teknik Informatika"},
    "24013060": {"nama": "JOZIA ABRAHAM KOMALING", "nim": "24013060", "kelas": "B", "prodi": "Teknik Informatika"},
    "24013064": {"nama": "CLAY VALENTINO WALONI", "nim": "24013064", "kelas": "B", "prodi": "Teknik Informatika"},
    "24013057": {"nama": "Albert", "nim": "ECKLEYSIO SASTRO ANTHONIO NANURU", "kelas": "B", "prodi": "Teknik Informatika"}
}


@app.route("/scan", methods=["POST"])
def scan():
    file = request.files.get("frame")
    if not file:
        return jsonify({"status": "gagal"})

    img = Image.open(file.stream)
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    barcodes = decode(img)
    if len(barcodes) == 0:
        return jsonify({"status": "tidak ditemukan"})

    kode = barcodes[0].data.decode("utf-8")
    mhs = data_mahasiswa.get(kode, None)

    return jsonify({
        "status": "berhasil",
        "barcode": kode,
        "data": mhs
    })

@app.route("/")
def home():
    return app.send_static_file("index.html")

if __name__ == "__main__":
    app.run(debug=True)
