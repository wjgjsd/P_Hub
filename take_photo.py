def take_photo():
    import cv2

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("카메라를 열 수 없습니다.")
        return False

    while True:
        ret, frame = cap.read()
        if not ret:
            print("프레임을 읽을 수 없습니다.")
            break

        cv2.imshow('Camera', frame)
        key = cv2.waitKey(1) & 0xFF

        if key == 32:  # 스페이스바
            cv2.imwrite('captured_image.jpg', frame)
            break

    cap.release()
    cv2.destroyAllWindows()
    return True

if __name__ == '__main__':
    take_photo()