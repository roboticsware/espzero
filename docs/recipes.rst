예제 (Recipes)
==============

이 섹션은 ``espzero`` 를 사용하여 다양한 센서와 부품을 제어하는 실전 예제를 다룹니다.
``espzero`` 는 첫 사용 시 보드를 자동으로 감지하므로 ``begin()`` 호출 없이 곧바로 사용할 수 있습니다. (라즈베리파이 피코용 ``picozero-rw`` 라이브러리와 100% 동일한 사용 경험을 제공합니다.)

보드 핀맵 확인 (Pinout)
--------------------

ESP32 보드의 핀맵과 기능을 터미널에 아스키 다이어그램으로 출력합니다. (``picozero-rw`` 호환)

.. code-block:: python

    from espzero import pinout

    pinout() # ESP32 표준 핀아웃 다이어그램 출력

내장 LED (Built-in LED)
---------------------

보드에 내장된 LED를 제어하는 가장 간단한 방법입니다. ``pico_led`` 별칭도 완벽히 지원됩니다.

.. code-block:: python

    from espzero import esp_led, pico_led
    from time import sleep

    esp_led.on()  # 켜기
    sleep(1)
    esp_led.off() # 끄기
    esp_led.blink() # 백그라운드에서 깜빡이기

    # picozero-rw 호환 코드로도 동일하게 작동합니다:
    pico_led.on()

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

외장 4핀 RGB LED (External RGB LED)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

빨강, 초록, 파랑 핀을 각각 연결하여 다양한 색상을 만듭니다.
(ESP32-S3 등 일부 칩셋은 22~34번 핀이 없으므로, 모든 보드에서 공통으로 지원하는 GPIO 4, 5, 6번 등을 사용합니다.)

.. code-block:: python

    from espzero import RGBLED

    # ESP32 및 ESP32-S3 공통 지원 핀 (예: GPIO 4, 5, 6)
    rgb = RGBLED(red=4, green=5, blue=6)

    rgb.color = (255, 0, 0)   # 빨간색
    rgb.color = (0, 255, 0)   # 초록색
    rgb.color = (255, 255, 0) # 노란색 (빨강+초록)
    rgb.off()

온보드 내장 RGB LED (ESP32-S3 WS2812 NeoPixel)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ESP32-S3 또는 M5Stack 등 보드 자체에 WS2812 NeoPixel RGB LED가 내장된 경우, 핀 번호 지정 없이 ``esp_led`` 로 간편하게 제어합니다.

.. code-block:: python

    from espzero import esp_led

    esp_led.color = (255, 0, 0)   # 빨간색
    esp_led.color = (0, 255, 0)   # 초록색
    esp_led.color = (0, 0, 255)   # 파란색
    esp_led.off()

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

    print("정규화 값 (0.0 - 1.0):", pot.value)
    print("원시 16비트 ADC 값 (0 - 65535):", pot.raw_value)
    print("전압 (V):", pot.voltage)

서보 모터 (Servo)
~~~~~~~~~~~~~~~

서보 모터를 0~1 비율 또는 각도(0~180도)로 제어합니다. (``picozero-rw`` 호환)

.. code-block:: python

    from espzero import Servo
    from time import sleep

    servo = Servo(13)

    # 기본 위치 제어 (0.0: 최소, 0.5: 중간, 1.0: 최대)
    servo.mid()
    sleep(1)

    # 각도 단위 직접 제어 (picozero-rw의 move_to_degree API)
    servo.move_to_degree(90)   # 90도 (중앙)
    sleep(1)
    servo.move_to_degree(180)  # 180도 (최대)
    sleep(1)
    servo.move_to_degree(0)    # 0도 (최소)

내장 터치 센서 (Capacitive Touch)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ESP32 및 ESP32-S3 칩에 내장된 정전용량식 터치 센서를 사용합니다. 외부 저항이나 회로 없이 핀에 손가락을 대는 것만으로 터치를 감지합니다.

.. code-block:: python

    from espzero import CapTouch
    from time import sleep

    # WROOM은 T0~T9 (예: GPIO 4), S3은 터치 지원 핀 (예: GPIO 1)
    touch = CapTouch(1)

    while True:
        # value: 원시 측정값 (손을 대면 값이 감소함)
        # is_touched: threshold(기본값 300)보다 작으면 True
        print("Raw:", touch.value, "터치됨:", touch.is_touched)
        sleep(0.2)

초음파 거리 센서 (Distance Sensor)
-------------------------------

HC-SR04 등의 초음파 센서를 사용하여 거리를 측정합니다.

.. code-block:: python

    from espzero import DistanceSensor

    # echo=14, trigger=13
    ds = DistanceSensor(echo=14, trigger=13)

    while True:
        print("거리: ", ds.distance, "cm")
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

스텝 모터 (Stepper Motor)
------------------------

드라이버 보드(예: ULN2003)를 통해 연결된 스텝 모터를 제어합니다.

아날로그 시계 (Analog clock)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

연속으로 회전하는 아날로그 시계의 초침을 만듭니다:

.. literalinclude:: examples/stepper_analog_clock.py

자동 블라인드 (Automatic blinds)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

시간 기반 블라인드 컨트롤러:

.. literalinclude:: examples/stepper_automatic_blinds.py

LCD 디스플레이 (LCD Display)
--------------------------

I2C 버스와 PCF8574 I2C 어댑터를 사용하여 LiquidCrystal 디스플레이(LCD)에 문자를 출력합니다.

.. literalinclude:: examples/i2c_lcd.py

GPIO 핀만 사용하여 LiquidCrystal 디스플레이(LCD)에 문자를 출력합니다.

.. literalinclude:: examples/lcd.py


AI 비전 (AI Vision)
-----------------

ESP32-S3 AI 비전 카메라와 에디터 연동 및 단독 실행 AI 예제입니다.

PC 연동 AI (MediaPipe 연동)
~~~~~~~~~~~~~~~~~~~~~~~~~

ESP32 카메라 영상을 PC(에디터)로 전송하고, PC의 MediaPipe 라이브러리를 사용해 손가락 관절 등을 실시간으로 분석합니다. 분석된 좌표는 다시 ESP32에 전송되어 제어에 사용됩니다.

.. code-block:: python

    from espzero import vision
    from time import sleep

    # PC로 실시간 카메라 영상 전송 시작
    vision.start_stream_to_pc()

    while True:
        # 에디터가 분석하여 주입해 준 손가락 좌표 읽기
        if "__pc_ai_data" in globals():
            x = __pc_ai_data.get("hand_x", 0)
            y = __pc_ai_data.get("hand_y", 0)
            print("손가락 위치 -> X:", x, "Y:", y)
        sleep(0.1)

기기 단독 AI (On-Device TFLite)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ESP32 내부에 다운로드한 `.tflite` 모델 파일을 읽어와 직접 AI 추론을 수행합니다. PC와 연결되지 않은 상태에서도 동작할 수 있습니다.

.. note::
    사용 가능한 샘플 `.tflite` 모델 파일들은 구글의 텐서플로우 라이트 공식 모델 저장소(https://www.tensorflow.org/lite/guide/hosted_models)에서 직접 내려받을 수 있습니다.

.. code-block:: python

    import camera
    import tflite
    from time import sleep

    # 카메라 초기화 및 TFLite 모델 로드
    camera.init(framesize=camera.FRAME_QVGA)
    model = tflite.load("model.tflite")

    while True:
        img = camera.capture()
        if img:
            # 이미지 분석 및 클래스 결과 추출
            result = model.detect(img)
            print("인식된 클래스 ID:", result.class_id)
        sleep(0.5)

