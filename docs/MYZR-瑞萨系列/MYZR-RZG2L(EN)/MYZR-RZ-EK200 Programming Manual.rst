MYZR-RZ-EK200 Programming Manual
==================================

| There are multiple programming methods, and different images correspond to different programming methods. This document will introduce various image programming methods, and users can choose one or more methods to update the image according to the conditions of their development project.

mytool Programming
--------------------

**This method is only used to update the uboot image and is also the only update method for the uboot image of the current version.**

| The software compression package is located in MYZR-RZ -> 05 Others -> mytool.rar. Extract the compression package and enter the mytool folder.
| Double-click to open mytool.exe

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/Mytool_1.png
   :alt: Mytool_1.png

| Click the Browse button to select the directory where the image is stored (MYZR-RZ -> 01_Programming -> rzg2l/rzg2ul/rzfive folder). Take programming rzg2l as an example.

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/Mytool_2.png
   :alt: Mytool_2.png

| Ensure that the development board is connected to the serial cable, select the COM port, and click the Connect button. (Make sure the COM port of the development board is not opened in other software.)

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/Mytool_3.png
   :alt: Mytool_3.png

| Ensure that the boot dip switch of the development board is set to programming mode, then power on the development board again or press the reset button of the development board. The text window at the top of mytool displays the words "SCIF Download mode".

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/Mytool_4.png
   :alt: Mytool_4.png

| Click the One-key operation button to start programming.
| Alternatively, you can skip the one-key operation button: first click the Loading mot button to load the image, then click Writing uboot to start programming. bl2 is the factory firmware and generally does not need to be updated. After programming is completed, click the Disconnect button to terminate the connection.

TF Card Programming
----------------------

**TF card programming can be used to update the kernel, device tree, and file system. This method enables comprehensive image update, features simple subsequent operations, and is suitable for programming in the production stage.**

| Requirements for TF card: Ensure that the TF card has one partition (Partition 1), and the storage space of Partition 1 is larger than the total storage space of all programming images.
| Connect the TF card to the computer via a card reader, and copy the following images to the TF card. Image directory (MYZR-RZ -> 01_Programming -> rzg2l/rzg2ul/rzfive folder)

+----------+-------------+----------------------------------------------------+
|  Model   | Image Type  |                     Image Name                     |
+==========+=============+====================================================+
| rzg2l    | Kernel      | Image                                              |
+          +-------------+----------------------------------------------------+
|          | Device Tree | myzr-rzg2l-dsi.dtb                                 |
+          +             +                                                    +
|          |             | myzr-rzg2l-rgb.dtb                                 |
+          +-------------+----------------------------------------------------+
|          | File System | core-image-qt-myzr-rzg2l-Release.xxx.tar.bz2       |
+          +-------------+----------------------------------------------------+
|          | ramdisk     | core-image-mini-myzr-rzg2l-mod.cpio.gz.uboot       |
+----------+-------------+----------------------------------------------------+
| rzg2ul   | Kernel      | Image                                              |
+          +-------------+----------------------------------------------------+
|          | Device Tree | myzr-rzg2ul-eth.dtb                                |
+          +             +                                                    +
|          |             | myzr-rzg2ul-lcd.dtb                                |
+          +-------------+----------------------------------------------------+
|          | File System | core-image-bsp-myzr-rzg2ul-Release.xxx.tar.bz2     |
+          +-------------+----------------------------------------------------+
|          | ramdisk     | core-image-mini-myzr-rzg2ul-mod.cpio.gz.uboot      |
+----------+-------------+----------------------------------------------------+
| rzfive   | Kernel      | Image                                              |
+          +-------------+----------------------------------------------------+
|          | Device Tree | myzr-rzfive-2g.dtb                                 |
+          +-------------+----------------------------------------------------+
|          | File System | core-image-minimal-myzr-rzfive-Release.xxx.tar.bz2 |
+          +-------------+----------------------------------------------------+
|          | ramdisk     | core-image-minimal-myzr-rzfive-mod.cpio.gz.u-boot  |
+----------+-------------+----------------------------------------------------+

**For the file system name, you need to remove the version number, that is, rename it to (core-image-qt-myzr-rzg2l.tar.bz2).**

| Insert the TF card into the TF card slot of the board, and start the board to enter the uboot command line mode:

.. code-block:: shell

   U-Boot 2021.10 (Feb 07 2023 - 11:36:41 +0800)

   CPU:   Renesas Electronics K rev 16.15
   Model: myzr-rzg2l
   DRAM:  1.9 GiB
   MMC:   sd@11c00000: 0, sd@11c10000: 1
   Loading Environment from MMC... OK
   In:    serial@1004b800
   Out:   serial@1004b800
   Err:   serial@1004b800
   Net:   
   Error: ethernet@11c20000 address not set.
   No ethernet found.

   Hit any key to stop autoboot:  0 
   =>

| Enter the following command to start the system from the TF card:

.. code-block:: shell

   => setenv startup_mode sd
   => boot

| After the system starts, enter the command to update the image:

.. code-block:: shell

   # ./sdupdate.sh

| Wait for the programming to complete, and the message "sdcard update succeed !!!" will be displayed. Restart the board to complete the update.

Image Replacement Update
--------------------------

**This method can independently update the kernel and device tree images, and is suitable for the development and debugging stage.**

1. After the development board starts, enter the following command to mount Partition 1 of the eMMC:

.. code-block:: shell

   # mount /dev/mmcblk0p1 /mnt/

2. Navigate to the mounted directory /mnt and delete the original image.
3. Then copy the new image to this directory.
4. Use the command to unmount the directory and restart the board.

.. code-block:: shell

   # umount /mnt/