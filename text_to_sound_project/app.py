from flask import Flask, request, jsonify, send_file, render_template
from gtts import gTTS
import uuid
import os

app = Flask(__name__)

# 👉 index.html 경로 연결
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/speak', methods=['POST'])
def speak():
    text = request.json.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    filename = f"tts_{uuid.uuid4()}.mp3"
    tts = gTTS(text=text, lang='ko')
    tts.save(filename)

    return send_file(filename, mimetype="audio/mpeg", as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)
