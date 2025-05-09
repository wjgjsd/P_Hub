import os
import re
import sys
import time
import take_photo
from google.cloud import vision

base_dir = getattr(sys, '_MEIPASS', os.path.dirname(__file__))
key_path = os.path.join(base_dir, 'haca-459308-5f83d6e8fa46.json')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path

def quickstart():
    image_path = 'captured_image.jpg'
    take_photo.take_photo()

    # ✅ 저장 대기 (최대 5초)
    for _ in range(50):
        if os.path.exists(image_path) and os.path.getsize(image_path) > 0:
            break
        time.sleep(0.1)
    else:
        print("❌ 사진 저장 실패")
        return "FAIL"

    client = vision.ImageAnnotatorClient()
    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)

    text = response.text_annotations
    if not text:
        print("❌ 텍스트 인식 실패")
        return "텍스트가 감지되지 않았습니다. 사진을 다시 찍습니다."

    combined_text = text[0].description
    clean = re.sub(r'[^a-zA-Z0-9\s\uAC00-\uD7A3\.]', ' ', combined_text)
    clean = re.sub(r'[^a-zA-Z0-9\s\uAC00-\uD7A3\.]', ' ', clean)

    if response.error.message:
        raise Exception(f'{response.error.message}')
    
    return clean

if __name__ == '__main__':
    result = quickstart()
    print(result)

