Firmware Flashing
===================

Installing the DriverAssitant Driver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Locate the Rockchip USB driver installation package in the downloaded network disk materials. The path is: 3. Software Materials --> 3.2 - Tools --> DriverAssitant_v5.11.zip
- Extract DriverAssitant_v5.11.zip and enter the DriverAssitant_v5.11 folder
- Double-click the DriverInstall.exe program directly to start the driver installation. The installation steps are as follows:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件1.png
   :alt: 刷新固件1.png
   :width: 60%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件2.png
   :alt: 刷新固件2.png
   :width: 60%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件3.png
   :alt: 刷新固件3.png
   :width: 60%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件4.png
   :alt: 刷新固件4.png
   :width: 60%

Flashing with the RKDevTool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Find the RKDevTool driver installation package in the downloaded network disk materials. The path is: 3. Software Materials --> 3.2 - Tools --> RKDevTool_Release_v3.15.zip
- Extract RKDevTool_Release_v3.15.zip and enter the RKDevTool_Release_v3.15 folder
- Double-click RKDevTool.exe to launch the program

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件5.png
   :alt: 刷新固件5.png
   :width: 60%


Full Firmware Flashing
^^^^^^^^^^^^^^^^^^^^^^^^

|  Flash the entire firmware

- Click to enter the "Firmware Upgrade" interface

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件6.png
   :alt: 刷新固件6.png
   :width: 60%

- Click the "Firmware" button, then select the corresponding img image file

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件7.png
   :alt: 刷新固件7.png
   :width: 60%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件8.png
   :alt: 刷新固件8.png
   :width: 60%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件9.png
   :alt: 刷新固件9.png
   :width: 60%

- Connect the type-c flashing cable to the development board's CON6 interface, press and hold the USER1 button on the development board, and power it on. After about 3 seconds, you will see the development board enter download mode.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件10.png
   :alt: 刷新固件10.png
   :width: 60%

- Click the "Upgrade" button to start flashing. When the flashing is successful, a success message will be displayed on the right side.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件11.png
   :alt: 刷新固件11.png
   :width: 60%

- After the flashing is completed, power on the development board again.

Partial Flashing
^^^^^^^^^^^^^^^^^^^

- Flash one or more image files individually
- Copy the U-Boot image (uboot.img), Linux kernel image (boot.img), or file system image (rootfs.img) to be replaced, as well as the mkimage/output/Image/parameter.txt (partition table) file, to a Windows working directory without Chinese characters.
- Connect the type-c flashing cable to the development board's CON6 interface, press and hold the USER1 button on the development board, then connect the power cable to the development board. After about 3 seconds, you will see the development board enter the downloadLOADER mode. Follow the steps in the figure below to import the configuration.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件12.png
   :alt: 刷新固件12.png
   :width: 60%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件13.png
   :alt: 刷新固件13.png
   :width: 60%

- Check the "parameter" option, then click to read the partition table from the device's partitions.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件14.png
   :alt: 刷新固件14.png
   :width: 60%

|  Follow the steps in the figure below to perform the flashing

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/刷新固件15.png
   :alt: 刷新固件15.png
   :width: 60%

- After the flashing is completed, power on the development board again.