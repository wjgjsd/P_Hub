import os
import re
import take_photo
import subprocess
from google.cloud import vision
base_dir = os.path.dirname(__file__)
key_path = os.path.join(base_dir, 'haca-459308-5f83d6e8fa46.json')
take_photo_dir = os.path.join(base_dir, 'take_photo.py')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path
def quickstart():
    
    client = vision.ImageAnnotatorClient()

    image_path = 'captured_image.jpg'

    while(True):
        with open(image_path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)
        response = client.text_detection(image=image)

        text = response.text_annotations
        combined_text = ''

        if text:
            combined_text = text[0].description
            break
        else:
            print("텍스트가 감지되지 않았습니다. 사진을 다시 찍습니다.")
            subprocess.run(["python", take_photo_dir])

    temp_text = re.sub(r'[^a-zA-Z0-9\s\uAC00-\uD7A3\.]', ' ', combined_text)
    new_text = re.sub(r'[^a-zA-Z0-9\s\uAC00-\uD7A3\.]', ' ', temp_text)

    print(new_text)

    if response.error.message:
        raise Exception(f'{response.error.message}')

if __name__ == '__main__':
    quickstart()
