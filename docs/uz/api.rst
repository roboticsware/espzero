API ma'lumotnomasi
==================

Ushbu bo'limda ``espzero`` kutubxonasidagi barcha ochiq klasslar va funksiyalar uchun batafsil texnik tavsiflar keltirilgan.
U `roboticsware/picozero <https://github.com/roboticsware/picozero>`_ (`picozero-rw <https://picozero-rw.readthedocs.io/>`_) bilan 1:1 API mosligini ta'minlaydi, bu esa Raspberry Pi Pico uchun yozilgan kodlarni ESP32 da deyarli o'zgarishsiz ishlatish imkonini beradi.

Asosiy funksiyalar (Core Functions)
-----------------------------------

.. autofunction:: espzero.begin

Chiqish qurilmalari (Output Devices)
------------------------------------

DigitalLED
~~~~~~~~~~
.. autoclass:: espzero.DigitalLED
   :members:

PWMLED
~~~~~~
.. autoclass:: espzero.PWMLED
   :members:

RGBLED
~~~~~~
.. autoclass:: espzero.RGBLED
   :members:

Speaker
~~~~~~~
.. autoclass:: espzero.Speaker
   :members:

Kirish qurilmalari (Input Devices)
----------------------------------

Button
~~~~~~
.. autoclass:: espzero.Button
   :members:

Potentiometer
~~~~~~~~~~~~~
.. autoclass:: espzero.Potentiometer
   :members:

CapTouch
~~~~~~~~
.. autoclass:: espzero.CapTouch
   :members:

Sensorlar (Sensors)
-------------------

DistanceSensor
~~~~~~~~~~~~~~
.. autoclass:: espzero.DistanceSensor
   :members:

ESPTemperatureSensor
~~~~~~~~~~~~~~~~~~~~
.. autoclass:: espzero.ESPTemperatureSensor
   :members:

Displeylar (Displays)
---------------------

OLED
~~~~
.. autoclass:: espzero.OLED
   :members:

I2cLcd
~~~~~~
.. autoclass:: espzero.I2cLcd
   :members:

GpioLcd
~~~~~~~
.. autoclass:: espzero.GpioLcd
   :members:

Audio
-------------------------------------

I2SMic
~~~~~~
.. autoclass:: espzero.I2SMic
   :members:

Audio DSP va Wi-Fi striming (``espzero.audio``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: espzero.audio.spectrum

.. autofunction:: espzero.audio.mfcc

.. autofunction:: espzero.audio.freq_to_note

.. autofunction:: espzero.audio.start_wifi_stream

.. autofunction:: espzero.audio.get_ai_result

.. autofunction:: espzero.audio.stop_stream
