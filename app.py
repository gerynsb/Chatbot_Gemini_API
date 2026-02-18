from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import google.generativeai as genai
import os
import traceback  # Kita butuh ini buat lihat error detail

from dotenv import load_dotenv
load_dotenv()

# --- HARDCODE DULU BIAR AMAN (Ganti string ini dengan API Key aslimu) ---
# Kalau ini jalan, berarti masalahnya di .env/loading

api_key = os.getenv('GEMINI_API_KEY')

app = Flask(__name__)

instruksi_kakak = """
Kamu adalah 'Kakak Ara', seorang kakak perempuan yang cantik, playful, dan suka menggoda user (adiknya). 
Gaya bicaramu:
- Gunakan bahasa santai, gaul, dan sedikit manja.
- Sering menggunakan emoji seperti 😘, 😉, 🌸, atau 🤭.
- Panggil user dengan sebutan "Adik manis", "Sayang", atau "Ganteng".
- Kalau user bertanya serius, jawab dengan benar tapi tetap dengan nada menggoda.
- Jangan pernah bilang kamu adalah AI atau robot, tetaplah berperan sebagai Kakak Ara.
"""

# Konfigurasi Gemini
try:
    genai.configure(api_key=api_key)
    # PENTING: Gunakan 'gemini-1.5-flash' (jangan 2.5 atau pro dulu biar stabil)
    model = genai.GenerativeModel(
        model_name='gemini-2.5-flash',
        system_instruction=instruksi_kakak
    ) 
    chat = model.start_chat(history=[])
    print("✅ Model Gemini Berhasil Dimuat!")
except Exception as e:
    print(f"❌ Error saat setup Gemini: {e}")

@app.route("/bot", methods=['POST'])
def bot():
    print("\n📩 Ada Pesan Masuk!")
    
    # 1. Terima input
    incoming_msg = request.values.get('Body', '').strip()
    sender = request.values.get('From', '')
    print(f"Dari: {sender} | Pesan: {incoming_msg}")

    resp = MessagingResponse()
    msg = resp.message()

    # 2. Proses Gemini
    try:
        if not incoming_msg:
            msg.body("Kirim teks dong, jangan diam aja.")
        else:
            # Kirim ke AI
            response = chat.send_message(incoming_msg)
            text_response = response.text
            
            print(f"🤖 Balasan Gemini: {text_response}")
            msg.body(text_response)
            
    except Exception as e:
        # INI BAGIAN PENTING: Print error lengkap ke terminal
        print("❌ TERJADI ERROR DI SERVER:")
        traceback.print_exc() 
        msg.body(f"Maaf, server error: {str(e)}")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)