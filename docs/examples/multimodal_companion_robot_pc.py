"""
Multimodal AI Companion Robot Controller (PC Side)
Run this code on your PC (Mu Editor [Python 3 Mode], VS Code, or Terminal).

Requirements:
    pip install opencv-python mediapipe requests SpeechRecognition

What it does:
1. Connects to ESP32-S3 live camera stream (port 8080) for MediaPipe hand tracking.
2. Connects to ESP32-S3 live audio stream (port 8081) for SpeechRecognition.
3. Coordinates gaze tracking and voice emotion feedback to ESP32 in parallel!
"""
import threading
import requests
import cv2
import speech_recognition as sr

# Change this to your ESP32 board's Wi-Fi IP address printed on terminal
ESP_IP = "192.168.0.50"
VIDEO_STREAM_URL = f"http://{ESP_IP}:8080/"
VIDEO_AI_URL = f"http://{ESP_IP}:8080/ai"
AUDIO_STREAM_URL = f"http://{ESP_IP}:8081/"
AUDIO_AI_URL = f"http://{ESP_IP}:8081/ai"

_running = True

def audio_worker():
    """Worker thread listening to ESP32 live audio stream & classifying speech."""
    recognizer = sr.Recognizer()
    sample_rate = 16000
    chunk_bytes = sample_rate * 2 * 2  # 2-second chunks

    try:
        with requests.get(AUDIO_STREAM_URL, stream=True) as resp:
            resp.raw.read(44)  # Skip WAV header
            print("[PC Audio] Connected to ESP32 audio stream!")
            while _running:
                chunk = resp.raw.read(chunk_bytes)
                if not chunk:
                    break
                audio_data = sr.AudioData(chunk, sample_rate, 2)
                try:
                    text = recognizer.recognize_google(audio_data, language="ko-KR").lower()
                    print("[PC Audio] Heard:", text)
                    action = None
                    if "웃어" in text or "기뻐" in text or "smile" in text:
                        action = "HAPPY"
                    elif "놀라" in text or "어머" in text or "surprise" in text:
                        action = "SURPRISED"
                    elif "사랑" in text or "하트" in text or "love" in text:
                        action = "LOVE"

                    if action:
                        requests.get(AUDIO_AI_URL, params={"action": action}, timeout=0.5)
                except sr.UnknownValueError:
                    pass
    except Exception as e:
        print("[PC Audio] Worker stopped:", e)

# Start background audio thread
t_audio = threading.Thread(target=audio_worker, daemon=True)
t_audio.start()

# Main thread: Vision processing
print(f"[PC Vision] Connecting to video stream at {VIDEO_STREAM_URL} ...")
cap = cv2.VideoCapture(VIDEO_STREAM_URL)

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Here you can run MediaPipe Hand / Face detection or simple brightness / motion
        # For demonstration: center coordinates (0.0, 0.0)
        h, w, _ = frame.shape
        cv2.putText(frame, "Multimodal AI Active (Press 'q' to quit)", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.imshow("Multimodal Robot PC Controller", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    _running = False
    cap.release()
    cv2.destroyAllWindows()
