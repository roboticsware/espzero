"""
Voice-Controlled Smart Car Controller via PC Microphone (PC Side)
Run this code on your PC (Mu Editor [Python 3 Mode], VS Code, or Terminal).

Requirements:
    pip install SpeechRecognition requests PyAudio

What it does:
1. Listens for your voice using PC / laptop built-in microphone.
2. Transcribes voice commands using SpeechRecognition (Google STT).
3. Sends movement commands ('GO', 'BACK', 'LEFT', 'RIGHT', 'STOP', 'DANCE') to ESP32 over Wi-Fi.
"""
import requests
import speech_recognition as sr

# Change this to your ESP32 board's Wi-Fi IP address printed on terminal
ESP_IP = "192.168.0.50"
CMD_URL = f"http://{ESP_IP}:8080/ai"

recognizer = sr.Recognizer()
mic = sr.Microphone()  # Uses PC / laptop built-in microphone

print("=== PC Voice-Controlled Smart Car Controller ===")
print("Command examples: 'forward'/'go', 'back', 'left', 'right', 'stop', 'dance'")
print("한국어 명령어: '출발'/'앞으로', '뒤로', '왼쪽', '오른쪽', '멈춰', '춤춰'")

with mic as source:
    recognizer.adjust_for_ambient_noise(source)

while True:
    print("\n[Listening... Speak into PC microphone]")
    with mic as source:
        audio = recognizer.listen(source)

    try:
        # Change language to "ko-KR", "en-US", "uz-UZ", etc.
        text = recognizer.recognize_google(audio, language="ko-KR")
        print("Recognized voice:", text)

        action = None
        lower = text.lower()

        if "출발" in text or "앞으로" in text or "가자" in text or "forward" in lower or "go" in lower:
            action = "GO"
        elif "뒤로" in text or "후진" in text or "back" in lower:
            action = "BACK"
        elif "왼쪽" in text or "left" in lower:
            action = "LEFT"
        elif "오른쪽" in text or "right" in lower:
            action = "RIGHT"
        elif "멈춰" in text or "정지" in text or "stop" in lower:
            action = "STOP"
        elif "춤" in text or "dance" in lower:
            action = "DANCE"

        if action:
            requests.get(CMD_URL, params={"action": action}, timeout=0.5)
            print(f"Sent command to ESP32: action={action}")

    except sr.UnknownValueError:
        pass
    except Exception as e:
        print("Communication error:", e)
