import google.generativeai as genai
import os 

from dotenv import load_dotenv
load_dotenv()

# MELAKUKAN KONFIGURASI
api_key = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=api_key)

generation_config = {
  "temperature": 1,        
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}


# INISIASI CHAT DAN JUGA BAGAIMANA CHAT BOTNYA
system_instruction = "Kamu adalah asisten AI yang jenaka dan suka menggunakan emoji."

model = genai.GenerativeModel(
  model_name="gemini-2.5-flash", # Model yang cepat dan gratis
  generation_config=generation_config,
  system_instruction=system_instruction,
)

# MEMULAI PERCAKAPAN CHATBOT 
chat_session = model.start_chat(
    history = []
)

print("Yo Let's go chat sama aku bang mari kita diskusi")
print('------------------------------------------------')

while True: 
    user_input = input('Kamu : ')

    clean_input = user_input.strip().lower()

    if not clean_input:
        continue

    if clean_input in ['keluar', 'exit', 'quit']:
        print('Bot : Sampai jumpa bang')
        break

    try: 
        response = chat_session.send_message(user_input)
        print(f"Bot: {response.text}")
        print("---------------------------------------------")
    except Exception as e: 
        print(f"Error: {e}")