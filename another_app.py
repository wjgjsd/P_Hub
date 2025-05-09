from gtts import gTTS
import uuid
import os
import subprocess
import keyboard
from playsound import playsound
import threading

# ESC 눌렸는지 체크할 플래그
stop_flag = False

def esc_listener(proc):
    keyboard.wait('esc')
    print("🚪 ESC 눌림 → OCR 프로세스 및 전체 종료")
    try:
        proc.terminate()  # OCR 프로세스 강제 종료
    except Exception:
        pass
    os._exit(0)  # 전체 종료

base_dir = os.path.dirname(__file__)
ocr_path = os.path.join(base_dir, 'ocr.py')

print("▶ 텍스트 인식 및 음성 출력 시작 (ESC를 누르면 종료)")

while True:
    # ✅ OCR 먼저 실행해서 proc 얻고
    proc = subprocess.Popen(["python", ocr_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # ✅ 그 다음에 proc을 넘겨서 esc_listener 실행
    threading.Thread(target=esc_listener, args=(proc,), daemon=True).start()

    # OCR stdout 결과 읽기
    stdout, _ = proc.communicate()  # 여기서 OCR 실행 완료될 때까지 대기
    text = stdout

    if not text.strip():
        print("⚠️ 텍스트 인식 실패")
        continue

    filename = f"tts_{uuid.uuid4()}.mp3"
    tts = gTTS(text=text.strip(), lang='ko')
    tts.save(filename)
    playsound(filename)
    os.remove(filename)