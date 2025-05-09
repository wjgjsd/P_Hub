from gtts import gTTS
import uuid
import os
import subprocess
import keyboard
from playsound import playsound
import threading
import sys
import ocr

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)

ocr_path = os.path.join(base_path, "ocr.py")

def esc_listener():
    keyboard.wait('esc')
    print("🚪 ESC 눌림 → OCR 프로세스 및 전체 종료")
    os._exit(0)  # 전체 종료

threading.Thread(target=esc_listener, daemon=True).start()
print("▶ 텍스트 인식 및 음성 출력 시작 (ESC를 누르면 종료)")

while True:
    text = ocr.quickstart()

    if not text.strip():
        print("⚠️ 텍스트 인식 실패")
        continue

    filename = f"tts_{uuid.uuid4()}.mp3"
    tts = gTTS(text=text.strip(), lang='ko')
    tts.save(filename)
    playsound(filename)
    os.remove(filename)