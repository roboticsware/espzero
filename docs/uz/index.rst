espzero: ESP32 uchun eng oson dasturlash kutubxonasi
=============================================

.. image:: https://raw.githubusercontent.com/roboticsware/espzero/main/docs/_static/logo.png
   :width: 200px
   :align: center
   :alt: espzero logotipi

**espzero** — bu ESP32 va ESP8266 mikrokontrollerlari uchun yangi boshlovchilarga mo'ljallangan apparatni boshqarish kutubxonasi. U Raspberry Pi Pico uchun mashhur bo'lgan ``picozero`` kutubxonasining soddaligini ESP32 ekotizimiga olib keladi.

Asosiy falsafa
--------------

* **Soddalik**: Registrlar yoki PWM chastotalari haqida qayg'urmasdan, ``LED.on()`` kabi bitta qator bilan boshlang.
* **Abstraksiya**: Qaysi platadan foydalanishingizdan qat'i nazar, kodingiz o'zgarishsiz qoladi. Platalar orasidagi farqlar ``espzero.begin()`` tomonidan hal qilinadi.
* **Zamonaviy**: Fon vazifalarini oson boshqarish uchun o'rnatilgan asinxron rejalashtiruvchi.

Asosiy xususiyatlar
-------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Komponent
     - Qo'llab-quvvatlanadigan xususiyatlar
   * - **Chiqish qurilmalari**
     - LED, PWM LED, RGB LED, Buzzer, Speaker (Melody), Motor
   * - **Kirish qurilmalari**
     - Button, Switch, Motion Sensor, Touch, Potentiometer
   * - **Sensorlar**
     - Distance (HC-SR04), Temperature (Internal/External)
   * - **Ulanish**
     - Oddiy WiFi ulanishi va holatni boshqarish

Ishni boshlash
--------------

1. **O'rnatish**: Mu Editor-ning paket menejeri yoki ``pip`` orqali ``espzero``-ni o'rnating.
2. **Ishga tushirish**: Skriptingizning yuqori qismida ``espzero.begin()`` funksiyasini chaqiring.

.. code-block:: python

    import espzero
    from espzero import LED
    
    espzero.begin()
    led = LED(4)
    led.pulse() # Orqa fonda silliq miltillash

Mundarija
---------

.. toctree::
   :maxdepth: 2
   :caption: Qo'llanmalar va Retseptlar

   recipes
   boards
   api

.. toctree::
   :maxdepth: 1
   :caption: Loyiha haqida

   contributing
   license

Yordam kerakmi?
---------------

* **GitHub ombori**: Savollaringizni `Issues <https://github.com/roboticsware/espzero/issues>`_ yorlig'ida qoldiring.
* **Hamjamiyat**: Loyihalaringizni baham ko'ring va blogimiz yoki forumlarimizda misollar toping.
