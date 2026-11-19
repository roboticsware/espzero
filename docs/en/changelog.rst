Change log
==========

.. currentmodule:: espzero

0.0.8 - unreleased
------------------
+ Introduced ``OLED`` class supporting SSD1306 and SH1106 I2C displays
+ Updated Ultrasonic (HC-SR04P) and LCD (PCF8574 with level shifter) circuit diagrams for safe 3.3V operation
+ Redesigned circuit wiring diagrams for Freenove ESP32-S3 WROOM CAM (N16R8) with camera-safe pins
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
+ Added official Freenove ESP32-S3 WROOM CAM pin aliases and board metadata
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
