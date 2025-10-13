Firmware Flashing
===================

Installing the DriverAssitant Driver
--------------------------------------

- Locate the Rockchip USB driver installation package from the downloaded network disk materials. The path is: 3. Software Materials --> 3.2 - Tools --> DriverAssitant_v5.11.zip
- Extract DriverAssitant_v5.11.zip and enter the DriverAssitant_v5.11 folder
- Double-click the DriverInstall.exe program directly to start the driver installation. The installation steps are as follows:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/刷新固件1.png
   :alt: 刷新固件1.png
   :width: 60%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/刷新固件2.png
   :alt: 刷新固件2.png
   :width: 60%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/刷新固件3.png
   :alt: 刷新固件3.png
   :width: 60%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/刷新固件4.png
   :alt: 刷新固件4.png
   :width: 60%

Flashing Firmware with the RKDevTool
--------------------------------------

- Locate the RKDevTool installation package from the downloaded network disk materials. The path is: 3. Software Materials --> 3.2 - Tools --> RKDevTool_Release_v3.15.zip
- Extract RKDevTool_Release_v3.15.zip and enter the RKDevTool_Release_v3.15 folder
- Image Description

+--------------------+------------+----------------+-----------------------+---------------------+
| uboot.img          | boot.img   | recover.img    | rootfs.img            | update.img          |
+--------------------+------------+----------------+-----------------------+---------------------+
| U-boot Boot Loader | Boot Image | Recovery Image | Root Filesystem Image | Full Firmware Image |
+--------------------+------------+----------------+-----------------------+---------------------+

- Double-click RKDevTool.exe to launch the program

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/刷新固件5.png
   :alt: 刷新固件5.png
   :width: 60%

Full Firmware Flashing
------------------------

|  Flash the entire firmware

- Click to enter the "Upgrade Firmware" interface
- Click the "Firmware" button, then select the corresponding img image file

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/刷新固件6.png
   :alt: 刷新固件6.png
   :width: 60%

- Connect the USB flashing cable to the J6 interface of the development board, press and hold the KEY1 (RECOVER) button on the development board, then connect the power cable to the board. After powering on for approximately 3 seconds, the development board will enter the downloadLOADER mode

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/刷新固件7.png
   :alt: 刷新固件7.png
   :width: 60%

- Click the "Upgrade" button to start flashing. When the flashing is successful, a success message will be displayed on the right side

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/刷新固件8.png
   :alt: 刷新固件8.png
   :width: 60%

Partial Firmware Flashing
---------------------------

- Flash one or more image files individually
- Copy the U-Boot image (uboot.img), Linux kernel image (boot.img), or filesystem image (rootfs.img) to be replaced, along with the mkimage/output/Image/parameter.txt (partition table) file, to a non-Chinese working directory in Windows
- Connect the Type-C flashing cable to the OTG2.0 interface of the development board, press and hold the KEY1 button on the board, then connect the power cable. After powering on for about 3 seconds, the development board will enter the downloadLOADER mode. Click to read the partition table from the device and follow the steps in the figure below to perform the flashing

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/刷新固件9.png
   :alt: 刷新固件9.png
   :width: 60%

- After the flashing is completed, power on the development board again.