import cv2

# 1. Khởi tạo đối tượng camera (thông thường số 0 là camera mặc định của laptop)
cap = cv2.VideoCapture(0)

# Kiểm tra xem camera có mở được không
if not cap.isOpened():
    print("Không thể mở camera. Vui lòng kiểm tra lại kết nối!")
    exit()

print("Đang mở camera... Nhấn phím 'q' trên bàn phím để thoát.")

while True:
    # 2. Đọc từng khung hình (frame) từ camera
    ret, frame = cap.read()

    # Nếu đọc khung hình lỗi thì thoát vòng lặp
    if not ret:
        print("Lỗi khi nhận hình ảnh. Đang thoát...")
        break

    # 3. Hiển thị hình ảnh lên một cửa sổ
    cv2.imshow('Cua so Camera cua toi', frame)

    # 4. Chờ phím nhấn. Nếu nhấn 'q' thì thoát vòng lặp
    # cv2.waitKey(1) sẽ đợi 1 miligiây giữa các khung hình
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 5. Giải phóng tài nguyên và đóng các cửa sổ
cap.release()
cv2.destroyAllWindows()