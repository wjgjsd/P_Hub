import os
import re
from google.cloud import vision

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'C:\\Users\\pjh\\Desktop\\Haca\\haca-459308-5f83d6e8fa46.json'

def extract_text():

    client = vision.ImageAnnotatorClient()

    image_path = './images/captured_image.jpg'

    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)

    text = response.text_annotations
    combined_text = ''

    if text:
        combined_text = text[0].description 


    temp_text = re.sub(r'[^a-zA-Z0-9\s\uAC00-\uD7A3\.]', ' ', combined_text)
    new_text = re.sub(r'[^a-zA-Z0-9\s\uAC00-\uD7A3\.]', ' ', temp_text)

    print(new_text)

    if response.error.message:
        raise Exception(f'{response.error.message}')
    return new_text
if __name__ == '__main__':
    extract_text()
