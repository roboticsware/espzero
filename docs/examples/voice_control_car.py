"""
Voice-Controlled Robot Car via PC Microphone (ESP32 Side)
No microphone and no OLED required on the ESP32!
The PC/laptop microphone listens for voice commands via SpeechRecognition,
and sends movement commands to the ESP32 robot car over Wi-Fi HTTP.
"""
from espzero import WiFi, Robot, vision, esp_led
from time import sleep

# 1. Connect to local Wi-Fi
wifi = WiFi()
wifi.connect("YOUR_WIFI_SSID", "YOUR_WIFI_PASSWORD")

# 2. Setup 2WD Robot Motors (camera-safe pins)
car = Robot(left=(41, 42), right=(47, 21))

# 3. Start background HTTP server to receive AI commands (port 8080)
vision.start_wifi_stream(port=8080)

print("ESP32 Robot ready! Waiting for voice commands from PC...")

while True:
    if "__pc_ai_data" in globals():
        action = __pc_ai_data.get("action", "")

        # Control Robot Car movements
        if action == "GO":
            car.forward(0.6)
            esp_led.color = "green"
        elif action == "BACK":
            car.backward(0.5)
            esp_led.color = "orange"
        elif action == "LEFT":
            car.left(0.7, t=0.4, wait=True)
            car.stop()
        elif action == "RIGHT":
            car.right(0.7, t=0.4, wait=True)
            car.stop()
        elif action == "STOP":
            car.stop()
            esp_led.color = "red"
        elif action == "DANCE":
            esp_led.color = "purple"
            car.left(0.8, t=0.3, wait=True)
            car.right(0.8, t=0.3, wait=True)
            car.stop()

    sleep(0.05)
