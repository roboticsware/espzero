Supported Boards
================

``espzero`` supports various ESP32 boards through its board profile system.

Support List
------------

* **esp32_devkit_v1**: Standard ESP32-WROOM-32 development board.
* **esp32_38pin_nodemcu**: Type-C/Micro-USB 38-pin board (GPIO 1 built-in LED).
* **esp32_s3_devkit**: ESP32-S3 based boards (NeoPixel built-in LED).
* **esp32_c3_mini**: ESP32-C3 based mini boards.
* **m5stack_atom**: M5Stack ATOM series.
* **esp8266_lolin_v3**: ESP8266 based NodeMCU boards.

Auto-detection
--------------

In most cases, calling ``espzero.begin()`` without arguments will automatically detect your board type. If detection fails or you want to force a specific board, you can specify the name as follows:

.. code-block:: python

    espzero.begin("esp32_devkit_v1")
