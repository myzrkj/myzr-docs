Firmware Flashing Manual
==========================

File Download
----------------

|  Open the network disk and download the compressed package named "uuu-5.10.72-imx8mm.patch.*.zip" from the "uuu-5.10.72-imx8mm" directory.


File Extraction
------------------

|  Extract **uuu-5.10.72-imx8mm.patch.*.zip** to the **uuu-5.10.72-imx8mm** directory.

Connect the Flashing Cable
-----------------------------

|  Power off the development board, and use a USB cable to connect the flashing port (DOWNLOAD) of the development board to the PC.

Set DIP Switches to Flashing Mode
-----------------------------------

|  Set the "SW1" DIP switch of the development board to *Flashing Mode*.

+------------+------------+------------+------------+---------------+
| BOOT_MODE0 | BOOT_MODE1 | BOOT_MODE2 | BOOT_MODE3 | Description   |
+============+============+============+============+===============+
| 1          | 0          | 1          | 0          | Flashing Mode |
+------------+------------+------------+------------+---------------+
| 0          | 1          | 1          | 0          | Boot Mode     |
+------------+------------+------------+------------+---------------+

|  Note: The ON (1) position of the DIP switch is on the side with letters, and the OFF (0) position is on the side with numbers.

Execute Flashing
------------------

|  Power on the development board, double-click to run the file "auto-myimx8mmek200-ucp.bat". At this point, the following information will be displayed in the Windows command prompt window:

::

   uuu (Universal Update Utility) for nxp imx chips –libuuu_1.2.135-0-gacaf035
   Success 0 Failure 0 1:32 ……


Flashing Completion
----------------------

|  After the flashing is completed, the information in the Windows command prompt window is as follows:

::

   uuu (Universal Update Utility) for nxp imx chips –
   libuuu_1.2.135-0-gacaf035 Success 1 Failure 0 1:32 24/24 [Done ] FBK:
   DONE Press any key to continue. . .


Start the Development Board
------------------------------

|  Power off the development board, set the "SW1" DIP switch to *Boot Mode*, then power on the development board. The development board will start normally.
