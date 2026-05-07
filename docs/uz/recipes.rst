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

Turli xil ranglarni yaratish uchun Qizil, Yashil va Moviy pinlarni birlashtiring.

.. code-block:: python

    from espzero import RGBLED

    rgb = RGBLED(red=25, green=26, blue=27)

    rgb.color = (255, 0, 0)   # Qizil
    rgb.color = (0, 255, 0)   # Yashil
    rgb.color = (255, 255, 0) # Sariq (Qizil + Yashil)
    rgb.off()

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

