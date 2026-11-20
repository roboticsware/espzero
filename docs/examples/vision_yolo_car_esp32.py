"""Wi-Fi Vision YOLO Autonomous Car (ESP32)"""
from espzero import WiFi, vision, Robot
from time import sleep

WiFi().connect("YOUR_WIFI_SSID", "YOUR_WIFI_PASSWORD")
car = Robot(left=(41, 42), right=(47, 21))
vision.start_wifi_stream(port=8080)

while True:
    if "__pc_ai_data" in globals():
        if __pc_ai_data.get("action") == "GO":
            car.forward(0.6)
        else:
            car.stop()
    sleep(0.05)
