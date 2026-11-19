espzero: ESP32 uchun eng oson dasturlash kutubxonasi
=====================================================

|pypibadge| |docsbadge|

.. image:: /images/logo.png
   :width: 200px
   :align: center
   :alt: espzero logotipi

**espzero** — bu ESP32 va ESP8266 mikrokontrollerlari uchun yangi boshlovchilarga mo'ljallangan apparatni boshqarish kutubxonasi. U Raspberry Pi Pico uchun mashhur bo'lgan `picozero <https://picozero-rw.readthedocs.io/>`_ kutubxonasining soddaligini ESP32 ekotizimiga olib keladi.

Asosiy falsafa
--------------

* **Soddalik**: Registrlar yoki PWM chastotalari haqida qayg'urmasdan, ``LED.on()`` kabi bitta qator bilan boshlang.
* **Abstraksiya**: Qaysi platadan foydalanishingizdan qat'i nazar, kodingiz o'zgarishsiz qoladi. Platalar orasidagi farqlar kutubxona tomonidan avtomatik aniqlanadi.
* **Zamonaviy**: Fon vazifalarini oson boshqarish uchun o'rnatilgan asinxron rejalashtiruvchi.

Asosiy xususiyatlar
-------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Komponent
     - Qo'llab-quvvatlanadigan xususiyatlar
   * - **Chiqish qurilmalari**
     - LED, PWM LED, RGB LED, Buzzer, Speaker (Melody), Motor, OLED (SSD1306/SH1106), LCD (PCF8574/GPIO)
   * - **Kirish qurilmalari**
     - Button, Switch, Motion Sensor, Touch, Potentiometer
   * - **Sensorlar**
     - Distance (HC-SR04P / HC-SR04), Temperature (Internal/External)
   * - **Ulanish**
     - Oddiy WiFi ulanishi va holatni boshqarish

Ishni boshlash
--------------

1. **O'rnatish**: 

   Yangi boshlovchilar uchun `Mu Editor <gettingstarted.html#mu-yordamida-o-rnatish>`_\ dagi paket menejeri orqali avtomatik yoki fayllarni sudrab olib o'tish (drag & drop) orqali osongina o'rnatishni tavsiya qilamiz (batafsil ma'lumot uchun :doc:`gettingstarted` qo'llanmasiga qarang).

   Terminal orqali plataga to'g'ridan-to'g'ri o'rnatish uchun rasmiy ``mpremote`` CLI vositasidan foydalanishni tavsiya etamiz:
   
   .. code-block:: bash
   
       # Kompyuter terminalida mpremote CLI vositasini o'rnatish
       pip install mpremote

       # Ulangan ESP32 platasiga espzero-ni avtomatik yuklab olish va o'rnatish
       mpremote mip install espzero

   Yoki kompyuteringizda (IDE-da avtomatik to'ldirish uchun) ``pip`` orqali o'rnating:
   
   .. code-block:: bash
   
       pip install espzero

2. **Foydalanish**: Ortiqcha sozlamalarsiz komponentlarni import qiling va darhol ishlating (plata avtomatik aniqlanadi).

.. code-block:: python

    from espzero import LED

    led = LED(4)
    led.pulse() # Orqa fonda silliq miltillash

.. note::
   Plata birinchi komponentdan foydalanishda avtomatik aniqlangani uchun ``espzero.begin()`` ni chaqirish majburiy emas (ixtiyoriy). Faqatgina platani qo'lda aniq belgilash kerak bo'lganda ``espzero.begin("plata_nomi")`` chaqiriladi.

Mundarija
---------

.. toctree::
   :maxdepth: 2
   :caption: Qo'llanmalar va Retseptlar

   gettingstarted
   recipes
   boards
   api

.. toctree::
   :maxdepth: 1
   :caption: Loyiha haqida

   contributing
   changelog
   license

Yordam kerakmi?
---------------

* **GitHub ombori**: Savollaringizni `Issues <https://github.com/roboticsware/espzero/issues>`_ yorlig'ida qoldiring.
* **Hamjamiyat**: Loyihalaringizni baham ko'ring va blogimiz yoki forumlarimizda misollar toping.

.. |pypibadge| image:: https://badge.fury.io/py/espzero.svg
   :target: https://badge.fury.io/py/espzero
   :alt: PyPI Package Version

.. |docsbadge| image:: https://readthedocs.org/projects/espzero/badge/
   :target: https://espzero.readthedocs.io/
   :alt: Documentation Status
