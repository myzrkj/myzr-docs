Firmware Update
==================

Firmware Flashing via TF Card
--------------------------------

|  The PhoenixCard tool can be used to burn a Linux system image file to an SD card via a card reader, turning the SD card into a "boot card" or "mass production card".

1. Connect a blank SD card to the computer via a card reader, then double-click to launch the PhoenixCard system burning tool.

.. image:: /image/MYZR-全志系列/MYZR-T113-i-EK168/刷新固件1.png
   :alt: 刷新固件1.jpg
   :width: 60%

2. After the tool runs, it will automatically detect the SD card connected to the computer.
3. Click "Firmware" to select the target image to be burned, choose "Boot Card", and finally click "Burn Card".

.. image:: /image/MYZR-全志系列/MYZR-T113-i-EK168/刷新固件2.png
   :alt: 刷新固件2.jpg
   :width: 60%

4. Burning completed

.. image:: /image/MYZR-全志系列/MYZR-T113-i-EK168/刷新固件3.png
   :alt: 刷新固件3.jpg
   :width: 60%

5. Start the development board:

|  Power off the development board, insert the burned TF card into the Micro SD (CON7) interface of the development board, set the SW2 DIP switch to 0 to enable the Micro SD interface. Then power on the development board, and it will start normally.



Firmware Flashing via USB-to-Type-C Data Cable
-------------------------------------------------

1. Use a Type-C cable to connect the USB0 DRD interface of the development board to the USB interface of the PC.
2. Double-click PhoenixSuit_CN.msi to start the installation; you can use the default installation options. After the installation is complete, a shortcut will be created on the desktop.

.. image:: /image/MYZR-全志系列/MYZR-T113-i-EK168/刷新固件4.png
   :alt: 刷新固件4.jpg
   :width: 60%

3. Double-click to open the PhoenixSuit tool, click "One-Click Flashing", then click "Browse" to select the Linux system image file.

.. image:: /image/MYZR-全志系列/MYZR-T113-i-EK168/刷新固件5.png
   :alt: 刷新固件5.jpg
   :width: 60%

4. Power off the development board, press and hold the KEY1 button, then power on the development board. When the PhoenixSuit tool displays the interface as shown in the figure below, release the KEY1 button and select "Yes" on the PhoenixSuit tool interface.

.. image:: /image/MYZR-全志系列/MYZR-T113-i-EK168/刷新固件6.png
   :alt: 刷新固件6.jpg
   :width: 60%

5. The following interface indicates that the firmware flashing is completed.

.. image:: /image/MYZR-全志系列/MYZR-T113-i-EK168/刷新固件7.png
   :alt: 刷新固件7.jpg
   :width: 60%

6. Power off the development board, set the SW2 DIP switch to 1, and power it on again. The development board will automatically start the system from the EMMC.


Partition Burning
-------------------

|  Please open the PhoenixSuit tool, click "One-Click Flashing", then select the system image file. After that, check the "Single or Multiple Partitions" option. Once checked, the following partition options will appear. You can check the corresponding partitions for burning according to actual needs; if none are selected, only boot0 and boot1 (i.e., the boot_package.fex file) will be downloaded, which can be used to update U-Boot and the device tree.

.. image:: /image/MYZR-全志系列/MYZR-T113-i-EK168/刷新固件8.png
   :alt: 刷新固件8.jpg
   :width: 60%

|  BOOT-RESOURCE: Stores resources such as bootlogo.
|  ENV: Stores the U-Boot environment variable env.fex.
|  ENV-REDUND: Stores the U-Boot environment variable env.fex (redundant copy).
|  BOOT: Stores the kernel image boot.fex.
|  ROOTFS: Stores the file system image rootfs.fex.