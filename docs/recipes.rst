예제 (Recipes)
==============

이 섹션은 ``espzero``를 사용하여 다양한 센서와 부품을 제어하는 실전 예제를 다룹니다. 모든 예제는 ``import espzero; espzero.begin()``이 호출되었다고 가정합니다.

내장 LED (Built-in LED)
---------------------

보드에 내장된 LED를 제어하는 가장 간단한 방법입니다.

.. code-block:: python

    from espzero import esp_led
    from time import sleep

    esp_led.on()  # 켜기
    sleep(1)
    esp_led.off() # 끄기
    esp_led.blink() # 백그라운드에서 깜빡이기

디지털 출력 (LED)
---------------

일반 LED를 특정 핀에 연결하여 제어합니다.

.. code-block:: python

    from espzero import LED

    led = LED(4) # GPIO 4번

    led.on()
    led.off()
    led.toggle()
    
    # 0.5초 켜지고 0.5초 꺼지기를 5번 반복 (비동기)
    led.blink(on_time=0.5, off_time=0.5, n=5)

PWM 제어 (밝기 조절)
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    led.value = 0.5 # 50% 밝기
    led.pulse()     # 서서히 밝아졌다 어두워졌다 반복

RGB LED
-------

빨강, 초록, 파랑 핀을 각각 연결하여 다양한 색상을 만듭니다.

.. code-block:: python

    from espzero import RGBLED

    rgb = RGBLED(red=25, green=26, blue=27)

    rgb.color = (255, 0, 0)   # 빨간색
    rgb.color = (0, 255, 0)   # 초록색
    rgb.color = (255, 255, 0) # 노란색 (빨강+초록)
    rgb.off()

부저 및 스피커 (Buzzer & Speaker)
-------------------------------

단순 경고음 (Beep)
~~~~~~~~~~~~~~~~

.. code-block:: python

    from espzero import Buzzer

    bz = Buzzer(15)
    bz.beep(on_time=0.1, off_time=0.1, n=3) # "삑-삑-삑"

멜로디 연주 (Play)
~~~~~~~~~~~~~~~~

.. code-block:: python

    from espzero import Speaker

    spk = Speaker(15)

    # (음계, 박자) 튜플의 리스트
    tune = [
        ('c4', 0.5), ('d4', 0.5), ('e4', 0.5), ('c4', 0.5),
        ('e4', 0.5), ('c4', 0.5), ('g4', 1.0)
    ]
    spk.play(tune)

입력 장치 (Input Devices)
-----------------------

버튼 (Button)
~~~~~~~~~~~~

.. code-block:: python

    from espzero import Button

    btn = Button(5)

    btn.when_pressed = lambda: print("눌림!")
    btn.when_released = lambda: print("떨어짐!")

가변저항 (Potentiometer)
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from espzero import Pot

    pot = Pot(34) # 아날로그 핀 (ADC)

    print("현재 값 (0-1):", pot.value)
    print("전압 (V):", pot.voltage)

초음파 거리 센서 (Distance Sensor)
-------------------------------

HC-SR04 등의 초음파 센서를 사용하여 거리를 측정합니다.

.. code-block:: python

    from espzero import DistanceSensor

    # echo=14, trigger=13
    ds = DistanceSensor(echo=14, trigger=13)

    while True:
        print("거리: ", ds.distance, "m")
        sleep(0.5)

온도 센서 (Temperature Sensor)
----------------------------

내장 온도 센서
~~~~~~~~~~~~

ESP32 칩 내부의 온도를 측정합니다. (주의: 외부 기온과는 차이가 있을 수 있습니다.)

.. code-block:: python

    from espzero import esp_temp_sensor

    print("칩 내부 온도:", esp_temp_sensor.temp, "C")

복합 예제: 버튼으로 조명 제어
--------------------------

버튼을 누를 때마다 LED가 토글되는 예제입니다.

.. code-block:: python

    from espzero import LED, Button, begin

    begin()
    led = LED(4)
    btn = Button(5)

    btn.when_pressed = led.toggle

    while True:
        pass # 이벤트 대기
