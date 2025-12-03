import os
import qrcode
from PIL import Image, ImageDraw, ImageFont

# Folder output
OUTPUT_FOLDER = "QR_CODE"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Data
data_mahasiswa = {
    "24013025": {"nama": "Daniel Riky Warouw", "nim": "24013025"},
    "24013037": {"nama": "Marcois Soleman Benedictus Makalew", "nim": "24013037"},
    "24013058": {"nama": "Reins Orlando Maindjanga", "nim": "24013058"},
    "24013048": {"nama": "Selomitha Anastacia Nong", "nim": "24013048"},
    "24013011": {"nama": "ANDRIANO DARINDING", "nim": "24013011"},
    "24013031": {"nama": "YUSLI NGONGANO", "nim": "24013031"},
    "24013023": {"nama": "KEVIN LIONEL SONDAKH", "nim": "24013023"},
    "24013060": {"nama": "JOZIA ABRAHAM KOMALING", "nim": "24013060"},
    "24013064": {"nama": "CLAY VALENTINO WALONI", "nim": "24013064"},
    "24013057": {"nama": "ECKLEYSIO SASTRO ANTHONIO NANURU", "nim": "24013057"},
}

# Load font
try:
    font_title = ImageFont.truetype("arial.ttf", 28)
    font_nama = ImageFont.truetype("arial.ttf", 24)
    font_nim = ImageFont.truetype("arial.ttf", 24)
except:
    font_title = ImageFont.load_default()
    font_nama = ImageFont.load_default()
    font_nim = ImageFont.load_default()

for kode, mhs in data_mahasiswa.items():
    nim = mhs["nim"].strip()

    # Generate QR
    qr = qrcode.QRCode(
        version=2,
        box_size=10,
        border=2
    )
    qr.add_data(nim)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img = qr_img.resize((260, 260))

    # Canvas (lebih besar & modern)
    img = Image.new("RGB", (700, 420), "#F5F5F5")
    draw = ImageDraw.Draw(img)

    # Box Border
    draw.rectangle((20, 20, 680, 400), outline="#BFBFBF", width=3)

    # Paste QR
    img.paste(qr_img, (40, 70))

    # Text Title
    draw.text((330, 70), "Kartu QR Mahasiswa", fill="black", font=font_title)

    # Nama
    draw.text((330, 140), "Nama:", fill="#444", font=font_nim)
    draw.text((330, 170), mhs["nama"], fill="black", font=font_nama)

    # NIM
    draw.text((330, 230), "NIM:", fill="#444", font=font_nim)
    draw.text((330, 260), nim, fill="black", font=font_nama)

    # Save File
    file_path = os.path.join(OUTPUT_FOLDER, f"kartu_{nim}.png")
    img.save(file_path)

print("Selesai. Kartu QR berhasil dibuat dengan desain baru.")
