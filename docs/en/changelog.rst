Change log
==========

.. currentmodule:: espzero

0.1.0 - 2026-11-23
------------------
+ Introduced ``I2SSpeaker`` class (``audio.py``) for driving hardware I2S amplifiers and speakers (e.g. MAX98357A):
  - Hardware ``I2S(1)`` TX playback for 16-bit PCM bytes and 8~48kHz WAV files (with automatic 44-byte WAV header parsing & skipping)
  - Camera-safe and microphone-safe pin auto-mapping on ESP32-S3 WROOM CAM (``BCLK=38, LRC=39, DIN=40``) coexisting with OV2640 camera and ``I2SMic`` (I2S 0 RX)
+ Added high-resolution zero-crossing SVG circuit wiring diagram for MAX98357A I2S amplifier and 3W speaker (``circuit_i2s_speaker.svg``)
+ Reorganized I2S digital speaker recipe under the **Buzzer & Speaker** section across all 3 documentation languages (ko, en, uz)
+ Integrated and stabilized camera snapshot APIs (``vision.capture()``, ``vision.save_photo()``) and I2S audio features

0.0.10 - 2026-11-23
-------------------
+ Added ``vision.capture()``, ``vision.save_photo()``, and ``vision.close()`` snapshot helpers with camera streamer reuse
+ Added standalone **Camera** main section to recipes (photo capture/saving, time-lapse & dataset collection) and ``espzero.vision`` functions to API reference
+ Added ``InternalTouchSensor`` alias for ``CapTouch`` and clarified distinction from external ``TouchSensor`` module
+ Reorganized recipe sections: moved built-in touch and internal temperature sensors under **Input Devices**, promoted **Servo Motor** to its own main section, and renamed Motor & Robot to **DC Motor & Robot**
+ Fixed RTD multilingual ``literalinclude`` paths (``examples/...``) and unified shared PC voice examples to English (``en-US``)

0.0.9 - 2026-11-20
------------------
+ Introduced ``audio.py`` (``I2SMic``) supporting INMP441 I2S microphones and DSP signal analysis (FFT spectrum, MFCC acoustic feature extraction)
+ Added real-time Wi-Fi audio streaming server (``audio.start_wifi_stream``) and AI inference feedback interface (``audio.get_ai_result``)
+ Added 5 new high-resolution SVG circuit wiring diagrams:
  - INMP441 I2S digital microphone module (``circuit_inmp441_mic.svg``)
  - 28BYJ-48 5-wire stepper motor & ULN2003 driver (``circuit_stepper.svg``)
  - Smart security doorlock with servo, RGB LED, and buzzer (``circuit_smart_doorlock.svg``)
  - Ultrasonic parking assist system with dynamic beep rate (``circuit_parking_assist.svg``)
  - Autonomous obstacle-avoiding rover with panning ultrasonic sensor (``circuit_obstacle_rover.svg``)
+ Reorganized Recipes with a comprehensive **Combined Examples** section:
  - Structured 8-tier step-by-step projects (LED button toggle, smart doorlock, potentiometer gaze, analog clock, automatic blinds, parking assist, clap door, obstacle rover, multimodal companion robot)
  - Streamlined and minimalized source code with essential logic highlighted for beginners
  - Paired architecture for all Wi-Fi AI projects with dedicated ESP32 firmware (``_esp32.py``) and PC inference (``_pc.py``) scripts
+ Reorganized sensor navigation structure:
  - Simplified ``Temperature Sensor`` into a standalone main section placed immediately after ``Input Devices``
  - Relocated ``Distance Sensor`` right after ``Temperature Sensor`` for cohesive sensor exploration
  - Placed ``Microphone`` section right after ``Buzzer & Speaker`` for seamless audio I/O workflow
+ Enhanced Mock I2S HAL for desktop emulation and CI testing

0.0.8 - 2026-11-20
------------------
+ Introduced ``OLED`` class supporting SSD1306 and SH1106 I2C displays
+ Added expressive robot facial animations (``show_face`` with 10 emotion presets) and gaze tracking (``look_at``)
+ Designed vector SVG diagram (``oled_robot_faces.svg``) illustrating 8 OLED robot expressions
+ Added **AI Voice** section with PC-microphone voice-controlled smart car recipes
+ Enhanced firmware flashing guide covering Mu Editor's online cloud flasher ([ESP Online Flasher]) and offline flasher
+ Clarified environment setup distinguishing Mu Editor built-in packages from standard Python environments (VS Code, Thonny, mpremote)
+ Updated Ultrasonic (HC-SR04P) and LCD (PCF8574 with level shifter) circuit diagrams for safe 3.3V operation
+ Redesigned circuit wiring diagrams for ESP32-S3 WROOM CAM (N16R8) with camera-safe pins
+ Added PyPI and ReadTheDocs badges and version tracking to documentation index
+ Added ``changelog.rst`` across English, Korean, and Uzbek documentation

0.0.7 - 2026-11-17
------------------
+ Added YOLO installation guide and WiFi YOLO autonomous car recipes
+ Enhanced ``vision.py`` module with non-blocking stream and WiFi support
+ Added standalone ``main.py`` battery operation and outdoor AP hotspot guidance
+ Full Korean and Uzbek documentation updates

0.0.6 - 2026-11-16
------------------
+ Introduced camera vision module and supporting rst documentation
+ Added official ESP32-S3 WROOM CAM pin aliases and board metadata
+ Improved NeoPixelLED with color setter and clear pin validation for ESP32-S3
+ Added Sphinx multilingual documentation configuration (en, ko, uz)

0.0.5 - 2026-11-15
------------------
+ Added CapTouch capacitive touch sensor documentation
+ Fixed internal temperature sensor (``esp_temp_sensor`` / ``mcu_temperature``) for ESP32-S3 and ESP32-C3
+ ReadTheDocs configuration setup and link improvements

0.0.3 - 2026-11-14
------------------
+ Ported ``Stepper`` motor and ``I2cLcd`` / ``GpioLcd`` display controllers
+ Updated ``DistanceSensor`` unit to centimetres (cm)
+ Added ESP32 38-pin NodeMCU profile and restricted pins safety net

0.0.2 - 2026-11-13
------------------
+ Added built-in LED alias ``esp_led`` and custom software scheduler
+ Added NodeMCU V3 Lolin (ESP8266) board profile support
+ MicroPython compatibility and package import fixes

0.0.1 - 2026-11-12
------------------
+ Initial release of espzero library for ESP32 and ESP8266 physical computing
