"""Voice-Controlled Smart Car Controller (PC)"""
import requests
import speech_recognition as sr

ESP_IP = "192.168.0.50"  # ESP32 IP
CMD_URL = f"http://{ESP_IP}:8080/ai"

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source)

while True:
    with mic as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="ko-KR").lower()
        print("Voice:", text)

        action = None
        if any(w in text for w in ("출발", "앞으로", "forward", "go")):
            action = "GO"
        elif any(w in text for w in ("뒤로", "후진", "back")):
            action = "BACK"
        elif any(w in text for w in ("왼쪽", "left")):
            action = "LEFT"
        elif any(w in text for w in ("오른쪽", "right")):
            action = "RIGHT"
        elif any(w in text for w in ("멈춰", "정지", "stop")):
            action = "STOP"
        elif any(w in text for w in ("춤", "dance")):
            action = "DANCE"

        if action:
            requests.get(CMD_URL, params={"action": action}, timeout=0.5)
    except sr.UnknownValueError:
        pass
