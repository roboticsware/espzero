"""
Wi-Fi Vision YOLO Autonomous Driving Controller (PC Side)
Run this code on your PC (Mu Editor [Python 3 Mode], VS Code, or Terminal).

Requirements:
    pip install ultralytics opencv-python requests

What it does:
1. Connects to ESP32-S3 live camera MJPEG video stream (http://<ESP32_IP>:8080/).
2. Runs YOLOv8 real-time object detection (detects humans / obstacles).
3. Sends autonomous commands back to ESP32: 'STOP' if obstacle ahead, else 'GO'.
4. Displays annotated video feed on PC screen.
"""
import cv2
import requests
from ultralytics import YOLO

# 1. Load lightweight YOLOv8 nano model
model = YOLO("yolov8n.pt")

# 2. Change this to your ESP32 board's Wi-Fi IP address printed on terminal
ESP_IP = "192.168.0.50"
STREAM_URL = f"http://{ESP_IP}:8080/"
CMD_URL = f"http://{ESP_IP}:8080/ai"

print(f"Connecting to ESP32 camera stream at {STREAM_URL} ...")
cap = cv2.VideoCapture(STREAM_URL)

if not cap.isOpened():
    print(f"Error: Could not open video stream from {STREAM_URL}")
    print("Ensure the ESP32 is powered on and connected to the same Wi-Fi network.")
    exit(1)

print("Connected! Running YOLOv8 object detection. Press 'q' in video window to exit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab video frame.")
        break

    # Run YOLOv8 inference (class 0 = person)
    results = model(frame, verbose=False)
    person_detected = False

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            if cls_id == 0:  # Person detected in path
                person_detected = True

    # Decide action: STOP if person in front, otherwise GO
    cmd = "STOP" if person_detected else "GO"
    try:
        requests.get(f"{CMD_URL}?action={cmd}", timeout=0.1)
    except Exception:
        pass

    # Display video with detection bounding boxes
    annotated = results[0].plot()
    cv2.imshow("ESPZero YOLO Autonomous Driving", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
