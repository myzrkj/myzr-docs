Update Firmware
=================

Install DriverAssitant
~~~~~~~~~~~~~~~~~~~~~~~~

- Find the Rockchip USB driver installation package from the downloaded network disk data. The path is: 3. Software Materials --> 3.2 - Tools --> DriverAssitant_v5.11.zip
- Unzip DriverAssitant_v5.11.zip and enter the DriverAssitant_v5.11 folder
- Double - click the DriverInstall.exe program to install the driver. The installation steps are as follows:

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

Use RKDevTool for flashing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Find the RKDevTool driver installation package from the downloaded network disk data. The path is: 3. Software Materials --> 3.2 - Tools --> RKDevTool_Release_v3.15.zip
- Unzip RKDevTool_Release_v3.15.zip and enter the RKDevTool_Release_v3.15 folder
- Double - click RKDevTool.exe to open the program

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/刷新固件5.png
   :alt: 刷新固件5.png
   :width: 60%

Separate burning
^^^^^^^^^^^^^^^^^^

Burning uboot
"""""""""""""""

- Connect the burning cable to the Type - C interface U4 of the development board (determine the button according to the silkscreen diagram), press and hold the VOL + 1 button of the development board (determine the button according to the silkscreen diagram), then power on the development board. After about 3 seconds of power - on, you can see that the development board has entered the download mode. Click the following position and select the corresponding uboot.img file

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/uboot_01.png
   :alt: uboot_01.png
   :width: 60%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/uboot_02.png
   :alt: uboot_02.png
   :width: 60%

- Complete the check according to the following operation sequence, click "Device Partition Table" and then click "Yes" in the pop - up window

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/uboot_03.png
   :alt: uboot_03.png
   :width: 60%

- Click "OK" to finish reading the partition table

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/uboot_04.png
   :alt: uboot_04.png
   :width: 60%

- Click the "Execute" button to burn the uboot. If the burning is successful, "Download completed" will be displayed on the right

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/uboot_05.png
   :alt: uboot_05.png
   :width: 60%

Burning boot
""""""""""""""

- Connect the burning cable to the development board, press and hold the VOL + 1 button of the development board (determine the button according to the silkscreen diagram), then power on the development board. After about 3 seconds of power - on, you can see that the development board has entered the download mode. Click the following position and select the corresponding boot.img file

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/boot_01.png
   :alt: boot_01.png
   :width: 60%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/boot_02.png
   :alt: boot_02.png
   :width: 60%

- Complete the check according to the following operation sequence, click "Device Partition Table" and then click "Yes" in the pop - up window

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/boot_03.png
   :alt: boot_03.png
   :width: 60%

- Click "OK" to finish reading the partition table

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/boot_04.png
   :alt: boot_04.png
   :width: 60%

- Click the "Execute" button to burn the boot. If the burning is successful, "Download completed" will be displayed on the right

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/boot_05.png
   :alt: boot_05.png
   :width: 60%

Burning recovery
""""""""""""""""""

- Connect the burning cable to the development board, press and hold the VOL + 1 button of the development board (determine the button according to the silkscreen diagram), then power on the development board. After about 3 seconds of power - on, you can see that the development board has entered the download mode. Click the following position and select the corresponding recovery.img file

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/recovery_01.png
   :alt: recovery_01.png
   :width: 60%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/recovery_02.png
   :alt: recovery_02.png
   :width: 60%

- Complete the check according to the following operation sequence, click "Device Partition Table" and then click "Yes" in the pop - up window

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/recovery_03.png
   :alt: recovery_03.png
   :width: 60%

- Click "OK" to finish reading the partition table

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/recovery_04.png
   :alt: recovery_04.png
   :width: 60%

- Click the "Execute" button to burn the recovery. If the burning is successful, "Download completed" will be displayed on the right

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/recovery_05.png
   :alt: recovery_05.png
   :width: 60%

Burning rootfs
""""""""""""""""

- Connect the burning cable to the development board, press and hold the VOL + 1 button of the development board (determine the button according to the silkscreen diagram), then power on the development board. After about 3 seconds of power - on, you can see that the development board has entered the download mode. Click the following position and select the corresponding rootfs.img file

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/rootfs_01.png
   :alt: rootfs_01.png
   :width: 60%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/rootfs_02.png
   :alt: rootfs_02.png
   :width: 60%

- Complete the check according to the following operation sequence, click "Device Partition Table" and then click "Yes" in the pop - up window

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/rootfs_03.png
   :alt: rootfs_03.png
   :width: 60%

- Click "OK" to finish reading the partition table

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/rootfs_04.png
   :alt: rootfs_04.png
   :width: 60%

- Click the "Execute" button to burn the rootfs. If the burning is successful, "Download completed" will be displayed on the right

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/rootfs_05.png
   :alt: rootfs_05.png
   :width: 60%

Complete burning
^^^^^^^^^^^^^^^^^^

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

- Connect the burning cable to the development board, press and hold the VOL + 1 button of the development board (determine the button according to the silkscreen diagram), then power on the development board. After about 3 seconds of power - on, you can see that the development board has entered the download mode

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/刷新固件10.png
   :alt: 刷新固件10.png
   :width: 60%

- Click the "Upgrade" button to flash the device. If the flashing is successful, the success character will be displayed on the right

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/刷新固件11.png
   :alt: 刷新固件11.png
   :width: 60%

- After the burning is completed, the development board system will restart automatically.