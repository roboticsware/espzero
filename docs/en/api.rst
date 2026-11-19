API Reference
=============

This section provides detailed specifications for all public classes and functions in the ``espzero`` library.
It maintains 1:1 API compatibility with `roboticsware/picozero <https://github.com/roboticsware/picozero>`_ (`picozero-rw <https://picozero-rw.readthedocs.io/>`_), allowing code written for the Raspberry Pi Pico to run on ESP32 with virtually no modification.

Core Functions
--------------

.. autofunction:: espzero.begin

Output Devices
--------------

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

Input Devices
-------------

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

Sensors
-------

DistanceSensor
~~~~~~~~~~~~~~
.. autoclass:: espzero.DistanceSensor
   :members:

ESPTemperatureSensor
~~~~~~~~~~~~~~~~~~~~
.. autoclass:: espzero.ESPTemperatureSensor
   :members:

Displays
--------

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
