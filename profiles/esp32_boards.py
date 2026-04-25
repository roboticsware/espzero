"""
espzero/profiles/esp32_boards.py
Board profile definitions for common ESP32-family boards.

Each class declares the hardware constants for one board variant.
Add new boards here by subclassing BoardProfile and overriding the
relevant fields.
"""
from ._base import BoardProfile


# ── ADC attenuation helper ─────────────────────────────────────
# Imported lazily so the profiles module can be parsed on the host
# (e.g. for IDE support) without requiring machine to be available.
def _atten():
    try:
        from machine import ADC
        return ADC.ATTN_11DB
    except Exception:
        return None


# ──────────────────────────────────────────────────────────────
# ESP32 DevKit V1 / WROOM-32
# ──────────────────────────────────────────────────────────────
class ESP32DevKitV1(BoardProfile):
    """
    Espressif ESP32 DevKit V1 (WROOM-32).
    Built-in LED: GPIO 2 (active-low, blue).
    ADC1: GPIO 32-39   ADC2: GPIO 0, 2, 4, 12-15, 25-27 (unusable with WiFi)
    Strapping pins: GPIO 0, 2, 5, 12, 15
    """
    NAME = "esp32_devkit_v1"
    CHIP = "esp32"

    PIN_ALIASES = {
        "internal": 2,
        "led":      2,
    }

    ADC_ATTEN            = _atten()
    ADC_VREF             = 3.6
    INTERNAL_LED_TYPE        = "digital"
    INTERNAL_LED_ACTIVE_HIGH = False   # active-low
    STRAPPING_PINS       = [0, 2, 5, 12, 15]
    ADC2_PINS            = [0, 2, 4, 12, 13, 14, 15, 25, 26, 27]


# ──────────────────────────────────────────────────────────────
# ESP32-S3 DevKit-C
# ──────────────────────────────────────────────────────────────
class ESP32S3DevKit(BoardProfile):
    """
    Espressif ESP32-S3 DevKitC-1.
    Built-in LED: GPIO 48 (WS2812 NeoPixel RGB).
    ADC1: GPIO 1-10    ADC2: GPIO 11-20 (unusable with WiFi)
    Strapping pins: GPIO 0, 3, 45, 46
    """
    NAME = "esp32_s3_devkit"
    CHIP = "esp32s3"

    PIN_ALIASES = {
        "internal": 48,
        "led":      48,
    }

    ADC_ATTEN            = _atten()
    ADC_VREF             = 3.6
    INTERNAL_LED_TYPE        = "neopixel"
    INTERNAL_LED_ACTIVE_HIGH = True
    STRAPPING_PINS       = [0, 3, 45, 46]
    ADC2_PINS            = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


# ──────────────────────────────────────────────────────────────
# ESP32-C3 Mini / SuperMini
# ──────────────────────────────────────────────────────────────
class ESP32C3Mini(BoardProfile):
    """
    ESP32-C3 Mini / SuperMini.
    Built-in LED: GPIO 8 (active-low).
    ADC1 only: GPIO 0-4. No ADC2 channel.
    Strapping pins: GPIO 2, 8, 9
    """
    NAME = "esp32_c3_mini"
    CHIP = "esp32c3"

    PIN_ALIASES = {
        "internal": 8,
        "led":      8,
    }

    ADC_ATTEN            = _atten()
    ADC_VREF             = 3.6
    INTERNAL_LED_TYPE        = "digital"
    INTERNAL_LED_ACTIVE_HIGH = False   # active-low
    STRAPPING_PINS       = [2, 8, 9]
    ADC2_PINS            = []          # C3 has no ADC2


# ──────────────────────────────────────────────────────────────
# M5Stack ATOM Lite / Matrix
# ──────────────────────────────────────────────────────────────
class M5StackAtom(BoardProfile):
    """
    M5Stack ATOM Lite / Matrix.
    Built-in LED: GPIO 27 (WS2812 NeoPixel).
    Built-in button: GPIO 39 (G39).
    """
    NAME = "m5stack_atom"
    CHIP = "esp32"

    PIN_ALIASES = {
        "internal": 27,
        "led":      27,
        "btn":      39,    # Built-in button (G39)
    }

    ADC_ATTEN            = _atten()
    ADC_VREF             = 3.6
    INTERNAL_LED_TYPE        = "neopixel"
    INTERNAL_LED_ACTIVE_HIGH = True
    STRAPPING_PINS       = [0, 2, 5, 12, 15]
    ADC2_PINS            = [0, 2, 4, 12, 13, 14, 15, 25, 26, 27]


# ──────────────────────────────────────────────────────────────
# Wemos D1 Mini32 (ESP32)
# ──────────────────────────────────────────────────────────────
class WemosD1Mini32(BoardProfile):
    """Wemos / LOLIN D1 Mini32."""
    NAME = "wemos_d1_mini32"
    CHIP = "esp32"

    PIN_ALIASES = {
        "internal": 2,
        "led":      2,
    }

    ADC_ATTEN            = _atten()
    ADC_VREF             = 3.6
    INTERNAL_LED_TYPE        = "digital"
    INTERNAL_LED_ACTIVE_HIGH = False
    STRAPPING_PINS       = [0, 2, 5, 12, 15]
    ADC2_PINS            = [0, 2, 4, 12, 13, 14, 15, 25, 26, 27]
