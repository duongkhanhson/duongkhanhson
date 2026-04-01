import cv2
import random
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Game đơn giản: bé dùng miệng ăn bong bóng
# Điều khiển: đưa mặt vào camera, dùng vùng miệng chạm vào bong bóng

WIDTH = 640
HEIGHT = 480
BUBBLE_RADIUS = 35
NUM_BUBBLES = 6
MOUTH_RADIUS = 50

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))


def load_font(size=24):
    possible_fonts = [
        "arial.ttf",
        "segoeui.ttf",
        "times.ttf",
        "DejaVuSans.ttf",
    ]
    for font_name in possible_fonts:
        try:
            return ImageFont.truetype(font_name, size)
        except OSError:
            continue

    try:
        windows_font_dir = os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "Fonts")
        for font_name in ["arial.ttf", "segoeui.ttf", "times.ttf"]:
            font_path = os.path.join(windows_font_dir, font_name)
            if os.path.exists(font_path):
                return ImageFont.truetype(font_path, size)
    except Exception:
        pass

    return ImageFont.load_default()


def draw_text(frame, text, position, color=(255, 255, 255), size=24):
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)
    font = load_font(size)
    draw.text(position, text, font=font, fill=color)
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)


class Bubble:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = random.randint(BUBBLE_RADIUS, WIDTH - BUBBLE_RADIUS)
        self.y = random.randint(BUBBLE_RADIUS, HEIGHT - BUBBLE_RADIUS)
        self.vx = random.uniform(-3.0, 3.0)
        self.vy = random.uniform(-2.0, 2.0)
        self.color = (
            random.randint(40, 255),
            random.randint(40, 255),
            random.randint(40, 255),
        )
        self.radius = BUBBLE_RADIUS

    def update(self):
        self.x += self.vx
        self.y += self.vy
        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.vx *= -1
            self.x = clamp(self.x, self.radius, WIDTH - self.radius)
        if self.y - self.radius < 0 or self.y + self.radius > HEIGHT:
            self.vy *= -1
            self.y = clamp(self.y, self.radius, HEIGHT - self.radius)

    def draw(self, frame):
        cv2.circle(frame, (int(self.x), int(self.y)), self.radius, self.color, -1)
        cv2.circle(frame, (int(self.x), int(self.y)), self.radius, (255, 255, 255), 3)


def find_mouth_center(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6, minSize=(100, 100))
    mask = np.zeros_like(frame)
    if len(faces) == 0:
        return None, mask

    face = max(faces, key=lambda rect: rect[2] * rect[3])
    x, y, w, h = face
    mouth_x = x + w // 2
    mouth_y = y + int(h * 0.75)
    mouth_w = int(w * 0.45)
    mouth_h = int(h * 0.2)
    mouth_center = (mouth_x, mouth_y)

    cv2.rectangle(mask, (x, y), (x + w, y + h), (255, 255, 255), 2)
    cv2.circle(frame, mouth_center, 10, (0, 255, 255), -1)
    cv2.circle(frame, mouth_center, MOUTH_RADIUS, (0, 255, 255), 2)

    return mouth_center, mask


def main():
    score = 0
    bubbles = [Bubble() for _ in range(NUM_BUBBLES)]

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (WIDTH, HEIGHT))

        mouth_center, mask = find_mouth_center(frame)

        for bubble in bubbles:
            bubble.update()
            bubble.draw(frame)

            if mouth_center is not None:
                dx = bubble.x - mouth_center[0]
                dy = bubble.y - mouth_center[1]
                if dx * dx + dy * dy < (bubble.radius + MOUTH_RADIUS) ** 2:
                    score += 1
                    bubble.reset()

        frame = draw_text(frame, f"Điểm: {score}", (18, 18), (0, 255, 0), 28)
        frame = draw_text(frame, "Đưa mặt vào camera để ăn bong bóng", (12, HEIGHT - 40), (220, 220, 220), 24)
        frame = draw_text(frame, "Nhấn 'q' để thoát, 'r' để chơi lại", (12, HEIGHT - 16), (220, 220, 220), 24)

        if mouth_center is None:
            frame = draw_text(frame, "Cần đưa mặt vào camera", (140, HEIGHT // 2 - 20), (0, 200, 255), 30)

        cv2.imshow("Mouth Game - Miệng ăn bong bóng", frame)
        cv2.imshow("Face Detect", mask)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        if key == ord('r'):
            score = 0
            bubbles = [Bubble() for _ in range(NUM_BUBBLES)]

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
