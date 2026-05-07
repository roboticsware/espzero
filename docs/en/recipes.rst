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
        print("Distance: ", ds.distance, "cm")
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

Stepper Motor
-------------

Control a stepper motor connected via a driver board (e.g. ULN2003).

Analog clock
~~~~~~~~~~~~

Create a continuously-running analog clock second hand:

.. literalinclude:: examples/stepper_analog_clock.py

Automatic blinds
~~~~~~~~~~~~~~~~

Time-based blind controller:

.. literalinclude:: examples/stepper_automatic_blinds.py

LCD Display
-----------

Print characters on LiquidCrystal displays (LCD) by using the I2C bus and a PCF8574 I2C adapter.

.. literalinclude:: examples/i2c_lcd.py

Print characters on LiquidCrystal displays (LCD) by using GPIO pins only.

.. literalinclude:: examples/lcd.py


AI Vision
---------

Examples for using the ESP32-S3 camera with PC-assisted AI and standalone on-device AI.

PC-Side AI (with MediaPipe)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Streams camera images to the PC (Pico Editor), which uses Google's MediaPipe library to track hands, faces, etc., in real time. The detected coordinates are sent back to the ESP32 for hardware control.

.. code-block:: python

    from espzero import vision
    from time import sleep

    # Start streaming camera frames to the PC
    vision.start_stream_to_pc()

    while True:
        # Read the hand coordinates injected by the editor
        if "__pc_ai_data" in globals():
            x = __pc_ai_data.get("hand_x", 0)
            y = __pc_ai_data.get("hand_y", 0)
            print("Hand position -> X:", x, "Y:", y)
        sleep(0.1)

On-Device AI (On-Device TFLite)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Loads a `.tflite` model file directly from the ESP32's file system to perform local AI inference. It can run independently of any computer.

.. note::
    You can download sample `.tflite` model files from the Google TensorFlow Lite official models repository (https://www.tensorflow.org/lite/guide/hosted_models).

.. code-block:: python

    import camera
    import tflite
    from time import sleep

    # Initialize camera and load TFLite model
    camera.init(framesize=camera.FRAME_QVGA)
    model = tflite.load("model.tflite")

    while True:
        img = camera.capture()
        if img:
            # Perform inference and extract the class result
            result = model.detect(img)
            print("Detected class ID:", result.class_id)
        sleep(0.5)

