from espzero import I2cLcd
from time import sleep

lcd = I2cLcd(0, 47, 21)  # i2c_id=0, scl=47, sda=21 (ESP32-S3)

lcd.putstr('Hello World')
sleep(1)
lcd.move_to(0, 1)
lcd.putstr('Hello Pi Pico')
