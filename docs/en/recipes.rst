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

.. image:: /images/circuit_led.svg
    :alt: ESP32 LED Circuit Wiring Diagram
    :align: center

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

.. image:: /images/circuit_rgb.svg
    :alt: ESP32 RGB LED Circuit Wiring Diagram
    :align: center

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

    # Named color strings are also supported (red, green, blue, yellow, cyan, magenta, purple, white, black, orange)
    rgb.color = "cyan"
    sleep(0.5)
    rgb.color = "orange"
    sleep(0.5)

    # Adjust individual channel brightness (0~255)
    rgb.red = 128
    rgb.blue = 255

    # Color inversion and toggle
    rgb.invert()
    rgb.toggle()

    # Dynamic animations (blink, pulse fade, rainbow cycle — named colors also work in colors=)
    rgb.blink(on_times=0.5, colors=("red", "cyan", "orange"), n=2, wait=True)
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

.. image:: /images/circuit_buzzer.svg
    :alt: ESP32-S3 Buzzer Circuit Wiring Diagram
    :align: center

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

I2S Digital Speaker (I2SSpeaker)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``I2SSpeaker`` drives a 3.3V/5V I2S amplifier module (such as ``MAX98357A``) on hardware ``I2S(1)`` (TX mode) for high-quality WAV/PCM voice and sound playback. On ESP32-S3, it automatically maps camera-safe pins (``BCLK=38, LRC=39, DIN=40``) so it runs alongside ``I2SMic`` (``I2S(0)``) and the OV2640 camera without conflicts.

.. image:: /images/circuit_i2s_speaker.svg
    :alt: ESP32-S3 I2S Digital Speaker (MAX98357A) Circuit Diagram
    :align: center

.. code-block:: python

    from espzero import I2SSpeaker

    # ESP32-S3 defaults: BCLK=38, LRC=39, DIN=40 (I2S 1 TX)
    spk = I2SSpeaker(sample_rate=24000)

    # Play a WAV file (auto-skips 44B header) or raw 16-bit PCM bytes via play_pcm()
    spk.play_wav("hello.wav")
    spk.close()

Microphone (I2S Microphone)
---------------------------

Using the ESP32-S3's processing performance and native I2S peripheral, you can capture crystal-clear audio directly from 24-bit digital MEMS microphones (such as the INMP441) and perform real-time signal analysis.

Connecting an I2S Microphone (INMP441, 3.3V)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``INMP441`` supports native 3.3V power and standard digital I2S signaling (SCK, WS, SD), offering much higher signal-to-noise ratio and immunity from interference compared to traditional analog microphones.
It connects directly to the safe default pins of the ESP32-S3 WROOM CAM (``SCK=41``, ``WS=42``, ``SD=2``) without requiring a level shifter.
(For single mono operation, wire the ``L/R`` pin to ``GND`` to select the left audio channel.)

.. image:: /images/circuit_inmp441_mic.svg
    :alt: ESP32-S3 I2S Digital Microphone (INMP441) Circuit Diagram
    :align: center

Basic Usage & Sound Detection (I2SMic)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instantiating ``I2SMic()`` automatically maps the safe hardware pins from the active board profile, providing sound volume (``level``, ``0.0 ~ 1.0``), sound pressure in decibels (``decibels``), dominant musical note (``note``), and clap detection events (``when_clap``).

.. code-block:: python

    from espzero import I2SMic, esp_led
    from time import sleep

    # Automatically maps safe I2S pins (ESP32-S3: SCK=41, WS=42, SD=2)
    mic = I2SMic()

    # Toggle the onboard LED whenever a clap or loud sound occurs
    mic.when_clap = esp_led.toggle

    while True:
        print("Level:", round(mic.level, 3), "| dB:", int(mic.decibels), "| Note:", mic.note or "---")
        sleep(0.2)

Real-Time OLED Audio Spectrum Visualizer (FFT Spectrum)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Compute a 16-band frequency spectrum using ``mic.spectrum(bins=16)`` and render real-time equalizer bars on an OLED display (``oled.show_spectrum()``), while pulsing the RGB LED on strong bass beats.

.. literalinclude:: examples/audio_spectrum_oled.py
      :start-at: from espzero import

Input Devices
-------------

Button
~~~~~~

.. image:: /images/circuit_button.svg
    :alt: ESP32 Button Circuit Wiring Diagram
    :align: center

.. code-block:: python

    from espzero import Button

    btn = Button(5)

    btn.when_pressed = lambda: print("Pressed!")
    btn.when_released = lambda: print("Released!")

Potentiometer
~~~~~~~~~~~~~

.. image:: /images/circuit_potentiometer.svg
    :alt: ESP32 Potentiometer Circuit Wiring Diagram
    :align: center

.. code-block:: python

    from espzero import Pot

    pot = Pot(1) # Analog pin (ADC1_CH0, ESP32-S3)

    print("Current value (0-1):", pot.value)
    print("Voltage (V):", pot.voltage)

Built-in Touch Sensor (Capacitive Touch)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the built-in capacitive touch peripheral on ESP32 / ESP32-S3. Detects touch directly from a finger or conductive wire without external resistors. (Also available via the ``InternalTouchSensor`` alias.)

.. note::
    **Difference from External ``TouchSensor``**:
    If you are connecting an external digital touch module (such as TTP223), use the ``picozero-rw``-compatible ``TouchSensor(pin)`` class instead. ``CapTouch`` (``InternalTouchSensor``) is specifically for ESP32's built-in hardware touch pins with no external module.

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

Internal Temperature Sensor
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Measure the internal temperature of the ESP32 chip. (Note: May differ from ambient temperature).

.. code-block:: python

    from espzero import esp_temp_sensor

    print("Internal chip temp:", esp_temp_sensor.temp, "C")

Distance Sensor
---------------

Measure distance safely on ESP32-S3 using a 3.3V-compatible ultrasonic sensor such as ``HC-SR04P``.

.. image:: /images/circuit_distance.svg
    :alt: ESP32-S3 HC-SR04P Ultrasonic Distance Sensor Circuit Wiring Diagram
    :align: center

.. warning::
    **Overvoltage Risk with Legacy 5V-Only HC-SR04 Sensors**:
    ESP32-S3 GPIOs have a maximum input tolerance of **3.6V**. Newer **HC-SR04P** / **HC-SR04+** sensors run directly from the board's **3V3** pin with safe 3.3V logic.
    If you use a legacy 5V-only **HC-SR04**, its ``ECHO`` pin outputs **5V**, which can damage ``G14``. You must insert a **1kΩ + 2kΩ resistor voltage divider** (``ECHO → 1kΩ → G14``, ``G14 → 2kΩ → GND``) to step the ``ECHO`` signal down to ~3.3V.

.. code-block:: python

    from espzero import DistanceSensor

    # echo=14, trigger=13
    ds = DistanceSensor(echo=14, trigger=13)

    while True:
        print("Distance: ", ds.distance, "cm")
        sleep(0.5)

DC Motors & Robots (DC Motor & Robot)
-------------------------------------

DC Motor (Motor)
~~~~~~~~~~~~~~~~

Control bidirectional DC motors via motor driver boards (e.g. L298N, L9110S, DRV8833).

.. image:: /images/circuit_motor.svg
    :alt: ESP32 DC Motor Driver Circuit Wiring Diagram
    :align: center

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

.. image:: /images/circuit_robot.svg
    :alt: ESP32 2-Wheel Robot Rover Circuit Wiring Diagram
    :align: center

.. code-block:: python

    from espzero import Robot
    from time import sleep

    # left=(fwd_pin, bwd_pin), right=(fwd_pin, bwd_pin) using camera-safe GPIOs
    robot = Robot(left=(41, 42), right=(47, 21))

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

Servo Motor (Servo)
-------------------

Control standard servo motors via ratio (0.0 to 1.0) or angles (0 to 180 degrees) with ``picozero-rw`` compatibility.

.. image:: /images/circuit_servo.svg
    :alt: ESP32 Servo Motor Circuit Wiring Diagram
    :align: center

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

Stepper Motor
-------------

Control a 28BYJ-48 stepper motor precisely by angle or full revolutions via a ULN2003 driver board.

.. image:: /images/circuit_stepper.svg
    :alt: ESP32-S3 ULN2003 28BYJ-48 Stepper Motor Circuit Diagram
    :align: center

.. code-block:: python

    from espzero import Stepper
    from time import sleep

    # Connect 4 camera-safe GPIOs (IN1=42, IN2=41, IN3=47, IN4=21)
    stepper = Stepper((42, 41, 47, 21))
    stepper.set_speed(10)          # Set rotation speed to 10 RPM

    stepper.turn(90, "cw")         # Turn 90 degrees clockwise
    sleep(0.5)
    stepper.rotate(1, "ccw")       # Rotate 1 full revolution counter-clockwise
    stepper.off()                  # De-energize coils to prevent heating

Displays (OLED & LCD)
---------------------

I2C OLED Display (SSD1306 / SH1106, 3.3V Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

0.96" (``SSD1306``) and 1.3" (``SH1106``) I2C OLED displays operate natively on 3.3V logic and can connect directly to the ESP32-S3 without a level shifter.

.. image:: /images/circuit_oled.svg
    :alt: ESP32-S3 I2C OLED Display Circuit Wiring Diagram
    :align: center

.. code-block:: python

    from espzero import OLED

    # 0.96" SSD1306 (pass driver="sh1106" for 1.3" SH1106 panels)
    oled = OLED(scl=47, sda=21)

    oled.clear()
    oled.text("Hello, ESPZero!", 0, 0)
    oled.text("ESP32-S3 OLED", 0, 20)
    oled.rect(0, 36, 128, 20, color=1)
    oled.show()

Robot Face Expressions & Gaze Tracking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``oled.show_face()`` provides 10 expressive robot emotion presets (``"normal"``, ``"happy"``, ``"surprised"``, ``"love"``, ``"thinking"``, ``"sleep"``, ``"blink"``, ``"angry"``, ``"sad"``, ``"listening"``) with customizable gaze direction (``look_x``, ``look_y``).
With ``oled.look_at(x, y)``, you can directly pass camera hand-tracking coordinates or joystick readings to have the robot eyes track user movements in real time.

.. image:: ../images/oled_robot_faces.svg
    :alt: ESPZero OLED Robot Face Diagram
    :align: center

.. code-block:: python

    from espzero import OLED
    from time import sleep

    oled = OLED(scl=47, sda=21)

    # 1. Emotion presets
    oled.show_face("happy")      # Cheerful smile (^ ^)
    sleep(1)
    oled.show_face("surprised")  # Wide-eyed surprised (O O)
    sleep(1)
    oled.show_face("love")       # Heart-shaped eyes
    sleep(1)

    # 2. Gaze direction: Left (-1.0) / Right (1.0) / Up / Down
    oled.show_face("normal", look_x=-1.0, look_y=0.0)  # Look left
    sleep(1)
    oled.show_face("normal", look_x=1.0, look_y=0.0)   # Look right
    sleep(1)

    # 3. Seamless eye gaze tracking with vision.get_hand() (desktop companion robot)
    # oled.look_at(hand_x, hand_y, emotion="happy")

LCD Display (16x2, PCF8574)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Print characters on LiquidCrystal displays (LCD) using the I2C bus and a PCF8574 I2C adapter.

.. warning::
    **Level Shifter Required for 5V PCF8574 I2C Adapters**:
    Most ``16x2 I2C LCD (PCF8574)`` modules operate at 5V and pull ``SDA`` / ``SCL`` up to **5V**.
    To protect ESP32-S3's 3.3V pins (``G21``, ``G47``), always place a **3.3V↔5V bidirectional I2C logic level shifter** between the board and the PCF8574 module (or use the native **3.3V OLED display** shown above).

.. image:: /images/circuit_i2c_lcd.svg
    :alt: ESP32-S3 I2C LCD with Logic Level Shifter Circuit Wiring Diagram
    :align: center

.. literalinclude:: examples/i2c_lcd.py

Print characters on LiquidCrystal displays (LCD) by using GPIO pins only.

.. literalinclude:: examples/lcd.py


Camera
------

Capture JPEG snapshots and save photos directly to flash storage on camera-equipped boards (such as ESP32-S3 WROOM CAM) without needing a PC or external AI server.

.. important::
    **Camera-Enabled Firmware Required**:
    The official generic MicroPython firmware does not include the camera C driver (``camera`` module).
    To use camera and vision features, ensure your board (e.g. ESP32-S3 WROOM CAM) is flashed with a **Camera-enabled MicroPython firmware**.

.. note::
    **Built-in Firmware Flashing in Mu Editor (Online / Offline Supported)**:

    You do not need to install complex external command-line tools (such as esptool). Simply open Mu Editor's **Settings (gear icon)** at the bottom-right and choose either method:

    * **Online Flashing ([ESP Online Flasher] tab)**:
      If connected to the internet, you do not need to download firmware files beforehand.
      In the board drop-down menu, ensure you select the specific camera & PSRAM profile (e.g., ``ESP32-S3 Camera (OV2640 / Octal SPIRAM)``) rather than the standard Generic profile. Then click **[Get versions] → [Erase & write]** to automatically download and flash the latest camera-enabled official MicroPython firmware directly from the cloud.

    * **Offline Flashing ([ESP Firmware flasher] tab)**:
      Useful when offline or using a pre-downloaded custom camera firmware (``.bin`` file). Select your board (``ESP32-S3``), browse for the firmware file on your computer, and click **[Erase & write firmware]** to flash directly.

Capturing & Saving Photos (``vision.save_photo`` / ``vision.capture``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Calling ``vision.save_photo()`` snaps a JPEG image and writes it straight to flash in one line, automatically detecting both modern (``camera.Camera``) and legacy (``camera.init``) camera firmwares. Use ``vision.capture()`` when you need raw JPEG bytes in memory (for Telegram / cloud AI APIs) or want to safely reuse the latest frame while background streaming (``start_wifi_stream()``) is running. Call ``vision.close()`` to release the camera hardware when finished.

.. code-block:: python

    from espzero import vision

    # 1. Take a photo and save directly to flash (framesize: QQVGA, HQVGA, QVGA, VGA)
    saved = vision.save_photo("snapshot.jpg", framesize="QVGA", quality=80)
    print("Saved:", saved)

    # 2. Or grab raw JPEG bytes directly (for network upload / cloud AI)
    jpg_bytes = vision.capture(framesize="QVGA", quality=70)
    print("Image size:", len(jpg_bytes), "bytes")

    # Release camera peripheral when done
    vision.close()

Time-Lapse & Image Dataset Collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Automatically capture a sequence of photos at fixed intervals for time-lapse photography or building image training datasets (e.g. for Edge Impulse TinyML models).

.. code-block:: python

    from espzero import vision, esp_led
    from time import sleep

    for i in range(1, 6):
        esp_led.color = (0, 255, 0)
        esp_led.on()
        path = vision.save_photo(f"photo_{i:03d}.jpg", framesize="QVGA")
        esp_led.off()
        print("Captured:", path)
        sleep(2)

    vision.close()


AI Vision
---------

Examples for combining the ESP32-S3 camera with PC-assisted AI (MediaPipe, YOLOv8) and standalone on-device TinyML. (Requires the Camera-enabled firmware described in the **Camera** section above.)
PC-Side AI (with MediaPipe — Mu Editor Only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
    **Mu Editor Serial Protocol Only**: ``vision.start_stream_to_pc()`` streams JPEG frames over USB serial directly to Mu Editor's built-in Camera/MediaPipe viewer. If you are using VS Code, Thonny, or another IDE, use the **Wi-Fi Video Streaming (``vision.start_wifi_stream()``)** workflow below instead.

Streams camera images to the PC (Mu Editor), which uses Google's MediaPipe library to track hands, faces, etc., in real time. The detected coordinates are sent back to the ESP32 for hardware control.

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

**Step-by-Step Practical Guide (Mu Editor / Standard Python IDEs)**:

1. **PC YOLO Environment Setup**:
   Prepare the required packages to run YOLO inference on your PC.

   * **Option A (In Mu Editor)**:
     Mu Editor already has ``opencv-python`` and ``requests`` built-in. Simply click the **Settings (gear icon)** at bottom-right → **[Third-party Packages]** tab, enter ``ultralytics``, and click [OK].

   * **Option B (External Editors like VS Code)**:
     If running outside Mu, install all necessary packages via CMD or PowerShell:

     .. code-block:: bash

         pip install ultralytics opencv-python requests

2. **Step 1: Upload ESP32 Robot Car Code (Mu [ESP32 Mode] or Thonny / mpremote)**:

   .. literalinclude:: examples/vision_yolo_car_esp32.py
      :start-at: from espzero import

3. **Step 2: Run PC AI Autonomous Driving Controller (Mu [Python 3 Mode] or Standard Python)**:

   .. literalinclude:: examples/vision_yolo_car_pc.py
      :start-at: import cv2

.. tip::
    **Standalone Battery Operation & Outdoor Hotspot (AP Mode) Tips**

    * **Completely Untethered Operation on Battery Power (Save as main.py)**:
      When completing your smart car, surveillance camera, or robot project to run untethered from a PC, save your code as ``main.py`` at the root of the ESP32 filesystem. Once saved, you can unplug the USB cable and power the board via a power bank or battery pack. The ESP32 will automatically connect to Wi-Fi and initiate the video streaming server on boot.
      On your PC or smartphone, enter the board's URL (e.g., ``http://192.168.x.x:8080/``) in Mu Editor's Wi-Fi camera pane or in any web browser to view the live feed and control the robot wirelessly.

    * **Standalone Hotspot (AP Mode) in Classrooms or Outdoors without a Router**:
      No Wi-Fi router nearby? You can turn the ESP32 itself into an Access Point (hotspot) for direct 1:1 wireless streaming without any external network:

      .. code-block:: python

          import network
          from espzero import vision

          # 1. Enable ESP32 as a standalone Wi-Fi Access Point (hotspot)
          ap = network.WLAN(network.AP_IF)
          ap.active(True)
          ap.config(essid="ESP32-CAM-ROBOT", authmode=network.AUTH_OPEN)

          # 2. Start video stream on the hotspot network (Default IP: http://192.168.4.1:8080/)
          vision.start_wifi_stream(port=8080)

      Connect your laptop or smartphone to the ``ESP32-CAM-ROBOT`` Wi-Fi network and open ``http://192.168.4.1:8080/`` to stream video and run AI remote control anywhere outdoors.

On-Device AI (On-Device TFLite)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Loads a ``.tflite`` model file directly from the ESP32's file system to perform local AI inference. It can run independently of any computer.

.. note::
    Lightweight ``.tflite`` models for ESP32 and microcontrollers can be downloaded directly from Kaggle Models (https://www.kaggle.com/models?framework=liteRT), Hugging Face LiteRT Community (https://huggingface.co/litert-community), or the official TensorFlow Lite Micro repository (https://github.com/tensorflow/tflite-micro).

.. code-block:: python

    from espzero import vision
    import tflite
    from time import sleep

    # Load TFLite model
    model = tflite.load("model.tflite")

    while True:
        img = vision.capture(framesize="QVGA")
        if img:
            # Perform inference and extract the class result
            result = model.detect(img)
            print("Detected class ID:", result.class_id)
        sleep(0.5)


AI Voice
--------

Control ESP32 cars and robots with your voice **without adding a physical microphone** to the ESP32 board, by leveraging your PC/laptop's high-quality built-in microphone over Wi-Fi.

Voice-Controlled Smart Car via PC Microphone
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This approach requires minimal hardware wiring and ensures high speech recognition accuracy even in noisy classrooms.

**How it Works**:

.. code-block:: text

    [ User ]
      🗣️ "Go forward!" / "Stop!" / "Spin around!"
      │
      ▼ (Captured by PC / Laptop Microphone)
    [ Mu Editor on PC - Python 3 Mode ] (Ears & Brain)
      - Listens via PC mic and transcribes speech using built-in SpeechRecognition
      - Sends movement commands over Wi-Fi HTTP:
        requests.get("http://<ESP32_IP>:8080/ai?action=GO")
      ▲
      │  (Wi-Fi Network: Text Command Transmission)
      ▼
    [ ESP32 Robot Car ] (Body, No Mic/OLED Needed!)
      - Executes received action ("GO") commands immediately
      - Steers 2WD motors and indicates status via onboard LED

**Step-by-Step Guide (Mu Editor / Standard Python IDEs)**:

1. **PC Speech Recognition Environment Setup**:
   Prepare the environment to transcribe speech and send commands to the ESP32.

   * **Option A (In Mu Editor)**:
     Mu Editor already has ``SpeechRecognition`` and ``requests`` built-in, so you can **run the script directly without installing anything**.

   * **Option B (External Editors like VS Code)**:
     If running in a generic Python environment, install the packages via CMD or PowerShell:

     .. code-block:: bash

         pip install SpeechRecognition requests PyAudio

2. **Step 1: Upload ESP32 Robot Car Script (Mu [ESP32 Mode] or Thonny / mpremote)**:

   .. literalinclude:: examples/voice_control_car_esp32.py
      :start-at: from espzero import

3. **Step 2: Run the PC Voice Controller (Mu [Python 3 Mode] or Standard Python)**:

   .. literalinclude:: examples/voice_control_car_pc.py
      :start-at: import requests

Wireless Wi-Fi Audio Streaming & Voice Robot Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Streams 16-bit WAV PCM audio captured by the ESP32-S3's I2S microphone in real-time over Wi-Fi (default port ``8081``) to a PC.
On your PC (Python 3 mode), speech recognition libraries like Whisper, Google SpeechRecognition, or Edge Impulse classify voice commands and send action parameters back to the ``/ai?action=...`` endpoint to control robot motions and OLED face expressions.

**How it Works**:

.. code-block:: text

    [ ESP32-S3 Board ] (Ears & Body)
      - Streams live I2S mic audio over Wi-Fi HTTP (WAV stream on port 8081)
      - Receives voice AI commands ('GO' / 'STOP' / 'DANCE') and drives motors & OLED faces
      ▲
      │  (Wi-Fi Network: Real-Time Audio Stream & Control Commands)
      ▼
    [ PC Mu Editor - Python 3 Mode ] (Voice AI Brain)
      - Reads audio chunks from http://<ESP32_IP>:8081/ and transcribes speech
      - Dispatches recognized commands to http://<ESP32_IP>:8081/ai?action=GO

1. **Upload ESP32-S3 Voice AI Robot Code (Mu [ESP32 Mode])**:

   .. literalinclude:: examples/audio_wifi_ai_robot_esp32.py
      :start-at: from espzero import

2. **Run PC Voice Controller (Mu [Python 3 Mode])**:
   Connects to the ESP32 audio stream, transcribes voice commands in real time, and sends robot actions:

   .. literalinclude:: examples/audio_wifi_ai_robot_pc.py
      :start-at: import io

On-Device TinyML Sound Classification (Edge Impulse & MFCC)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For standalone Keyword Spotting (KWS) or acoustic anomaly detection running entirely on the ESP32-S3 without a PC, use ``mic.mfcc()``:

.. note::
    **Edge Impulse & TinyML Audio Development**:
    To train custom keyword spotting or acoustic anomaly detection models in your browser and export them directly to microcontrollers, visit `Edge Impulse Studio <https://www.edgeimpulse.com/>`_ (https://www.edgeimpulse.com/) and the `Edge Impulse Audio Tutorial <https://docs.edgeimpulse.com/docs/tutorials/audio>`_. Pre-trained audio classification models can also be downloaded from `Kaggle Models <https://www.kaggle.com/models?framework=liteRT>`_ and `LiteRT Community <https://huggingface.co/litert-community>`_.

* **MFCC Feature Extraction**: ``mic.mfcc(num_cepstra=13)`` computes 13-dimensional Mel-Frequency Cepstral Coefficients, the standard audio feature representation for TinyML and TensorFlow Lite Micro models.
* **Dataset Collection**: ``mic.save_wav("sample.wav", duration=1.0)`` records microphone samples directly to onboard flash as 16-bit WAV files, ideal for building Edge Impulse training sets.

.. code-block:: python

    from espzero import I2SMic
    from time import sleep

    mic = I2SMic()

    # Extract 13-dimensional MFCC feature vector for TinyML sound models
    features = mic.mfcc(num_cepstra=13)
    print("MFCC features:", features[:5], "... (13 coefficients total)")

    # Record a 1.0-second sound sample to flash
    mic.save_wav("cough_sample.wav", duration=1.0)
    print("WAV audio sample saved to flash!")

Combined Examples
-----------------

Complete mini-projects combining multiple sensors, actuators, and AI capabilities, arranged in order of difficulty from beginner to advanced.

Button-Controlled Light
~~~~~~~~~~~~~~~~~~~~~~~

Toggle an LED each time a button is pressed.

.. code-block:: python

    from espzero import LED, Button

    led = LED(4)
    btn = Button(5)

    btn.when_pressed = led.toggle

    while True:
        pass # Wait for events

Smart Doorlock
~~~~~~~~~~~~~~

Combine the onboard RGB LED, a servo motor (bolt lock), and a buzzer to build an automated smart doorlock that flashes green with a double beep, unlocks the door, and re-locks it automatically.

.. image:: /images/circuit_smart_doorlock.svg
    :alt: ESP32-S3 Smart Doorlock Circuit Diagram
    :align: center

.. literalinclude:: examples/smart_doorlock.py

Potentiometer Gaze Controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Turn a potentiometer dial to steer the OLED robot's eyes left and right in real time, and press the button to show a ``"love"`` expression.

.. literalinclude:: examples/oled_pot_gaze.py
   :start-at: from espzero import

Analog Clock
~~~~~~~~~~~~

Create a continuously-running analog clock second hand rotating 1 revolution every 60 seconds using a stepper motor.

.. literalinclude:: examples/stepper_analog_clock.py

Automatic Blinds
~~~~~~~~~~~~~~~~

Time-based window blind controller driven by a stepper motor.

.. literalinclude:: examples/stepper_automatic_blinds.py

Smart Parking Assist
~~~~~~~~~~~~~~~~~~~~

Measures obstacle distance via an ultrasonic sensor and escalates OLED robot expressions (``happy`` → ``surprised`` → ``angry``), RGB LED color, and buzzer beep tempo as objects get closer.

.. image:: /images/circuit_parking_assist.svg
    :alt: ESP32-S3 Smart Parking Assist Circuit Diagram
    :align: center

.. literalinclude:: examples/smart_parking_assist.py
   :start-at: from espzero import

Clap-Controlled Smart Door
~~~~~~~~~~~~~~~~~~~~~~~~~~

Uses the I2S microphone's ``when_clap`` event to toggle a servo-driven door and update the OLED robot face completely on-device with no Wi-Fi or PC required.

.. literalinclude:: examples/clap_smart_door.py
   :start-at: from espzero import

Autonomous Obstacle-Avoiding Rover
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Combines a front-mounted ultrasonic sensor with a 2WD robot chassis to automatically reverse and turn whenever an obstacle comes within 20 cm.

.. image:: /images/circuit_obstacle_rover.svg
    :alt: ESP32-S3 Autonomous Obstacle-Avoiding Rover Circuit Diagram
    :align: center

.. literalinclude:: examples/obstacle_avoiding_rover.py
   :start-at: from espzero import

Multimodal AI Companion Robot (Vision AI + Voice AI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Streams live camera video (port ``8080``) and I2S microphone audio (port ``8081``) simultaneously from the ESP32-S3 to a PC. The PC runs visual tracking and speech recognition in parallel, driving expressive OLED robot faces (``look_at`` / ``show_face``) and RGB LED feedback wirelessly.

1. **Upload ESP32-S3 Multimodal Robot Code (Mu [ESP32 Mode])**:

   .. literalinclude:: examples/multimodal_companion_robot_esp32.py
      :start-at: from espzero import

2. **Run PC Multimodal AI Controller (Mu [Python 3 Mode])**:

   .. literalinclude:: examples/multimodal_companion_robot_pc.py
      :start-at: import threading
