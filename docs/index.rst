espzero: ESP32를 위한 가장 쉬운 코딩 라이브러리
==========================================

.. image:: /images/logo.png
   :width: 200px
   :align: center
   :alt: espzero logo

**espzero**는 ESP32 및 ESP8266 마이크로컨트롤러를 위한 초보자 친화적인 하드웨어 제어 라이브러리입니다. Raspberry Pi Pico의 인기 라이브러리인 ``picozero``의 사용법을 그대로 ESP32 환경에서 사용할 수 있게 해줍니다.

.. tip::
   🌐 **English Version**: You can find the English version of this documentation in the `docs/en/` directory.
   🌐 **O'zbekcha versiya**: Ushbu hujjatning o'zbekcha versiyasini `docs/uz/` katalogida topishingiz mumkin.

핵심 철학
--------

* **단순함**: 복잡한 레지스터 설정이나 PWM 주파수 계산 없이, ``LED.on()`` 한 줄로 시작하세요.
* **추상화**: 어떤 보드를 쓰더라도 코드는 동일하게 유지됩니다. 보드별 차이는 ``espzero.begin()``이 처리합니다.
* **현대적**: 비동기 스케줄러를 내장하여 백그라운드 작업을 손쉽게 처리합니다.

주요 기능
--------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - 구성 요소
     - 지원 기능
   * - **출력 장치**
     - LED, PWM LED, RGB LED, Buzzer, Speaker (Melody), Motor
   * - **입력 장치**
     - Button, Switch, Motion Sensor, Touch, Potentiometer
   * - **센서**
     - Distance (HC-SR04), Temperature (Internal/External)
   * - **무선 통신**
     - WiFi 간편 연결 및 상태 관리

시작하기
-------

1. **설치**: 
   
   보드에 직접 설치하려면 ``mpremote``를 추천합니다:
   
   .. code-block:: bash
   
       mpremote mip install espzero

   또는 PC 개발 환경에서 자동 완성을 위해 ``pip``로 설치할 수 있습니다:
   
   .. code-block:: bash
   
       pip install espzero

2. **초기화**: 스크립트 상단에서 ``espzero.begin()``을 호출합니다.

.. code-block:: python

    import espzero
    from espzero import LED
    
    espzero.begin()
    led = LED(4)
    led.pulse() # 부드럽게 깜빡이기

목차
----

.. toctree::
   :maxdepth: 2
   :caption: 가이드 및 레시피

   recipes
   boards
   api

.. toctree::
   :maxdepth: 1
   :caption: 프로젝트 정보

   contributing
   license

도움이 필요하신가요?
------------------

* **GitHub 저장소**: `Issues <https://github.com/roboticsware/espzero/issues>`_ 탭에 질문을 남겨주세요.
* **커뮤니티**: 관련 포럼이나 블로그를 통해 다양한 활용 사례를 공유하고 있습니다.
