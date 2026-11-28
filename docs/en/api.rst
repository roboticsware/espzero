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

TouchSensor (External Digital Module)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: espzero.TouchSensor
   :members:

CapTouch / InternalTouchSensor (ESP32 Built-in Touch)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

Camera & Vision
---------------

Snapshots, Photo Saving & Video Streaming (``espzero.vision``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: espzero.vision.capture

.. autofunction:: espzero.vision.save_photo

.. autofunction:: espzero.vision.close

.. autofunction:: espzero.vision.start_stream_to_pc

.. autofunction:: espzero.vision.start_wifi_stream

.. autofunction:: espzero.vision.stop_stream

Audio
----------------

I2SMic
~~~~~~
.. autoclass:: espzero.I2SMic
   :members:

I2SSpeaker
~~~~~~~~~~
.. autoclass:: espzero.I2SSpeaker
   :members:

Audio DSP & Wi-Fi Streaming (``espzero.audio``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: espzero.audio.spectrum

.. autofunction:: espzero.audio.mfcc

.. autofunction:: espzero.audio.freq_to_note

.. autofunction:: espzero.audio.start_wifi_stream

.. autofunction:: espzero.audio.start_ai_receiver

.. autofunction:: espzero.audio.get_ai_result

.. autofunction:: espzero.audio.stop_stream

Vision & Camera (``espzero.vision``)
------------------------------------

.. autofunction:: espzero.vision.capture

.. autofunction:: espzero.vision.save_photo

.. autofunction:: espzero.vision.close

.. autofunction:: espzero.vision.start_stream_to_pc

.. autofunction:: espzero.vision.start_wifi_stream

.. autofunction:: espzero.vision.get_hand

.. autofunction:: espzero.vision.stop_stream

Networking
----------

WiFi
~~~~
.. autoclass:: espzero.WiFi
   :members:
