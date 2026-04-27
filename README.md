# espzero

[![PyPI version](https://badge.fury.io/py/espzero.svg)](https://badge.fury.io/py/espzero)
[![License](https://img.shields.io/github/license/roboticsware/espzero)](https://github.com/roboticsware/espzero/blob/main/LICENSE)

> A single MicroPython library that ports [picozero](https://github.com/raspberrypilearning/picozero) to the ESP32 family (WROOM, S3, C3, and more).  
> **"One codebase, many boards"** — hardware differences are absorbed by the Board Profile system.

---

## Installation

### For your ESP32 board (Recommended)
Use `mpremote` to install directly from PyPI to your board:

```bash
mpremote mip install espzero
```

Or manually copy the `espzero/` directory to your board's root.

### For your PC (Development)
To get autocomplete and linting in your IDE:

```bash
pip install espzero
```

---

## Quick Start

```python
import espzero
espzero.begin()                # initialise: auto-detect board

# Built-in LED — available after begin()
from espzero import esp_led
from time import sleep

while True:
    esp_led.on()
    sleep(1)
    esp_led.off()
    sleep(1)
```

Specify a board explicitly instead of auto-detection:

```python
import espzero
espzero.begin("esp32_38pin_nodemcu")   # or "esp32_devkit_v1", "esp8266_lolin_v3", ...
```

Use other components after `begin()`:

```python
from espzero import LED, Button, Servo, WiFi

led = LED("internal")              # built-in LED — profile maps alias to real GPIO
btn = Button(0)                    # GPIO 0 (BOOT button)
led.blink(on_time=0.5, n=5)       # identical API to picozero

# WiFi (ESP32-specific)
wifi = WiFi()
ip = wifi.connect("MySSID", "password")
print("IP:", ip)

# Capacitive touch (WROOM/WROVER only)
from espzero import CapTouch
touch = CapTouch(pin=4)            # GPIO 4 = T0
if touch.is_touched:
    esp_led.on()

# Servo
servo = Servo(13)
servo.mid()
servo.value = 0.75                 # 0–1 range, same as picozero
```

---

## 1. File Structure

```
espzero/
├── __init__.py          # Public API entry point + begin()
├── _hal.py              # Hardware Abstraction Layer (HAL)
├── _core.py             # Ported picozero core logic
├── _wifi.py             # ESP32-specific: WiFi class
├── _touch.py            # ESP32-specific: capacitive touch class
└── profiles/
    ├── _base.py         # Abstract BoardProfile base class
    ├── auto.py          # Runtime board auto-detection
    └── esp32_boards.py  # Profile definitions for all supported boards
```

---

## 2. Board Profile System

### 2-A. Base Class (`profiles/_base.py`)

```python
class BoardProfile:
    NAME = "unknown"            # Human-readable board name
    CHIP = "esp32"              # esp32 / esp32s3 / esp32c3 / esp8266

    # Pin aliases — lets users write LED("internal") instead of LED(2)
    PIN_ALIASES = {}

    # ADC settings
    ADC_MAX_RAW  = 4095         # 12-bit resolution (0–4095)
    ADC_SCALE    = 65535        # Scale target for picozero read_u16() compatibility
    ADC_ATTEN    = None         # e.g. machine.ADC.ATTN_11DB; None = firmware default
    ADC_VREF     = 3.3          # Maximum input voltage (tied to attenuation)

    # PWM settings
    PWM_DEFAULT_FREQ  = 1000    # Hz — Pico default was 100 Hz; 1 kHz recommended for ESP32
    PWM_DUTY_MAX      = 65535   # Internal scale is always 16-bit

    # Servo
    SERVO_FREQ        = 50      # 50 Hz (20 ms frame) — same as picozero

    # Built-in LED type
    # "digital"  — standard GPIO LED
    # "neopixel" — WS2812 RGB (e.g. ESP32-S3 DevKit, M5Stack ATOM)
    INTERNAL_LED_TYPE        = "digital"
    INTERNAL_LED_ACTIVE_HIGH = True

    # Boot strapping pins — connecting a button here may cause boot failures
    STRAPPING_PINS = []         # e.g. [0, 2, 5, 12, 15]

    # ADC2 pins — cannot be used while WiFi is active
    ADC2_PINS = []              # e.g. [0, 2, 4, 12, 13, 14, 15, 25, 26, 27]
```

### 2-B. Board Profile Examples (`profiles/esp32_boards.py`)

```python
class ESP32DevKitV1(BoardProfile):
    NAME = "esp32_devkit_v1"
    CHIP = "esp32"
    PIN_ALIASES = {"internal": 2, "led": 2}
    ADC_ATTEN            = ADC.ATTN_11DB   # 0–3.6 V
    ADC_VREF             = 3.6
    INTERNAL_LED_TYPE        = "digital"
    INTERNAL_LED_ACTIVE_HIGH = False       # active-low
    STRAPPING_PINS       = [0, 2, 5, 12, 15]
    ADC2_PINS            = [0, 2, 4, 12, 13, 14, 15, 25, 26, 27]


class ESP32S3DevKit(BoardProfile):
    NAME = "esp32_s3_devkit"
    CHIP = "esp32s3"
    PIN_ALIASES = {"internal": 48, "led": 48}
    INTERNAL_LED_TYPE = "neopixel"         # WS2812 RGB on GPIO 48
    STRAPPING_PINS    = [0, 3, 45, 46]
    ADC2_PINS         = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


class ESP32C3Mini(BoardProfile):
    NAME = "esp32_c3_mini"
    CHIP = "esp32c3"
    PIN_ALIASES = {"internal": 8, "led": 8}
    INTERNAL_LED_ACTIVE_HIGH = False
    STRAPPING_PINS = [2, 8, 9]
    ADC2_PINS      = []                    # C3 has no ADC2
```

### 2-C. Auto-detection (`profiles/auto.py`)

```python
import sys

def detect() -> str:
    """
    Identify the chip from sys.implementation._machine.
    Returns a board key that matches an entry in espzero._PROFILE_MAP.
    """
    try:
        machine_str = sys.implementation._machine.lower()
    except AttributeError:
        return "esp32_devkit_v1"   # fallback

    if "esp32s3" in machine_str or "esp32-s3" in machine_str:
        return "esp32_s3_devkit"
    elif "esp32c3" in machine_str or "esp32-c3" in machine_str:
        return "esp32_c3_mini"
    else:
        return "esp32_devkit_v1"   # default: WROOM
```

---

## 3. Hardware Abstraction Layer (`_hal.py`)

All `machine.Pin / machine.PWM / machine.ADC` calls are routed through this layer.  
Swapping the board profile is enough to support a new board — `_core.py` requires no changes.

```python
_profile     = None    # Set by begin() to a BoardProfile instance
_wifi_active = False   # True while WiFi is connected

def make_digital_in(pin, pull_up=False):
    """Create input Pin. Warns if GPIO is a strapping pin."""
    gpio = resolve_pin(pin)
    if gpio in get_profile().STRAPPING_PINS:
        print("[espzero] WARNING: GPIO {} is a strapping pin. "
              "Attaching a button may cause boot issues.".format(gpio))
    ...

def set_duty_u16(pwm_obj, value):
    """Set duty cycle. Falls back to duty(0–1023) on firmware < 1.19."""
    try:
        pwm_obj.duty_u16(value)
    except AttributeError:
        pwm_obj.duty(value >> 6)    # 16-bit → 10-bit

def make_adc(pin):
    """Create ADC. Warns if WiFi is active and pin is in ADC2 group."""
    if _wifi_active and gpio in get_profile().ADC2_PINS:
        print("[espzero] WARNING: WiFi is active. ADC2 (GPIO {}) "
              "cannot be used. Switch to an ADC1 pin.".format(gpio))
    ...
```

---

## 4. picozero → espzero Change Table

| Topic | picozero (Pico) | espzero (ESP32) | How |
|-------|----------------|-----------------|-----|
| **Pin creation** | `Pin(num, ...)` directly | `_hal.make_digital_out(pin)` | HAL wrapper |
| **PWM channel conflict** | `PIN_TO_PWM_CHANNEL[]` table | **Removed** (ESP32 LEDC: any pin, any channel) | Deleted |
| **PWM duty write** | `duty_u16(val)` | Same, with fallback for firmware < 1.19 | `_hal.set_duty_u16()` |
| **ADC read** | `adc.read_u16()` | `adc_read_u16()` → scales `read()×16` internally | HAL |
| **ADC attenuation** | None | `ATTN_11DB` (set in profile) | Profile |
| **Built-in LED** | `LED("LED")` or `LED(25)` | `LED("internal")` → profile maps to real pin | Alias system |
| **Built-in temp** | `pico_temp_sensor` (ADC ch.4) | `esp_temp_sensor` (ESP32 `esp32` module) | Separate class |
| **PWM default freq** | 100 Hz | 1000 Hz (`PWM_DEFAULT_FREQ` in profile) | Profile value |
| **Servo freq** | 50 Hz | 50 Hz (unchanged) | — |
| **WiFi** | None | `WiFi` class | New |
| **Touch** | `TouchSensor` (external TTP223) | + `CapTouch` (ESP32 built-in touch peripheral) | New |

---

## 5. Key `_core.py` Changes

### 5-A. `PWMOutputDevice` — Channel restriction removed

```python
# picozero: PIN_TO_PWM_CHANNEL table + _check_pwm_channel() → removed
# espzero:  ESP32 LEDC assigns each pin an independent channel — no conflicts

class PWMOutputDevice(OutputDevice, PinMixin):
    def __init__(self, pin, freq=None, duty_factor=65535, ...):
        self._pwm = _hal.make_pwm(pin, freq)   # routed through HAL

    def _write(self, value):
        _hal.set_duty_u16(self._pwm, self._value_to_state(value))  # with fallback
```

### 5-B. `AnalogInputDevice` — ADC scale correction

```python
class AnalogInputDevice(InputDevice, PinMixin):
    def __init__(self, pin, ...):
        self._adc = _hal.make_adc(pin)         # attenuation applied in profile

    def _read(self):
        raw_u16 = _hal.adc_read_u16(self._adc) # scaled to 0–65535
        return self._state_to_value(raw_u16)   # upper logic unchanged

    @property
    def voltage(self):
        return self.value * _hal.get_profile().ADC_VREF
```

### 5-C. Built-in objects renamed

```python
# picozero:  pico_led, pico_temp_sensor
# espzero:
esp_led         = LED("internal")          # profile resolves "internal" alias
esp_temp_sensor = ESPTemperatureSensor()   # uses esp32.raw_temperature()
```

---

## 6. ESP32-Specific Classes

### 6-A. `WiFi` (`_wifi.py`)

```python
from espzero import WiFi

wifi = WiFi()
ip = wifi.connect("MySSID", "password", timeout=10)
print("Connected:", ip)         # blocks until connected or raises OSError

wifi.scan()                     # returns list of nearby APs
wifi.is_connected               # True / False
wifi.ip                         # current IP string
wifi.disconnect()
```

> **Note:** After `connect()`, the HAL sets `_wifi_active = True` automatically.  
> Any attempt to use an ADC2 pin after this will print a warning.

### 6-B. `CapTouch` — Capacitive touch (`_touch.py`)

```python
from espzero import CapTouch

touch = CapTouch(pin=4, threshold=300)  # GPIO 4 = T0 on WROOM
if touch.is_touched:
    print("Touched! Raw:", touch.value)
```

Unlike `TouchSensor` (which wraps an external TTP223 IC), `CapTouch` uses the ESP32's built-in capacitive touch peripheral directly. Available on pins T0–T9 of WROOM/WROVER modules.

### 6-C. `NeoPixelLED` — Built-in RGB LED wrapper (`_core.py`)

```python
class NeoPixelLED:
    """
    Treats a single WS2812 pixel as a simple on/off LED.
    Automatically used as esp_led on boards where INTERNAL_LED_TYPE == 'neopixel'
    (e.g. ESP32-S3 DevKit GPIO 48, M5Stack ATOM GPIO 27).
    """
```

---

## 7. Safety Nets for Beginners

espzero includes three runtime warnings designed to save beginners from common hardware pitfalls:

| # | Trigger | Warning |
|---|---------|---------|
| 1 | Using an **ADC2 pin while WiFi is active** | `[espzero] WARNING: WiFi is active. ADC2 (GPIO N) cannot be used...` |
| 2 | Attaching a **button to a strapping pin** | `[espzero] WARNING: GPIO N is a strapping pin. Boot issues may occur.` |
| 3 | Running on **firmware < 1.19** (no `duty_u16`) | Silently falls back to `duty()` — no crash |

---

## 8. Supported Boards

| Board | Built-in LED | ADC1 Pins | ADC2 Pins* | Touch Pins |
|-------|-------------|-----------|------------|------------|
| ESP32 DevKit V1 (WROOM) | GPIO 2 (active-low) | 32–39 | 0,2,4,12–15,25–27 | T0(4)–T9(32) |
| ESP32-S3 DevKit | GPIO 48 (RGB) | 1–10 | 11–20 | T1–T14 |
| ESP32-C3 Mini | GPIO 8 (active-low) | 0–4 | None | None |
| M5Stack ATOM Lite | GPIO 27 (RGB) | 33,35,36 | 0,2,4,12–15,25–27 | T0(4),T3(15) |
| Wemos D1 Mini32 | GPIO 2 (active-low) | 32–39 | 0,2,4,12–15,25–27 | T0(4)–T9(32) |
| NodeMCU V3 Lolin (ESP8266) | GPIO 2 (active-low) | A0 only (10-bit, 0–1.0 V) | None | None |

> \* ADC2 pins cannot be used while WiFi is active. For educational use, stick to ADC1 pins only.
>
> **ESP8266 ADC note:** A0 accepts 0–1.0 V only. Use a voltage divider (e.g. 220 kΩ + 100 kΩ) to measure 3.3 V signals safely.

---

## 9. Implementation Roadmap

```
Phase 1 — Core port (complete)
  [x] profiles/_base.py         — BoardProfile abstract base class
  [x] profiles/esp32_boards.py  — WROOM, S3, C3, M5Stack, Wemos profiles
  [x] profiles/auto.py          — Runtime auto-detection
  [x] _hal.py                   — HAL wrappers
  [x] _core.py                  — Ported picozero core logic
        · PWMOutputDevice: removed channel-collision check
        · AnalogInputDevice: ADC read routed through HAL
        · pico_led / pico_temp_sensor → esp_led / esp_temp_sensor
  [x] __init__.py               — begin() + public API

Phase 2 — ESP32-specific features (complete)
  [x] _wifi.py                  — WiFi class
  [x] _touch.py                 — CapTouch class
  [x] Additional board profiles — S3, C3, M5Stack, Wemos

Phase 3 — Mu Editor integration (complete)
  [x] mu/resources/esp32/       — Library bundled with Mu Editor
  [x] mu/logic.py               — esp32_lib auto-provisioned to mu_code/
  [x] mu/interface/editor.py    — Jedi search path includes esp32_lib
                                  (dynamic autocomplete via source analysis)
```

---

## 10. Design Decisions

| # | Topic | Decision |
|---|-------|----------|
| 1 | **ADC2 + WiFi warning** | `_hal.make_adc()` checks `_wifi_active` flag and prints a warning |
| 2 | **`duty_u16()` fallback** | `_hal.set_duty_u16()` wrapper silently falls back to `duty(val>>6)` on firmware < 1.19 |
| 3 | **Strapping pin warning** | `make_digital_in()` checks `STRAPPING_PINS` and prints a warning |
| 4 | **NeoPixel built-in LED** | `INTERNAL_LED_TYPE = "neopixel"` profile field selects `NeoPixelLED` wrapper automatically |
| 5 | **Lazy profile loading** | `_PROFILE_MAP` dict + `importlib` — only the selected board's module is imported |
| 6 | **Autocomplete** | Jedi analyses live source in `mu/resources/esp32/` — no separate static API file needed |

---

## License

MIT License — contributions welcome.  
This library is part of the [Mu Editor](https://github.com/roboticsware/mu) project for educational IoT programming.
