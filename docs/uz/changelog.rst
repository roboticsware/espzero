O'zgarishlar tarixi
===================

.. currentmodule:: espzero

0.0.8 - 2026-11-20
------------------
+ 10 xil his-tuyg'uni aks ettiruvchi robot yuz ifodalari (`show_face`) va nigohni boshqarish (`look_at`) qo'shildi
+ 8 ta OLED robot ifodasini tasvirlovchi vektorli SVG diagrammasi (`oled_robot_faces.svg`) yaratildi
+ Kompyuter mikrofoni orqali ovoz bilan boshqariladigan aqlli avtomobil retsepti bilan **AI Ovoz (AI Voice)** bo'limi ochildi
+ Mu muharririning onlayn bulutli proshivka qiluvchisi ([ESP Online Flasher]) va oflayn fleshri bo'yicha ko'rsatmalar kengaytirildi
+ Mu muharriri va standart Python muhitlarini (VS Code, Thonny, mpremote) aniq ajratgan holda o'rnatish qo'llanmasi yaxshilandi
+ SSD1306 va SH1106 I2C displeylarini qo'llab-quvvatlovchi ``OLED`` klassi joriy etildi
+ Ultratovush (HC-SR04P 3.3V) va LCD (daraja o'zgartirgichli PCF8574) ulanish diagrammalari xavfsiz 3.3V sxemalarga almashtirildi
+ Freenove ESP32-S3 WROOM CAM (N16R8) kamera xavfsiz pinlari asosida yuqori aniqlikdagi SVG sxemalari yaratildi
+ Hujjatlar indeksiga PyPI joriy versiya nishoni va ReadTheDocs holati nishoni qo'shildi
+ Versiyalar tarixini boshqarish uchun ingliz, koreys va o'zbek tillarida ``changelog.rst`` qo'shildi

0.0.7 - 2026-11-17
------------------
+ YOLO o'rnatish qo'llanmasi va WiFi YOLO avtonom avtomobili retseptlari qo'shildi
+ To'xtovsiz oqim (non-blocking stream) va WiFi qo'llab-quvvatlash bilan ``vision.py`` moduli kuchaytirildi
+ Alohida batareyadan quvvatlanuvchi ``main.py`` va tashqi AP hotspot bo'yicha ko'rsatmalar kiritildi
+ Koreys va o'zbek tillaridagi hujjatlar to'liq yangilandi

0.0.6 - 2026-11-16
------------------
+ Kamera ko'rish moduli (vision) va rst hujjatlari qo'shildi
+ Freenove ESP32-S3 WROOM CAM rasmiy pin nomlari va plata metama'lumotlari kiritildi
+ ESP32-S3 uchun NeoPixelLED rang sozlagichi va pin tekshiruvi yaxshilandi
+ Sphinx ko'p tilli (en, ko, uz) hujjatlar tuzilmasi yaratildi

0.0.5 - 2026-11-15
------------------
+ CapTouch sig'imli sensor hujjatlari qo'shildi
+ ESP32-S3 va ESP32-C3 uchun ichki harorat sensori (``esp_temp_sensor`` / ``mcu_temperature``) xatosi tuzatildi
+ ReadTheDocs sozlamalari va havolalari yaxshilandi

0.0.3 - 2026-11-14
------------------
+ ``Stepper`` motori va ``I2cLcd`` / ``GpioLcd`` displeylarini boshqarish imkoniyatlari kiritildi
+ ``DistanceSensor`` o'lchov birligi santimetrga (cm) o'zgartirildi
+ ESP32 38-pinli NodeMCU profili va cheklangan pinlar xavfsizlik tarmog'i qo'shildi

0.0.2 - 2026-11-13
------------------
+ O'rnatilgan LED uchun ``esp_led`` taxallusi va maxsus dasturiy rejalashtiruvchi qo'shildi
+ NodeMCU V3 Lolin (ESP8266) plata profili qo'shildi
+ MicroPython mosligi va paket importi xatolari tuzatildi

0.0.1 - 2026-11-12
------------------
+ ESP32 va ESP8266 uchun espzero kutubxonasining birinchi rasmiy relizi
