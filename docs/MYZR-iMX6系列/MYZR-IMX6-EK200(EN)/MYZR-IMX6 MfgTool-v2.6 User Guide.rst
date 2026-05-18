MYZR-IMX6 MfgTool-v2.6 User Guide(EN)
========================================

System version supported by development board
-----------------------------------------------

|   First, it is necessary to understand the system versions supported by the development board and select the corresponding **system version**.

**Supported Linux System Version**

+----------------------+-----------------+------------------+-----------------+-----------------+-----------------+
| Linux System Version | MYZR-IMX6-EK140 | MYZR-IMX6-EK140P | MYZR-IMX6-EK200 | MYZR-IMX6-EK314 | MYZR-IMX6-EK336 |
+----------------------+-----------------+------------------+-----------------+-----------------+-----------------+
| Linux-3.0.35         |                 |                  | √               | √               |                 |
+----------------------+-----------------+------------------+-----------------+-----------------+-----------------+
| Linux-3.14.52        |                 |                  | √               | √               | √               |
+----------------------+-----------------+------------------+-----------------+-----------------+-----------------+
| Linux-4.1.15         | √               | √                | √               | √               | √               |
+----------------------+-----------------+------------------+-----------------+-----------------+-----------------+
| Linux-4.9.88         | √               | √                | Debugging       | Debugging       | Debugging       |
+----------------------+-----------------+------------------+-----------------+-----------------+-----------------+

**Supported QT version**

|   【Linux-3.0.35】：QT-4.8.5
|   【Linux-3.14.52】：QT-5.5.0
|   【Linux-4.1.15】：QT-5.6.1
|   【Linux-4.9.88】：QT-5.9.4

**Supported Android System Version**

+------------------------+-----------------+------------------+-----------------+-----------------+-----------------+
| Android System Version | MYZR-IMX6-EK140 | MYZR-IMX6-EK140P | MYZR-IMX6-EK200 | MYZR-IMX6-EK314 | MYZR-IMX6-EK336 |
+------------------------+-----------------+------------------+-----------------+-----------------+-----------------+
| Android-4.2.2          |                 |                  | √               |                 |                 |
+------------------------+-----------------+------------------+-----------------+-----------------+-----------------+
| Android-4.4.2          |                 |                  | √               | √               |                 |
+------------------------+-----------------+------------------+-----------------+-----------------+-----------------+
| Android-5.1.1          |                 |                  | √               | √               | √               |
+------------------------+-----------------+------------------+-----------------+-----------------+-----------------+


Prepare to burn tool
----------------------

**Download Burn Tool**

1. Open the corresponding *_OS_* directory according to the desired target system, and click 01_ManufacturingToolkit.

|   MYZR-IMX6-EK140、MYZR-IMX6-EK140P 下载 MY-IMX-A7 目录。
|   MYZR-IMX6-EK200、MYZR-IMX6-EK314、MYZR-IMX6-EK3336 下载 MY-IMX-A9 目录。

2. Unpack the downloaded file to the current folder.

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY_WinRAR_Extract.png
   :alt: MY_WinRAR_Extract.png

**Configure Burn Tool**

1. Run burn tool configuration MfgConfig.exe.
2. 【Evaluation Kit】: According to their own development board main model selection.
3. 【CPU Type】: Choose according to your own development board specifications.
4. 【Memory Size】:Choose according to your own development board specifications(if you are not sure, try selecting Default first).
5. 【OS Select】:Choose according to the directory system you need.
6. 【Rootfs File】:If optional, it is recommended to select one with QT.
7. Click Make, and the configuration tool generates the profile "cfg. ini" used by the burn tool.
8. Run burn tool main program MfgTool2.exe（if reported wrong, try to copy burn tool to another computer for operation).

**Document System Description**

|  fsl-image-qt5-validation contain fsl-image-validation；
|  core-image-sato contain core-image-base；
|  For the list of file systems, see the corresponding manifest file in "Pro Files/linux/os / Image-\*-rootfs".

Burn system for development board
-----------------------------------

**Put the development board in download mode**

|   Find the two dial switches indicated on the development board BOOTMODE or BOOT SWITCH, 1 dial to ON, 2 dial to OFF.

**Connect development board and computer**

1. Connect the development board and computer with the MiniUSB cable(to ensure the stability of the burn, use the computer's rear USB port. If USB HUB is used, connect to USB HUB).
2. Connect the development board and computer with a serial port line, refer to :doc:`《Terminal Software Reference Manual》 </docs/COMMON/Xshell.RM Reference Manual >` In **connection to session** Open serial session.
3. Connect the power cord for the development board and then power it.

**Burn system to development board**

1. 1. To avoid unnecessary errors, close the burn tool main program ** MfgTools 2. EXE ** and rerun.

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY_IMX6_MfgTool_3.3.0.1.jpg
   :alt: MY_IMX6_MfgTool_3.3.0.1.jpg

|  If the main program starts with an error, close MfgPool in the Windows Task Manager's process list and then run the main program.
|  If the main program displays No Development Connected, you need to check the connection of the MiniUSB line and confirm whether the dial of the development board is in download mode.

2. Click Start button on the main interface of the burn tool to Start the burn.

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY_IMX6_MfgTool_3.5.0.1.jpg
   :alt: MY_IMX6_MfgTool_3.5.0.1.jpg

3. During the burning process, the PC will recognize the assessment board as a storage device. At this time, a dialogue box will pop up to indicate whether it needs to be formatted. Here, please cancel or ignore the dialogue box or close the dialogue box.

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY_IMX6_MfgTool_3.5.0.2.jpg
   :alt: MY_IMX6_MfgTool_3.5.0.2.jpg

4. After the burn is completed, the information bar will output Done and the status bar will become green. Click Stop to complete the burn. Click Exit to exit MFG Tools.

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY_IMX6_MfgTool_3.5.0.3.jpg
   :alt: MY_IMX6_MfgTool_3.5.0.3.jpg

**Burn error handling**

1. Observe and retain the content of the information on the main program of the burning tool. This information will indicate the specific stage of the burning error.
2. Observe and retain the information on the last part of the computer serial terminal software. This information will indicate the specific reason for the burning error.

|   Tip:If you can't read it, you can send these two parts to our email(Service@myzr.com.cn) or the bbs.myzr.com.cn for support.

**Start the development board**

1. After the burn is completed, turn off the power of the development board.
2. Find the two-bit dialing SWITCH indicated by BOOTMODE or BOOT SWITCH ON the development board and dial 1 to OFF and 2 to ON.
3. Make the development board power, serial terminal software to see the system startup information on the right.

Production and use of burning tools
--------------------------------------

**Configure burning tools to burn multiple devices at the same time**

|  Our current burning tool can burn seven devices at the same time by: opening the UICfg.ini，in the burning tool, and changing portmgrDlg = 1 to portmgrDlg = 7.
|  Then the computer connects seven devices through USB HUB, and then opens the burning tool and follows the burning process.

**Burn your own compiled Image**

|  According to the later system version and the corresponding file relationship table, replace the corresponding files in the burning tool with the files compiled by itself, and re-burn the system for the development board.
|  For example: u-Boot compiled the Linux -3.14.52 MYZR-IMX6-EK200-6Q-1G development board, Then open the burn tool to * image-L3.14.52-Uboot ** directory to replace the compiled u-boot file with uboot-myimx6ek 200-6q.imx.

**Burn your own application**

|  Pack your application as my-demo.tar.bz2，And according to the back System Version and Corresponding File Relation Table，Replace the my-demo.tar.bz2，and for the development of the board re-burn system.
|  【Instructions】：my-demo.tar.bz2 will be burned to the root directory of the development board.

**Burn your own file system update**

|  According to the following System Version and Corresponding File Relation Table，Pack your own update package, replace the corresponding files in the burning tool, and re-burn the system for the development board.
|  【Instructions】：The file system update package will be burned to the root directory of the development board.

**Burning tool, continuous burning.**

|  In the production process, if you do not make changes to the configuration of the burning tool, you do not need to repeatedly exit and run the burning tool, even without clicking the STOP button of the burning tool master program. When a device is burned, the device can be turned off. After the new device is plugged in, the burning tool will burn the device.

Addendum
-----------

**Table 1: System version and corresponding file relationship table**

+----------------+----------------------------+----------------------------+--------------------------------------------------------------+
| System Version |         File Type          |      Locate directory      |                      Corresponding file                      |
+================+============================+============================+==============================================================+
| Linux-4.9.88   | U-Boot file                | Profiles/Linux/OS Firmware | image-L4.9.88-uboot/uboot-<ek_name>-<ek_spec>.imx            |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | Environment Variable File  |                            | image-L4.9.88-uboot/my_environment*.scr                      |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | Kernel file                |                            | image-L4.9.88-kernel/zImage-myimx6[a7 / a9]                  |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | 内核模块包                 |                            | image-L4.9.88-kernel/kernel-modules-myimx6[a7 / a9].tar.bz2  |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | 设备树文件                 |                            | image-L4.9.88-dtb/<ek_name>-<ek_spec>.dtb                    |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | 文件系统更新包             |                            | image-L4.9.88-update/L4988-rootfs-update.tar.bz2             |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | MYZR Demo                  |                            | image-L4.9.88-update/my-demo.tar.bz2                         |
+----------------+----------------------------+----------------------------+--------------------------------------------------------------+
| Linux-4.1.15   | U-Boot file                | Profiles/Linux/OS Firmware | image-L4.1.15-uboot/uboot-<ek_name>-<ek_spec>.imx            |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | Kernel file                |                            | image-L4.1.15-kernel/zImage-myimx6[a7 / a9]                  |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | Kernel module package      |                            | image-L4.1.15-kernel/kernel-modules-myimx6[a7 / a9].tar.bz2  |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | Device Tree File           |                            | image-L4.1.15-dtb/<ek_name>-<ek_spec>.dtb                    |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | File System Update Package |                            | image-L4.1.15-update/L4115-rootfs-update.tar.bz2             |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | MYZR Demo                  |                            | image-L4.1.15-update/my-demo.tar.bz2                         |
+----------------+----------------------------+----------------------------+--------------------------------------------------------------+
| Linux-3.14.52  | U-Boot file                | Profiles/Linux/OS Firmware | image-L3.14.52-uboot/uboot-<ek_name>-<ek_spec>.imx           |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | Kernel file                |                            | image-L3.14.52-kernel/zImage-myimx6[a9 / a7 ]                |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | Kernel module package      |                            | image-L3.14.52-kernel/kernel-modules-myimx6[a9 / a7].tar.bz2 |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | Device Tree File           |                            | image-L3.14.52-dtb/<ek_name>-<ek_spec>.dtb                   |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | File System Update Package |                            | image-L3.14.52-update/L31452-rootfs-update.tar.bz2           |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | MYZR Demo                  |                            | image-L3.14.52-update/my-demo.tar.bz2                        |
+----------------+----------------------------+----------------------------+--------------------------------------------------------------+
| Linux-3.0.35   | U-Boot file                | Profiles/Linux/OS Firmware | image-L3.0.35-uboot/uboot-<ek_name>-<ek_spec>.imx            |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | Kernel file                |                            | image-L3.0.35-kernel/zImage-myimx6a9                         |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | Kernel module package      |                            | image-L3.0.35-kernel/kernel-modules-myimx6a9.tar.bz2         |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | File System Update Package |                            | image-L3.0.35-update/L3035-rootfs-update.tar.bz2             |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | MYZR Demo                  |                            | image-L3.0.35-update/my-demo.tar.bz2                         |
+----------------+----------------------------+----------------------------+--------------------------------------------------------------+
| Android-5.1.1  | U-Boot file                | Profiles/Linux/OS Firmware | image-android-511/uboot-ard511-<ek_name>-<ek_spec>.bin       |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | Boot Image                 |                            | image-android-511/boot-ard511-<ek_name>.img                  |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | Recovery Image             |                            | image-android-511/recovery-ard511-<ek_name>.img              |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | System Image               |                            | image-android-511/system-ard511.img                          |
+----------------+----------------------------+----------------------------+--------------------------------------------------------------+
| Android-4.4.2  | U-Boot file                | Profiles/Linux/OS Firmware | image-android-442/uboot-ard442-<ek_name>-<ek_spec>.bin       |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | Boot Image                 |                            | image-android-442/boot-ard442-<ek_name>.img                  |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | Recovery Image             |                            | image-android-442/recovery-ard442-<ek_name>.img              |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | System Image               |                            | image-android-442/system-ard442-<ek_name>.img                |
+----------------+----------------------------+----------------------------+--------------------------------------------------------------+
| Android-4.2.2  | U-Boot file                | Profiles/Linux/OS Firmware | image-android-422/uboot-ard422-<ek_name>-<ek_spec>.bin       |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | Boot Image                 |                            | image-android-422/boot-ard422-<ek_name>.img                  |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | Recovery Image             |                            | image-android-422/recovery-ard422-<ek_name>.img              |
+                +----------------------------+                            +--------------------------------------------------------------+
|                | System Image               |                            | image-android-422/system-ard422-<ek_name>.img                |
+----------------+----------------------------+----------------------------+--------------------------------------------------------------+