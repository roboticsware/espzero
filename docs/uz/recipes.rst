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

.. code-block:: python

    from espzero import Button

    btn = Button(5)

    btn.when_pressed = lambda: print("Bosildi!")
    btn.when_released = lambda: print("Qo'yib yuborildi!")

Potentiometr
~~~~~~~~~~~~

.. code-block:: python

    from espzero import Pot

    pot = Pot(34) # Analog pin (ADC)

    print("Joriy qiymat (0-1):", pot.value)
    print("Kuchlanish (V):", pot.voltage)

Servo motor (Servo)
~~~~~~~~~~~~~~~~~~~

Standart servo motorlarni nisbat (0.0 dan 1.0 gacha) yoki burchak (0 dan 180 gradusgacha) bo'yicha boshqarish (``picozero-rw`` bilan to'liq mos):

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

.. literalinclude:: examples/i2c_lcd.py

Faqat GPIO pinlari yordamida LiquidCrystal displeylarida (LCD) belgilarni chop etish.

.. literalinclude:: examples/lcd.py


AI Vision (AI vizualizatsiyasi)
-------------------------------

ESP32-S3 kamerasi yordamida kompyuter ko'magidagi AI va mustaqil ishlaydigan qurilmadagi AI misollari.

PC ko'magidagi AI (MediaPipe bilan)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Kamera tasvirlarini kompyuterga (Pico Editor) uzatadi va u real vaqt rejimida qo'llarni, yuzlarni va h.k.larni kuzatish uchun Google MediaPipe kutubxonasidan foydalanadi. Aniqlangan koordinatalar apparat boshqaruvi uchun ESP32 ga qaytarib yuboriladi.

.. code-block:: python

    from espzero import vision
    from time import sleep

    # Kamera kadrlarini kompyuterga uzatishni boshlash
    vision.start_stream_to_pc()

    while True:
        # Muharrir tomonidan kiritilgan qo'l koordinatalarini o'qish
        if "__pc_ai_data" in globals():
            x = __pc_ai_data.get("hand_x", 0)
            y = __pc_ai_data.get("hand_y", 0)
            print("Qo'l holati -> X:", x, "Y:", y)
        sleep(0.1)

Qurilmadagi AI (On-Device TFLite)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mahalliy AI xulosalarini chiqarish uchun bevosita ESP32 fayl tizimidan `.tflite` model faylini yuklaydi. U har qanday kompyuterga ulanmasdan ham mustaqil ishlashi mumkin.

.. note::
    Siz namunaviy `.tflite` model fayllarini Google TensorFlow Lite rasmiy modellar repozitoriysidan (https://www.tensorflow.org/lite/guide/hosted_models) yuklab olishingiz mumkin.

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

