import cv2
import ocr
import tts  # Import the TTS module

# 카메라 열기 (기본 카메라: 0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

print("스페이스바를 누르면 사진이 저장됩니다. ESC를 누르면 종료합니다.")

while True:
    ret, frame = cap.read() 
    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break

    # 화면에 출력
    cv2.imshow('Camera', frame)

    # 키 입력 대기 (1ms)
    key = cv2.waitKey(1) & 0xFF

    if key == 27:  # ESC키 종료
        break
    elif key == 32:  # 스페이스바
        # 사진 저장
        cv2.imwrite('./images/captured_image.jpg', frame)
        print("사진이 'captured_image.jpg'로 저장되었습니다.")
        # OCR 처리
        extracted_text = ocr.extract_text()
        if not extracted_text:
            print("OCR 처리 중 오류가 발생했습니다.")
        else:
            ############# OCR 처리 결과 출력 #############
            print("OCR 처리 결과:")
            print(extracted_text)
            tts.text_to_speech(extracted_text)
            print("TTS 처리가 완료되었습니다."    
        
        )

# 자원 해제
cap.release()
cv2.destroyAllWindows()
