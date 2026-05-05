Getting Started
===============

Install using Mu
================

Requirements
------------

A Windows or macOS computer with the `Mu Editor`_ installed.

.. _Mu Editor: https://github.com/roboticsware/mu/releases/latest

Select the MicroPython mode
---------------------------

Open Mu and click on the **Mode** button in the top left. Select **ESP32** and click **OK**.

.. image:: /images/mu-select-mode-esp32.jpg
    :alt: Selecting ESP32 mode in Mu Editor

Install espzero from PyPI/MIP in Mu
-----------------------------------

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
----------------------------

espzero can be installed by copying the ``espzero`` library folder inside the ``espzero_lib`` folder to your ESP32 using Mu's file manager.

Click on the **Files** button to open the file manager.

.. image:: /images/mu-files-button.jpg
    :alt: Clicking the Files button in Mu

In Mu, find the ``espzero`` folder inside the ``espzero_lib`` folder in the **Files on your computer** pane. Drag and drop it to the **Files on your device** pane.

.. image:: /images/mu-drag-and-drop.jpg
    :alt: Drag and drop espzero from computer to device in Mu
