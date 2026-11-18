API 레퍼런스 (API Reference)
==========================

이 섹션은 ``espzero`` 라이브러리의 모든 공개 클래스와 함수에 대한 상세 사양을 다룹니다.
``roboticsware/picozero`` (``picozero-rw``) 와의 1:1 API 호환성을 유지하여, 라즈베리 파이 피코용으로 작성된 코드도 거의 수정 없이 ESP32에서 실행할 수 있습니다.

핵심 함수 (Core Functions)
------------------------

.. autofunction:: espzero.begin

.. autofunction:: espzero.pinout

출력 장치 (Output Devices)
------------------------

DigitalLED
~~~~~~~~~~
.. autoclass:: espzero.DigitalLED
   :members:

PWMLED
~~~~~~
.. autoclass:: espzero.PWMLED
   :members:

NeoPixelLED
~~~~~~~~~~~
.. autoclass:: espzero.NeoPixelLED
   :members:

RGBLED
~~~~~~
.. autoclass:: espzero.RGBLED
   :members:

Buzzer & PWMBuzzer
~~~~~~~~~~~~~~~~~~
.. autoclass:: espzero.Buzzer
   :members:

.. autoclass:: espzero.PWMBuzzer
   :members:

Speaker
~~~~~~~
.. autoclass:: espzero.Speaker
   :members:

Servo
~~~~~
.. autoclass:: espzero.Servo
   :members: move_to_degree, min, mid, max, off

모터 및 로봇 (Motors & Robotics)
------------------------------

Motor
~~~~~
.. autoclass:: espzero.Motor
   :members:

Robot
~~~~~
.. autoclass:: espzero.Robot
   :members:

Stepper
~~~~~~~
.. autoclass:: espzero.Stepper
   :members:

입력 장치 (Input Devices)
-----------------------

Button
~~~~~~
.. autoclass:: espzero.Button
   :members:

Switch
~~~~~~
.. autoclass:: espzero.Switch
   :members:

MotionSensor
~~~~~~~~~~~~
.. autoclass:: espzero.MotionSensor
   :members:

TouchSensor
~~~~~~~~~~~
.. autoclass:: espzero.TouchSensor
   :members:

Potentiometer (Pot)
~~~~~~~~~~~~~~~~~~~
.. autoclass:: espzero.Potentiometer
   :members: value, raw_value, voltage

CapTouch (ESP32 내장 터치)
~~~~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: espzero.CapTouch
   :members:

센서 (Sensors)
-------------

DistanceSensor
~~~~~~~~~~~~~~
.. autoclass:: espzero.DistanceSensor
   :members:

TemperatureSensor
~~~~~~~~~~~~~~~~~
.. autoclass:: espzero.TemperatureSensor
   :members:

ESPTemperatureSensor
~~~~~~~~~~~~~~~~~~~~
.. autoclass:: espzero.ESPTemperatureSensor
   :members:

디스플레이 (Displays)
-------------------

I2cLcd
~~~~~~
.. autoclass:: espzero.I2cLcd
   :members:

GpioLcd
~~~~~~~
.. autoclass:: espzero.GpioLcd
   :members:

통신 (Networking)
---------------

WiFi
~~~~
.. autoclass:: espzero.WiFi
   :members:
