import os
from dotenv import load_dotenv
import google.generativeai as genai

# Загружаем API ключ из .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Выбираем модель
model = genai.GenerativeModel("gemini-2.5-flash")

user_prompt = input("Напиши, что хочешь спросить у Wayzen AI: ")
response = model.generate_content(user_prompt)
print(response.text)