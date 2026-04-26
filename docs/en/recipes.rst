Recipes
=======

This section covers practical examples for controlling various sensors and components using ``espzero``. All examples assume ``import espzero; espzero.begin()`` has been called.

Built-in LED
------------

The simplest way to control the on-board LED.

.. code-block:: python

    from espzero import esp_led
    from time import sleep

    esp_led.on()    # Turn on
    sleep(1)
    esp_led.off()   # Turn off
    esp_led.blink() # Blink in the background

Digital Output (LED)
--------------------

Control a regular LED connected to a specific pin.

.. code-block:: python

    from espzero import LED

    led = LED(4) # GPIO 4

    led.on()
    led.off()
    led.toggle()
    
    # Blink 5 times with 0.5s intervals (asynchronous)
    led.blink(on_time=0.5, off_time=0.5, n=5)

PWM Control (Brightness)
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    led.value = 0.5 # 50% brightness
    led.pulse()     # Fade in and out repeatedly

RGB LED
-------

Combine Red, Green, and Blue pins to create various colors.

.. code-block:: python

    from espzero import RGBLED

    rgb = RGBLED(red=25, green=26, blue=27)

    rgb.color = (255, 0, 0)   # Red
    rgb.color = (0, 255, 0)   # Green
    rgb.color = (255, 255, 0) # Yellow (Red + Green)
    rgb.off()

Buzzer & Speaker
----------------

Simple Beep
~~~~~~~~~~~

.. code-block:: python

    from espzero import Buzzer

    bz = Buzzer(15)
    bz.beep(on_time=0.1, off_time=0.1, n=3) # "Beep-Beep-Beep"

Playing Melodies
~~~~~~~~~~~~~~~~

.. code-block:: python

    from espzero import Speaker

    spk = Speaker(15)

    # List of (note, duration) tuples
    tune = [
        ('c4', 0.5), ('d4', 0.5), ('e4', 0.5), ('c4', 0.5),
        ('e4', 0.5), ('c4', 0.5), ('g4', 1.0)
    ]
    spk.play(tune)

Input Devices
-------------

Button
~~~~~~

.. code-block:: python

    from espzero import Button

    btn = Button(5)

    btn.when_pressed = lambda: print("Pressed!")
    btn.when_released = lambda: print("Released!")

Potentiometer
~~~~~~~~~~~~~

.. code-block:: python

    from espzero import Pot

    pot = Pot(34) # Analog pin (ADC)

    print("Current value (0-1):", pot.value)
    print("Voltage (V):", pot.voltage)

Distance Sensor
---------------

Measure distance using an ultrasonic sensor like HC-SR04.

.. code-block:: python

    from espzero import DistanceSensor

    # echo=14, trigger=13
    ds = DistanceSensor(echo=14, trigger=13)

    while True:
        print("Distance: ", ds.distance, "m")
        sleep(0.5)

Temperature Sensor
------------------

Internal Temperature
~~~~~~~~~~~~~~~~~~~~

Measure the internal temperature of the ESP32 chip. (Note: May differ from ambient temperature).

.. code-block:: python

    from espzero import esp_temp_sensor

    print("Internal chip temp:", esp_temp_sensor.temp, "C")

Complex Example: Button-controlled Light
---------------------------------------

Toggle an LED each time a button is pressed.

.. code-block:: python

    from espzero import LED, Button, begin

    begin()
    led = LED(4)
    btn = Button(5)

    btn.when_pressed = led.toggle

    while True:
        pass # Wait for events
