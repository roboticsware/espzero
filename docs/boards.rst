지원 보드 (Supported Boards)
============================

``espzero``는 보드 프로필 시스템을 통해 다양한 ESP32 보드를 지원합니다.

지원 목록
--------

* **esp32_devkit_v1**: 표준 ESP32-WROOM-32 개발 보드.
* **esp32_38pin_nodemcu**: Type-C/Micro-USB 38핀 보드 (GPIO 1 내장 LED).
* **esp32_s3_devkit**: ESP32-S3 기반 보드 (NeoPixel 내장 LED).
* **esp32_c3_mini**: ESP32-C3 기반 미니 보드.
* **m5stack_atom**: M5Stack ATOM 시리즈.
* **esp8266_lolin_v3**: ESP8266 기반 NodeMCU 보드.

자동 감지
--------

대부분의 경우 ``espzero.begin()``을 인자 없이 호출하면 보드 종류를 자동으로 감지합니다. 만약 감지에 실패하거나 특정 보드를 강제하고 싶다면 다음과 같이 이름을 명시할 수 있습니다.

.. code-block:: python

    espzero.begin("esp32_devkit_v1")
