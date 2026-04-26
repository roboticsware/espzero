espzero
=======

**espzero**는 Raspberry Pi Pico용 `picozero` 라이브러리를 ESP32 및 ESP8266 환경에서도 동일하게 사용할 수 있도록 이식한 라이브러리입니다. 초보자도 쉽고 직관적으로 하드웨어를 제어할 수 있도록 설계되었습니다.

.. image:: https://img.shields.io/github/license/roboticsware/espzero
   :target: https://github.com/roboticsware/espzero/blob/main/LICENSE
   :alt: License

특징
----

* **직관적인 API**: `LED.on()`, `Button.when_pressed` 등 사람이 이해하기 쉬운 함수명을 사용합니다.
* **보드 프로필 시스템**: ESP32의 수많은 변종 보드들을 자동으로 감지하고 핀 맵을 맞춰줍니다.
* **비동기 지원**: 복잡한 타이머 설정 없이도 여러 개의 LED를 동시에 다른 주기로 깜빡일 수 있습니다.

빠른 시작
--------

라이브러리를 설치한 후, 가장 먼저 ``begin()`` 함수를 호출하여 보드를 초기화해야 합니다.

.. code-block:: python

    import espzero
    from time import sleep

    # 보드 자동 감지 및 초기화
    espzero.begin()

    # 내장 LED 깜빡이기
    while True:
        espzero.esp_led.on()
        sleep(1)
        espzero.esp_led.off()
        sleep(1)

목차
----

.. toctree::
   :maxcode-depth: 2

   recipes
   api
   boards

.. note::
   이 프로젝트는 오픈 소스이며 `GitHub <https://github.com/roboticsware/espzero>`_에서 소스 코드를 확인하실 수 있습니다.
