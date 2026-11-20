"""
Wi-Fi Audio Streaming Voice AI Controller (PC Side)
Run this code on your PC (Mu Editor [Python 3 Mode], VS Code, or Terminal).

Requirements:
    pip install requests SpeechRecognition

What it does:
1. Connects to ESP32-S3 live WAV audio stream (http://<ESP32_IP>:8081/).
2. Listens for speech using SpeechRecognition (Google STT / Whisper).
3. Sends recognized action commands back to ESP32 (http://<ESP32_IP>:8081/ai?action=...).
"""
import io
import requests
import speech_recognition as sr

# Change this to your ESP32 board's Wi-Fi IP address printed on terminal
ESP_IP = "192.168.0.50"
AUDIO_STREAM_URL = f"http://{ESP_IP}:8081/"
AI_FEEDBACK_URL = f"http://{ESP_IP}:8081/ai"

SAMPLE_RATE = 16000
CHUNK_BYTES = SAMPLE_RATE * 2 * 2  # 2-second audio chunks (16kHz * 16-bit mono)

recognizer = sr.Recognizer()

print(f"Connecting to ESP32 live audio stream at {AUDIO_STREAM_URL} ...")
try:
    with requests.get(AUDIO_STREAM_URL, stream=True) as resp:
        resp.raw.read(44)  # Skip 44-byte standard WAV header
        print("Connected to ESP32 stream! Speak into the ESP32 microphone (e.g., 'forward', 'stop', 'dance'):")

        while True:
            pcm_chunk = resp.raw.read(CHUNK_BYTES)
            if not pcm_chunk:
                break

            audio_data = sr.AudioData(pcm_chunk, SAMPLE_RATE, 2)
            try:
                # Transcribe speech (language="ko-KR", "en-US", "uz-UZ", etc.)
                text = recognizer.recognize_google(audio_data, language="ko-KR")
                print("Recognized speech:", text)

                action = None
                if "출발" in text or "앞으로" in text or "가자" in text or "forward" in text or "go" in text:
                    action = "GO"
                elif "멈춰" in text or "정지" in text or "stop" in text:
                    action = "STOP"
                elif "춤" in text or "dance" in text or "raqs" in text:
                    action = "DANCE"

                if action:
                    requests.get(AI_FEEDBACK_URL, params={"action": action, "score": 0.95}, timeout=0.5)
                    print(f"Sent command to ESP32: action={action}")

            except sr.UnknownValueError:
                pass
            except Exception as e:
                print("Recognition error:", e)

except Exception as err:
    print(f"Failed to connect to ESP32 at {AUDIO_STREAM_URL}: {err}")
    print("Make sure the ESP32 is powered on and connected to the same Wi-Fi network.")
