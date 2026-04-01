// Kiểm Tra và Điều Khiển LED Pin 13 qua Serial Monitor

const int LED_PIN = 13;
bool ledState = LOW;

void setup() {
  Serial.begin(9600);        // Baud rate 9600
  pinMode(LED_PIN, OUTPUT);  // Pin 13 là OUTPUT
  digitalWrite(LED_PIN, LOW); // Tắt LED lúc khởi động
  
  Serial.println("================================");
  Serial.println("LED Pin 13 Control System");
  Serial.println("================================");
  Serial.println("\nLệnh điều khiển:");
  Serial.println("  '1' hoặc 'ON'  → Bật LED");
  Serial.println("  '0' hoặc 'OFF' → Tắt LED");
  Serial.println("  'T'            → Toggle LED (bật/tắt)");
  Serial.println("  'S'            → Kiểm tra trạng thái");
  Serial.println("  'BLINK'        → LED nháy 5 lần");
  Serial.println("  'HELP'         → Hiện trợ giúp");
  Serial.println("================================\n");
  
  Serial.println("Sẵn sàng! Hãy gửi lệnh:\n");
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim();     // Xóa khoảng trắng
    command.toUpperCase(); // Chuyển thành chữ hoa
    
    Serial.print("Lệnh nhận: ");
    Serial.println(command);
    
    // Xử lý lệnh
    if (command == "1" || command == "ON") {
      digitalWrite(LED_PIN, HIGH);
      ledState = HIGH;
      Serial.println("✓ LED: BẬT");
      Serial.println("");
    }
    else if (command == "0" || command == "OFF") {
      digitalWrite(LED_PIN, LOW);
      ledState = LOW;
      Serial.println("✓ LED: TẮT");
      Serial.println("");
    }
    else if (command == "T" || command == "TOGGLE") {
      ledState = !ledState;
      digitalWrite(LED_PIN, ledState);
      String status = ledState ? "BẬT" : "TẮT";
      Serial.print("✓ Toggle! LED: ");
      Serial.println(status);
      Serial.println("");
    }
    else if (command == "S" || command == "STATUS") {
      String status = ledState ? "ON (BẬT)" : "OFF (TẮT)";
      Serial.print("Trạng thái LED: ");
      Serial.println(status);
      Serial.println("");
    }
    else if (command == "BLINK") {
      Serial.println("LED đang nháy 5 lần...");
      for (int i = 0; i < 5; i++) {
        digitalWrite(LED_PIN, HIGH);
        delay(300);
        digitalWrite(LED_PIN, LOW);
        delay(300);
        Serial.print(".");
      }
      ledState = LOW;
      Serial.println("\n✓ Nháy xong!");
      Serial.println("");
    }
    else if (command == "HELP") {
      printHelp();
    }
    else {
      Serial.println("✗ Lệnh không hợp lệ!");
      Serial.println("Gõ 'HELP' để xem các lệnh");
      Serial.println("");
    }
  }
}

void printHelp() {
  Serial.println("\n================================");
  Serial.println("DANH SÁCH LỆNh:");
  Serial.println("================================");
  Serial.println("  1 / ON      → Bật LED");
  Serial.println("  0 / OFF     → Tắt LED");
  Serial.println("  T / TOGGLE  → Đảo trạng thái LED");
  Serial.println("  S / STATUS  → Kiểm tra trạng thái");
  Serial.println("  BLINK       → Nháy 5 lần");
  Serial.println("  HELP        → Hiện trợ giúp");
  Serial.println("================================\n");
}
