"""
Wi-Fi Vision YOLO Autonomous Driving Car (ESP32 Side)
Upload this code to the ESP32-S3 board (Mu Editor [ESP32 Mode] or Thonny / mpremote).

What it does:
1. Connects to local Wi-Fi network.
2. Initializes 2WD robot motors on camera-safe pins (left: 41, 42 / right: 47, 21).
3. Streams live MJPEG camera video over Wi-Fi (http://<ESP32_IP>:8080/).
4. Listens for autonomous drive commands ('GO' / 'STOP') from the PC YOLO controller.
"""
from espzero import WiFi, vision, Robot
from time import sleep

# 1. Connect to Wi-Fi
wifi = WiFi()
wifi.connect("YOUR_WIFI_SSID", "YOUR_WIFI_PASSWORD")

# 2. Configure 2WD robot motors (safe GPIO pins avoiding camera conflicts)
car = Robot(left=(41, 42), right=(47, 21))

# 3. Start background Wi-Fi MJPEG video stream (port 8080)
vision.start_wifi_stream(port=8080)

print("ESP32 Vision Car ready! Awaiting autonomous driving commands from PC...")

# 4. Process real-time autonomous steering commands sent by PC YOLO controller
while True:
    if "__pc_ai_data" in globals():
        action = __pc_ai_data.get("action", "STOP")
        if action == "GO":
            car.forward(0.6)  # Drive forward when path is clear
        else:
            car.stop()        # Stop immediately when person/obstacle is detected
    sleep(0.05)
