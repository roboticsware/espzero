예제 (Recipes)
==============

이 섹션은 ``espzero``\ 를 사용하여 다양한 센서와 부품을 제어하는 실전 예제를 다룹니다.
``espzero``\ 는 첫 사용 시 보드를 자동으로 감지하므로 ``begin()`` 호출 없이 곧바로 사용할 수 있습니다. (라즈베리파이 피코용 ``picozero-rw`` 라이브러리와 100% 동일한 사용 경험을 제공합니다.)

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

.. image:: /images/circuit_led.svg
    :alt: ESP32 LED 회로 연결도
    :align: center

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

.. image:: /images/circuit_rgb.svg
    :alt: ESP32 RGB LED 회로 연결도
    :align: center

.. code-block:: python

    from espzero import RGBLED
    from time import sleep

    # ESP32 및 ESP32-S3 공통 지원 핀 (예: GPIO 4, 5, 6)
    rgb = RGBLED(red=4, green=5, blue=6)

    rgb.color = (255, 0, 0)   # 빨간색
    sleep(0.5)
    rgb.color = (0, 255, 0)   # 초록색
    sleep(0.5)
    rgb.color = (255, 255, 0) # 노란색 (빨강+초록)
    sleep(0.5)

    # 색상 이름 문자열로 간편하게 지정 (red, green, blue, yellow, cyan, magenta, purple, white, black, orange)
    rgb.color = "cyan"
    sleep(0.5)
    rgb.color = "orange"
    sleep(0.5)

    # 개별 채널 강도 조절 (0~255)
    rgb.red = 128
    rgb.blue = 255

    # 색상 반전 및 토글
    rgb.invert()
    rgb.toggle()

    # 다채로운 자동 애니메이션 (점멸, 페이드, 무지개 순환 — 색상 이름 문자열도 사용 가능)
    rgb.blink(on_times=0.5, colors=("red", "cyan", "orange"), n=2, wait=True)
    rgb.pulse(fade_times=1, n=2, wait=True)  # 부드럽게 페이드
    rgb.cycle(fade_times=1, n=2, wait=True)  # 무지개 색상 순환

    rgb.off()

온보드 내장 RGB LED (ESP32-S3 WS2812 NeoPixel)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ESP32-S3 또는 M5Stack 등 보드 자체에 WS2812 NeoPixel RGB LED가 내장된 경우, 핀 번호 지정 없이 ``esp_led``\ 로 간편하게 제어합니다.

.. code-block:: python

    from espzero import esp_led
    from time import sleep

    esp_led.color = (255, 0, 0)   # 빨간색
    sleep(0.5)
    esp_led.color = (0, 255, 0)   # 초록색
    sleep(0.5)
    esp_led.color = (0, 0, 255)   # 파란색
    sleep(0.5)

    # 내장 네오픽셀 무지개 순환 효과
    esp_led.cycle(fade_times=0.5, n=3, wait=True)
    esp_led.off()

부저 및 스피커 (Buzzer & Speaker)
-------------------------------

단순 경고음 (Beep)
~~~~~~~~~~~~~~~~

.. image:: /images/circuit_buzzer.svg
    :alt: ESP32 부저 회로 연결도
    :align: center

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

I2S 디지털 스피커 (I2SSpeaker)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``I2SSpeaker``\ 는 ``MAX98357A`` 같은 3.3V/5V I2S 앰프 모듈을 하드웨어 ``I2S(1)`` (TX)로 구동하여 WAV/PCM 음성이나 효과음을 고음질로 출력합니다. ``I2SMic`` (``I2S(0)``) 및 OV2640 카메라와 핀이나 버스가 겹치지 않도록 ESP32-S3에서는 기본 핀(``BCLK=38, LRC=39, DIN=40``)이 자동 매핑됩니다.

.. image:: /images/circuit_i2s_speaker.svg
    :alt: ESP32-S3 I2S 디지털 스피커(MAX98357A) 회로 연결도
    :align: center

.. code-block:: python

    from espzero import I2SSpeaker

    # ESP32-S3 기본 핀: BCLK=38, LRC=39, DIN=40 (I2S 1 TX)
    spk = I2SSpeaker(sample_rate=24000)

    # WAV 파일 또는 16-bit PCM 바이트 재생 (44B 헤더 자동 스킵)
    spk.play_wav("hello.wav")
    spk.close()

마이크 (I2S Microphone)
-----------------------

ESP32-S3의 빠른 연산 속도와 I2S 하드웨어 인터페이스를 사용하여 고성능 24-bit 디지털 MEMS 마이크(INMP441 등)로부터 오디오 신호를 직접 수음하고 실시간으로 분석합니다.

I2S 마이크 연결 (INMP441, 3.3V)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``INMP441``\ 은 3.3V 전원과 디지털 I2S 버스(SCK, WS, SD)를 지원하여 아날로그 마이크에 비해 노이즈가 매우 적고 선명한 음질을 제공합니다.
ESP32-S3 WROOM CAM 보드의 기본 핀(``SCK=41``, ``WS=42``, ``SD=2``)에 별도의 레벨 시프터 없이 3.3V 신호로 안전하게 직결할 수 있습니다.
(단일 모노 마이크로 사용할 경우 ``L/R`` 핀을 ``GND``\ 에 연결하여 좌측 채널로 설정합니다.)

.. image:: /images/circuit_inmp441_mic.svg
    :alt: ESP32-S3 I2S 디지털 마이크(INMP441) 회로 연결도
    :align: center

기본 사용 및 소리 감지 (I2SMic)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

보드 프로파일의 기본 핀을 자동으로 할당받아 인스턴스를 생성하며, 현재 소리 크기(``level``, ``0.0 ~ 1.0``), 데시벨(``decibels``), 기본 주파수 음계(``note``) 및 박수 이벤트(``when_clap``)를 직관적으로 다룹니다.

.. code-block:: python

    from espzero import I2SMic, esp_led
    from time import sleep

    # 기본 I2S 핀 자동 매핑 (ESP32-S3: SCK=41, WS=42, SD=2)
    mic = I2SMic()

    # 박수 또는 큰 소리가 감지될 때마다 내장 LED 토글
    mic.when_clap = esp_led.toggle

    while True:
        print("소리 크기:", round(mic.level, 3), "| dB:", int(mic.decibels), "| 음계:", mic.note or "---")
        sleep(0.2)

실시간 OLED 오디오 스펙트럼 분석기 (FFT Spectrum)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``mic.spectrum(bins=16)``\ 으로 추출한 16밴드 주파수 에너지를 OLED 화면에 실시간 막대 그래프(``oled.show_spectrum()``)로 렌더링하고, 강한 비트에 맞춰 RGB LED를 제어합니다.

.. literalinclude:: examples/audio_spectrum_oled.py
      :start-at: from espzero import

입력 장치 (Input Devices)
-----------------------

버튼 (Button)
~~~~~~~~~~~~

.. image:: /images/circuit_button.svg
    :alt: ESP32 버튼 회로 연결도
    :align: center

.. code-block:: python

    from espzero import Button

    btn = Button(5)

    btn.when_pressed = lambda: print("눌림!")
    btn.when_released = lambda: print("떨어짐!")

가변저항 (Potentiometer)
~~~~~~~~~~~~~~~~~~~~~

.. image:: /images/circuit_potentiometer.svg
    :alt: ESP32 가변저항 회로 연결도
    :align: center

.. code-block:: python

    from espzero import Pot

    pot = Pot(1) # 아날로그 핀 (ADC1_CH0, ESP32-S3)

    print("정규화 값 (0.0 - 1.0):", pot.value)
    print("원시 16비트 ADC 값 (0 - 65535):", pot.raw_value)
    print("전압 (V):", pot.voltage)

내장 터치 센서 (Capacitive Touch)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ESP32 및 ESP32-S3 칩에 내장된 정전용량식 터치 센서를 사용합니다. 외부 저항이나 회로 없이 핀에 손가락을 대는 것만으로 터치를 감지합니다. (``InternalTouchSensor`` 별칭도 동일하게 사용할 수 있습니다.)

.. note::
    **외부 터치 모듈(``TouchSensor``)과의 차이**:
    TTP223 같은 외부 디지털 터치 센서 모듈을 연결할 때는 ``picozero-rw``와 호환되는 ``TouchSensor(pin)`` 클래스를 사용하세요. ``CapTouch`` (``InternalTouchSensor``)는 외부 모듈 없이 ESP32 칩 자체의 터치 핀을 직접 읽는 내장 기능 전용 클래스입니다.

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

내장 온도 센서 (Internal Temperature Sensor)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ESP32 칩 내부의 온도를 측정합니다. (주의: 외부 기온과는 차이가 있을 수 있습니다.)

.. code-block:: python

    from espzero import esp_temp_sensor

    print("칩 내부 온도:", esp_temp_sensor.temp, "C")

초음파 거리 센서 (Distance Sensor)
-------------------------------

``HC-SR04P`` (3.3V~5V 겸용 신형 모델) 등의 초음파 센서를 사용하여 거리를 측정합니다.

.. image:: /images/circuit_distance.svg
    :alt: ESP32-S3 HC-SR04P 초음파 센서 회로 연결도
    :align: center

.. warning::
    **구형 5V 전용 HC-SR04 사용 시 주의 (ECHO 핀 과전압 위험)**:
    ESP32-S3 GPIO의 최대 허용 입력 전압은 **3.6V** 입니다. ``HC-SR04P`` (또는 ``HC-SR04+``) 신형 모델은 보드의 **3V3** 핀에 연결하면 3.3V 신호로 안전하게 직결됩니다.
    만약 5V 전원이 필수인 **구형 HC-SR04** 센서를 사용하려면, ``ECHO`` 출력(5V)이 ``G14`` 핀을 손상시키지 않도록 **1kΩ + 2kΩ 저항 전압 분배 회로** (``ECHO → 1kΩ → G14``, ``G14 → 2kΩ → GND``)를 반드시 구성해 3.3V로 강압하여 연결하세요.

.. code-block:: python

    from espzero import DistanceSensor

    # echo=14, trigger=13
    ds = DistanceSensor(echo=14, trigger=13)

    while True:
        print("거리: ", ds.distance, "cm")
        sleep(0.5)

DC 모터 및 로봇 (DC Motor & Robot)
---------------------------------

DC 모터 (Motor)
~~~~~~~~~~~~~~

모터 드라이버(예: L298N, L9110S, DRV8833 등)를 통해 양방향 회전이 가능한 DC 모터를 제어합니다.

.. image:: /images/circuit_motor.svg
    :alt: ESP32 DC 모터 드라이버 회로 연결도
    :align: center

.. code-block:: python

    from espzero import Motor
    from time import sleep

    # forward 핀, backward 핀 지정 (PWM 속도 제어 지원)
    motor = Motor(forward=4, backward=5)

    # 최고 속도 전진 회전
    motor.forward()
    sleep(1)

    # 50% 속도로 후진 회전
    motor.backward(0.5)
    sleep(1)

    # 시간 지정 회전 (1초간 정회전 후 자동 정지)
    motor.forward(speed=0.8, t=1, wait=True)

    # 모터 정지
    motor.stop()

로봇 로버 (Robot Rover / 2륜 구동 플랫폼)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

좌/우 2개의 모터를 제어하여 전진, 후진, 좌회전, 우회전하는 로봇 플랫폼을 편리하게 구동합니다.

.. image:: /images/circuit_robot.svg
    :alt: ESP32 2륜 로봇 로버 회로 연결도
    :align: center

.. code-block:: python

    from espzero import Robot
    from time import sleep

    # left=(전진핀, 후진핀), right=(전진핀, 후진핀) — 카메라와 충돌하지 않는 안전 핀 사용
    robot = Robot(left=(41, 42), right=(47, 21))

    # 기본 전진 / 후진
    robot.forward()
    sleep(1)
    robot.backward(0.6)
    sleep(1)

    # 좌회전 및 우회전
    robot.left(speed=0.8)
    sleep(0.5)
    robot.right(speed=0.8)
    sleep(0.5)

    # 시간 지정 주행 (1초 전진 -> 0.5초 좌회전 사각 주행)
    for _ in range(4):
        robot.forward(t=1, wait=True)
        robot.left(t=0.5, wait=True)

    # 로봇 정지
    robot.stop()

서보 모터 (Servo)
----------------

서보 모터를 0~1 비율 또는 각도(0~180도)로 제어합니다. (``picozero-rw`` 호환)

.. image:: /images/circuit_servo.svg
    :alt: ESP32 서보 모터 회로 연결도
    :align: center

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

    # 부드러운 왕복 스위핑 (0도 <-> 180도 연속 왕복)
    servo.pulse(fade_in_time=1, fade_out_time=1)

스텝 모터 (Stepper Motor)
-------------------------

ULN2003 드라이버 보드와 28BYJ-48 스텝 모터를 연결하여 원하는 각도나 회전수만큼 정밀하게 제어합니다.

.. image:: /images/circuit_stepper.svg
    :alt: ESP32-S3 ULN2003 28BYJ-48 스텝 모터 회로 연결도
    :align: center

.. code-block:: python

    from espzero import Stepper
    from time import sleep

    # 카메라 안전 핀 4개 연결 (IN1=42, IN2=41, IN3=47, IN4=21)
    stepper = Stepper((42, 41, 47, 21))
    stepper.set_speed(10)          # 10 RPM 속도 설정

    stepper.turn(90, "cw")         # 시계 방향으로 90도 회전
    sleep(0.5)
    stepper.rotate(1, "ccw")       # 반시계 방향으로 1바퀴(360도) 회전
    stepper.off()                  # 코일 전원 차단 (발열 방지)

디스플레이 (OLED & LCD Display)
-------------------------------

I2C OLED 디스플레이 (SSD1306 / SH1106, 3.3V 권장)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

0.96인치(``SSD1306``) 또는 1.3인치(``SH1106``) I2C OLED 디스플레이는 3.3V 전원과 I2C 신호를 기본 지원하므로 별도의 레벨 시프터 없이 ESP32-S3에 안전하게 직결할 수 있습니다.

.. image:: /images/circuit_oled.svg
    :alt: ESP32-S3 I2C OLED 디스플레이 회로 연결도
    :align: center

.. code-block:: python

    from espzero import OLED

    # 0.96인치 SSD1306 (1.3인치 모델은 driver="sh1106" 지정)
    oled = OLED(scl=47, sda=21)

    oled.clear()
    oled.text("Hello, ESPZero!", 0, 0)
    oled.text("ESP32-S3 OLED", 0, 20)
    oled.rect(0, 36, 128, 20, color=1)
    oled.show()

로봇 얼굴 감정 표현 및 시선 추적 (Robot Face & Gaze)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``oled.show_face()``\ 는 10가지 감정 프리셋(``"normal"``, ``"happy"``, ``"surprised"``, ``"love"``, ``"thinking"``, ``"sleep"``, ``"blink"``, ``"angry"``, ``"sad"``, ``"listening"``)을 제공하며, 눈동자 위치(``look_x``, ``look_y``)를 미세 조절할 수 있습니다.
또한 ``oled.look_at(x, y)``\ 를 사용하면 카메라 손 추적 좌표나 가변저항/조이스틱 좌표를 그대로 전달하여 로봇 눈동자가 사용자의 움직임을 실시간으로 쳐다보게 만들 수 있습니다.

.. image:: /images/oled_robot_faces.svg
    :alt: ESPZero OLED 로봇 표정 다이어그램
    :align: center

.. code-block:: python

    from espzero import OLED
    from time import sleep

    oled = OLED(scl=47, sda=21)

    # 1. 감정 표정 전환
    oled.show_face("happy")      # 웃는 표정 (^ ^)
    sleep(1)
    oled.show_face("surprised")  # 깜짝 놀란 표정 (O O)
    sleep(1)
    oled.show_face("love")       # 하트 눈
    sleep(1)

    # 2. 시선 제어: 왼쪽(-1.0) / 오른쪽(1.0) / 위 / 아래
    oled.show_face("normal", look_x=-1.0, look_y=0.0)  # 왼쪽 쳐다보기
    sleep(1)
    oled.show_face("normal", look_x=1.0, look_y=0.0)   # 오른쪽 쳐다보기
    sleep(1)

    # 3. vision.get_hand() 좌표와 결합한 실시간 시선 추적 (데스크탑 반려 로봇)
    # oled.look_at(hand_x, hand_y, emotion="happy")

LCD 디스플레이 (16x2, PCF8574)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I2C 버스와 PCF8574 I2C 어댑터를 사용하여 LiquidCrystal 디스플레이(LCD)에 문자를 출력합니다.

.. warning::
    **PCF8574 (5V) I2C 백팩 사용 시 레벨 시프터 필수**:
    대부분의 ``16x2 I2C LCD (PCF8574)`` 모듈은 5V 전원을 사용하며 내부 I2C 풀업 저항이 **5V** 에 연결되어 있습니다.
    따라서 ESP32-S3(3.3V 로직)의 ``G21`` (SDA), ``G47`` (SCL) 핀을 보호하려면 보드와 LCD 모듈 사이에 **3.3V↔5V 양방향 I2C 로직 레벨 시프터(Logic Level Shifter)**\ 를 반드시 추가해야 합니다. (레벨 시프터 없이 간편하게 사용하려면 위 **3.3V OLED 디스플레이** 사용을 권장합니다.)

.. image:: /images/circuit_i2c_lcd.svg
    :alt: ESP32-S3 I2C LCD 로직 레벨 시프터 회로 연결도
    :align: center

.. literalinclude:: examples/i2c_lcd.py

GPIO 핀만 사용하여 LiquidCrystal 디스플레이(LCD)에 문자를 출력합니다.

.. literalinclude:: examples/lcd.py


카메라 (Camera)
----------------

ESP32-S3 WROOM CAM 등 카메라가 탑재된 보드에서 별도의 PC나 AI 없이 단독으로 사진을 촬영하고 플래시 메모리에 저장합니다.

.. important::
    **카메라 지원 펌웨어 필요**:
    공식 MicroPython 기본 펌웨어에는 용량 문제로 카메라 드라이버(C 모듈 ``camera``)가 포함되어 있지 않습니다.
    카메라 및 비전 기능을 사용하려면 보드(ESP32-S3 WROOM CAM)에 **카메라 드라이버가 포함 빌드된 MicroPython 펌웨어(Camera-enabled Firmware)**\ 가 플래싱되어 있어야 합니다.

.. note::
    **Mu 에디터 내장 펌웨어 플래싱 안내 (온라인 / 오프라인 지원)**:

    별도의 복잡한 도구(esptool 등)를 설치할 필요 없이, Mu 에디터 우측 하단의 **설정 (톱니바퀴 아이콘)**\ 에서 다음 두 가지 방법 중 하나로 간편하게 카메라 지원 펌웨어를 보드에 설치할 수 있습니다:

    * **온라인 플래싱 ([ESP Online Flasher] 탭)**:
      컴퓨터가 인터넷에 연결되어 있다면 별도의 펌웨어 파일을 미리 다운로드할 필요가 없습니다.
      드롭다운 목록에서 일반 보드(Generic)가 아닌, **카메라와 PSRAM 드라이버가 포함된 보드 항목**\ (예: ``ESP32-S3 Camera (OV2640 / Octal SPIRAM)`` 등)을 정확히 선택한 후 **[버전 가져오기] → [지우고 쓰기]** 버튼을 누르면, 카메라 전용 공식 MicroPython 펌웨어를 클라우드에서 자동으로 내려받아 보드에 즉시 플래싱합니다.

    * **오프라인 플래싱 ([ESP Firmware flasher] 탭)**:
      인터넷이 없는 환경이거나 미리 준비된 특정 버전의 카메라 펌웨어(``.bin`` 파일)를 보유하고 있는 경우에 사용합니다. 보드 종류(``ESP32-S3``)를 선택하고 컴퓨터에 저장된 펌웨어 파일을 지정한 뒤 **[지우고 쓰기]** 버튼을 클릭하여 보드에 직접 덮어씁니다.

사진 촬영 및 저장 (``vision.save_photo`` / ``vision.capture``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``vision.save_photo()``\ 를 호출하면 신형(``camera.Camera``)과 구형(``camera.init``) 펌웨어를 자동 판별하여 단 한 줄로 JPEG 사진을 촬영해 보드 내장 플래시에 저장합니다. 원시 JPEG 바이트 데이터가 직접 필요하거나 클라우드 AI/메신저로 전송할 때는 ``vision.capture()``\ 를 사용하고, 백그라운드 스트리밍(``start_wifi_stream()``) 중에도 최신 프레임을 안전하게 가져옵니다. 촬영이 끝나면 ``vision.close()``\ 로 카메라 하드웨어 자원을 안전하게 해제할 수 있습니다.

.. code-block:: python

    from espzero import vision

    # 1. 사진 1장 촬영 후 보드 플래시에 저장 (해상도: QQVGA, HQVGA, QVGA, VGA)
    saved = vision.save_photo("snapshot.jpg", framesize="QVGA", quality=80)
    print("저장 완료:", saved)

    # 2. 원시 JPEG 바이트 데이터가 직접 필요할 때 (웹 전송/클라우드 AI용)
    jpg_bytes = vision.capture(framesize="QVGA", quality=70)
    print("이미지 크기:", len(jpg_bytes), "bytes")

    # 사용 완료 후 카메라 하드웨어 해제
    vision.close()

타임랩스 및 AI 학습용 이미지 데이터셋 수집
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

버튼 셔터나 일정 시간 간격으로 여러 장의 사진을 자동 저장하여 타임랩스를 만들거나, Edge Impulse 등 TinyML 비전 모델 학습용 이미지 데이터셋을 손쉽게 수집할 수 있습니다.

.. code-block:: python

    from espzero import vision, esp_led
    from time import sleep

    for i in range(1, 6):
        esp_led.color = (0, 255, 0)
        esp_led.on()
        path = vision.save_photo(f"photo_{i:03d}.jpg", framesize="QVGA")
        esp_led.off()
        print("촬영됨:", path)
        sleep(2)

    vision.close()


AI 비전 (AI Vision)
-------------------

ESP32-S3 카메라 영상을 PC 연동 AI(MediaPipe, YOLOv8)나 보드 단독 TinyML 모델과 결합해 활용하는 예제입니다. (사전에 위 **카메라 (Camera)** 섹션에서 안내한 카메라 지원 펌웨어가 설치되어 있어야 합니다.)
PC 연동 AI (MediaPipe 연동 — Mu 에디터 전용)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
    **Mu 에디터 전용 시리얼 프로토콜**: ``vision.start_stream_to_pc()``\ 는 USB 시리얼을 통해 Mu 에디터 내장 카메라/MediaPipe 뷰어와 직접 통신하는 기능입니다. VS Code, Thonny 등 타 에디터에서 사용하려면 아래의 **무선 Wi-Fi 스트리밍(``vision.start_wifi_stream()``)** 방식을 사용하세요.

ESP32 카메라 영상을 PC(Mu 에디터)로 전송하고, PC의 MediaPipe 라이브러리를 사용해 손가락 관절 등을 실시간으로 분석합니다. 분석된 좌표는 다시 ESP32에 전송되어 제어에 사용됩니다.

.. code-block:: python

    from espzero import vision
    from time import sleep

    # PC로 실시간 카메라 영상 전송 시작 (백그라운드 비동기 실행)
    vision.start_stream_to_pc()

    while True:
        # 에디터(PC)가 분석하여 주입해 준 손가락 좌표 읽기
        if "__pc_ai_data" in globals():
            x = __pc_ai_data.get("hand_x", 0)
            y = __pc_ai_data.get("hand_y", 0)
            detected = __pc_ai_data.get("hand_detected", False)
            if detected:
                print("손가락 감지됨 -> X:", x, "Y:", y)
        sleep(0.1)

무선 WiFi 영상 전송 및 PC YOLO 자율주행
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

마이크로컨트롤러인 ESP32-S3는 하드웨어 연산 능력과 메모리가 제한되어 있어 무거운 최신 딥러닝 모델(YOLOv8 등)을 단독으로 구동하기 어렵습니다.
하지만 ESP32와 PC가 **무선 Wi-Fi**\ 를 통해 역할을 분담하면, 실시간 객체 인식 기반의 고성능 자율주행 로봇 자동차를 쉽게 만들 수 있습니다.

**동작 원리 및 역할 분담**:

.. code-block:: text

    [ ESP32 로봇 자동차 ] (눈과 발 역할)
      - 카메라 영상을 Wi-Fi (MJPEG 스트림)로 실시간 전송
      - PC에서 수신된 무선 주행 명령('GO' / 'STOP')에 따라 모터 구동
      ▲
      │  (Wi-Fi 무선 네트워크: 실시간 영상 수신 & 주행 명령 전송)
      ▼
    [ PC의 Mu 에디터 - Python 3 모드 ] (두뇌 역할)
      - Wi-Fi 영상 스트림을 받아 PC의 고성능 CPU/GPU로 YOLOv8 실시간 객체 추론
      - 사람/장애물 감지 시 즉시 'STOP', 전방 안전 시 'GO' 주행 명령 전송

**단계별 실습 가이드 (Mu 에디터 / 일반 Python 에디터 공통)**:

1. **PC YOLO 환경 준비**:
   PC에서 YOLO 추론을 실행하기 위해 필요한 패키지를 준비합니다.

   * **방법 A (Mu 에디터 환경)**:
     Mu 에디터에는 ``opencv-python``\ 과 ``requests`` 패키지가 이미 기본 내장되어 있으므로, 우측 하단의 **설정 (톱니바퀴 아이콘) → [Third-party Packages (서드파티 패키지)]** 탭에서 ``ultralytics``\ 만 입력 후 [OK] 버튼을 누르면 즉시 사용할 수 있습니다.

   * **방법 B (VS Code 등 외부 에디터 환경)**:
     Mu가 아닌 일반 Python 환경을 사용할 경우, CMD 또는 PowerShell에서 아래 명령을 실행하여 필요한 패키지를 설치합니다:

     .. code-block:: bash

         pip install ultralytics opencv-python requests

2. **1단계: ESP32 로봇 자동차 코드 업로드 (Mu [ESP32 모드] 또는 Thonny / mpremote)**:
   아래 코드를 ``main.py`` 파일로 저장하여 ESP32 보드에 업로드합니다 (Mu 에디터에서는 **ESP32 모드** 사용, CLI에서는 ``mpremote cp main.py :main.py``).
   (``main.py`` 파일로 저장해 두면 PC와 USB 케이블을 분리하고 배터리만 연결해도 전원이 켜지는 즉시 스스로 Wi-Fi에 접속하여 무선 스트리밍을 시작합니다. 실행 시 터미널에 표시되는 ESP32의 IP 주소(예: ``http://192.168.0.50:8080/``)를 확인합니다.)

   .. literalinclude:: examples/vision_yolo_car_esp32.py
      :start-at: from espzero import

3. **2단계: PC AI 자율주행 컨트롤러 실행 (Mu [Python 3 모드] 또는 일반 Python)**:
   Mu 에디터에서는 좌측 상단의 **[모드(Mode)]**\ 를 **Python 3 모드**\ 로 변경해 실행하고, VS Code나 터미널에서는 일반 ``.py`` 파일로 저장 후 ``python vision_yolo_car_pc.py``\ 로 실행합니다.
   앞서 확인한 ESP32의 IP 주소를 ``STREAM_URL`` 및 ``CMD_URL`` 변수에 입력한 뒤 실행하면, PC 화면에 실시간 감지 결과가 표시되는 비디오 창이 열리며 로봇 자동차가 자율주행을 시작합니다.

   .. literalinclude:: examples/vision_yolo_car_pc.py
      :start-at: import cv2

.. tip::
    **완성 후 배터리 독립 구동 & 야외 핫스팟(AP) 꿀팁**

    * **PC 없이 보조배터리로 완전 무선 구동하기 (main.py 저장)**:
      스마트카나 로봇 프로젝트를 완성하여 PC 연결 없이 야외나 바닥에서 주행시킬 때는, 코드를 ESP32 보드 플래시 최상위에 ``main.py``\ 라는 이름의 파일로 저장하세요. USB 케이블을 뽑고 보조배터리나 어댑터만 연결하면, 부팅 즉시 Wi-Fi를 잡고 무선 영상 스트리밍과 주행 대기 상태에 들어갑니다.
      PC나 스마트폰에서는 Mu 에디터 카메라 창의 Wi-Fi 주소 입력란(``http://192.168.x.x:8080/``) 또는 웹 브라우저에서 보드 IP 주소로 접속하여 무선으로 영상을 보며 제어할 수 있습니다.

    * **공유기(Wi-Fi)가 없는 야외나 교실에서의 단독 핫스팟(AP 모드) 구동**:
      주변에 Wi-Fi 공유기가 없더라도 걱정할 필요가 없습니다. ESP32 자체를 무선 공유기(AP)로 동작시키면 외부 인터넷이나 공유기 없이도 스마트폰 또는 노트북과 1:1 직결 무선 스트리밍이 가능합니다:

      .. code-block:: python

          import network
          from espzero import vision

          # 1. ESP32 자체를 무선 핫스팟(AP)으로 활성화
          ap = network.WLAN(network.AP_IF)
          ap.active(True)
          ap.config(essid="ESP32-CAM-ROBOT", authmode=network.AUTH_OPEN)

          # 2. 자체 망에서 스트리밍 시작 (기본 IP: http://192.168.4.1:8080/)
          vision.start_wifi_stream(port=8080)

      노트북이나 스마트폰의 Wi-Fi 목록에서 ``ESP32-CAM-ROBOT`` 신호에 접속한 뒤, 브라우저나 PC 컨트롤러에서 ``http://192.168.4.1:8080/`` 주소로 연결하면 어디서든 무선 스트리밍 및 AI 원격 제어가 가능합니다.

기기 단독 AI (On-Device TFLite)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ESP32 내부에 다운로드한 ``.tflite`` 모델 파일을 읽어와 직접 AI 추론을 수행합니다. PC와 연결되지 않은 상태에서도 동작할 수 있습니다.

.. note::
    ESP32(마이크로컨트롤러)용 경량 ``.tflite`` 모델들은 Kaggle Models(https://www.kaggle.com/models?framework=liteRT), Hugging Face LiteRT 커뮤니티(https://huggingface.co/litert-community), 또는 텐서플로우 마이크로 공식 저장소(https://github.com/tensorflow/tflite-micro)에서 직접 내려받을 수 있습니다.

.. code-block:: python

    from espzero import vision
    import tflite
    from time import sleep

    # TFLite 모델 로드
    model = tflite.load("model.tflite")

    while True:
        img = vision.capture(framesize="QVGA")
        if img:
            # 이미지 분석 및 클래스 결과 추출
            result = model.detect(img)
            print("인식된 클래스 ID:", result.class_id)
        sleep(0.5)


AI 음성 (AI Voice)
------------------

ESP32 보드에 별도의 I2S 디지털 마이크 부품을 달지 않고도, **PC나 노트북의 고성능 내장 마이크**\ 를 통해 음성을 인식하고 Wi-Fi 무선 통신으로 ESP32 자동차와 로봇을 조작할 수 있습니다.

PC 음성 인식 기반 스마트카 무선 조작
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

이 방식은 하드웨어 배선이 가장 단순하며 소음이 많은 교실이나 야외에서도 높은 음성 인식률을 보장합니다.

**동작 원리 및 역할 분담**:

.. code-block:: text

    [ 사용자 ]
      🗣️ "앞으로!" / "멈춰!" / "돌아봐!"
      │
      ▼ (PC/노트북 내장 마이크로 수음)
    [ PC의 Mu 에디터 - Python 3 모드 ] (귀와 두뇌 역할)
      - PC 마이크로 음성을 듣고 내장된 SpeechRecognition으로 한국어/영어 분석
      - 분석된 명령어를 Wi-Fi HTTP 요청으로 전송:
        requests.get("http://<ESP32_IP>:8080/ai?action=GO")
      ▲
      │  (Wi-Fi 무선 네트워크: 텍스트 명령 전송)
      ▼
    [ ESP32 로봇 자동차 ] (몸 역할, 마이크/OLED 불필요!)
      - Wi-Fi로 수신된 action("GO") 명령 즉시 처리
      - 2륜 모터 구동 및 LED 상태 표시

**단계별 실습 가이드 (Mu 에디터 / 일반 Python 에디터 공통)**:

1. **PC 음성 인식 환경 준비**:
   마이크로 음성을 인식하고 ESP32로 명령을 전달할 환경을 준비합니다.

   * **방법 A (Mu 에디터 환경)**:
     Mu 에디터에는 ``SpeechRecognition``\ 과 ``requests`` 패키지가 이미 기본 내장되어 있으므로 **별도 패키지 설치 없이 곧바로 실행**할 수 있습니다.

   * **방법 B (VS Code 등 외부 에디터 환경)**:
     Mu가 아닌 일반 Python 환경을 사용할 경우, CMD 또는 PowerShell에서 아래 명령을 실행하여 필요한 패키지를 설치합니다:

     .. code-block:: bash

         pip install SpeechRecognition requests PyAudio

2. **1단계: ESP32 로봇 자동차 코드 업로드 (Mu [ESP32 모드] 또는 Thonny / mpremote)**:
   아래 코드를 작성하여 ESP32 보드에 업로드합니다. 보드가 Wi-Fi에 접속되면 터미널에 표시되는 IP 주소(예: ``http://192.168.0.50:8080/``)를 확인합니다.

   .. literalinclude:: examples/voice_control_car_esp32.py
      :start-at: from espzero import

3. **2단계: PC 음성 인식 컨트롤러 실행 (Mu [Python 3 모드] 또는 일반 Python)**:
   Mu 에디터에서는 **[모드(Mode)]**\ 를 **Python 3 모드**\ 로 변경해 실행하고, VS Code나 터미널에서는 ``python voice_control_car_pc.py``\ 로 실행합니다. 앞서 확인한 ESP32의 IP 주소를 ``ESP_IP``\ 에 입력한 뒤 실행하면, PC 마이크가 켜지고 음성 명령 대기 상태가 됩니다.

   .. literalinclude:: examples/voice_control_car_pc.py
      :start-at: import requests

무선 Wi-Fi 음성 전송 & 음성 로봇 제어
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ESP32-S3의 I2S 디지털 마이크로 수음한 고품질 오디오를 Wi-Fi 무선 네트워크를 통해 실시간 WAV 스트림(기본 포트 ``8081``)으로 PC에 전송할 수 있습니다.
PC(Python 3 모드)에서는 Whisper, SpeechRecognition 또는 Edge Impulse 모델로 음성을 실시간 분석한 뒤, ``/ai?action=...`` 엔드포인트로 제어 명령을 전달하여 ESP32 로봇과 OLED 표정을 무선 조작합니다.

**동작 원리 및 역할 분담**:

.. code-block:: text

    [ ESP32-S3 보드 ] (귀와 몸 역할)
      - I2S 마이크 오디오를 Wi-Fi (HTTP WAV 스트림, 포트 8081)로 실시간 전송
      - PC에서 수신된 음성 AI 명령('GO' / 'STOP' / 'DANCE')에 따라 로봇 구동 및 OLED 표정 변경
      ▲
      │  (Wi-Fi 무선 네트워크: 실시간 오디오 스트림 & 음성 AI 명령 전송)
      ▼
    [ PC의 Mu 에디터 - Python 3 모드 ] (음성 인식 두뇌 역할)
      - http://<ESP32_IP>:8081/ 스트림에서 오디오 청크를 읽어 음성 인식 수행
      - 인식된 명령어를 http://<ESP32_IP>:8081/ai?action=GO 로 전송

1. **ESP32-S3 음성 AI 로봇 코드 업로드 (Mu [ESP32 모드])**:

   .. literalinclude:: examples/audio_wifi_ai_robot_esp32.py
      :start-at: from espzero import

2. **PC 음성 인식 컨트롤러 실행 (Mu [Python 3 모드])**:
   PC에서 ESP32의 오디오 스트림을 수신하여 Google 음성 인식 또는 Whisper로 처리한 후 명령을 전송합니다:

   .. literalinclude:: examples/audio_wifi_ai_robot_pc.py
      :start-at: import io

기기 단독 온디바이스 TinyML 사운드 분류 (Edge Impulse & MFCC)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PC와의 무선 통신 없이 ESP32-S3 기기 단독으로 키워드 인식(KWS)이나 이상 음향 감지를 수행할 때는 ``mic.mfcc()``\ 를 활용합니다.

.. note::
    **Edge Impulse 및 TinyML 음성 모델 개발**:
    마이크로컨트롤러용 음향 인식 및 키워드 감지 모델을 웹 브라우저에서 손쉽게 학습하고 C++/MicroPython 라이브러리로 배포하려면 `Edge Impulse Studio <https://www.edgeimpulse.com/>`_ (https://www.edgeimpulse.com/) 및 `Edge Impulse 오디오 튜토리얼 <https://docs.edgeimpulse.com/docs/tutorials/audio>`_\ 을 이용할 수 있으며, `Kaggle Models <https://www.kaggle.com/models?framework=liteRT>`_\ 와 `LiteRT Community <https://huggingface.co/litert-community>`_\ 에서 사전 학습된 음향 분류 모델(``.tflite``)을 직접 내려받을 수도 있습니다.

* **MFCC 특징 벡터 추출**: ``mic.mfcc(num_cepstra=13)``\ 를 호출하면 음성 인식 인공지능 모델(TinyML / TFLite Micro)의 표준 입력으로 쓰이는 13차원 Mel-Frequency Cepstral Coefficients를 고속으로 추출합니다.
* **학습용 데이터셋 수집**: ``mic.save_wav("sample.wav", duration=1.0)``\ 로 온보드 플래시 메모리에 마이크 음성을 16-bit WAV 파일로 직접 저장하여 Edge Impulse 학습용 데이터셋을 손쉽게 구축할 수 있습니다.

.. code-block:: python

    from espzero import I2SMic
    from time import sleep

    mic = I2SMic()

    # 13차원 MFCC 특징 벡터 추출 (TinyML 음성 모델 입력용)
    features = mic.mfcc(num_cepstra=13)
    print("MFCC 특징 벡터:", features[:5], "... (총 13개)")

    # 1초 분량 학습용 음향 샘플 플래시 저장
    mic.save_wav("cough_sample.wav", duration=1.0)
    print("WAV 오디오 샘플 저장 완료!")

복합 예제 (Combined Examples)
-----------------------------

여러 센서와 액추에이터, 그리고 AI 기능을 결합한 완성형 프로젝트 예제입니다. 입문부터 고급까지 난이도 순으로 구성되어 있습니다.

버튼으로 조명 제어 (Button-Controlled Light)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

버튼을 누를 때마다 LED가 토글되는 가장 기본적인 입출력 결합 예제입니다.

.. code-block:: python

    from espzero import LED, Button

    led = LED(4)
    btn = Button(5)

    btn.when_pressed = led.toggle

    while True:
        pass # 이벤트 대기

스마트 안심 도어락 (Smart Doorlock)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

내장 RGB LED, 서보 모터(잠금장치), 부저(알림음)를 결합하여 출입 인증 성공 시 초록색 점등 및 알림음과 함께 문을 열고, 일정 시간 뒤 자동으로 잠그는 스마트 도어락 예제입니다.

.. image:: /images/circuit_smart_doorlock.svg
    :alt: ESP32-S3 스마트 안심 도어락 회로 연결도
    :align: center

.. literalinclude:: examples/smart_doorlock.py

다이얼로 시선을 조종하는 로봇 눈 (Potentiometer Gaze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

가변저항 다이얼을 돌리면 OLED 로봇 눈동자가 좌우로 실시간 움직이고, 버튼을 누르면 하트(``"love"``) 표정을 짓는 인터랙티브 데스크탑 토이입니다.

.. literalinclude:: examples/oled_pot_gaze.py
   :start-at: from espzero import

아날로그 시계 (Analog Clock)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

스텝 모터를 60초에 1바퀴(2048 스텝) 속도로 정밀 구동하여 연속으로 회전하는 아날로그 시계의 초침을 만듭니다.

.. literalinclude:: examples/stepper_analog_clock.py

자동 블라인드 (Automatic Blinds)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

스텝 모터를 활용해 정해진 시간 간격에 맞춰 창문 블라인드를 자동으로 여닫는 컨트롤러입니다.

.. literalinclude:: examples/stepper_automatic_blinds.py

자동차 후방 주차 경보기 (Smart Parking Assist)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

초음파 센서로 장애물과의 거리를 측정해 가까워질수록 OLED 로봇 표정(``happy`` → ``surprised`` → ``angry``), LED 색상(초록 → 노랑 → 빨강), 부저 경고음 주기가 단계적으로 변하는 실생활 안전 경보기입니다.

.. image:: /images/circuit_parking_assist.svg
    :alt: ESP32-S3 자동차 후방 주차 경보기 회로 연결도
    :align: center

.. literalinclude:: examples/smart_parking_assist.py
   :start-at: from espzero import

박수 소리로 여닫는 스마트 자동문 (Clap Smart Door)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I2S 디지털 마이크의 박수 감지 이벤트(``when_clap``)를 활용해, PC나 Wi-Fi 없이 손뼉을 칠 때마다 OLED 표정이 바뀌며 서보 모터로 문을 여닫는 온디바이스 자동문입니다.

.. literalinclude:: examples/clap_smart_door.py
   :start-at: from espzero import

초음파 자율주행 장애물 회피 로봇 (Obstacle-Avoiding Rover)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

전방 초음파 센서와 2륜 구동 로봇을 결합하여, 20cm 이내에 장애물이 감지되면 스스로 후진 후 방향을 전환해 주행을 이어가는 완전 자율주행 로버입니다.

.. image:: /images/circuit_obstacle_rover.svg
    :alt: ESP32-S3 초음파 장애물 회피 로봇 회로 연결도
    :align: center

.. literalinclude:: examples/obstacle_avoiding_rover.py
   :start-at: from espzero import

멀티모달 AI 반려 로봇 (Vision AI + Voice AI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ESP32-S3의 카메라 영상(포트 ``8080``)과 I2S 디지털 마이크 음성(포트 ``8081``)을 동시에 PC로 무선 스트리밍하고, PC에서 시각과 음성을 병렬 분석해 OLED 로봇 표정(``look_at`` / ``show_face``)과 RGB LED로 반응하는 통합 AI 반려 로봇입니다.

1. **ESP32-S3 멀티모달 로봇 코드 업로드 (Mu [ESP32 모드])**:

   .. literalinclude:: examples/multimodal_companion_robot_esp32.py
      :start-at: from espzero import

2. **PC 멀티모달 AI 컨트롤러 실행 (Mu [Python 3 모드])**:

   .. literalinclude:: examples/multimodal_companion_robot_pc.py
      :start-at: import threading
