Firmware Refresh
===================

Install the DriverAssitant Driver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Locate the Rockchip USB driver installation package from the downloaded network disk materials. The path is: 3. Software Materials --> 3.2 - Tools --> DriverAssitant_v5.11.zip
- Extract DriverAssitant_v5.11.zip and navigate to the DriverAssitant_v5.11 folder
- Double-click the DriverInstall.exe program directly to start the driver installation. The installation steps are as follows:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/DriverInstall-1.png
   :alt: DriverInstall-1.png
   :width: 60%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/DriverInstall-2.png
   :alt: DriverInstall-2.png
   :width: 60%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/DriverInstall-3.png
   :alt: DriverInstall-3.png
   :width: 60%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/DriverInstall-4.png
   :alt: DriverInstall-4.png
   :width: 60%

Flash the Firmware Using the RKDevTool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Find the RKDevTool driver installation package in the downloaded network disk materials. The path is: 3. Software Materials --> 3.2 - Tools --> RKDevTool_Release_v3.15.zip
- Extract RKDevTool_Release_v3.15.zip and enter the RKDevTool_Release_v3.15 folder
- Image Description

+--------------------------+------------+----------------+------------------------+---------------------+
| uboot.img                | boot.img   | recovery.img   | rootfs.img             | update.img          |
+--------------------------+------------+----------------+------------------------+---------------------+
| U-Boot Boot Loader Image | Boot Image | Recovery Image | Root File System Image | Full Firmware Image |
+--------------------------+------------+----------------+------------------------+---------------------+

- Double-click RKDevTool.exe to launch the program

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/RKDevTool-1.png
   :alt: RKDevTool-1.png
   :width: 60%


Full Flash
^^^^^^^^^^^^

| Flash the entire firmware

- Click to enter the "Upgrade Firmware" interface

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/RKDevTool-2.png
   :alt: RKDevTool-2.png
   :width: 60%

- Click the "Firmware" button, then select the corresponding img image file

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/RKDevTool-3.png
   :alt: RKDevTool-3.png
   :width: 60%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/RKDevTool-4.png
   :alt: RKDevTool-4.png
   :width: 60%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/RKDevTool-5.png
   :alt: RKDevTool-5.png
   :width: 60%

- Connect the Type-C flashing cable to the J5 port of the development board, press and hold the SW2 button on the development board, then power on the development board. After approximately 3 seconds of power-on, you can see that the development board has entered the DOWNLOADER mode

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/RKDevTool-6.png
   :alt: RKDevTool-6.png
   :width: 60%

- Click the "Upgrade" button to start flashing. When the flashing is successful, a success message will be displayed on the right side

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/RKDevTool-7.png
   :alt: RKDevTool-7.png
   :width: 60%

Partial Flash
^^^^^^^^^^^^^^^

- Flash one or more image files individually

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/RKDevTool-8.png
   :alt: RKDevTool-8.png
   :width: 60%

- After the flashing is completed, power on the development board again.