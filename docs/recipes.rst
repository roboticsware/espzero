예제 (Recipes)
==============

이 섹션은 ``espzero``를 사용하여 다양한 센서와 부품을 제어하는 방법을 설명합니다.

보드 초기화
----------

모든 코드의 시작 부분에는 반드시 ``begin()``을 호출해야 합니다.

.. code-block:: python

    import espzero
    espzero.begin()

LED 제어
-------

단순 켜기/끄기
~~~~~~~~~~~~~

.. code-block:: python

    from espzero import LED
    from time import sleep

    led = LED(4) # GPIO 4번에 연결된 LED

    led.on()
    sleep(1)
    led.off()

깜빡이기 (Blink)
~~~~~~~~~~~~~~

``espzero``의 강력한 기능 중 하나는 백그라운드 깜빡임입니다. ``wait=False``(기본값)를 사용하면 LED가 깜빡이는 동안 다른 코드를 계속 실행할 수 있습니다.

.. code-block:: python

    from espzero import LED

    led = LED(4)
    led.blink(on_time=0.5, off_time=0.5, n=10) # 10번 깜빡임

버튼 입력
--------

버튼 누름 감지
~~~~~~~~~~~~~

.. code-block:: python

    from espzero import Button

    button = Button(5) # GPIO 5번에 연결된 버튼

    if button.is_pressed:
        print("버튼이 눌려있습니다!")

이벤트 기반 처리 (Callback)
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from espzero import Button

    button = Button(5)

    def hello():
        print("안녕하세요!")

    button.when_pressed = hello

    # 프로그램이 종료되지 않도록 무한 루프
    while True:
        pass

서보 모터 (Servo)
---------------

.. code-block:: python

    from espzero import Servo

    servo = Servo(18)

    servo.min() # 0도
    servo.mid() # 90도
    servo.max() # 180도
    servo.value = 0.5 # 중간 위치

WiFi 연결
--------

.. code-block:: python

    from espzero import WiFi

    wifi = WiFi()
    wifi.connect("SSID_NAME", "PASSWORD")

    if wifi.is_connected:
        print("IP 주소:", wifi.ip)
