"""
Audio Spectrum Equalizer & Beat-Reactive NeoPixel
Uses I2SMic to capture 16-band real-time FFT spectrum and renders it on an I2C OLED.
"""
from espzero import I2SMic, OLED, esp_led
from time import sleep

mic = I2SMic()         # Default I2S mic pins (SCK=41, WS=42, SD=2 on ESP32-S3)
oled = OLED(scl=47, sda=21)

while True:
    bands = mic.spectrum(bins=16)
    note = mic.note or "---"
    oled.show_spectrum(bands, title="{} ({}dB)".format(note, int(mic.decibels)))

    # Pulse the built-in RGB NeoPixel on strong bass beats
    bass = (bands[0] + bands[1]) / 2
    if bass > 0.4:
        esp_led.color = (255, 0, 128)
    else:
        esp_led.off()

    sleep(0.03)
