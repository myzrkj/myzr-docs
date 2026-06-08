MYZR-SSD2351-EK112 Programming Manual
=======================================

USB Interface Download
~~~~~~~~~~~~~~~~~~~~~~~~

| Programming mode DIP switch settings: 1: on, 2: off, 3: off, 4: off
| Programming tool: UsbFactoryTool_1.0.0.19.tar.gz
| Image file: SstarUsbImage_202503050415.bin

Extract the Programming Tool
------------------------------

| Right-click to extract to the current directory. My computer is 64-bit, so select the tool USB_Factory_Tool_64_1.0.0.19.exe

Set Sheet Metal Programming Mode
-----------------------------------

| Programming mode DIP switch settings: 1: on, 2: off, 3: off, 4: off

Download
----------

| Connect the power supply and USB cable, and the computer detects the "USB mass storage device"

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/烧录手册01.png
   :alt: 烧录手册01.png
   :width: 60%

Double-click the programming tool, USB_Factory_Tool_64_1.0.0.19.exe, as follows:

1. You can see the detected device
2. Select the firmware to be programmed
3. Click the green button to start programming

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/烧录手册02.png
   :alt: 烧录手册02.png
   :width: 60%

4. When the progress reaches 100%, click the red stop button to end

Flash_Tool Programming
~~~~~~~~~~~~~~~~~~~~~~~~

| Programming tool: FlashTool_5.0.52.tar.gz
| This method is applicable for blank chip programming or when the board cannot enter the Uboot console.
| If it is not a blank chip or can start normally and you want to use Flash Tool for programming, you need to turn off Debug Uart first as follows

- Under the uboot console, directly enter `debug`, then close the serial terminal

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/烧录手册03.png
   :alt: 烧录手册03.png
   :width: 60%

- Under the kernel, enter `11111`, then close the serial terminal

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/烧录手册04.png
   :alt: 烧录手册04.png
   :width: 60%

1. Power on, and ensure that the serial port log cannot reach the uboot console (if it can start normally, you need to enter the debug command in the uboot console first to stop the serial port debugging function)
2. Close the serial debugging terminal
3. The necessary partitions and their starting addresses required to boot to Uboot

| Nand Flash:

+-------------+----------+--------------------------------------+
| Binary file |  offset  |      Binary placement directory      |
+=============+==========+======================================+
| cis.bin     | 0x00000  | project\image\output\images\cis.bin  |
+-------------+----------+--------------------------------------+
| cis.bin     | 0x20000  | project\image\output\images\cis.bin  |
+-------------+----------+--------------------------------------+
| boot.bin    | 0x140000 | project\image\output\images\boot.bin |
+-------------+----------+--------------------------------------+

| Program the cis.bin image (program both 0x00000 and 0x20000)

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/烧录手册05.png
   :alt: 烧录手册05.png
   :width: 60%

| Program the boot.bin image

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/烧录手册06.png
   :alt: 烧录手册06.png
   :width: 60%

TFTP Server Programming
~~~~~~~~~~~~~~~~~~~~~~~~~

| #Open the TFTP server, the default path of the compiled image is project/image/output/images. Copy the image to the computer, select Browse to set the path, as follows:

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/烧录手册07.png
   :alt: 烧录手册07.png
   :width: 60%

| #The board needs to enter the boot mode: Boot DIP switch mode: 1: on, 2: on, 3: off, 4: off
| #Insert the TYPE-C cable, power on and hold Enter to enter the Uboot console, set the IP as follows
| setenv ipaddr 192.168.137.81;     //Set the board IP, which is required to ping the PC
| setenv serverip 192.168.137.99；  //Set the PC IP
| setenv -f ethact sstar_emac;          //Set to use Emac, this platform uses Emac
| setenv -f ethaddr 00:11:22:33:44:55; //Set the MAC address
| setenv -f netmask 255.255.255.0;    //Set the subnet mask
| setenv -f gatewayip 192.168.137.1;    //Set the gateway
| estart    //Initialize the network. This command needs to be entered before using the network under uboot
| estar
| #After successful programming, the board will start automatically
| #The difference from full programming is that this method can execute the script in estar auto_update.txt to program any individual partition