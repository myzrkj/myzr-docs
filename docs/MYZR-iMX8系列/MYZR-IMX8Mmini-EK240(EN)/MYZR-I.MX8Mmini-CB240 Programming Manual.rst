MYZR-I.MX8Mmini-CB240 Programming Manual
============================================

**download file**

|  Open the network disk to "2.1_OS_Linux-4.14.98 -> 01_ManufacturingToolkit", download the "UUU-MYIMX8MM-L4.14.98" directory and the "UUU-MYIMX8MM-L4.14.98-Patch.*.rar" compressed package.

**unzip files**

|  Unzip MYIMX8MM-L4.14.98-Patch.*.rar, copy fsl-image-validation-myimx8m.tar.bz2 and fsl-image-validation-myimx8m.manifest to image-rootfs-L4.14.98 directory.

**Connect the programming line**

|  Power off the development board and connect the programming port of the development board to the PC with a USB cable.

**Dial code to download mode**

|  and set the "Boot Mode" of the development board to "OFF ON".

**Perform burning**

|  Power on the development board, double-click to run the "myimx8mmek240-8mm.bat" file, then the Windows command line window will see the following information:

.. code-block:: shell

   <code>uuu (Universal Update Utility) for nxp imx chips -- libuuu_1.2.135-0-gacaf035
   Success 0    Failure 0
   1:32    ......
   </code>

**Burning complete**

|  After the burning is completed, the Windows command line window information is as follows:

.. code-block:: shell

   <code>uuu (Universal Update Utility) for nxp imx chips -- libuuu_1.2.135-0-gacaf035
   Success 1    Failure 0
   1:32    24/24 [Done                                  ] FBK: DONE
   请按任意键继续. . .
   </code>

**Start the development board**

|  Power off the development board, switch "Boot Mode" to "ON OFF", and power on the development board, the development board can start normally