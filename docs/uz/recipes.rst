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

    # Rang nomlari qator sifatida ham qo'llab-quvvatlanadi (red, green, blue, yellow, cyan, magenta, purple, white, black, orange)
    rgb.color = "cyan"
    sleep(0.5)
    rgb.color = "orange"
    sleep(0.5)

    # Alohida kanal yorqinligini boshqarish (0~255)
    rgb.red = 128
    rgb.blue = 255

    # Rangni teskari aylantirish (invert) va holatni almashtirish (toggle)
    rgb.invert()
    rgb.toggle()

    # Avtomatik animatsiyalar (miltillash, ravon pulsatsiya, kamalak aylanishi — rang nomlari ham ishlaydi)
    rgb.blink(on_times=0.5, colors=("red", "cyan", "orange"), n=2, wait=True)
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

.. image:: /images/circuit_buzzer.svg
    :alt: ESP32-S3 Buzzer sxemasi
    :align: center

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

I2S Raqamli Dinamik (I2SSpeaker)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``I2SSpeaker`` apparat ``I2S(1)`` (TX rejimi) orqali 3.3V/5V I2S audio kuchaytirgich modulini (masalan, ``MAX98357A``) boshqarib, WAV/PCM ovoz va tovushlarni yuqori sifatda ijro etadi. ESP32-S3 platasida u ``I2SMic`` (``I2S(0)``) va OV2640 kamerasi bilan to'qnashmasligi uchun xavfsiz pinlarni (``BCLK=38, LRC=39, DIN=40``) avtomatik biriktiradi.

.. image:: /images/circuit_i2s_speaker.svg
    :alt: ESP32-S3 I2S raqamli dinamik (MAX98357A) ulanish sxemasi
    :align: center

.. code-block:: python

    from espzero import I2SSpeaker

    # ESP32-S3 standart pinlari: BCLK=38, LRC=39, DIN=40 (I2S 1 TX)
    spk = I2SSpeaker(sample_rate=24000)

    # WAV faylni ijro etish (44 baytli sarlavhani avtomatik o'tkazadi) yoki play_pcm()
    spk.play_wav("hello.wav")
    spk.close()

Mikrofon (I2S Microphone)
--------------------------

ESP32-S3 ning tezkor hisoblash quvvati va I2S apparat interfeysidan foydalanib, 24-bitli raqamli MEMS mikrofonlaridan (masalan, INMP441) to'g'ridan-to'g'ri toza ovozni yozib olish va real vaqtda audio signallarni tahlil qilish mumkin.

I2S mikrofonni ulash (INMP441, 3.3V)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``INMP441`` moduli 3.3V quvvat va raqamli I2S shinasi (SCK, WS, SD) orqali ishlaydi, shuning uchun oddiy analog mikrofonlarga qaraganda shovqindan xoli yuqori sifatli ovozni ta'minlaydi.
Uni daraja o'zgartirgichsiz (level shifter) to'g'ridan-to'g'ri ESP32-S3 WROOM CAM platasining xavfsiz standart pinlariga (``SCK=41``, ``WS=42``, ``SD=2``) 3.3V signallari bilan ulash mumkin.
(Yagona mono mikrofon sifatida ishlatish uchun ``L/R`` pinini ``GND`` ga ulab chap kanalni tanlang.)

.. image:: /images/circuit_inmp441_mic.svg
    :alt: ESP32-S3 I2S raqamli mikrofon (INMP441) ulanish sxemasi
    :align: center

Asosiy foydalanish va tovushni aniqlash (I2SMic)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Plata profilidagi standart pinlar avtomatik biriktiriladi. Joriy ovoz balandligi (``level``, ``0.0 ~ 1.0``), detsibellari (``decibels``), asosiy musiqa notasi (``note``) va qarsak urish hodisalari (``when_clap``) oson boshqariladi.

.. code-block:: python

    from espzero import I2SMic, esp_led
    from time import sleep

    # Standart I2S pinlarini avtomatik biriktirish (ESP32-S3: SCK=41, WS=42, SD=2)
    mic = I2SMic()

    # Qarsak yoki kuchli ovoz eshitilganda platadagi LED holatini o'zgartirish
    mic.when_clap = esp_led.toggle

    while True:
        print("Ovoz kuchi:", round(mic.level, 3), "| dB:", int(mic.decibels), "| Nota:", mic.note or "---")
        sleep(0.2)

Real vaqtda OLED audio spektr analizatori (FFT Spectrum)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``mic.spectrum(bins=16)`` orqali 16 diapazonli chastota energiyasini ajratib olib, OLED displeyida real vaqtda ekvalayzer ustunlarini (``oled.show_spectrum()``) chizish va ritmga moslab RGB LEDni miltillatish mumkin.

.. literalinclude:: examples/audio_spectrum_oled.py
      :start-at: from espzero import

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

    pot = Pot(1) # Analog pin (ADC1_CH0, ESP32-S3)

    print("Joriy qiymat (0-1):", pot.value)
    print("Kuchlanish (V):", pot.voltage)

O'rnatilgan sensorli tugma (Capacitive Touch)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ESP32 va ESP32-S3 chiplariga o'rnatilgan sig'imli sensorli periferiyadan foydalanadi. Tashqi rezistorlarsiz barmog'ingiz bilan teginishni aniqlaydi. (``InternalTouchSensor`` taxallusi orqali ham foydalanish mumkin.)

.. note::
    **Tashqi ``TouchSensor`` modulidan farqi**:
    Agar TTP223 kabi tashqi raqamli sensor modulini ulasangiz, ``picozero-rw`` bilan mos keluvchi ``TouchSensor(pin)`` klassidan foydalaning. ``CapTouch`` (``InternalTouchSensor``) esa tashqi modulsiz to'g'ridan-to'g'ri ESP32 chipining ichki sensor pinlari uchun mo'ljallangan.

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

Ichki harorat sensori (Internal Temperature Sensor)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ESP32 chipining ichki haroratini o'lchang. (Eslatma: Atrof-muhit haroratidan farq qilishi mumkin).

.. code-block:: python

    from espzero import esp_temp_sensor

    print("Chip ichki harorati:", esp_temp_sensor.temp, "C")

Masofa sensori (Distance Sensor)
--------------------------------

``HC-SR04P`` (3.3V–5V) kabi ultratovushli sensor yordamida ESP32-S3 bilan masofani xavfsiz o'lchang.

.. image:: /images/circuit_distance.svg
    :alt: ESP32-S3 HC-SR04P Masofa sensori sxemasi
    :align: center

.. warning::
    **Eski 5V faqat HC-SR04 sensorlarida kuchlanish oshishi xavfi (ECHO pin)**:
    ESP32-S3 GPIO pinlarining maksimal kirish kuchlanishi **3.6V** dir. Yangi **HC-SR04P** / **HC-SR04+** modellari platadagi **3V3** piniga ulanib, xavfsiz 3.3V mantiqiy signal bilan ishlaydi.
    Agar faqat 5V da ishlaydigan **eski HC-SR04** sensoridan foydalansangiz, uning ``ECHO`` chiqishi **5V** bo'ladi va ``G14`` pinini shikastlashi mumkin. Shu sababli ``ECHO`` signalini ~3.3V ga tushirish uchun **1kΩ + 2kΩ rezistorli kuchlanish bo'luvchi (Voltage Divider)** (``ECHO → 1kΩ → G14``, ``G14 → 2kΩ → GND``) ulashingiz shart.

.. code-block:: python

    from espzero import DistanceSensor

    # echo=14, trigger=13
    ds = DistanceSensor(echo=14, trigger=13)

    while True:
        print("Masofa: ", ds.distance, "cm")
        sleep(0.5)

DC Motorlar va Robotlar (DC Motor & Robot)
------------------------------------------

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

    # left=(oldinga_pin, orqaga_pin), right=(oldinga_pin, orqaga_pin) — kamera bilan to'qnashmaydigan xavfsiz pinlar
    robot = Robot(left=(41, 42), right=(47, 21))

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

Servo motor (Servo)
-------------------

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

Stepper motor (Stepper Motor)
-----------------------------

ULN2003 drayver platasi va 28BYJ-48 stepper motorini ulab, aniq burchak yoki aylanishlar soni bo'yicha boshqaring.

.. image:: /images/circuit_stepper.svg
    :alt: ESP32-S3 ULN2003 28BYJ-48 Stepper motor ulanish sxemasi
    :align: center

.. code-block:: python

    from espzero import Stepper
    from time import sleep

    # 4 ta kamera uchun xavfsiz GPIO pinlari (IN1=42, IN2=41, IN3=47, IN4=21)
    stepper = Stepper((42, 41, 47, 21))
    stepper.set_speed(10)          # Aylanish tezligini 10 RPM ga sozlash

    stepper.turn(90, "cw")         # Soat strelkasi bo'yicha 90 daraja burish
    sleep(0.5)
    stepper.rotate(1, "ccw")       # Soat strelkasiga qarshi 1 marta to'liq aylantirish
    stepper.off()                  # Qizib ketmasligi uchun g'altaklarni o'chirish

Displeylar (OLED & LCD)
-----------------------

I2C OLED Displey (SSD1306 / SH1106, 3.3V Tavsiya etiladi)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

0.96 dyuymli (``SSD1306``) yoki 1.3 dyuymli (``SH1106``) I2C OLED displeylar tabiiy ravishda 3.3V kuchlanish va I2C signalida ishlaydi, shu bois daraja o'zgartirgichsiz to'g'ridan-to'g'ri ESP32-S3 ga xavfsiz ulanadi.

.. image:: /images/circuit_oled.svg
    :alt: ESP32-S3 I2C OLED Displey sxemasi
    :align: center

.. code-block:: python

    from espzero import OLED

    # 0.96" SSD1306 (1.3" SH1106 ekranlar uchun driver="sh1106" kiriting)
    oled = OLED(scl=47, sda=21)

    oled.clear()
    oled.text("Hello, ESPZero!", 0, 0)
    oled.text("ESP32-S3 OLED", 0, 20)
    oled.rect(0, 36, 128, 20, color=1)
    oled.show()

Robot yuzi his-tuyg'ulari va nigohni boshqarish (Robot Face & Gaze)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``oled.show_face()`` 10 xil robot his-tuyg'usi oldindan sozlangan holatlarini taqdim etadi (``"normal"``, ``"happy"``, ``"surprised"``, ``"love"``, ``"thinking"``, ``"sleep"``, ``"blink"``, ``"angry"``, ``"sad"``, ``"listening"``) va qorachiqlar yo'nalishini (``look_x``, ``look_y``) sozlash imkonini beradi.
Shuningdek, ``oled.look_at(x, y)`` yordamida kamera qo'l koordinatalarini to'g'ridan-to'g'ri uzatib, robot ko'zlarini real vaqtda harakatga qaratish mumkin.

.. image:: ../images/oled_robot_faces.svg
    :alt: ESPZero OLED Robot Yuzi Diagrammasi
    :align: center

.. code-block:: python

    from espzero import OLED
    from time import sleep

    oled = OLED(scl=47, sda=21)

    # 1. His-tuyg'ularni o'zgartirish
    oled.show_face("happy")      # Xursand yuz (^ ^)
    sleep(1)
    oled.show_face("surprised")  # Hayratlangan yuz (O O)
    sleep(1)
    oled.show_face("love")       # Yurak shaklidagi ko'zlar
    sleep(1)

    # 2. Nigohni boshqarish: Chapga (-1.0) / O'ngga (1.0) / Yuqoriga / Pastga
    oled.show_face("normal", look_x=-1.0, look_y=0.0)  # Chapga qarash
    sleep(1)
    oled.show_face("normal", look_x=1.0, look_y=0.0)   # O'ngga qarash
    sleep(1)

    # 3. vision.get_hand() koordinatalari bilan nigohni kuzatish (interaktiv robot)
    # oled.look_at(hand_x, hand_y, emotion="happy")

LCD Displey (16x2, PCF8574)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

I2C shinasidan va PCF8574 I2C adapteridan foydalanib LiquidCrystal displeylarida (LCD) belgilarni chop etish.

.. warning::
    **5V PCF8574 I2C adapterlari uchun daraja o'zgartirgich (Level Shifter) zarur**:
    Aksariyat ``16x2 I2C LCD (PCF8574)`` modullari 5V da ishlaydi va ``SDA`` / ``SCL`` liniyalarini **5V** ga tortadi (pull-up).
    ESP32-S3 ning 3.3V pinlarini (``G21``, ``G47``) himoya qilish uchun plata va PCF8574 moduli orasiga **3.3V↔5V ikki yo'nalishli I2C mantiqiy daraja o'zgartirgich (Logic Level Shifter)** ulashingiz shart (yoki yuqoridagi **3.3V OLED displeydan** foydalaning).

.. image:: /images/circuit_i2c_lcd.svg
    :alt: ESP32-S3 I2C LCD va mantiqiy daraja o'zgartirgich sxemasi
    :align: center

.. literalinclude:: examples/i2c_lcd.py

Faqat GPIO pinlari yordamida LiquidCrystal displeylarida (LCD) belgilarni chop etish.

.. literalinclude:: examples/lcd.py


Kamera (Camera)
---------------

ESP32-S3 WROOM CAM kabi kamerali platalarda kompyuter yoki AI serversiz mustaqil ravishda suratga olish va flash xotiraga saqlash misollari.

.. important::
    **Kamerani qo'llab-quvvatlovchi proshivka zarur**:
    Rasmiy standart MicroPython proshivkasida xotira cheklovlari tufayli kamera drayveri (``camera`` moduli) mavjud emas.
    Kamera va vizual funksiyalardan foydalanish uchun platangizga (ESP32-S3 WROOM CAM) **Kamera drayveri bilan yig'ilgan MicroPython proshivkasi (Camera-enabled Firmware)** o'rnatilgan bo'lishi kerak.

.. note::
    **Mu Muharririda o'rnatilgan proshivka qilish yo'riqnomasi (Onlayn / Oflayn qo'llab-quvvatlanadi)**:

    Qo'shimcha murakkab dasturlarni (masalan, esptool) o'rnatish shart emas. Mu muharririning pastki o'ng burchagidagi **Sozlamalar (tishli g'ildirak)** bo'limida quyidagi ikki usuldan biri orqali kamerani qo'llab-quvvatlovchi proshivkani plataga osongina o'rnatishingiz mumkin:

    * **Onlayn proshivka qilish ([ESP Online Flasher] bo'limi)**:
      Kompyuteringiz internetga ulangan bo'lsa, proshivka faylini oldindan yuklab olish shart emas.
      Plata turlari ro'yxatidan standart (Generic) emas, balki **kamera va PSRAM drayverlari kiritilgan variantni** (masalan, ``ESP32-S3 Camera (OV2640 / Octal SPIRAM)``) tanlang. So'ngra **[Versiyalarni olish] → [O'chirish va yozish]** tugmasini bosing — kamera drayveri kiritilgan eng so'nggi rasmiy MicroPython proshivkasi bulutdan avtomatik yuklab olinib, darhol plataga yoziladi.

    * **Oflayn proshivka qilish ([ESP Firmware flasher] bo'limi)**:
      Internet bo'lmaganda yoki kompyuteringizda oldindan tayyorlab qo'yilgan ma'lum bir versiyadagi kamera proshivkasi (``.bin`` fayli) mavjud bo'lganda ishlatiladi. Plata turini (``ESP32-S3``) tanlang, kompyuteringizdagi faylni ko'rsating va **[O'chirish va yozish]** tugmasini bosing.

Suratga olish va saqlash (``vision.save_photo`` / ``vision.capture``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``vision.save_photo()`` funksiyasi yangi (``camera.Camera``) va eski (``camera.init``) proshivkalarni avtomatik aniqlab, bir qator kod bilan JPEG surat oladi va plata xotirasiga saqlaydi. Telegram yoki bulutli AI uchun xom JPEG baytlari kerak bo'lganda yoki fon oqimi (``start_wifi_stream()``) davomida oxirgi kadrni xavfsiz olish uchun ``vision.capture()`` dan foydalaning. Ishni tugatgach ``vision.close()`` orqali kamera resurslarini xavfsiz bo'shating.

.. code-block:: python

    from espzero import vision

    # 1. 1 ta surat olib flash xotiraga saqlash (o'lchamlar: QQVGA, HQVGA, QVGA, VGA)
    saved = vision.save_photo("snapshot.jpg", framesize="QVGA", quality=80)
    print("Saqlandi:", saved)

    # 2. Xom JPEG baytlarini to'g'ridan-to'g'ri olish (tarmoq/bulutli AI uchun)
    jpg_bytes = vision.capture(framesize="QVGA", quality=70)
    print("Rasm hajmi:", len(jpg_bytes), "bayt")

    # Ishlatib bo'lgach kamerani yopish
    vision.close()

Taymlaps va AI o'qitish uchun rasm to'plash
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ma'lum vaqt oralig'ida bir nechta suratlarni avtomatik saqlab, taymlaps yaratish yoki Edge Impulse kabi TinyML modellari uchun rasm to'plamini yig'ish mumkin.

.. code-block:: python

    from espzero import vision, esp_led
    from time import sleep

    for i in range(1, 6):
        esp_led.color = (0, 255, 0)
        esp_led.on()
        path = vision.save_photo(f"photo_{i:03d}.jpg", framesize="QVGA")
        esp_led.off()
        print("Suratga olindi:", path)
        sleep(2)

    vision.close()


AI vizualizatsiyasi (AI vision)
-------------------------------

ESP32-S3 kamerasini kompyuter ko'magidagi AI (MediaPipe, YOLOv8) va mustaqil qurilmadagi TinyML modellari bilan birlashtirish misollari. (Yuqoridagi **Kamera (Camera)** bo'limida ko'rsatilgan kamera proshivkasi o'rnatilgan bo'lishi kerak.)
PC ko'magidagi AI (MediaPipe bilan — Faqat Mu Muharriri)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
    **Faqat Mu Muharriri serial protokoli**: ``vision.start_stream_to_pc()`` USB serial orqali Mu muharririning ichki Kamera/MediaPipe ko'ruvchisi bilan bevosita ishlaydi. VS Code, Thonny kabi boshqa muharrirlarda quyidagi **Wi-Fi orqali video uzatish (``vision.start_wifi_stream()``)** usulidan foydalaning.

Kamera tasvirlarini kompyuterga (Mu Muharriri) uzatadi va u real vaqt rejimida qo'llarni, yuzlarni va h.k.larni kuzatish uchun Google MediaPipe kutubxonasidan foydalanadi. Aniqlangan koordinatalar apparat boshqaruvi uchun ESP32 ga qaytarib yuboriladi.

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

**Bosqichma-bosqich Amaliy Qo'llanma (Mu Muharriri / Standart Python IDElar)**:

1. **Kompyuterda YOLO muhitini tayyorlash**:
   Kompyuteringizda YOLOv8 ni ishga tushirish uchun paketlarni tayyorlang.

   * **A usuli (Mu muharriri muhitida)**:
     Mu muharririda ``opencv-python`` va ``requests`` paketlari allaqachon mavjud. Faqatgina **Sozlamalar (tishli g'ildirak) → [Third-party Packages]** bo'limiga o'tib, ``ultralytics`` deb yozing va [OK] bosing.

   * **B usuli (VS Code va boshqa tashqi muharrirlarda)**:
     Mu dan tashqari standart Python muhitida ishlatayotgan bo'lsangiz, CMD yoki PowerShell da quyidagi buyruqni bajaring:

     .. code-block:: bash

         pip install ultralytics opencv-python requests

2. **1-bosqich: ESP32 Robot kodini yuklash (Mu [ESP32 rejimi] yoki Thonny / mpremote)**:
   Quyidagi kodni plataga ``main.py`` nomi bilan saqlang (Mu da **ESP32 rejimi**, terminalda ``mpremote cp main.py :main.py``).
   (``main.py`` qilib saqlanganda, USB kabelni uzib, faqat batareya ulaganingizda ham plata o'z-o'zidan Wi-Fi ga ulanadi va simsiz video uzatishni boshlaydi. REPL da chiqqan ESP32 IP manzilini (masalan, ``192.168.0.50``) eslab qoling.)

   .. literalinclude:: examples/vision_yolo_car_esp32.py
      :start-at: from espzero import

3. **2-bosqich: Kompyuter AI Avtonom Boshqaruvchisini ishga tushirish (Mu [Python 3 rejimi] yoki standart Python)**:
   Mu muharririda **Python 3 rejimi**\ da ishga tushiring, yoki VS Code / terminalda ``yolo_drive.py`` fayliga saqlab ``python yolo_drive.py`` buyrug'i bilan bajaring (avval ``STREAM_URL`` va ``CMD_URL`` ga ESP32 IP manzilini kiriting).
   Kompyuteringizda real vaqtda aniqlangan obyektlar ramka bilan ko'rsatilgan video oyna ochiladi va robot mashina avtonom harakatni boshlaydi.

   .. literalinclude:: examples/vision_yolo_car_pc.py
      :start-at: import cv2

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

Mahalliy AI xulosalarini chiqarish uchun bevosita ESP32 fayl tizimidan ``.tflite`` model faylini yuklaydi. U har qanday kompyuterga ulanmasdan ham mustaqil ishlashi mumkin.

.. note::
    ESP32 va mikrokontrollerlar uchun mo'ljallangan ixcham ``.tflite`` model fayllarini Kaggle Models (https://www.kaggle.com/models?framework=liteRT), Hugging Face LiteRT Community (https://huggingface.co/litert-community) yoki rasmiy TensorFlow Lite Micro repozitoriysidan (https://github.com/tensorflow/tflite-micro) to'g'ridan-to'g'ri yuklab olishingiz mumkin.

.. code-block:: python

    from espzero import vision
    import tflite
    from time import sleep

    # TFLite modelini yuklash
    model = tflite.load("model.tflite")

    while True:
        img = vision.capture(framesize="QVGA")
        if img:
            # Xulosa chiqarish va sinf natijasini olish
            result = model.detect(img)
            print("Aniqlangan sinf ID:", result.class_id)
        sleep(0.5)


AI ovoz (AI voice)
------------------

ESP32 platasiga alohida I2S mikrofon qo'shmasdan ham, **kompyuter yoki noutbukning yuqori sifatli ichki mikrofonidan** foydalanib Wi-Fi orqali ESP32 avtomobil va robotini ovoz bilan boshqarish mumkin.

Kompyuter mikrofoni orqali ovoz bilan boshqariladigan aqlli avtomobil
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Bu usul simlarni ulashni minimal darajaga tushiradi va shovqinli xonalarda ham aniq ovoz tanishni ta'minlaydi.

**Ishlash prinsipi va vazifalar taqsimoti**:

.. code-block:: text

    [ Foydalanuvchi ]
      🗣️ "Oldinga!" / "To'xta!" / "Aylan!"
      │
      ▼ (Kompyuter / Noutbuk ichki mikrofonida yozib olinadi)
    [ Mu Muharriri (Kompyuter) - Python 3 Rejimi ] (Quloq va Aql)
      - Kompyuter mikrofonidan ovoz oladi va ichki SpeechRecognition yordamida tahlil qiladi
      - Wi-Fi HTTP so'rovi orqali buyruqlarni yuboradi:
        requests.get("http://<ESP32_IP>:8080/ai?action=GO")
      ▲
      │  (Wi-Fi tarmog'i: Matnli buyruqlarni uzatish)
      ▼
    [ ESP32 Robot Avtomobili ] (Tana, Mikrofon/OLED keraksiz!)
      - Qabul qilingan action ("GO") buyrug'ini darhol bajaradi
      - Motorlarni harakatga keltiradi va platadagi LED orqali holatni bildiradi

**Bosqichma-bosqich qo'llanma (Mu Muharriri / Standart Python IDElar)**:

1. **Kompyuterda ovoz tanish muhitini tayyorlash**:
   Ovozni aniqlash va ESP32 ga buyruq yuborish muhitini tayyorlang.

   * **A usuli (Mu muharriri muhitida)**:
     Mu muharririda ``SpeechRecognition`` va ``requests`` paketlari allaqachon mavjud, shu sababli **hech qanday qo'shimcha o'rnatishlarsiz to'g'ridan-to'g'ri ishga tushirish mumkin**.

   * **B usuli (VS Code va boshqa tashqi muharrirlarda)**:
     Standart Python muhitida ishlatayotgan bo'lsangiz, CMD yoki PowerShell da quyidagi buyruqni bajaring:

     .. code-block:: bash

         pip install SpeechRecognition requests PyAudio

2. **1-qadam: ESP32 Robot Avtomobili kodini yuklash (Mu [ESP32 Rejimi] yoki Thonny / mpremote)**:

   .. literalinclude:: examples/voice_control_car_esp32.py
      :start-at: from espzero import

3. **2-qadam: Kompyuter Ovozli Boshqaruv skriptini ishga tushirish (Mu [Python 3 Rejimi] yoki standart Python)**:

   .. literalinclude:: examples/voice_control_car_pc.py
      :start-at: import requests

Simsiz Wi-Fi audio uzatish va ovozli robot boshqaruvi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ESP32-S3 ning I2S mikrofoni orqali yozib olingan audio Wi-Fi orqali real vaqtda 16-bitli WAV strimi (standart port ``8081``) sifatida kompyuterga yuboriladi.
Kompyuterda (Python 3 rejimida) Whisper, SpeechRecognition yoki Edge Impulse modellari orqali ovozli buyruqlar tahlil qilinadi va ``/ai?action=...`` oxirgi nuqtasiga yuborilib robot harakati hamda OLED yuz ifodalari simsiz boshqariladi.

**Ishlash prinsipi va vazifalar taqsimoti**:

.. code-block:: text

    [ ESP32-S3 Platasi ] (Quloq va Tana)
      - I2S mikrofon audiosini Wi-Fi (HTTP WAV strimi, 8081-port) orqali uzatadi
      - Qabul qilingan ovozli buyruqlar ('GO' / 'STOP' / 'DANCE') asosida robot va OLED yuzini boshqaradi
      ▲
      │  (Wi-Fi tarmog'i: Real vaqtda audio strim va buyruqlar almashinuvi)
      ▼
    [ Kompyuter Mu Muharriri - Python 3 Rejimi ] (Ovozli AI Aqli)
      - http://<ESP32_IP>:8081/ manzilidan audio o'qib ovozli buyruqlarni taniydi
      - Aniqlangan buyruqlarni http://<ESP32_IP>:8081/ai?action=GO ga yuboradi

1. **ESP32-S3 Ovozli AI robot kodini yuklash (Mu [ESP32 Rejimi])**:

   .. literalinclude:: examples/audio_wifi_ai_robot_esp32.py
      :start-at: from espzero import

2. **Kompyuter Ovoz Boshqaruvchisini ishga tushirish (Mu [Python 3 Rejimi])**:
   ESP32 audio strimiga ulanib, real vaqtda ovozli buyruqlarni taniydi va robotga yo'naltiradi:

   .. literalinclude:: examples/audio_wifi_ai_robot_pc.py
      :start-at: import io

Qurilmaning o'zida mustaqil TinyML ovoz tasnifi (Edge Impulse & MFCC)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Kompyutersiz, to'g'ridan-to'g'ri ESP32-S3 ning o'zida kalit so'zlarni tanish (KWS) yoki nostandart tovushlarni aniqlash uchun ``mic.mfcc()`` dan foydalaning:

.. note::
    **Edge Impulse va TinyML audio modelini yaratish**:
    Mikrokontrollerlar uchun maxsus ovozli kalit so'zlarni yoki nostandart tovushlarni aniqlash modellarini to'g'ridan-to'g'ri brauzerda o'rgatish va eksport qilish uchun `Edge Impulse Studio <https://www.edgeimpulse.com/>`_ (https://www.edgeimpulse.com/) hamda `Edge Impulse Audio Qo'llanmasi <https://docs.edgeimpulse.com/docs/tutorials/audio>`_ dan foydalanishingiz mumkin. Shuningdek, oldindan o'rgatilgan audio modellarini `Kaggle Models <https://www.kaggle.com/models?framework=liteRT>`_ va `LiteRT Community <https://huggingface.co/litert-community>`_ dan ham yuklab olish mumkin.

* **MFCC belgilar vektorini ajratish**: ``mic.mfcc(num_cepstra=13)`` TinyML va TensorFlow Lite Micro modellari uchun standart bo'lgan 13 o'lchamli Mel-chastotali sepsral koeffitsientlarni tezkor hisoblaydi.
* **O'rganish uchun ma'lumot to'plash**: ``mic.save_wav("sample.wav", duration=1.0)`` mikrofon ovozini to'g'ridan-to'g'ri plata xotirasiga 16-bitli WAV fayl sifatida yozib oladi, bu esa Edge Impulse uchun ma'lumotlar to'plamini yig'ishda juda qulaydir.

.. code-block:: python

    from espzero import I2SMic
    from time import sleep

    mic = I2SMic()

    # TinyML modeli uchun 13 o'lchamli MFCC belgilar vektorini olish
    features = mic.mfcc(num_cepstra=13)
    print("MFCC belgilari:", features[:5], "... (jami 13 ta)")

    # 1.0 soniyalik audio namunani xotiraga yozib olish
    mic.save_wav("cough_sample.wav", duration=1.0)
    print("WAV audio namunasi xotiraga saqlandi!")

Murakkab misollar (Combined Examples)
-------------------------------------

Bir nechta sensorlar, aktuatorlar va AI funksiyalarini birlashtirgan amaliy loyihalar. Oddiydan murakkabga qarab tartiblangan.

Tugma bilan chiroqni boshqarish (Button-Controlled Light)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tugma bosilganda LED holatini o'zgartirish.

.. code-block:: python

    from espzero import LED, Button

    led = LED(4)
    btn = Button(5)

    btn.when_pressed = led.toggle

    while True:
        pass # Hodisalarni kutish

Aqlli xavfsiz eshik qulfi (Smart Doorlock)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ichki RGB LED, servo motor (qulf mexanizmi) va zummerni birlashtirib, ruxsat berilganda yashil chiroq va signal bilan eshikni ochadigan hamda avtomatik yopadigan aqlli eshik qulfi misoli.

.. image:: /images/circuit_smart_doorlock.svg
    :alt: ESP32-S3 Aqlli eshik qulfi ulanish sxemasi
    :align: center

.. literalinclude:: examples/smart_doorlock.py

Potentiometr bilan robot nigohini boshqarish (Potentiometer Gaze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Potentiometr buragichini aylantirganda OLED robot ko'zlari chapga va o'ngga harakatlanadi, tugma bosilganda esa yurakcha (``"love"``) ifodasi paydo bo'ladi.

.. literalinclude:: examples/oled_pot_gaze.py
   :start-at: from espzero import

Analog soat (Analog Clock)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Stepper motor yordamida har 60 soniyada 1 marta to'liq aylanadigan analog soat soniya milini yarating.

.. literalinclude:: examples/stepper_analog_clock.py

Avtomatik jalyuzilar (Automatic Blinds)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Stepper motor yordamida vaqtga asoslangan avtomatik jalyuzi boshqaruvchisi.

.. literalinclude:: examples/stepper_automatic_blinds.py

Aqlli avtoturargoh ogohlantiruvchisi (Smart Parking Assist)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ultratovush sensori yordamida to'siqqacha masofani o'lchab, yaqinlashgan sari OLED robot yuz ifodasi (``happy`` → ``surprised`` → ``angry``), LED rangi va zummer signalini bosqichma-bosqich o'zgartiradi.

.. image:: /images/circuit_parking_assist.svg
    :alt: ESP32-S3 Aqlli avtoturargoh ogohlantiruvchisi sxemasi
    :align: center

.. literalinclude:: examples/smart_parking_assist.py
   :start-at: from espzero import

Qarsak bilan ochiladigan aqlli eshik (Clap Smart Door)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I2S mikrofonining qarsakni aniqlash hodisasi (``when_clap``) yordamida Wi-Fi va kompyutersiz qarsak chalinganda servo eshikni ochib-yopuvchi va OLED yuzini o'zgartiruvchi tizim.

.. literalinclude:: examples/clap_smart_door.py
   :start-at: from espzero import

To'siqlarni aylanib o'tuvchi avtonom robot (Obstacle-Avoiding Rover)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Old ultratovush sensori va 2WD robot shassisini birlashtirib, 20 sm masofada to'siq aniqlanganda mustaqil ravishda orqaga qaytib buriladigan avtonom robot.

.. image:: /images/circuit_obstacle_rover.svg
    :alt: ESP32-S3 To'siqlarni aylanib o'tuvchi avtonom robot sxemasi
    :align: center

.. literalinclude:: examples/obstacle_avoiding_rover.py
   :start-at: from espzero import

Multimodal AI hamroh robot (Vision AI + Voice AI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ESP32-S3 ning kamera videosi (``8080``-port) va I2S mikrofoni audiosini (``8081``-port) bir vaqtning o'zida kompyuterga simsiz uzatadi. Kompyuterda tasvir va ovoz parallel tahlil qilinib, OLED robot yuz ifodalari (``look_at`` / ``show_face``) va RGB LED simsiz boshqariladi.

1. **ESP32-S3 Multimodal robot kodini yuklash (Mu [ESP32 Rejimi])**:

   .. literalinclude:: examples/multimodal_companion_robot_esp32.py
      :start-at: from espzero import

2. **Kompyuter Multimodal AI boshqaruvchisini ishga tushirish (Mu [Python 3 Rejimi])**:

   .. literalinclude:: examples/multimodal_companion_robot_pc.py
      :start-at: import threading
