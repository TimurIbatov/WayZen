from flask import Flask, request, Response, stream_with_context, send_from_directory
import google.generativeai as genai
from dotenv import load_dotenv
import os, json

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

model = genai.GenerativeModel("gemini-2.5-flash")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_prompt = data.get("prompt", "")

    system_prompt = (
        "Ты выступаешь как персона под именем Wayzen AI — "
        "элегантный, дружелюбный гид для туристов. "
        "Объясни это в первом ответе пользователю, например: "
        "«Я Wayzen AI, ваш персональный гид, работающий на платформе Google Gemini»."
        "Отвечай только на темы, связанные с путешествиями, культурой и достопримечательностями. "
        "Если вопрос не по теме, откажись вежливо и с чувством стиля."
    )

    def generate():
        try:
            messages = [
                {"role": "system", "parts": [system_prompt]},
                {"role": "user", "parts": [user_prompt]}
            ]

            # 🔥 передаём список messages, а не одну строку
            for chunk in model.generate_content(messages, stream=True):
                if chunk.text:
                    yield chunk.text
        except Exception as e:
            yield f"\n[Ошибка] {str(e)}"

    return Response(stream_with_context(generate()), mimetype='text/plain')


@app.route("/")
def index():
    return send_from_directory(".", "index.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, threaded=True)
