espzero: The Easiest Coding Library for ESP32
=============================================

.. image:: /images/logo.png
   :width: 200px
   :align: center
   :alt: espzero logo

**espzero** is a beginner-friendly hardware control library for ESP32 and ESP8266 microcontrollers. It brings the simplicity of the popular ``picozero`` library to the ESP32 ecosystem.

.. tip::
   🌐 **한국어 버전**: 이 문서의 한국어 버전은 `docs/` 루트 디렉토리에서 확인하실 수 있습니다.
   🌐 **O'zbekcha versiya**: Ushbu hujjatning o'zbekcha versiyasini `docs/uz/` katalogida topishingiz mumkin.

Core Philosophy
---------------

* **Simplicity**: Start with a single line like ``LED.on()``, without worrying about registers or PWM frequencies.
* **Abstraction**: Your code remains the same regardless of which board you use. Board-specific differences are handled by ``espzero.begin()``.
* **Modern**: Built-in asynchronous scheduler for easy background task management.

Key Features
------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Component
     - Supported Features
   * - **Output Devices**
     - LED, PWM LED, RGB LED, Buzzer, Speaker (Melody), Motor
   * - **Input Devices**
     - Button, Switch, Motion Sensor, Touch, Potentiometer
   * - **Sensors**
     - Distance (HC-SR04), Temperature (Internal/External)
   * - **Connectivity**
     - Simple WiFi connection and status management

Getting Started
---------------

1. **Install**: 

   To install directly to your board, we recommend using ``mpremote``:
   
   .. code-block:: bash
   
       mpremote mip install espzero

   Alternatively, for IDE autocomplete and linting on your PC:
   
   .. code-block:: bash
   
       pip install espzero

2. **Initialize**: Call ``espzero.begin()`` at the top of your script.

.. code-block:: python

    import espzero
    from espzero import LED
    
    espzero.begin()
    led = LED(4)
    led.pulse() # Blink smoothly in the background

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2
   :caption: Guides & Recipes

   gettingstarted
   recipes
   boards
   api

.. toctree::
   :maxdepth: 1
   :caption: Project Info

   contributing
   license

Need Help?
----------

* **GitHub Repository**: Post your questions in the `Issues <https://github.com/roboticsware/espzero/issues>`_ tab.
* **Community**: Share your projects and find examples on our blog or forums.
