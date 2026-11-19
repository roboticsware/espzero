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

    # 개별 채널 강도 조절 (0~255)
    rgb.red = 128
    rgb.blue = 255

    # 색상 반전 및 토글
    rgb.invert()
    rgb.toggle()

    # 다채로운 자동 애니메이션 (점멸, 페이드, 무지개 순환)
    rgb.blink(on_times=0.5, colors=((255, 0, 0), (0, 255, 0), (0, 0, 255)), n=2, wait=True)
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

서보 모터 (Servo)
~~~~~~~~~~~~~~~

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

모터 및 로봇 (Motor & Robot)
---------------------------

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


AI 비전 (AI Vision)
-----------------

ESP32-S3 AI 비전 카메라와 에디터 연동 및 단독 실행 AI 예제입니다.

.. important::
    **카메라 지원 펌웨어 필요**:
    공식 MicroPython 기본 펌웨어에는 용량 문제로 카메라 드라이버(C 모듈 ``camera``)가 포함되어 있지 않습니다.
    비전 기능을 사용하려면 보드(ESP32-S3 WROOM CAM)에 **카메라 드라이버가 포함 빌드된 MicroPython 펌웨어(Camera-enabled Firmware)**\ 가 플래싱되어 있어야 합니다.

.. note::
    **Mu 에디터에서 직접 펌웨어 플래싱 지원**:
    별도의 복잡한 도구(esptool 등)를 설치할 필요 없이 Mu 에디터 안에서 카메라 지원 펌웨어를 직접 플래싱할 수 있습니다.
    Mu 우측 하단의 **설정 (톱니바퀴 아이콘) → [ESP Firmware flasher]** 탭(또는 **[ESP Online Flasher]** 탭)에서 보드 종류(ESP32-S3)를 선택하고 카메라 펌웨어(``.bin`` 파일)를 지정한 뒤 **[Erase & write firmware]** 버튼을 누르면 자동으로 보드에 플래싱됩니다.

PC 연동 AI (MediaPipe 연동)
~~~~~~~~~~~~~~~~~~~~~~~~~

ESP32 카메라 영상을 PC(에디터)로 전송하고, PC의 MediaPipe 라이브러리를 사용해 손가락 관절 등을 실시간으로 분석합니다. 분석된 좌표는 다시 ESP32에 전송되어 제어에 사용됩니다.

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

**Mu 에디터 단계별 실습 가이드**:

1. **PC YOLO 환경 준비**:
   PC에서 YOLO 추론을 실행하기 위해 필요한 패키지를 설치합니다:

   * **방법 A (Mu 에디터 설정)**: Mu 우측 하단의 **설정 (톱니바퀴 아이콘) → [Third-party Packages (서드파티 패키지)]** 탭에서 ``ultralytics`` 입력 후 [OK] 버튼을 클릭합니다.
   * **방법 B (터미널)**: CMD 또는 PowerShell에서 ``pip install ultralytics opencv-python requests`` 명령을 실행합니다.

2. **1단계: ESP32 로봇 자동차 코드 업로드 (Mu [ESP32 모드])**:
   Mu 에디터 상단 모드를 **ESP32 모드**\ 로 설정하고 아래 코드를 작성한 후, 파일 이름을 ``main.py`` 파일로 지정하여 ESP32 보드에 저장합니다.
   (``main.py`` 파일로 저장해 두면 PC와 USB 케이블을 분리하고 배터리만 연결해도 전원이 켜지는 즉시 스스로 Wi-Fi에 접속하여 무선 스트리밍을 시작합니다. 실행 시 터미널에 표시되는 ESP32의 IP 주소(예: ``http://192.168.0.50:8080/``)를 확인합니다.)

   .. code-block:: python

       from espzero import WiFi, vision, Robot
       from time import sleep

       # 1. WiFi 공유기 연결
       wifi = WiFi()
       wifi.connect("내_와이파이_이름", "비밀번호")

       # 2. 2륜 구동 로봇 모터 설정 (카메라와 충돌하지 않는 안전 핀: 왼쪽 41, 42 / 오른쪽 47, 21)
       car = Robot(left=(41, 42), right=(47, 21))

       # 3. 무선 카메라 스트리밍 시작 (기본 포트: 8080)
       vision.start_wifi_stream(port=8080)

       # 4. PC AI 판단 데이터 수신 및 주행 루프
       while True:
           if "__pc_ai_data" in globals():
               action = __pc_ai_data.get("action", "STOP")
               if action == "GO":
                   car.forward(0.6) # 전방 안전 시 전진
               else:
                   car.stop()       # 사람/장애물 감지 시 정지
           sleep(0.05)

3. **2단계: PC AI 자율주행 컨트롤러 실행 (Mu [Python 3 모드])**:
   Mu 에디터 좌측 상단의 **[모드(Mode)]** 버튼을 클릭하여 **Python 3 모드**\ 로 변경합니다.
   새 탭에 아래 스크립트를 작성하고, 앞서 확인한 ESP32의 IP 주소를 ``STREAM_URL`` 및 ``CMD_URL`` 변수에 입력한 뒤 **[실행(Play)]** 버튼을 누릅니다.
   PC 화면에 실시간 감지 결과가 표시되는 비디오 창이 열리며 로봇 자동차가 자율주행을 시작합니다.

   .. code-block:: python

       import cv2
       import requests
       from ultralytics import YOLO

       # 경량 고속 모델 로드 및 ESP32 카메라 스트림 주소 설정
       model = YOLO("yolov8n.pt")
       STREAM_URL = "http://192.168.0.50:8080/"  # ESP32 IP 주소
       CMD_URL = "http://192.168.0.50:8080/ai"

       cap = cv2.VideoCapture(STREAM_URL)

       while cap.isOpened():
           ret, frame = cap.read()
           if not ret:
               break

           # YOLOv8 실시간 객체 추론 (0: 사람, 9: 신호등)
           results = model(frame, verbose=False)
           person_detected = False

           for r in results:
               for box in r.boxes:
                   cls_id = int(box.cls[0])
                   if cls_id == 0: # 사람 감지
                       person_detected = True

           # 사람 감지 시 즉시 정지, 없으면 주행 명령 전송
           cmd = "STOP" if person_detected else "GO"
           try:
               requests.get(f"{CMD_URL}?action={cmd}", timeout=0.1)
           except Exception:
               pass

           # 화면에 바운딩 박스 표시
           annotated = results[0].plot()
           cv2.imshow("ESP32-S3 YOLO AI Auto-Driving", annotated)
           if cv2.waitKey(1) & 0xFF == ord('q'):
               break

       cap.release()
       cv2.destroyAllWindows()

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

