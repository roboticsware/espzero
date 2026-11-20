"""
Multimodal AI Companion Robot (ESP32-S3 Side)
Upload this code to the ESP32-S3 board (Mu Editor [ESP32 Mode] or Thonny / mpremote).

What it does:
1. Connects to Wi-Fi.
2. Streams live video (port 8080) and live I2S audio (port 8081).
3. Receives unified vision (look_x, look_y) + voice commands from PC!
4. Updates OLED robot eyes (show_face, look_at) and NeoPixel status in real time.
"""
from espzero import WiFi, OLED, I2SMic, vision, audio, esp_led
from time import sleep

# 1. Connect to Wi-Fi
wifi = WiFi()
wifi.connect("YOUR_WIFI_SSID", "YOUR_WIFI_PASSWORD")

# 2. Initialize OLED Robot Face & I2S Microphone
oled = OLED(scl=47, sda=21)
mic = I2SMic()

# 3. Start dual Wi-Fi streaming servers
# Port 8080: Camera MJPEG Video Stream
# Port 8081: I2S Microphone WAV Audio Stream
vision.start_wifi_stream(port=8080)
audio.start_wifi_stream(mic=mic, port=8081)

oled.show_face("normal")
print("ESP32 Multimodal Robot is ready! Streaming video on 8080 & audio on 8081.")

while True:
    # Check for AI visual tracking coordinates (from vision endpoint /ai)
    # PC sends: requests.get(f"http://{ESP_IP}:8080/ai?hand_x=0.2&hand_y=-0.1&detected=1")
    if "__pc_ai_data" in globals():
        detected = __pc_ai_data.get("detected", False)
        if detected:
            hx = __pc_ai_data.get("hand_x", 0.0)
            hy = __pc_ai_data.get("hand_y", 0.0)
            oled.look_at(hx, hy, emotion="happy")
            esp_led.color = "green"

    # Check for AI voice commands (from audio endpoint /ai)
    # PC sends: requests.get(f"http://{ESP_IP}:8081/ai?action=DANCE&score=0.9")
    audio_res = audio.get_ai_result()
    action = (audio_res.get("action") or "").upper()
    if action == "HAPPY":
        oled.show_face("happy")
        esp_led.color = "yellow"
        sleep(0.5)
    elif action == "SURPRISED":
        oled.show_face("surprised")
        esp_led.color = "red"
        sleep(0.5)
    elif action == "LOVE":
        oled.show_face("love")
        esp_led.color = "purple"
        sleep(0.5)

    sleep(0.05)
