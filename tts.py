from gtts import gTTS
import os
import cv2
import ocr
from playsound import playsound  # 음성 재생을 위한 playsound 라이브러리

def text_to_speech(text):
    # 텍스트를 음성으로 변환
    tts = gTTS(text=text, lang='ko')  
    tts.save("output.mp3")  # 음성 파일 저장

    # 음성을 재생
    playsound("output.mp3")

    # 음성 재생이 끝난 후 파일 삭제
    os.remove("output.mp3")
    print("output.mp3 파일이 삭제되었습니다.")

def main():
    extracted_text = ocr.extract_text()  # OCR로 텍스트 추출
    text_to_speech(extracted_text)  # 텍스트를 음성으로 변환하여 출력

if __name__ == '__main__':
    main()
