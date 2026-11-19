Getting Started
===============

This guide explains how to install the ``espzero`` library on your ESP32 using both the beginner-friendly **Mu Editor** and command-line tools (**mpremote / pip**).

Install using Command Line Tools (CLI)
--------------------------------------

If you work in a terminal or command prompt (PowerShell, CMD, Bash), you can easily install espzero using CLI tools.

Direct Install to Board via mpremote
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``mpremote`` is the official MicroPython command-line tool. It connects directly to your board via USB serial to manage files and automatically fetch and install packages via MIP.

1. **Install mpremote on your PC**:
   
   .. code-block:: bash

       pip install mpremote

2. **Install espzero directly to the connected ESP32**:
   
   With your ESP32 connected to your PC via USB, run:

   .. code-block:: bash

       mpremote mip install espzero

.. tip::
    If multiple boards are connected or you need to specify a serial port explicitly, use ``mpremote connect COMx mip install espzero`` (Windows) or ``mpremote connect /dev/ttyUSB0 mip install espzero`` (macOS/Linux).

Install via pip for PC Development (Autocomplete / Linting)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To enable code completion (IntelliSense) and type checking in desktop IDEs such as VS Code or PyCharm, install espzero in your Python environment:

.. code-block:: bash

    pip install espzero

Install using Mu
----------------

Requirements
~~~~~~~~~~~~

A Windows or macOS computer with the `Mu Editor`_ installed.

.. _Mu Editor: https://github.com/roboticsware/mu/releases/latest

Select the MicroPython mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open Mu and click on the **Mode** button in the top left. Select **ESP32** and click **OK**.

.. image:: /images/mu-select-mode-esp32.jpg
    :alt: Selecting ESP32 mode in Mu Editor

Automatic Installation (Package Manager)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::
    **Internet Connection Required**: Since Mu searches and downloads the latest package online from PyPI/MIP, your computer must be connected to the internet.

To install espzero within Mu, click on the **Packages** button.

.. image:: /images/mu-packages-button.jpg
    :alt: Clicking the Packages button in Mu

Search for `espzero` and click **Search**.

.. image:: /images/mu-search-espzero.jpg
    :alt: Searching for espzero in Mu package manager

Click on **Install** to download and install the package to your device.

.. image:: /images/mu-install-package.jpg
    :alt: Clicking install in Mu package manager

Manual install (Drag & Drop)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

espzero can be installed by copying the ``espzero`` library folder inside the ``espzero_lib`` folder to your ESP32 using Mu's file manager.

Click on the **Files** button to open the file manager.

.. image:: /images/mu-files-button.jpg
    :alt: Clicking the Files button in Mu

In Mu, find the ``espzero`` folder inside the ``espzero_lib`` folder in the **Files on your computer** pane. Drag and drop it to the **Files on your device** pane.

.. image:: /images/mu-drag-and-drop.jpg
    :alt: Drag and drop espzero from computer to device in Mu
