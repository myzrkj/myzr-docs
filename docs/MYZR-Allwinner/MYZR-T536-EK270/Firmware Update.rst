Firmware Update
==================

Firmware Flashing via USB
----------------------------

Installing the PhoenixSuit Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Locate the PhoenixSuit installation package in the downloaded network disk materials. The path is: 3. Software Materials --> 3.2 - Tools --> PhoenixSuit_msi V1.19.zip
- Extract PhoenixSuit_msi V1.19.zip and enter the PhoenixSuit_msi V1.19 folder
- Double-click the PhoenixSuit_CN.msi program directly to start the installation. The installation steps are as follows:

.. image:: /image/MYZR-全志系列/MYZR-T536-EK270/刷新固件1.png
   :alt: 刷新固件1.jpg
   :width: 60%

.. image:: /image/MYZR-全志系列/MYZR-T536-EK270/刷新固件2.png
   :alt: 刷新固件2.jpg
   :width: 60%

.. image:: /image/MYZR-全志系列/MYZR-T536-EK270/刷新固件3.png
   :alt: 刷新固件3.jpg
   :width: 60%

.. image:: /image/MYZR-全志系列/MYZR-T536-EK270/刷新固件4.png
   :alt: 刷新固件4.jpg
   :width: 60%

.. image:: /image/MYZR-全志系列/MYZR-T536-EK270/刷新固件5.png
   :alt: 刷新固件5.jpg
   :width: 60%

.. image:: /image/MYZR-全志系列/MYZR-T536-EK270/刷新固件6.png
   :alt: 刷新固件6.jpg
   :width: 60%

Firmware Flashing
~~~~~~~~~~~~~~~~~~~~

- Open PhoenixSuit, connect the development board to the computer using a Type-C cable, and power on the development board
- After the development board starts up completely, you can click "Update Now", or press and hold KEY3 before powering on to start direct flashing

.. image:: /image/MYZR-全志系列/MYZR-T536-EK270/刷新固件7.png
   :alt: 刷新固件7.jpg
   :width: 60%

- The flashing interface is as follows

.. image:: /image/MYZR-全志系列/MYZR-T536-EK270/刷新固件8.png
   :alt: 刷新固件8.jpg
   :width: 60%

- Once the flashing is completed, restart the development board

Firmware Flashing via TF Card
--------------------------------

Creating a Flashing Card
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Find PhoenixCard V4.3.1.zip in the downloaded network disk materials. The path is: 3. Software Materials --> 3.2 - Tools --> PhoenixCard V4.3.1.zip
- Extract PhoenixCard V4.3.1.zip, open the extracted folder, find and double-click to launch PhoenixCard.exe.

.. image:: /image/MYZR-全志系列/MYZR-T536-EK270/刷新固件9.png
   :alt: 刷新固件9.jpg
   :width: 60%

- Connect the TF card to the computer via a card reader (Note: The TF card will be automatically formatted when files are flashed to it), and wait for the software to detect the TF card. A successful detection is shown as follows

.. image:: /image/MYZR-全志系列/MYZR-T536-EK270/刷新固件10.png
   :alt: 刷新固件10.jpg
   :width: 60%

- Click "Select Firmware" to choose the file to be flashed, select "Mass Production Card" for "Card Type to Create", and click "Flash Card"

.. image:: /image/MYZR-全志系列/MYZR-T536-EK270/刷新固件11.png
   :alt: 刷新固件11.jpg
   :width: 60%

- Wait for the flashing to complete. The output information after successful flashing is as follows

.. image:: /image/MYZR-全志系列/MYZR-T536-EK270/刷新固件12.png
   :alt: 刷新固件12.jpg
   :width: 60%

Firmware Flashing
~~~~~~~~~~~~~~~~~~~~

| After creating the flashing card, insert it into the TF card slot of the development board and power on the board. When the serial terminal displays the following printed information, it indicates that the system flashing has been completed. At this point, remove the flashing card and restart the development board to enter the flashed system.