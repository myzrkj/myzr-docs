Firmware Flashing
===================

Installing the DriverAssitant Driver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Locate the Rockchip USB driver installation package in the downloaded network disk materials. The path is: 3. Software Materials --> 3.2 - Tools --> DriverAssitant_v5.11.zip
- Extract DriverAssitant_v5.11.zip and navigate to the DriverAssitant_v5.11 folder
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

Flashing with the RKDevTool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Find the RKDevTool driver installation package in the downloaded network disk materials. The path is: 3. Software Materials --> 3.2 - Tools --> RKDevTool_Release_v3.15.zip
- Extract RKDevTool_Release_v3.15.zip and enter the RKDevTool_Release_v3.15 folder
- Double-click RKDevTool.exe to launch the program

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/刷新固件5.png
   :alt: 刷新固件5.png
   :width: 60%

Individual Flashing
^^^^^^^^^^^^^^^^^^^^^

Flashing U-Boot
"""""""""""""""""

- Connect the programming cable to the development board, press and hold the VOL+1 button on the development board (confirm the button position by referring to the silkscreen), then power on the development board. After approximately 3 seconds of power-on, the development board will enter download mode. Click the position shown below and select the corresponding uboot.img file

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/uboot_01.png
   :alt: uboot_01.png
   :width: 60%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/uboot_02.png
   :alt: uboot_02.png
   :width: 60%

- Follow the sequence shown in the figure below to complete the checking process. Click "Device Partition Table" and then click "Yes" in the pop-up window

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/uboot_03.png
   :alt: uboot_03.png
   :width: 60%

- Click "OK" to complete the partition table reading

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/uboot_04.png
   :alt: uboot_04.png
   :width: 60%

- Click the "Execute" button to start flashing U-Boot. Upon successful flashing, "Download Completed" will be displayed on the right side

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/uboot_05.png
   :alt: uboot_05.png
   :width: 60%

Flashing Boot
"""""""""""""""

- Connect the programming cable to the development board, press and hold the VOL+1 button on the development board (confirm the button position by referring to the silkscreen), then power on the development board. After approximately 3 seconds of power-on, the development board will enter download mode. Click the position shown below and select the corresponding boot.img file

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/boot_01.png
   :alt: boot_01.png
   :width: 60%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/boot_02.png
   :alt: boot_02.png
   :width: 60%

- Follow the sequence shown in the figure below to complete the checking process. Click "Device Partition Table" and then click "Yes" in the pop-up window

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/boot_03.png
   :alt: boot_03.png
   :width: 60%

- Click "OK" to complete the partition table reading

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/boot_04.png
   :alt: boot_04.png
   :width: 60%

- Click the "Execute" button to start flashing Boot. Upon successful flashing, "Download Completed" will be displayed on the right side

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/boot_05.png
   :alt: boot_05.png
   :width: 60%

Flashing Recovery
"""""""""""""""""""

- Connect the programming cable to the development board, press and hold the VOL+1 button on the development board (confirm the button position by referring to the silkscreen), then power on the development board. After approximately 3 seconds of power-on, the development board will enter download mode. Click the position shown below and select the corresponding recovery.img file

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/recovery_01.png
   :alt: recovery_01.png
   :width: 60%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/recovery_02.png
   :alt: recovery_02.png
   :width: 60%

- Follow the sequence shown in the figure below to complete the checking process. Click "Device Partition Table" and then click "Yes" in the pop-up window

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/recovery_03.png
   :alt: recovery_03.png
   :width: 60%

- Click "OK" to complete the partition table reading

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/recovery_04.png
   :alt: recovery_04.png
   :width: 60%

- Click the "Execute" button to start flashing Recovery. Upon successful flashing, "Download Completed" will be displayed on the right side

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/recovery_05.png
   :alt: recovery_05.png
   :width: 60%

Flashing Rootfs
"""""""""""""""""

- Connect the programming cable to the development board, press and hold the VOL+1 button on the development board (confirm the button position by referring to the silkscreen), then power on the development board. After approximately 3 seconds of power-on, the development board will enter download mode. Click the position shown below and select the corresponding rootfs.img file

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/rootfs_01.png
   :alt: rootfs_01.png
   :width: 60%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/rootfs_02.png
   :alt: rootfs_02.png
   :width: 60%

- Follow the sequence shown in the figure below to complete the checking process. Click "Device Partition Table" and then click "Yes" in the pop-up window

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/rootfs_03.png
   :alt: rootfs_03.png
   :width: 60%

- Click "OK" to complete the partition table reading

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/rootfs_04.png
   :alt: rootfs_04.png
   :width: 60%

- Click the "Execute" button to start flashing Rootfs. Upon successful flashing, "Download Completed" will be displayed on the right side

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/rootfs_05.png
   :alt: rootfs_05.png
   :width: 60%

Full Flashing
^^^^^^^^^^^^^^^^

- Click to enter the "Upgrade Firmware" interface

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/刷新固件6.png
   :alt: 刷新固件6.png
   :width: 60%

- Click the "Firmware" button, then select the corresponding img image file

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/刷新固件7.png
   :alt: 刷新固件7.png
   :width: 60%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/刷新固件8.png
   :alt: 刷新固件8.png
   :width: 60%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/刷新固件9.png
   :alt: 刷新固件9.png
   :width: 60%

- Connect the programming cable to the development board, press and hold the VOL+1 button on the development board (confirm the button position by referring to the silkscreen), then power on the development board. After approximately 3 seconds of power-on, the development board will enter download mode

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/刷新固件10.png
   :alt: 刷新固件10.png
   :width: 60%

- Click the "Upgrade" button to start flashing. Upon successful flashing, success characters will be displayed on the right side

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/刷新固件11.png
   :alt: 刷新固件11.png
   :width: 60%

- After the flashing is completed, the development board system will restart automatically.