Qo'llab-quvvatlanadigan platalar
==================================

``espzero`` o'zining plata profili tizimi orqali turli xil ESP32 platalarini qo'llab-quvvatlaydi.

Qo'llab-quvvatlash ro'yxati
--------------------------

* **esp32_devkit_v1**: Standart ESP32-WROOM-32 ishlab chiqish platasi.
* **esp32_38pin_nodemcu**: Type-C/Micro-USB 38-pinli plata (GPIO 1 o'rnatilgan LED).
* **esp32_s3_devkit**: ESP32-S3 asosidagi platalar (NeoPixel o'rnatilgan LED).
* **esp32_c3_mini**: ESP32-C3 asosidagi mini platalar.
* **m5stack_atom**: M5Stack ATOM seriyasi.
* **esp8266_lolin_v3**: ESP8266 asosidagi NodeMCU platalari.

Avtomatik aniqlash
------------------

Ko'p hollarda ``espzero.begin()`` funksiyasini argumentlarsiz chaqirish plata turini avtomatik ravishable aniqlaydi. Agar aniqlash muvaffaqiyatsiz tugasa yoki ma'lum bir platani majburlamoqchi bo'lsangiz, nomini quyidagicha ko'rsatishingiz mumkin:

.. code-block:: python

    espzero.begin("esp32_devkit_v1")
