MYZR-IMX8M-EK300 Programming Manual
=======================================

download file
-----------------

|  Open the network disk to “2.1_OS_Linux-4.14.98 -> 01_ManufacturingToolkit”，download “UUU-MYIMX8M-L4.14.98” Directory and “UUU-MYIMX8M-L4.14.98-Patch.*.rar” Archive。


unzip files
--------------

|  Unzip MYIMX8M-L4.14.98-Patch.*.rar，Copy fsl-image-validation-myimx8m.tar.bz2 and fsl-image-validation-myimx8m.manifest to image-rootfs-L4.14.98 Directory。


Connect the programming cable
----------------------------------

|  To power off the development board, connect the programming port of the development board to the PC with a USB cable.


Dial to download mode
------------------------

|  And set the "Boot Mode" of the development board to "OFF ON"。


Perform burning
------------------

|  Power on the development board and double-click to run the "myimx8mek300-8mq.bat" file. At this time, the Windows command line window will see the following information:

.. code-block:: shell

   uuu (Universal Update Utility) for nxp imx chips -- libuuu_1.2.135-0-gacaf035
   Success 0    Failure 0
   1:32    ......

Burning completed
-------------------

|  After the programming is complete, the Windows command line window information is as follows：

.. code-block:: shell

   uuu (Universal Update Utility) for nxp imx chips -- libuuu_1.2.135-0-gacaf035
   Success 1    Failure 0
   1:32    24/24 [Done                                  ] FBK: DONE
   请按任意键继续. . .

Start development board
--------------------------

|  Power off the development board, set "Boot Mode" to "ON OFF", and power on the development board, the development board can start normally.