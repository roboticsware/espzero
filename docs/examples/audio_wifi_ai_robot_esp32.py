"""
Wi-Fi Audio Streaming + Voice AI Robot (ESP32-S3 Side)
Run this code on the ESP32-S3 board (Mu Editor [ESP32 Mode] or Thonny / mpremote).

What it does:
1. Connects to local Wi-Fi network.
2. Streams live 16-bit WAV audio from I2S microphone (port 8081).
3. Polls the /ai endpoint for action commands ('GO', 'STOP', 'DANCE') sent by PC!
"""
from espzero import WiFi, I2SMic, OLED, Robot, audio, esp_led
from time import sleep

# 1. Connect to Wi-Fi
wifi = WiFi()
wifi.connect("YOUR_WIFI_SSID", "YOUR_WIFI_PASSWORD")

# 2. Initialize I2S microphone, OLED face, and optional 2WD robot
mic = I2SMic()
oled = OLED(scl=47, sda=21)
robot = Robot(left=(41, 42), right=(47, 21))

# 3. Start background HTTP WAV audio streaming server (port 8081)
audio.start_wifi_stream(mic=mic, port=8081)
oled.show_face("listening")

# 4. Poll real-time AI classification results from PC (/ai?label=...&score=...&action=...)
while True:
    res = audio.get_ai_result()
    action = (res.get("action") or "").upper()
    score = res.get("score", 0.0)

    if score >= 0.7:
        if action == "GO":
            oled.show_face("happy")
            esp_led.color = "green"
            robot.forward(0.6)
        elif action == "STOP":
            oled.show_face("surprised")
            esp_led.color = "red"
            robot.stop()
        elif action == "DANCE":
            oled.show_face("love")
            esp_led.color = "purple"
            robot.left(0.7, t=0.4, wait=True)
            robot.right(0.7, t=0.4, wait=True)
            robot.stop()

    sleep(0.05)
