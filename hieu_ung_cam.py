import cv2

# Khởi tạo camera
cap = cv2.VideoCapture(0)

print("Đang chạy... Nhấn 'q' để thoát.")

while True:
    # Đọc khung hình từ camera
    ret, frame = cap.read()
    
    if not ret:
        break

    # 1. Chuyển đổi khung hình sang màu xám (Grayscale)
    # Đây là bước xử lý ảnh cơ bản trong lập trình thị giác máy tính
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 2. Hiển thị cửa sổ gốc (Màu)
    cv2.imshow('Camera Goc (Mau)', frame)

    # 3. Hiển thị cửa sổ đã xử lý (Den Trang)
    cv2.imshow('Camera Da Xu Ly (Xam)', gray_frame)

    # Thoát khi nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()