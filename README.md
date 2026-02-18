# 🤖 Gemini AI Chatbot: CLI & WhatsApp Integration

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask)
![Gemini API](https://img.shields.io/badge/Google%20Gemini-AI-orange?style=for-the-badge&logo=google)
![Twilio](https://img.shields.io/badge/Twilio-WhatsApp-red?style=for-the-badge&logo=twilio)

## Fitur utamanya adalah seperti ini : 

- 🔭 Mendukung chat bersama dengan BOT
- 💬 Memiliki 2 jenis chat CLI dan chat terhubung dengan Whatsapp
- 📡 Untuk Whatsapp terhubung menggunakan twilio
- ⚡ Backend yang digunakan adalah menggunakan flask 

## Tech Stack 
- **Languages :** Python
- **AI Model :** Google Generative AI (Gemini)
- **Framework :** Flask
- **Infrastructures :** Ngrok (Local Tuneling), Twilio (Whatsapp API)
- **Environment Managament :** Python-dotenv

## Project Structures

```bash
Chatbot_Gemini_API/
├── venv/                   # Virtual Environment (Ignored in Git)
├── app.py                  # Main server file for WhatsApp Bot (Flask)
├── commandline.py          # Script for CLI Chatbot
├── requirements.txt        # List of dependencies
├── .env                    # API Keys and Secrets (Ignored in Git)
├── .gitignore              # Git ignore rules
└── README.md               # Project Documentation
```

## ⚙️ Setup & Installation
### 1. Clone Repository 

```bash
git clone [https://github.com/username/Chatbot_Gemini_API.git](https://github.com/username/Chatbot_Gemini_API.git)
cd Chatbot_Gemini_API
```

### 2. Create Virtual Environment 
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash 
pip install -r requirements.txt
```

### 4. Configure Environment Variables 
Buatlah file ```bash .env``` dan tambahkan API anda : 
``` bash
GEMINI_API_KEY=your_google_api_key_here
```         

## Cara Menjalankan 
### Terminal 
```bash 
python commandline.py
```
<i>Type exit, quit, or keluar to end the session.<i>

### Whatsapp Bot
1. Start the Flask Server:
```bash 
python app.py
```

2.  Host di local dengan ngrok
Di terminal jalankan 
```bash 
ngrok http 5000
```

4. Configure Twilio : 
- Copy link Ngrok 
- Masuk ke twilio <b>Twilio Console > Messaging > Sandbox Settings<b>
- Paste URL ke bagian "When a message comes in"
- Contoh ```https://xxxx.ngrok-free.app/bot```
- Save

Mulai chatting dengan Whatsapp dari nomor yang diberikan Twilio 

### 🔮 Future Improvements (Roadmap)
[ ] Implement database (MySQL/PostgreSQL) to store chat history per user.

[ ] Add RAG (Retrieval-Augmented Generation) to allow the bot to read PDF/Text files.


[ ] Deploy to a cloud server (Render/Railway/Heroku).

## Tampilan Penggunaan 
### 1. CommandLine Bot

<img width="1559" height="864" alt="image" src="https://github.com/user-attachments/assets/655f2713-74d6-4b7f-996d-779251595895" />

<br />
### 2. Whatsapp Bot 
<br />
<img width="720" height="1600" alt="image" src="https://github.com/user-attachments/assets/655e5c6f-22d4-415a-8905-d3d9609463d4" />
<br />

<img width="1919" height="1098" alt="Screenshot 2026-02-17 234049" src="https://github.com/user-attachments/assets/abb15e38-995d-4ea4-8d7a-19ba1eb45801" />
<br />

<img width="1919" height="1066" alt="Screenshot 2026-02-17 234144" src="https://github.com/user-attachments/assets/27f70ad4-beb7-4660-bae5-c67d86d0a0f2" />
<br />

<img width="1564" height="694" alt="Screenshot 2026-02-17 234337" src="https://github.com/user-attachments/assets/3d643cf9-04c9-4c71-9b37-ca195a634108" />






