from gtts import gTTS
import uuid
import os
import subprocess
import keyboard
from playsound import playsound
import threading

# ESC 눌렸는지 체크할 플래그
stop_flag = False

def esc_listener():
    global stop_flag
    keyboard.wait('esc')
    print("🚪 ESC 키 입력됨: 종료 준비 중...")
    stop_flag = True
    os._exit(0)

# 백그라운드 ESC 감지 스레드 시작
threading.Thread(target=esc_listener, daemon=True).start()

base_dir = os.path.dirname(__file__)
ocr_path = os.path.join(base_dir, 'ocr.py')

print("▶ 텍스트 인식 및 음성 출력 시작 (ESC를 누르면 종료)")

while not stop_flag:
    # ocr.py 실행해서 결과 얻기
    result = subprocess.run(["python", ocr_path], capture_output=True, text=True)
    text = result.stdout

    if not text.strip():
        print("⚠️ 텍스트가 인식되지 않았습니다.")
        continue

    # gTTS로 음성 출력
    filename = f"tts_{uuid.uuid4()}.mp3"
    tts = gTTS(text=text.strip(), lang='ko')
    tts.save(filename)
    playsound(filename)
    os.remove(filename)