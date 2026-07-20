.. raw:: html

   <style>
   h1 {
       color: #4CAF50;
   }
   </style>


Firmware Update
===============

Installing the DriverAssitant Driver
------------------------------------

#. Find the Rockchip USB driver installation package from the downloaded cloud drive materials, path: 3. Software Materials --> 3.2 Tools --> DriverAssitant_v5.11.zip

#. Extract DriverAssitant_v5.11.zip and enter the DriverAssitant_v5.11 folder

#. Double-click the DriverInstall.exe program to install the driver. The installation steps are as follows:

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件1.png
   :alt: 刷新固件1.png
   :width: 100%

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件2.png
   :alt: 刷新固件2.png
   :width: 100%

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件3.png
   :alt: 刷新固件3.png
   :width: 100%

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件4.png
   :alt: 刷新固件4.png
   :width: 100%

Flashing with the RKDevTool
----------------------------

#. Find the RKDevTool driver installation package from the downloaded cloud drive materials, path: 3. Software Materials --> 3.2 Tools --> RKDevTool_Release_v3.15.zip

#. Extract RKDevTool_Release_v3.15.zip and enter the RKDevTool_Release_v3.15 folder

#. Double-click RKDevTool.exe to open the program

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件5.png
   :alt: 刷新固件5.png
   :width: 100%

Full Flash
^^^^^^^^^^

Flash the entire firmware.

* Click to enter the "Upgrade Firmware" interface

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件6.png
   :alt: 刷新固件6.png
   :width: 100%

* Click the "Firmware" button, then select the corresponding img image file

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件7.png
   :alt: 刷新固件7.png
   :width: 100%

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件8.png
   :alt: 刷新固件8.png
   :width: 100%

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件9.png
   :alt: 刷新固件9.png
   :width: 100%

* Connect the Type-C flashing cable to CON6 on the development board, press and hold the USER1 button on the development board, then power on. After about 3 seconds, the development board will enter download mode.

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件10.png
   :alt: 刷新固件10.png
   :width: 100%

* Click the "Upgrade" button to flash. A success message will appear on the right side when flashing is complete.

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件11.png
   :alt: 刷新固件11.png
   :width: 100%

* After flashing is complete, power cycle the development board.

Individual Flash
^^^^^^^^^^^^^^^^

* Flash one or more individual image files.

* Copy the U-Boot image uboot.img, Linux kernel image boot.img, or file system image rootfs.img to be replaced, along with the mkimage/output/Image/parameter.txt (partition table) file, to a Windows working directory without Chinese characters in the path.

* Connect the Type-C flashing cable to CON6 on the development board, press and hold the USER1 button on the development board, then connect the power cable. After about 3 seconds, the development board will enter LOADER mode. Follow the steps below to import the configuration.

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件12.png
   :alt: 刷新固件12.png
   :width: 100%

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件13.png
   :alt: 刷新固件13.png
   :width: 100%

* Check the parameter box and click "Read Partition Table" to read the partitions.

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件14.png
   :alt: 刷新固件14.png
   :width: 100%

Follow the steps below to flash.

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件15.jpg
   :alt: 刷新固件15.jpg
   :width: 100%

* After flashing is complete, power cycle the development board.