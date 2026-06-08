Firmware Update
=================

Installation and Usage of Titan Flasher Tool
----------------------------------------------

Download Titan Flasher Tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


|   Select the corresponding version according to your operating system. This document demonstrates the Windows platform:

+----------------------------------------------+----------+---------+--------------------------------------------------------------------------------------------------------------------+
| Resource                                     | Platform | ARCH    | Download                                                                                                           |
+----------------------------------------------+----------+---------+--------------------------------------------------------------------------------------------------------------------+
| TITANTOOLS FOR WINDOWS (X86/X64) (INSTALLER) | WINDOWS  | X86/X64 | `Download <https://cloud.spacemit.com/prod-api/release/download/tools?token=titantools_for_windows_X86_X64>`_      |
+----------------------------------------------+----------+---------+--------------------------------------------------------------------------------------------------------------------+
| TITANTOOLS FOR LINUX X64 (64-BIT) (APPIMAGE) | LINUX    | X64     | `Download <https://cloud.spacemit.com/prod-api/release/download/tools?token=titantools_for_linux_64BIT_APPIMAGE>`_ |
+----------------------------------------------+----------+---------+--------------------------------------------------------------------------------------------------------------------+

Titan Flasher Tool Installation Steps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Double-click the downloaded titantools_for_windows-2.0.7-Rc.exe
2. Click Run

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/刷新固件1.png
   :alt: 刷新固件1.png
   :width: 60%

3. You can click Browse (B) to select the installation path (not demonstrated here), then click Install (I)

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/刷新固件2.png
   :alt: 刷新固件2.png
   :width: 60%

4. You can choose not to launch titanflasher, then click Finish (F)

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/刷新固件3.png
   :alt: 刷新固件3.png
   :width: 60%

Titan Flasher Tool Operation Steps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Enter the titanflasher directory and open titanflasher.exe

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/刷新固件4.png
   :alt: 刷新固件4.png
   :width: 60%

2. Click R&D Tools

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/刷新固件5.png
   :alt: 刷新固件5.png
   :width: 60%

3. Click Standalone Burning

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/刷新固件6.png
   :alt: 刷新固件6.png
   :width: 60%

4. Connect one end of the Type-C cable to U18 and the other end to the rear USB port of the computer; toggle the SW2 DIP switch of the development board to burning mode; connect 12V power to CON1 and switch POW_KEY to ON to power on the development board.

+------------+------------+------------+------------+--------------+
| QSPI_DATA0 | QSPI_DATA1 | QSPI_DATA2 | QSPI_DATA3 | Description  |
+------------+------------+------------+------------+--------------+
| 0          | 0          | 0          | 1          | Burning Mode |
+------------+------------+------------+------------+--------------+
| 0          | 0          | 0          | 0          | Boot Mode    |
+------------+------------+------------+------------+--------------+

|   Note: For the DIP switch, ON (1) refers to the letter side, and OFF (0) refers to the number side

5. Click Scan Device

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/刷新固件7.png
   :alt: 刷新固件7.png
   :width: 60%

|   The device will be recognized in a few seconds

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/刷新固件8.png
   :alt: 刷新固件8.png
   :width: 60%

6. Click Select Firmware File

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/刷新固件9.png
   :alt: 刷新固件9.png
   :width: 60%

7. Double-click bianbu-linux-k1_v2.zip

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/刷新固件10.png
   :alt: 刷新固件10.png
   :width: 60%

8. After selection, click Start Burning. If debug serial port and HDMI are connected, burning logs can be viewed.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/刷新固件11.png
   :alt: 刷新固件11.png
   :width: 60%

9. Wait until the burning process is completed successfully

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/刷新固件12.png
   :alt: 刷新固件12.png
   :width: 60%

Independent Burning of Kernel and Device Tree
-----------------------------------------------

1. Connect one end of the Type-C cable to Debug and the other end to the computer USB port; connect 12V power to CON1, toggle the SW2 DIP switch of the development board to boot mode, and switch POW_KEY to ON to power on the development board.

+------------+------------+------------+------------+--------------+
| QSPI_DATA0 | QSPI_DATA1 | QSPI_DATA2 | QSPI_DATA3 | Description  |
+------------+------------+------------+------------+--------------+
| 0          | 0          | 0          | 1          | Burning Mode |
+------------+------------+------------+------------+--------------+
| 0          | 0          | 0          | 0          | Boot Mode    |
+------------+------------+------------+------------+--------------+

|   Note: For the DIP switch, ON (1) refers to the letter side, and OFF (0) refers to the number side

2. After system startup, when `Bianbu login:` is displayed, log in with the following information:

|   Username: root
|   Password: bianbu

3. Copy the compiled Image and k1-x_deb1.dtb files to the development board system.
4. Run the command `mount /dev/mmcblk2p5 /mnt/`, replace `/mnt/Image` and `/mnt/k1-x_deb1.dtb`, execute `sync`, then run `reboot` to restart the development board.

Replace Camera Module Library
-------------------------------

|   After the development board starts up, copy `output\k1_v2\build\k1x-cam-0.0.11\demo\libsdkcam.so` and `output\k1_v2\build\k1x-cam-0.0.11\sensors\libcam_sensors.so` to the development board, and replace `/usr/lib/libsdkcam.so` and `/usr/lib/libcam_sensors.so`.

