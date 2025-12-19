const video = document.getElementById("camera");
const statusText = document.getElementById("status");
const uploadInput = document.getElementById("uploadInput");
const preview = document.getElementById("preview");

// Elemen Card
const resultBox = document.getElementById("result-box");
const namaEl = document.getElementById("nama");
const nimEl = document.getElementById("nim");
const kelasEl = document.getElementById("kelas");

// Elemen Tabel
const tableBody = document.getElementById("table-body");
const emptyMsg = document.getElementById("empty-msg");

// Memory penyimpanan NIM agar tidak double scan
let scannedNIMs = []; 

async function startCamera() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } });
        video.srcObject = stream;
        setInterval(scanFrame, 1000); // Scan tiap 1 detik
    } catch (err) {
        console.error(err);
        statusText.innerHTML = "Gagal akses kamera (Periksa izin browser)";
    }
}

async function scanFrame() {
    if (video.readyState !== video.HAVE_ENOUGH_DATA) return;

    const canvas = document.createElement("canvas");
    const ctx = canvas.getContext("2d");
    canvas.width = 400;
    canvas.height = 300;
    ctx.drawImage(video, 0, 0, 400, 300);

    const blob = await new Promise(resolve => canvas.toBlob(resolve, "image/jpeg"));
    sendToServer(blob);
}

async function sendToServer(blob) {
    const formData = new FormData();
    formData.append("frame", blob, "frame.jpg");

    try {
        const res = await fetch("/scan", { method: "POST", body: formData });
        const result = await res.json();

        if (result.status === "berhasil") {
            if (result.data) {
                // Update Card
                statusText.innerHTML = `Status: <span class="text-green-600 font-bold">Sukses: ${result.data.nama}</span>`;
                resultBox.classList.remove("hidden");
                
                namaEl.textContent = result.data.nama;
                nimEl.textContent = result.data.nim;
                kelasEl.textContent = result.data.kelas || "-";

                // Masukkan ke Tabel (Cek duplikat dulu)
                addToTable(result.data);
            } else {
                statusText.innerHTML = `Status: <span class="text-red-500">QR Terbaca, Data Tidak Ada di Sistem</span>`;
            }
        }
    } catch (error) {
        console.error("Error:", error);
    }
}

function addToTable(data) {
    // CEK DUPLIKAT: Jika NIM sudah ada di list, STOP.
    if (scannedNIMs.includes(data.nim)) return;

    // Tambahkan ke memori
    scannedNIMs.push(data.nim);
    emptyMsg.classList.add("hidden"); // Hilangkan pesan kosong

    // Buat Baris Tabel
    const now = new Date();
    const waktu = now.toLocaleTimeString('id-ID'); // Jam:Menit:Detik
    const no = scannedNIMs.length;

    const rowHTML = `
        <tr class="hover:bg-green-50 transition">
            <td class="px-4 py-3 text-sm text-gray-900">${no}</td>
            <td class="px-4 py-3 text-sm text-gray-600 font-mono">${waktu}</td>
            <td class="px-4 py-3 text-sm font-bold text-gray-900">${data.nama}</td>
            <td class="px-4 py-3 text-sm text-gray-600">${data.nim}</td>
            <td class="px-4 py-3 text-sm text-gray-600">Hadir</td>
        </tr>
    `;

    tableBody.insertAdjacentHTML('beforeend', rowHTML);
}

// FUNGSI EXPORT PDF
function exportToPDF() {
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    doc.setFontSize(16);
    doc.text("Laporan Kehadiran Mahasiswa", 14, 20);
    doc.setFontSize(11);
    doc.text("Tanggal: " + new Date().toLocaleDateString('id-ID'), 14, 28);

    doc.autoTable({
        html: '#tabel-absensi',
        startY: 35,
        theme: 'grid',
        headStyles: { fillColor: [40, 40, 40] } // Header Hitam/Abu
    });

    doc.save("Absensi_Mahasiswa.pdf");
}

// FUNGSI UPLOAD MANUAL
uploadInput.addEventListener("change", function() {
    const file = this.files[0];
    if (file) {
        preview.src = URL.createObjectURL(file);
        preview.classList.remove("hidden");
        sendToServer(file);
    }
});

startCamera();