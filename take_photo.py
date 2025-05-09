import cv2

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

    if key == 32:  # 사진 찍기
        # 사진 저장
        cv2.imwrite('captured_image.jpg', frame)
        print("사진이 'captured_image.jpg'로 저장되었습니다.")
        break
        

# 자원 해제
cap.release()
cv2.destroyAllWindows()
