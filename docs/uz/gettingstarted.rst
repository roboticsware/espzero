Ishni boshlash
==============

Ushbu qo'llanma ``espzero`` kutubxonasini yangi boshlovchilar uchun qulay **Mu Editor** hamda ishlab chiquvchilar uchun buyruqlar satri vositalari (**mpremote / pip**) yordamida ESP32 ga o'rnatish yo'llarini tushuntiradi.

Mu yordamida o'rnatish (GUI)
----------------------------

Talablar
~~~~~~~~

Windows yoki macOS kompyuteri (`Mu Editor`_\ o'rnatilgan).

.. _Mu Editor: https://github.com/roboticsware/mu/releases/latest

MicroPython rejimini tanlash
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mu-ni oching va yuqori chap burchakdagi **Mode** tugmasini bosing. **ESP32**\ ni tanlang va **OK** tugmasini bosing.

.. image:: /images/mu-select-mode-esp32.jpg
    :alt: Mu Editor-da ESP32 rejimini tanlash

Avtomatik o'rnatish (Paket menejeri)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::
    **Internet ulanishi zarur**: Mu paket menejeri orqali kutubxonani onlayn (PyPI/MIP) qidirib yuklab olganligi sababli, kompyuteringiz internetga ulangan bo'lishi kerak.

Mu-da espzero-ni o'rnatish uchun **Packages** tugmasini bosing.

.. image:: /images/mu-packages-button.jpg
    :alt: Mu-dagi Packages tugmasini bosish

`espzero`\ ni qidiring va **Search** tugmasini bosing.

.. image:: /images/mu-search-espzero.jpg
    :alt: Mu paket menejerida espzero-ni qidirish

Paketni yuklab olish va qurilmangizga o'rnatish uchun **Install** tugmasini bosing.

.. image:: /images/mu-install-package.jpg
    :alt: Mu paket menejerida o'rnatish tugmasini bosish

Qo'lda o'rnatish (Drag & Drop)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

espzero-ni Mu fayl menejeri yordamida ``espzero_lib`` papkasi ichidagi ``espzero`` kutubxonasini ESP32-ga nusxalash orqali o'rnatish mumkin.

Fayl menejerini ochish uchun **Files** tugmasini bosing.

.. image:: /images/mu-files-button.jpg
    :alt: Mu-dagi Files tugmasini bosish

Mu-dagi **Kompyuteringizdagi fayllar (Files on your computer)** oynasidan ``espzero_lib`` papkasi ichidagi ``espzero`` papkasini toping. Ularni **Qurilmadagi fayllar (Files on your device)** oynasiga sudrab olib o'ting (drag and drop).

.. image:: /images/mu-drag-and-drop.jpg
    :alt: Mu-da espzero-ni kompyuterdan qurilmaga sudrab olib o'tish

Buyruqlar satri (CLI) orqali o'rnatish
--------------------------------------

Terminal yoki buyruqlar satrida (PowerShell, CMD, Bash) ishlasangiz, quyidagi vositalar orqali o'rnatishingiz mumkin.

mpremote orqali plataga to'g'ridan-to'g'ri o'rnatish
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``mpremote`` — bu MicroPython-ning rasmiy buyruqlar satri vositasi bo'lib, USB orqali ulangan plata bilan to'g'ridan-to'g'ri aloqa o'rnatadi va MIP orqali kutubxonalarni avtomatik yuklab olib o'rnatadi.

1. **Kompyuteringizda mpremote-ni o'rnatish**:
   
   .. code-block:: bash

       pip install mpremote

2. **Ulangan ESP32 platasiga espzero-ni o'rnatish**:
   
   ESP32 platangiz kompyuterga USB orqali ulangan holatda quyidagi buyruqni bajaring:

   .. code-block:: bash

       mpremote mip install espzero

.. tip::
    Agar bir nechta plata ulangan bo'lsa yoki portni qo'lda ko'rsatish kerak bo'lsa, ``mpremote connect COMx mip install espzero`` (Windows) yoki ``mpremote connect /dev/ttyUSB0 mip install espzero`` (macOS/Linux) buyrug'idan foydalaning.

Kompyuterda dasturlash uchun pip orqali o'rnatish (Avtomatik to'ldirish)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VS Code, PyCharm kabi muhitlarda kod yozishda avtomatik to'ldirish (IntelliSense) va turlarni tekshirishdan foydalanish uchun kompyuteringizga ham o'rnating:

.. code-block:: bash

    pip install espzero
