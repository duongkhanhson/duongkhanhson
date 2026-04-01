import cv2
import numpy as np

# Mở camera (0 = webcam mặc định)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    # Chuyển từ BGR sang HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Ngưỡng màu xanh lá trong HSV
    lower_green = np.array([35, 50, 50])
    upper_green = np.array([85, 255, 255])

    # Tạo mask chỉ giữ màu xanh
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Tìm contour của vùng màu xanh
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        # Lọc vùng nhỏ
        if area > 500:
            x, y, w, h = cv2.boundingRect(cnt)

            # Vẽ khung quanh vật màu xanh
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(frame, "Green Object", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    # Hiển thị hình ảnh
    cv2.imshow("Camera", frame)
    cv2.imshow("Mask Green", mask)

    # Nhấn q để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()