Retseptlar (Recipes)
===================

Ushbu bo'limda ``espzero`` yordamida turli xil sensorlar va komponentlarni boshqarish bo'yicha amaliy misollar keltirilgan. Barcha misollarda ``import espzero; espzero.begin()`` chaqirilgan deb hisoblanadi.

O'rnatilgan LED (Built-in LED)
------------------------------

Platadagi LEDni boshqarishning eng oson yo'li.

.. code-block:: python

    from espzero import esp_led
    from time import sleep

    esp_led.on()    # Yoqish
    sleep(1)
    esp_led.off()   # O'chirish
    esp_led.blink() # Orqa fonda miltillash

Raqamli chiqish (LED)
---------------------

Muayyan pinga ulangan oddiy LEDni boshqarish.

.. image:: /images/circuit_led.svg
    :alt: ESP32 LED sxemasi
    :align: center

.. code-block:: python

    from espzero import LED

    led = LED(4) # GPIO 4

    led.on()
    led.off()
    led.toggle()
    
    # 0.5 soniya oralig'ida 5 marta miltillash (asinxron)
    led.blink(on_time=0.5, off_time=0.5, n=5)

PWM boshqaruvi (Yorqinlikni sozlash)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    led.value = 0.5 # 50% yorqinlik
    led.pulse()     # Sekin yonib-o'chish

RGB LED
-------

Tashqi 4-pinli RGB LED
~~~~~~~~~~~~~~~~~~~~~~

Turli xil ranglarni yaratish uchun Qizil, Yashil va Moviy pinlarni birlashtiring.
(Eslatma: ESP32-S3 platalarida 22–34 pinlar mavjud emas, shuning uchun GPIO 4, 5, 6 kabi pinlardan foydalaning.)

.. image:: /images/circuit_rgb.svg
    :alt: ESP32 RGB LED sxemasi
    :align: center

.. code-block:: python

    from espzero import RGBLED
    from time import sleep

    # ESP32 va ESP32-S3 uchun umumiy qo'llab-quvvatlanadigan pinlar (masalan, GPIO 4, 5, 6)
    rgb = RGBLED(red=4, green=5, blue=6)

    rgb.color = (255, 0, 0)   # Qizil
    sleep(0.5)
    rgb.color = (0, 255, 0)   # Yashil
    sleep(0.5)
    rgb.color = (255, 255, 0) # Sariq (Qizil + Yashil)
    sleep(0.5)

    # Alohida kanal yorqinligini boshqarish (0~255)
    rgb.red = 128
    rgb.blue = 255

    # Rangni teskari aylantirish (invert) va holatni almashtirish (toggle)
    rgb.invert()
    rgb.toggle()

    # Avtomatik animatsiyalar (miltillash, ravon pulsatsiya, kamalak aylanishi)
    rgb.blink(on_times=0.5, colors=((255, 0, 0), (0, 255, 0), (0, 0, 255)), n=2, wait=True)
    rgb.pulse(fade_times=1, n=2, wait=True)  # Ravon o'chib-yonish
    rgb.cycle(fade_times=1, n=2, wait=True)  # Kamalak ranglari tsikli

    rgb.off()

O'rnatilgan RGB LED (ESP32-S3 WS2812 NeoPixel)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O'rnatilgan WS2812 NeoPixel RGB LED (ESP32-S3 DevKit yoki M5Stack) bo'lgan platalar uchun pin raqamlarini ko'rsatmasdan ``esp_led`` dan foydalaning:

.. code-block:: python

    from espzero import esp_led
    from time import sleep

    esp_led.color = (255, 0, 0)   # Qizil
    sleep(0.5)
    esp_led.color = (0, 255, 0)   # Yashil
    sleep(0.5)
    esp_led.color = (0, 0, 255)   # Moviy
    sleep(0.5)

    # O'rnatilgan NeoPixel kamalak aylanish effekti
    esp_led.cycle(fade_times=0.5, n=3, wait=True)
    esp_led.off()

Buzzer va Dinamik (Buzzer & Speaker)
------------------------------------

Oddiy signal (Beep)
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from espzero import Buzzer

    bz = Buzzer(15)
    bz.beep(on_time=0.1, off_time=0.1, n=3) # "Bip-Bip-Bip"

Melodiyalarni ijro etish (Play)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from espzero import Speaker

    spk = Speaker(15)

    # (nota, davomiylik) tuplar ro'yxati
    tune = [
        ('c4', 0.5), ('d4', 0.5), ('e4', 0.5), ('c4', 0.5),
        ('e4', 0.5), ('c4', 0.5), ('g4', 1.0)
    ]
    spk.play(tune)

Kirish qurilmalari (Input Devices)
----------------------------------

Tugma (Button)
~~~~~~~~~~~~~~

.. image:: /images/circuit_button.svg
    :alt: ESP32 Tugma sxemasi
    :align: center

.. code-block:: python

    from espzero import Button

    btn = Button(5)

    btn.when_pressed = lambda: print("Bosildi!")
    btn.when_released = lambda: print("Qo'yib yuborildi!")

Potentiometr
~~~~~~~~~~~~

.. image:: /images/circuit_potentiometer.svg
    :alt: ESP32 Potentiometr sxemasi
    :align: center

.. code-block:: python

    from espzero import Pot

    pot = Pot(34) # Analog pin (ADC)

    print("Joriy qiymat (0-1):", pot.value)
    print("Kuchlanish (V):", pot.voltage)

Servo motor (Servo)
~~~~~~~~~~~~~~~~~~~

Standart servo motorlarni nisbat (0.0 dan 1.0 gacha) yoki burchak (0 dan 180 gradusgacha) bo'yicha boshqarish (``picozero-rw`` bilan to'liq mos):

.. image:: /images/circuit_servo.svg
    :alt: ESP32 Servo motor sxemasi
    :align: center

.. code-block:: python

    from espzero import Servo
    from time import sleep

    servo = Servo(13)

    # Holatni boshqarish (0.0: min, 0.5: o'rta, 1.0: maks)
    servo.mid()
    sleep(1)

    # Aniq burchakka burish (move_to_degree API)
    servo.move_to_degree(90)   # 90 gradus (markaz)
    sleep(1)
    servo.move_to_degree(180)  # 180 gradus (maks)
    sleep(1)
    servo.move_to_degree(0)    # 0 gradus (min)

    # Ravon tebranish (0 <-> 180 gradus uzluksiz harakat)
    servo.pulse(fade_in_time=1, fade_out_time=1)

Motorlar va Robotlar (Motor & Robot)
------------------------------------

DC Motor (Motor)
~~~~~~~~~~~~~~~~

Drayver platalari (masalan, L298N, L9110S, DRV8833) orqali ikki yo'nalishli DC motorni boshqarish:

.. image:: /images/circuit_motor.svg
    :alt: ESP32 DC Motor sxemasi
    :align: center

.. code-block:: python

    from espzero import Motor
    from time import sleep

    # Oldinga va orqaga pinlarini ko'rsatish (PWM tezlikni boshqarish)
    motor = Motor(forward=4, backward=5)

    # To'liq tezlikda oldinga aylantirish
    motor.forward()
    sleep(1)

    # 50% tezlikda orqaga aylantirish
    motor.backward(0.5)
    sleep(1)

    # Vaqt bilan aylantirish (1 soniya aylanib, avtomatik to'xtaydi)
    motor.forward(speed=0.8, t=1, wait=True)

    # Motorni to'xtatish
    motor.stop()

Robot Rover (Ikki g'ildirakli robot platformasi)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

2 g'ildirakli robot platformasini oldinga, orqaga, chapga va o'ngga boshqarish:

.. image:: /images/circuit_robot.svg
    :alt: ESP32 2 g'ildirakli robot sxemasi
    :align: center

.. code-block:: python

    from espzero import Robot
    from time import sleep

    # left=(oldinga_pin, orqaga_pin), right=(oldinga_pin, orqaga_pin)
    robot = Robot(left=(4, 5), right=(6, 7))

    # Asosiy harakatlar
    robot.forward()
    sleep(1)
    robot.backward(0.6)
    sleep(1)

    # Chapga va o'ngga burilish
    robot.left(speed=0.8)
    sleep(0.5)
    robot.right(speed=0.8)
    sleep(0.5)

    # Vaqt bo'yicha kvadrat shaklida harakatlanish
    for _ in range(4):
        robot.forward(t=1, wait=True)
        robot.left(t=0.5, wait=True)

    # Robotni to'xtatish
    robot.stop()

O'rnatilgan sensorli tugma (Capacitive Touch)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ESP32 va ESP32-S3 chiplariga o'rnatilgan sig'imli sensorli periferiyadan foydalanadi. Tashqi rezistorlarsiz barmog'ingiz bilan teginishni aniqlaydi.

.. code-block:: python

    from espzero import CapTouch
    from time import sleep

    # WROOM: T0~T9 (masalan, GPIO 4), S3: touch pin (masalan, GPIO 1)
    touch = CapTouch(1)

    while True:
        # value: xom o'lchov qiymati (tegilganda kamayadi)
        # is_touched: threshold (standart 300) dan kichik bo'lsa True
        print("Xom qiymat:", touch.value, "Tegildi:", touch.is_touched)
        sleep(0.2)

Masofa sensori (Distance Sensor)
--------------------------------

HC-SR04 kabi ultratovushli sensor yordamida masofani o'lchang.

.. image:: /images/circuit_distance.svg
    :alt: ESP32 Masofa sensori sxemasi
    :align: center

.. code-block:: python

    from espzero import DistanceSensor

    # echo=14, trigger=13
    ds = DistanceSensor(echo=14, trigger=13)

    while True:
        print("Masofa: ", ds.distance, "cm")
        sleep(0.5)

Harorat sensori (Temperature Sensor)
------------------------------------

Ichki harorat
~~~~~~~~~~~~~

ESP32 chipining ichki haroratini o'lchang. (Eslatma: Atrof-muhit haroratidan farq qilishi mumkin).

.. code-block:: python

    from espzero import esp_temp_sensor

    print("Chip ichki harorati:", esp_temp_sensor.temp, "C")

Murakkab misol: Tugma bilan chiroqni boshqarish
----------------------------------------------

Tugma bosilganda LED holatini o'zgartirish.

.. code-block:: python

    from espzero import LED, Button, begin

    begin()
    led = LED(4)
    btn = Button(5)

    btn.when_pressed = led.toggle

    while True:
        pass # Hodisalarni kutish

Stepper motor (Stepper motor)
-----------------------------

Drayver platasi (masalan, ULN2003) orqali ulangan stepper motorni boshqarish.

Analog soat (Analog clock)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Uzluksiz ishlaydigan analog soat soniya mili yarating:

.. literalinclude:: examples/stepper_analog_clock.py

Avtomatik jalyuzilar (Automatic blinds)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vaqtga asoslangan jalyuzi boshqaruvchisi:

.. literalinclude:: examples/stepper_automatic_blinds.py

LCD Displey (LCD Display)
-------------------------

I2C shinasidan va PCF8574 I2C adapteridan foydalanib LiquidCrystal displeylarida (LCD) belgilarni chop etish.

.. image:: /images/circuit_i2c_lcd.svg
    :alt: ESP32 I2C LCD Displey sxemasi
    :align: center

.. literalinclude:: examples/i2c_lcd.py

Faqat GPIO pinlari yordamida LiquidCrystal displeylarida (LCD) belgilarni chop etish.

.. literalinclude:: examples/lcd.py


AI Vision (AI vizualizatsiyasi)
-------------------------------

ESP32-S3 kamerasi yordamida kompyuter ko'magidagi AI va mustaqil ishlaydigan qurilmadagi AI misollari.

.. important::
    **Kamerani qo'llab-quvvatlovchi proshivka zarur**:
    Rasmiy standart MicroPython proshivkasida xotira cheklovlari tufayli kamera drayveri (``camera`` moduli) mavjud emas.
    Vizual funksiyalardan foydalanish uchun platangizga (ESP32-S3 WROOM CAM) **Kamera drayveri bilan yig'ilgan MicroPython proshivkasi (Camera-enabled Firmware)** o'rnatilgan bo'lishi kerak.

    .. note::
        **Mu muharririda to'g'ridan-to'g'ri proshivka o'rnatish**:
        Qo'shimcha murakkab dasturlarni (masalan, esptool) o'rnatish shart emas. Mu muharririning o'zida proshivka qilish imkoni mavjud:
        Mu ning pastki o'ng burchagidagi **Sozlamalar (tishli g'ildirak)** tugmasini bosing → **[ESP Firmware flasher]** (yoki **[ESP Online Flasher]**) bo'limiga o'ting, plata turini (ESP32-S3) va kamera proshivkasini (``.bin`` fayli) tanlang hamda **[Erase & write firmware]** tugmasini bosing.

PC ko'magidagi AI (MediaPipe bilan)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Kamera tasvirlarini kompyuterga (Pico Editor) uzatadi va u real vaqt rejimida qo'llarni, yuzlarni va h.k.larni kuzatish uchun Google MediaPipe kutubxonasidan foydalanadi. Aniqlangan koordinatalar apparat boshqaruvi uchun ESP32 ga qaytarib yuboriladi.

.. code-block:: python

    from espzero import vision
    from time import sleep

    # Kamera kadrlarini kompyuterga uzatishni boshlash (asinxron fon oqimi)
    vision.start_stream_to_pc()

    while True:
        # Muharrir tomonidan kiritilgan qo'l koordinatalarini o'qish
        if "__pc_ai_data" in globals():
            x = __pc_ai_data.get("hand_x", 0)
            y = __pc_ai_data.get("hand_y", 0)
            detected = __pc_ai_data.get("hand_detected", False)
            if detected:
                print("Qo'l aniqlandi -> X:", x, "Y:", y)
        sleep(0.1)

Wi-Fi orqali video uzatish va kompyuterda YOLO avtonom boshqaruvi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mikrokontroller sifatida ESP32-S3 cheklangan RAM va hisoblash quvvatiga ega bo'lib, YOLOv8 kabi og'ir zamonaviy chuqur o'rganish (deep learning) modellarini to'g'ridan-to'g'ri qurilmada ishga tushirish qiyin.
Biroq, ESP32 va kompyuter o'rtasida **Wi-Fi** orqali vazifalarni taqsimlash orqali siz yuqori samarali avtonom harakatlanuvchi robot mashinani osongina yaratishingiz mumkin.

**Ishlash printsipi va vazifalar taqsimoti**:

.. code-block:: text

    [ ESP32 Robot Mashina ] (Ko'zlar va Oyoqlar roli)
      - Wi-Fi orqali kamera videosini simsiz uzatadi (MJPEG oqimi)
      - Kompyuterdan qabul qilingan simsiz buyruqlar ('GO' / 'STOP') asosida motorlarni harakatga keltiradi
      ▲
      │  (Wi-Fi tarmog'i: Real vaqtda video uzatish & Haydash buyruqlari)
      ▼
    [ Kompyuter / Mu Muharriri - Python 3 rejimi ] (Miya roli)
      - Wi-Fi video oqimini qabul qiladi va kompyuterning yuqori quvvatli CPU/GPU sida YOLOv8 ni ishlatadi
      - Odam/to'siq aniqlanganda darhol 'STOP', yo'l ochiq bo'lsa 'GO' buyrug'ini yuboradi

**Mu Muharririda Bosqichma-bosqich Amaliy Qo'llanma**:

1. **Kompyuterda YOLO muhitini tayyorlash**:
   Kompyuteringizda YOLOv8 ni ishga tushirish uchun kerakli paketlarni o'rnating:
   * **A usuli (Mu sozlamalarida)**: Mu pastki o'ng burchagidagi **Sozlamalar (tishli g'ildirak)** tugmasini bosing → **[Third-party Packages (Uchinchi tomon paketlari)]** bo'limiga o'ting, ``ultralytics`` deb yozing va [OK] tugmasini bosing.
   * **B usuli (Terminalda)**: CMD yoki PowerShell da ``pip install ultralytics opencv-python requests`` buyrug'ini bajaring.

2. **1-bosqich: ESP32 Robot kodini yuklash (Mu [ESP32 rejimi])**:
   Mu muharririning rejimini **ESP32 rejimi**ga o'tkazing va quyidagi kodni yozib, plataga ``main.py`` nomi bilan saqlang.
   (``main.py`` qilib saqlanganda, USB kabelni uzib, faqat batareya ulaganingizda ham plata o'z-o'zidan Wi-Fi ga ulanadi va simsiz video uzatishni boshlaydi. REPL da chiqqan ESP32 IP manzilini (masalan, ``192.168.0.50``) eslab qoling.)

.. code-block:: python

    from espzero import WiFi, vision, Robot
    from time import sleep

    # 1. Wi-Fi ga ulanish
    wifi = WiFi()
    wifi.connect("Mening_WiFi_Nomi", "parol1234")

    # 2. 2 g'ildirakli robot motorini sozlash (Chap: GPIO 4, 5 / O'ng: GPIO 6, 7)
    car = Robot(left=(4, 5), right=(6, 7))

    # 3. Simsiz kamera oqimini boshlash (standart port: 8080)
    vision.start_wifi_stream(port=8080)

    # 4. Kompyuter AI qarorlarini qabul qilish va boshqarish davri
    while True:
        if "__pc_ai_data" in globals():
            action = __pc_ai_data.get("action", "STOP")
            if action == "GO":
                car.forward(0.6) # Yo'l bo'sh bo'lsa oldinga harakatlanish
            else:
                car.stop()       # Odam yoki to'siq aniqlanganda to'xtash
        sleep(0.05)

3. **2-bosqich: Kompyuter AI Avtonom Boshqaruvchisini ishga tushirish (Mu [Python 3 rejimi])**:
   Mu muharririning yuqori chap burchagidagi **[Rejim (Mode)]** tugmasini bosib **Python 3 rejimi**ga o'ting.
   Yangi oynada quyidagi skriptni yozing, yuqorida olingan ESP32 IP manzilini ``STREAM_URL`` va ``CMD_URL`` ga kiriting hamda **[Boshlash (Play)]** tugmasini bosing.
   Kompyuteringizda real vaqtda aniqlangan obyektlar ramka bilan ko'rsatilgan video oyna ochiladi va robot mashina avtonom harakatni boshlaydi.

.. code-block:: python

    import cv2
    import requests
    from ultralytics import YOLO

    # Yengil YOLOv8 modelini yuklash va ESP32 oqim manzilini belgilash
    model = YOLO("yolov8n.pt")
    STREAM_URL = "http://192.168.0.50:8080/"  # ESP32 IP manzili
    CMD_URL = "http://192.168.0.50:8080/ai"

    cap = cv2.VideoCapture(STREAM_URL)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Real vaqtda obyektni aniqlash (0: Odam, 9: Svetofor)
        results = model(frame, verbose=False)
        person_detected = False

        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                if cls_id == 0: # Odam aniqlandi
                    person_detected = True

        # Buyruq yuborish (STOP yoki GO)
        cmd = "STOP" if person_detected else "GO"
        try:
            requests.get(f"{CMD_URL}?action={cmd}", timeout=0.1)
        except Exception:
            pass

        # Natijani ekranda ko'rsatish
        annotated = results[0].plot()
        cv2.imshow("ESP32-S3 YOLO AI Auto-Driving", annotated)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

.. tip::
    **Batareyada mustaqil ishlash va ochiq havoda Hotspot (AP rejimi) bo'yicha maslahatlar**

    * **Kompyutersiz batareyada to'liq simsiz ishlash (main.py sifatida saqlash)**:
      Aqlli mashina, robot yoki kuzatuv kamerasi loyihasini yakunlab, kompyutersiz mustaqil ishlatish uchun kodni ESP32 xotirasiga ``main.py`` nomi bilan saqlang. Shundan so'ng, USB kabelni uzib, faqat batareya ulashingiz kifoya: plata yoqilishi bilanoq avtomatik Wi-Fi ga ulanadi va video uzatish serverini ishga tushiradi.
      Kompyuter yoki smartfoningizdan Mu muharriri kamera oynasidagi Wi-Fi maydoniga (``http://192.168.x.x:8080/``) yoki brauzerga plata IP manzilini kiritib, jonli efirni ko'rishingiz va robotni simsiz boshqarishingiz mumkin.

    * **Wi-Fi router bo'lmagan ochiq havoda yoki sinfda Hotspot (AP rejimi) orqali ishlash**:
      Atrofda Wi-Fi router bo'lmasa ham muammo yo'q! ESP32 ning o'zini simsiz Wi-Fi nuqtasi (Access Point) sifatida yoqib, tashqi internetsiz smartfon yoki noutbuk bilan to'g'ridan-to'g'ri 1:1 bog'lanish mumkin:

      .. code-block:: python

          import network
          from espzero import vision

          # 1. ESP32 ni mustaqil Wi-Fi kirish nuqtasi (AP) sifatida yoqish
          ap = network.WLAN(network.AP_IF)
          ap.active(True)
          ap.config(essid="ESP32-CAM-ROBOT", authmode=network.AUTH_OPEN)

          # 2. Hotspot tarmog'ida video uzatishni boshlash (Standart IP: http://192.168.4.1:8080/)
          vision.start_wifi_stream(port=8080)

      Noutbuk yoki telefoningizdan ``ESP32-CAM-ROBOT`` Wi-Fi tarmog'iga ulaning va brauzer yoki kompyuter dasturida ``http://192.168.4.1:8080/`` manziliga kirib, istalgan joyda simsiz video va AI boshqaruvidan foydalaning.

Qurilmadagi AI (On-Device TFLite)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mahalliy AI xulosalarini chiqarish uchun bevosita ESP32 fayl tizimidan `.tflite` model faylini yuklaydi. U har qanday kompyuterga ulanmasdan ham mustaqil ishlashi mumkin.

.. note::
    ESP32 va mikrokontrollerlar uchun mo'ljallangan ixcham `.tflite` model fayllarini Kaggle Models (https://www.kaggle.com/models?framework=liteRT), Hugging Face LiteRT Community (https://huggingface.co/litert-community) yoki rasmiy TensorFlow Lite Micro repozitoriysidan (https://github.com/tensorflow/tflite-micro) to'g'ridan-to'g'ri yuklab olishingiz mumkin.

.. code-block:: python

    import camera
    import tflite
    from time import sleep

    # Kamerani ishga tushirish va TFLite modelini yuklash
    camera.init(framesize=camera.FRAME_QVGA)
    model = tflite.load("model.tflite")

    while True:
        img = camera.capture()
        if img:
            # Xulosa chiqarish va sinf natijasini olish
            result = model.detect(img)
            print("Aniqlangan sinf ID:", result.class_id)
        sleep(0.5)

