MYZR-RK3399-EK314 Burn Manual
==============================

Ready to Burn Tool
--------------------


Download burning tool
~~~~~~~~~~~~~~~~~~~~~~

|   Download the burning tool :AndroidTool_Release_v2.58.zip Unzip AndroidTool_Release_v2.58.zip..

Download usb driver
~~~~~~~~~~~~~~~~~~~~~

|   Download the usb driver archive:DriverAssitant_v4.5.rar Install and extract DriverAssitant_v4.5.rar

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3399-EK314/My-rk3399-ek314_download_3.1.1.png
   :alt: My-rk3399-ek314_download_3.1.1.png

|   Double-click the red arrow file to install

Open burning tool
~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3399-EK314/My-rk3399-ek314_download_3.1.2.png
   :alt: My-rk3399-ek314_download_3.1.2.png

|   Double-click the red arrow file to open the burning tool

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3399-EK314/My-rk3399-ek314_download_3.1.3.png
   :alt: My-rk3399-ek314_download_3.1.3.png

Programming instructions
~~~~~~~~~~~~~~~~~~~~~~~~~~

- If you want to flash the unified firmware for all images, skip to the section "Flashing the same firmware".
- If you want to program the kernel, u-boot or file system separately, skip to the section "Program the kernel, u-boot or file system separately".

Flash unified firmware
~~~~~~~~~~~~~~~~~~~~~~~

- Click to upgrade firmware
- Click "Firmware" to select the firmware to be burned
- Using USB cable to connect development board and computer
- Press and hold the vol + button of the development board, turn on the power of the development board, and release the vol + button when the programming tool appears "发现一个LOADER设备"
- Click “升级” to flash

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3399-EK314/My-rk3399-ek314_download_3.1.4.png
   :alt: My-rk3399-ek314_download_3.1.4.png

**note**

|   Flashing from android system to ubuntu system requires flash to be erased before programming, and burning from ubuntu system to android system must also be erased before programming.

Write the kernel separately, u-boot or file system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Click to download mirror
- Right-click in the table and select Import Configuration, select the configuration file, and the configuration file is in the root directory of the programming tool. rk3399-config.cfg is the configuration of ubuntu16.04, rk3399-android81.cfg is the configuration of android8.1
- After importing the configuration, check the box before the image to be flashed.

.. code-block:: shell
    
    Loader：MiniLoaderAll.bin
    Parameter：parameter.txt
    Uboot：uboot.img
    Trust：trust.img
    Boot：boot.img
    Rootfs：rootfs.img

- Using USB cable to connect development board and computer
- Press and hold the vol + button of the development board, turn on the power of the board, and release the vol + button when the programming tool displays“发现一个LOADER设备”
- Click execute to start programming

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3399-EK314/My-rk3399-ek314_download_3.1.5.png
   :alt: My-rk3399-ek314_download_3.1.5.png
