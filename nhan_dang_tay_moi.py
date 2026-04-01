import cv2
import mediapipe as mp

# 1. Khởi tạo các giải pháp của MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# 2. Cấu hình mô hình nhận diện
# min_detection_confidence: Độ tin tưởng tối thiểu để nhận diện (0.7 = 70%)
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)

# 3. Mở Camera
cap = cv2.VideoCapture(0)

print("Đang khởi động Camera... Nhấn phím 'q' để thoát.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Không thể nhận khung hình từ Camera.")
        break

    # Lật ảnh theo chiều ngang để không bị ngược tay
    frame = cv2.flip(frame, 1)

    # Chuyển hệ màu từ BGR sang RGB cho MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Xử lý hình ảnh và tìm bàn tay
    results = hands.process(rgb_frame)

    # 4. Vẽ các điểm mốc nếu tìm thấy bàn tay
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Vẽ các đường nối và điểm khớp xương
            mp_drawing.draw_landmarks(
                frame, 
                hand_landmarks, 
                mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=4), # Điểm
                mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2) # Đường nối
            )

    # Hiển thị cửa sổ kết quả
    cv2.imshow('Nhan Dang Ban Tay', frame)

    # Thoát khi nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()