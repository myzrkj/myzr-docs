Firmware Flashing
====================

Preparation:
---------------

1. Prepare an SD card with a capacity of at least 16GB (since the SD card needs to be formatted before flashing the image, **be sure to back up all data in the SD card in advance**), and prepare a card reader.
2. Run the software **SD Card Formatter** to format the SD card.

.. image:: /image/MYZR-全志系列/MYZR-H618-EK120/刷新固件1.png
   :alt: Firmware Flashing 1.png
   :width: 60%

Image Flashing:
-----------------

1. Run **balenaEtcher**; you will see the following interface:

.. image:: /image/MYZR-全志系列/MYZR-H618-EK120/刷新固件2.png
   :alt: Firmware Flashing 2.png
   :width: 60%

2. Click "Flash from file" and select the Linux image to be flashed:

.. image:: /image/MYZR-全志系列/MYZR-H618-EK120/刷新固件3.png
   :alt: Firmware Flashing 3.png
   :width: 60%

3. Click "Select target" and choose the SD card that was formatted in the preparation step:

.. image:: /image/MYZR-全志系列/MYZR-H618-EK120/刷新固件4.png
   :alt: Firmware Flashing 4.png
   :width: 60%

4. Click "Flash!" and wait for the flashing process to complete:

.. image:: /image/MYZR-全志系列/MYZR-H618-EK120/刷新固件5.png
   :alt: Firmware Flashing 5.png
   :width: 60%

5. Once the flashing is complete, insert the SD card into the development board and power it on to start the system:

.. image:: /image/MYZR-全志系列/MYZR-H618-EK120/刷新固件6.png
   :alt: Firmware Flashing 6.png
   :width: 60%

|  Note: Currently, Ubuntu and Debian images only support SD card flashing. If you need to flash the image to eMMC, please perform the following operation: "Download Image from SD Card to eMMC".


Download Image from SD Card to eMMC
-------------------------------------

|  After starting the system, execute the following command in the terminal:

.. code-block:: shell

   sudo nand-sata-install 2 1

|  Press Enter and enter the password: **myzr**
|  Wait for the flashing process to complete:

.. image:: /image/MYZR-全志系列/MYZR-H618-EK120/刷新固件7.png
   :alt: Firmware Flashing 7.png
   :width: 60%

|  Flashing completed:

.. image:: /image/MYZR-全志系列/MYZR-H618-EK120/刷新固件8.png
   :alt: Firmware Flashing 8.png
   :width: 60%

|  Press Enter. After pressing Enter, power off the development board, then remove the SD card. The system can now be started from eMMC.
|  Note: It is a normal phenomenon to see the following similar output after pressing Enter:

.. image:: /image/MYZR-全志系列/MYZR-H618-EK120/刷新固件9.png
   :alt: Firmware Flashing 9.png
   :width: 60%

|  If you need to erase eMMC, execute the following command:

.. code-block:: shell

   mkfs.ext4 /dev/mmcblk0
