Recipes
=======

This section covers practical examples for controlling various sensors and components using ``espzero``. All examples assume ``import espzero; espzero.begin()`` has been called.

Built-in LED
------------

The simplest way to control the on-board LED.

.. code-block:: python

    from espzero import esp_led
    from time import sleep

    esp_led.on()    # Turn on
    sleep(1)
    esp_led.off()   # Turn off
    esp_led.blink() # Blink in the background

Digital Output (LED)
--------------------

Control a regular LED connected to a specific pin.

.. code-block:: python

    from espzero import LED

    led = LED(4) # GPIO 4

    led.on()
    led.off()
    led.toggle()
    
    # Blink 5 times with 0.5s intervals (asynchronous)
    led.blink(on_time=0.5, off_time=0.5, n=5)

PWM Control (Brightness)
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    led.value = 0.5 # 50% brightness
    led.pulse()     # Fade in and out repeatedly

RGB LED
-------

External 4-pin RGB LED
~~~~~~~~~~~~~~~~~~~~~~

Combine Red, Green, and Blue pins to create various colors.
(Note: ESP32-S3 boards lack pins 22–34, so use universally supported pins such as GPIO 4, 5, 6.)

.. code-block:: python

    from espzero import RGBLED
    from time import sleep

    # Universally supported pins for ESP32 and ESP32-S3 (e.g. GPIO 4, 5, 6)
    rgb = RGBLED(red=4, green=5, blue=6)

    rgb.color = (255, 0, 0)   # Red
    sleep(0.5)
    rgb.color = (0, 255, 0)   # Green
    sleep(0.5)
    rgb.color = (255, 255, 0) # Yellow (Red + Green)
    sleep(0.5)

    # Adjust individual channel brightness (0~255)
    rgb.red = 128
    rgb.blue = 255

    # Color inversion and toggle
    rgb.invert()
    rgb.toggle()

    # Dynamic animations (blink, pulse fade, rainbow cycle)
    rgb.blink(on_times=0.5, colors=((255, 0, 0), (0, 255, 0), (0, 0, 255)), n=2, wait=True)
    rgb.pulse(fade_times=1, n=2, wait=True)  # Smooth fade pulse
    rgb.cycle(fade_times=1, n=2, wait=True)  # Rainbow color cycle

    rgb.off()

Built-in Onboard RGB LED (ESP32-S3 WS2812 NeoPixel)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For boards with a built-in WS2812 NeoPixel RGB LED (such as ESP32-S3 DevKit or M5Stack), simply use ``esp_led`` without specifying pin numbers:

.. code-block:: python

    from espzero import esp_led
    from time import sleep

    esp_led.color = (255, 0, 0)   # Red
    sleep(0.5)
    esp_led.color = (0, 255, 0)   # Green
    sleep(0.5)
    esp_led.color = (0, 0, 255)   # Blue
    sleep(0.5)

    # On-board NeoPixel rainbow cycle animation
    esp_led.cycle(fade_times=0.5, n=3, wait=True)
    esp_led.off()

Buzzer & Speaker
----------------

Simple Beep
~~~~~~~~~~~

.. code-block:: python

    from espzero import Buzzer

    bz = Buzzer(15)
    bz.beep(on_time=0.1, off_time=0.1, n=3) # "Beep-Beep-Beep"

Playing Melodies
~~~~~~~~~~~~~~~~

.. code-block:: python

    from espzero import Speaker

    spk = Speaker(15)

    # List of (note, duration) tuples
    tune = [
        ('c4', 0.5), ('d4', 0.5), ('e4', 0.5), ('c4', 0.5),
        ('e4', 0.5), ('c4', 0.5), ('g4', 1.0)
    ]
    spk.play(tune)

Input Devices
-------------

Button
~~~~~~

.. code-block:: python

    from espzero import Button

    btn = Button(5)

    btn.when_pressed = lambda: print("Pressed!")
    btn.when_released = lambda: print("Released!")

Potentiometer
~~~~~~~~~~~~~

.. code-block:: python

    from espzero import Pot

    pot = Pot(34) # Analog pin (ADC)

    print("Current value (0-1):", pot.value)
    print("Voltage (V):", pot.voltage)

Servo Motor (Servo)
~~~~~~~~~~~~~~~~~~~

Control standard servo motors via ratio (0.0 to 1.0) or angles (0 to 180 degrees) with ``picozero-rw`` compatibility.

.. code-block:: python

    from espzero import Servo
    from time import sleep

    servo = Servo(13)

    # Position control (0.0: min, 0.5: mid, 1.0: max)
    servo.mid()
    sleep(1)

    # Move to specific angle (move_to_degree API)
    servo.move_to_degree(90)   # 90 degrees (mid)
    sleep(1)
    servo.move_to_degree(180)  # 180 degrees (max)
    sleep(1)
    servo.move_to_degree(0)    # 0 degrees (min)

    # Smooth sweeping back and forth (0 deg <-> 180 deg)
    servo.pulse(fade_in_time=1, fade_out_time=1)

Motors & Robots (Motor & Robot)
-------------------------------

DC Motor (Motor)
~~~~~~~~~~~~~~~~

Control bidirectional DC motors via motor driver boards (e.g. L298N, L9110S, DRV8833).

.. code-block:: python

    from espzero import Motor
    from time import sleep

    # Specify forward and backward GPIO pins (supports PWM speed control)
    motor = Motor(forward=4, backward=5)

    # Rotate forward at full speed
    motor.forward()
    sleep(1)

    # Rotate backward at 50% speed
    motor.backward(0.5)
    sleep(1)

    # Timed rotation (runs for 1s then stops automatically)
    motor.forward(speed=0.8, t=1, wait=True)

    # Stop motor
    motor.stop()

Robot Rover (Two-Wheel Drive Platform)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Easily steer a 2-wheeled robot rover with forward, backward, left, and right movements.

.. code-block:: python

    from espzero import Robot
    from time import sleep

    # left=(fwd_pin, bwd_pin), right=(fwd_pin, bwd_pin)
    robot = Robot(left=(4, 5), right=(6, 7))

    # Basic movements
    robot.forward()
    sleep(1)
    robot.backward(0.6)
    sleep(1)

    # Turning left and right
    robot.left(speed=0.8)
    sleep(0.5)
    robot.right(speed=0.8)
    sleep(0.5)

    # Timed movements (drive in a square pattern)
    for _ in range(4):
        robot.forward(t=1, wait=True)
        robot.left(t=0.5, wait=True)

    # Stop rover
    robot.stop()

Built-in Touch Sensor (Capacitive Touch)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the built-in capacitive touch peripheral on ESP32 / ESP32-S3. Detects touch directly from a finger or conductive wire without external resistors.

.. code-block:: python

    from espzero import CapTouch
    from time import sleep

    # WROOM: T0~T9 (e.g. GPIO 4), ESP32-S3: touch-capable pin (e.g. GPIO 1)
    touch = CapTouch(1)

    while True:
        # value: raw capacitance reading (decreases when touched)
        # is_touched: True if raw value drops below threshold (default: 300)
        print("Raw:", touch.value, "Touched:", touch.is_touched)
        sleep(0.2)

Distance Sensor
---------------

Measure distance using an ultrasonic sensor like HC-SR04.

.. code-block:: python

    from espzero import DistanceSensor

    # echo=14, trigger=13
    ds = DistanceSensor(echo=14, trigger=13)

    while True:
        print("Distance: ", ds.distance, "cm")
        sleep(0.5)

Temperature Sensor
------------------

Internal Temperature
~~~~~~~~~~~~~~~~~~~~

Measure the internal temperature of the ESP32 chip. (Note: May differ from ambient temperature).

.. code-block:: python

    from espzero import esp_temp_sensor

    print("Internal chip temp:", esp_temp_sensor.temp, "C")

Complex Example: Button-controlled Light
---------------------------------------

Toggle an LED each time a button is pressed.

.. code-block:: python

    from espzero import LED, Button, begin

    begin()
    led = LED(4)
    btn = Button(5)

    btn.when_pressed = led.toggle

    while True:
        pass # Wait for events

Stepper Motor
-------------

Control a stepper motor connected via a driver board (e.g. ULN2003).

Analog clock
~~~~~~~~~~~~

Create a continuously-running analog clock second hand:

.. literalinclude:: examples/stepper_analog_clock.py

Automatic blinds
~~~~~~~~~~~~~~~~

Time-based blind controller:

.. literalinclude:: examples/stepper_automatic_blinds.py

LCD Display
-----------

Print characters on LiquidCrystal displays (LCD) by using the I2C bus and a PCF8574 I2C adapter.

.. literalinclude:: examples/i2c_lcd.py

Print characters on LiquidCrystal displays (LCD) by using GPIO pins only.

.. literalinclude:: examples/lcd.py


AI Vision
---------

Examples for using the ESP32-S3 camera with PC-assisted AI and standalone on-device AI.

.. important::
    **Camera-Enabled Firmware Required**:
    The official generic MicroPython firmware does not include the camera C driver (``camera`` module).
    To use vision features, ensure your board (e.g. ESP32-S3 WROOM CAM) is flashed with a **Camera-enabled MicroPython firmware**.

PC-Side AI (with MediaPipe)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Streams camera images to the PC (Pico Editor), which uses Google's MediaPipe library to track hands, faces, etc., in real time. The detected coordinates are sent back to the ESP32 for hardware control.

.. code-block:: python

    from espzero import vision
    from time import sleep

    # Start streaming camera frames to the PC (non-blocking background thread)
    vision.start_stream_to_pc()

    while True:
        # Read the hand coordinates injected by the editor
        if "__pc_ai_data" in globals():
            x = __pc_ai_data.get("hand_x", 0)
            y = __pc_ai_data.get("hand_y", 0)
            detected = __pc_ai_data.get("hand_detected", False)
            if detected:
                print("Hand detected -> X:", x, "Y:", y)
        sleep(0.1)

Wi-Fi Video Streaming & PC YOLO Autonomous Driving
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As a microcontroller, the ESP32-S3 has limited hardware RAM and computing power, making it challenging to run heavy modern deep learning models (such as YOLOv8) directly on-device.
However, by dividing responsibilities between the ESP32 and a PC over **Wi-Fi**, you can build a high-performance autonomous driving robot car with ease.

**Working Principle & Role Division**:

.. code-block:: text

    [ ESP32 Robot Car ] (Eyes & Feet)
      - Streams camera video wirelessly over Wi-Fi (MJPEG stream)
      - Drives DC motors according to received wireless commands ('GO' / 'STOP')
      ▲
      │  (Wi-Fi Network: Real-time Video Stream & Driving Commands)
      ▼
    [ PC / Mu Editor - Python 3 Mode ] (Brain)
      - Receives Wi-Fi video stream and runs YOLOv8 in real time on PC CPU/GPU
      - Detects obstacles/pedestrians and sends 'STOP' or 'GO' commands wirelessly

**Step-by-Step Practical Guide with Mu Editor**:

1. **PC YOLO Environment Setup**:
   Install the required packages to run YOLO inference on your PC:
   * **Option A (In Mu Editor)**: Click the **Settings (gear icon)** at bottom-right → **[Third-party Packages]** tab, enter ``ultralytics``, and click [OK].
   * **Option B (In Terminal)**: Open CMD or PowerShell and run ``pip install ultralytics opencv-python requests``.

2. **Step 1: Upload ESP32 Robot Car Code (Mu [ESP32 Mode])**:
   Switch Mu Editor to **ESP32 mode** and save the code below as ``main.py`` on the board.
   (Saving as ``main.py`` allows you to unplug the USB cable and power the car with batteries; it will automatically connect to Wi-Fi and start streaming on boot. Check the ESP32 IP address printed in the REPL, e.g., ``192.168.0.50``.)

.. code-block:: python

    from espzero import WiFi, vision, Robot
    from time import sleep

    # 1. Connect to Wi-Fi access point
    wifi = WiFi()
    wifi.connect("My_WiFi_SSID", "password")

    # 2. Configure 2-wheel robot motors (Left: GPIO 4, 5 / Right: GPIO 6, 7)
    car = Robot(left=(4, 5), right=(6, 7))

    # 3. Start wireless camera stream (default port: 8080)
    vision.start_wifi_stream(port=8080)

    # 4. Driving loop reading AI decisions from PC
    while True:
        if "__pc_ai_data" in globals():
            action = __pc_ai_data.get("action", "STOP")
            if action == "GO":
                car.forward(0.6) # Move forward when clear
            else:
                car.stop()       # Stop if pedestrian or obstacle detected
        sleep(0.05)

3. **Step 2: Run PC AI Autonomous Driving Controller (Mu [Python 3 Mode])**:
   Switch Mu Editor mode to **Python 3 mode** via the **[Mode]** button at top-left.
   Paste the script below into a new tab, replace the ESP32 IP address in ``STREAM_URL`` and ``CMD_URL``, and click **[Play]**.
   A live video window showing real-time detection boxes will appear on your PC, autonomously piloting the robot car!

.. code-block:: python

    import cv2
    import requests
    from ultralytics import YOLO

    # Load lightweight YOLOv8 nano model and configure ESP32 stream URL
    model = YOLO("yolov8n.pt")
    STREAM_URL = "http://192.168.0.50:8080/"  # ESP32 IP address
    CMD_URL = "http://192.168.0.50:8080/ai"

    cap = cv2.VideoCapture(STREAM_URL)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Real-time object inference (Class 0: Person, 9: Traffic Light)
        results = model(frame, verbose=False)
        person_detected = False

        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                if cls_id == 0: # Person detected
                    person_detected = True

        # Send GO / STOP action wirelessly
        cmd = "STOP" if person_detected else "GO"
        try:
            requests.get(f"{CMD_URL}?action={cmd}", timeout=0.1)
        except Exception:
            pass

        # Display annotated bounding box video
        annotated = results[0].plot()
        cv2.imshow("ESP32-S3 YOLO AI Auto-Driving", annotated)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

On-Device AI (On-Device TFLite)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Loads a `.tflite` model file directly from the ESP32's file system to perform local AI inference. It can run independently of any computer.

.. note::
    Lightweight `.tflite` models for ESP32 and microcontrollers can be downloaded directly from Kaggle Models (https://www.kaggle.com/models?framework=liteRT), Hugging Face LiteRT Community (https://huggingface.co/litert-community), or the official TensorFlow Lite Micro repository (https://github.com/tensorflow/tflite-micro).

.. code-block:: python

    import camera
    import tflite
    from time import sleep

    # Initialize camera and load TFLite model
    camera.init(framesize=camera.FRAME_QVGA)
    model = tflite.load("model.tflite")

    while True:
        img = camera.capture()
        if img:
            # Perform inference and extract the class result
            result = model.detect(img)
            print("Detected class ID:", result.class_id)
        sleep(0.5)

