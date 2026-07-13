.. raw:: html

   <style>
   h1 {
       color: green;
   }
   </style>

Firmware Update
===============

Install DriverAssitant Driver
-----------------------------

* Find the Rockchip USB driver installation package from the downloaded cloud materials. Path: 3.Software Materials --> 3.2-Tools --> DriverAssitant_v5.11.zip

* Extract DriverAssitant_v5.11.zip and enter the DriverAssitant_v5.11 folder

* Double-click DriverInstall.exe to start the driver installation. Follow these steps:

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/安装DriverAssitant驱动.png
   :alt: Install DriverAssitant Driver
   :width: 100%

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/安装DriverAssitant驱动_02.png
   :alt: Install DriverAssitant Driver_02
   :width: 100%

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/安装DriverAssitant驱动_03.png
   :alt: Install DriverAssitant Driver_03
   :width: 100%

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/安装DriverAssitant驱动_04.png
   :alt: Install DriverAssitant Driver_04
   :width: 100%

Flashing with RKDevTool
-----------------------

* Find the RKDevTool installation package from the downloaded cloud materials. Path: 3.Software Materials --> 3.2-Tools --> RKDevTool_Release_v3.15.zip

* Extract RKDevTool_Release_v3.15.zip and enter the RKDevTool_Release_v3.15 folder

* Double-click RKDevTool.exe to launch the program

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/使用RKDevTool工具进行刷机.png
   :alt: Flashing with RKDevTool
   :width: 100%

Individual Flashing
~~~~~~~~~~~~~~~~~~~

Flash U-Boot
^^^^^^^^^^^^

* Connect the programming cable to the development board's Type-C port U4 (refer to the silk screen diagram), hold down the VOL+ button (refer to the silk screen diagram), then power on the board. After about 3 seconds, the board will enter download mode. Click the following location to select the corresponding uboot.img file

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/烧录uboot.png
   :alt: Flash U-Boot
   :width: 100%

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/烧录uboot_02.png
   :alt: Flash U-Boot_02
   :width: 100%

* Follow the order shown in the image to complete the selection. Click "设备分区表" and then click "Yes" in the pop-up window

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/烧录uboot_03.png
   :alt: Flash U-Boot_03
   :width: 100%

* Click "OK" to complete reading the partition table

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/烧录uboot_04.png
   :alt: Flash U-Boot_04
   :width: 100%

* Click the "Execute" button to flash U-Boot. When successful, "Download Complete" will be displayed on the right

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/烧录uboot_05.png
   :alt: Flash U-Boot_05
   :width: 100%

Flash Boot
^^^^^^^^^^

* Connect the programming cable to the development board's Type-C port U4 (refer to the silk screen diagram), hold down the VOL+ button (refer to the silk screen diagram), then power on the board. After about 3 seconds, the board will enter download mode. Click the following location to select the corresponding boot.img file

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/烧录boot.png
   :alt: Flash Boot
   :width: 100%

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/烧录boot_02.png
   :alt: Flash Boot_02
   :width: 100%

* Follow the order shown in the image to complete the selection. Click "设备分区表" and then click "Yes" in the pop-up window

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/烧录boot_03.png
   :alt: Flash Boot_03
   :width: 100%

* Click "OK" to complete reading the partition table

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/烧录boot_04.png
   :alt: Flash Boot_04
   :width: 100%

* Click the "Execute" button to flash Boot. When successful, "Download Complete" will be displayed on the right

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/烧录boot_05.png
   :alt: Flash Boot_05
   :width: 100%

Flash Recovery
^^^^^^^^^^^^^^

* Connect the programming cable to the development board's Type-C port U4 (refer to the silk screen diagram), hold down the VOL+ button (refer to the silk screen diagram), then power on the board. After about 3 seconds, the board will enter download mode. Click the following location to select the corresponding recovery.img file

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/烧录recovery.png
   :alt: Flash Recovery
   :width: 100%

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/烧录recovery_02.png
   :alt: Flash Recovery_02
   :width: 100%

* Follow the order shown in the image to complete the selection. Click "设备分区表" and then click "Yes" in the pop-up window

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/烧录recovery_03.png
   :alt: Flash Recovery_03
   :width: 100%

* Click "OK" to complete reading the partition table

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/烧录recovery_04.png
   :alt: Flash Recovery_04
   :width: 100%

* Click the "Execute" button to flash Recovery. When successful, "Download Complete" will be displayed on the right

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/烧录recovery_05.png
   :alt: Flash Recovery_05
   :width: 100%

Flash Rootfs
^^^^^^^^^^^^

* Connect the programming cable to the development board's Type-C port U4 (refer to the silk screen diagram), hold down the VOL+ button (refer to the silk screen diagram), then power on the board. After about 3 seconds, the board will enter download mode. Click the following location to select the corresponding rootfs.img file

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/烧录rootfs.png
   :alt: Flash Rootfs
   :width: 100%

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/烧录rootfs_02.png
   :alt: Flash Rootfs_02
   :width: 100%

* Follow the order shown in the image to complete the selection. Click "设备分区表" and then click "Yes" in the pop-up window

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/烧录rootfs_03.png
   :alt: Flash Rootfs_03
   :width: 100%

* Click "OK" to complete reading the partition table

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/烧录rootfs_04.png
   :alt: Flash Rootfs_04
   :width: 100%

* Click the "Execute" button to flash Rootfs. When successful, "Download Complete" will be displayed on the right

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/烧录rootfs_05.png 
   :alt: Flash Rootfs_05
   :width: 100%

Full Flashing
~~~~~~~~~~~~~

* Click to enter the "Upgrade Firmware" interface

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/完整烧录.png
   :alt: Full Flashing
   :width: 100%

* Click the "Firmware" button and select the corresponding img image file

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/完整烧录_02.png
   :alt: Full Flashing_02
   :width: 100%

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/完整烧录_03.png
   :alt: Full Flashing_03
   :width: 100%

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/完整烧录_04.png
   :alt: Full Flashing_04
   :width: 100%

* Connect the programming cable to the development board's Type-C port U4 (refer to the silk screen diagram), hold down the VOL+ button (refer to the silk screen diagram), then power on the board. After about 3 seconds, the board will enter download mode

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/完整烧录_05.png
   :alt: Full Flashing_05
   :width: 100%

* Click the "Upgrade" button to flash. When successful, "Success" will be displayed on the right

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/完整烧录_06.png
   :alt: Full Flashing_06
   :width: 100%

* After flashing is complete, the development board system will automatically reboot.