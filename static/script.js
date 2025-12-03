const video = document.getElementById("camera");
const statusText = document.getElementById("status");
const uploadInput = document.getElementById("uploadInput");
const preview = document.getElementById("preview");

const namaEl = document.getElementById("nama");
const nimEl = document.getElementById("nim");
const kelasEl = document.getElementById("kelas");
const kodeEl = document.getElementById("kode");
const resultBox = document.getElementById("result-box");

async function startCamera() {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    video.srcObject = stream;

    setInterval(scanFrame, 700);
}

async function scanFrame() {
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

    const res = await fetch("http://127.0.0.1:5000/scan", {
        method: "POST",
        body: formData
    });

    const result = await res.json();

    if (result.status === "berhasil") {
        statusText.textContent = "Status: Barcode terbaca";
        resultBox.classList.remove("hidden");

        namaEl.textContent = result.data?.nama ?? "-";
        nimEl.textContent = result.data?.nim ?? "-";
        kelasEl.textContent = result.data?.kelas ?? "-";
        kodeEl.textContent = result.barcode;
    }
}

// =======================
// FITUR UPLOAD GAMBAR
// =======================
uploadInput.addEventListener("change", async function () {
    const file = uploadInput.files[0];
    if (!file) return;

    // Tampilkan preview foto
    preview.src = URL.createObjectURL(file);
    preview.classList.remove("hidden");

    sendToServer(file);
});

startCamera();
