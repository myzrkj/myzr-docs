Firmware Flashing Manual
==========================

Download Files
----------------

|  Open the network disk and download the directory "uuu-5.10.72-imx8mp" and the compressed package "uuu-5.10.72-imx8mp.patch.*.zip".

Unzip Files
-------------

|  Unzip **uuu-5.10.72-imx8mp.patch.*.zip** to the **uuu-5.10.72-imx8mp** directory.

Connect the Flashing Cable
----------------------------

|  Power off the development board, and use a USB cable to connect the flashing port (DOWNLOAD) of the development board to the PC.

Set DIP Switches to Flashing Mode
-----------------------------------

|  Set the "SW3" of the development board to *Flashing Mode*.

+------------+------------+------------+------------+---------------+
| BOOT_MODE3 | BOOT_MODE2 | BOOT_MODE1 | BOOT_MODE0 | Description   |
+------------+------------+------------+------------+---------------+
| 0          | 0          | 0          | 1          | Flashing Mode |
+------------+------------+------------+------------+---------------+
| 0          | 0          | 1          | 0          | Boot Mode     |
+------------+------------+------------+------------+---------------+


|  Note: The ON (1) side of the DIP switch is the side with letters, and the OFF (0) side is the side with numbers.


Execute Flashing
------------------

|  Power on the development board.

|  If it is a 4GB DDR core board, double-click to run the file "myimx8mpek314-wic-full.bat".

|  If it is a 2GB DDR core board, double-click to run the file "myimx8mpek314-wic-2g-full.bat".

|  At this point, the following information will be displayed in the Windows command prompt window:

::

   uuu (Universal Update Utility) for nxp imx chips -- libuuu_1.4.243-0-ged48c51
   Success 0    Failure 0
   1:32    ......

Flashing Completed
--------------------

|  After the flashing is completed, the information in the Windows command prompt window is as follows:

::

   uuu (Universal Update Utility) for nxp imx chips -- libuuu_1.4.243-0-ged48c51
   Success 1    Failure 0
   1:32    24/24 [Done                                  ] FBK: DONE
   Press any key to continue. . .

Boot the Development Board
----------------------------

|  Power off the development board, set "SW3" to *Boot Mode*, then power on the development board, and the development board will start normally.
