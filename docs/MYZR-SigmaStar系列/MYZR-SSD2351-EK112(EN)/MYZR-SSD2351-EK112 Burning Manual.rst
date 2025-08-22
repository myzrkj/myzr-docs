MYZR-SSD2351-EK112 Burning Manual
====================================

Download via USB interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Boot mode DIP switch settings: 1: on, 2: off, 3: off, 4: off
|  Flashing tool: UsbFactoryTool_1.0.0.19.tar.gz
|  Mirroring File: SstarUsbImage_202503050415.bin

Unzip the burning tool
-------------------------

|  Right-click and extract to the current directory. My computer is 64-bit, so I choose the tool USB_Factory_Tool_64_1.0.0.19.exe 

Set the sheet metal programming mode
----------------------------------------

|  Boot mode DIP switch settings: 1: on, 2: off, 3: off, 4: off

Download
----------

|  Connect the power supply and USB cable, and the computer will detect a "USB Mass Storage Device". 

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/烧录手册01.png
   :alt: 烧录手册01.png
   :width: 60%

|  Double-click the burning tool, USB_Factory_Tool_64_1.0.0.19.exe, as follows: 

1. Detected devices can be seen
2. Select the firmware to be flashed
3. Click the green button to start programming

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/烧录手册02.png
   :alt: 烧录手册02.png
   :width: 60%

4. When the progress reaches 100%, click the red stop button to end 

Flash_Tool Burning
~~~~~~~~~~~~~~~~~~~~~

|  Flashing Tool: FlashTool_5.0.52.tar.gz
|  This method is applicable for use in the case of blank chip programming or when the board cannot enter the Uboot Console. 
|  If it is not an empty chip or can start normally and you want to use Flash Tool for programming, you need to first turn off Debug Uart in the following way 

- Directly enterdebugin the uboot Console, then close the serial end point

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/烧录手册03.png
   :alt: 烧录手册03.png
   :width: 60%

- Under the kernel, input11111, then close the serial end point

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/烧录手册04.png
   :alt: 烧录手册04.png
   :width: 60%

1. Power on and ensure that the serial port log cannot reach the U-Boot Console (if it can boot normally, you need to first enter the debug command in the U-Boot Console to disable the serial port debugging function)
2. Close the serial port debugging end point 
3. The necessary partitions and partition start addresses required to boot into Uboot

|  Nand Flash:

+-------------+----------+--------------------------------------+
| Binary file |  offset  |      Binary Placement Directory      |
+=============+==========+======================================+
| cis.bin     | 0x00000  | project\image\output\images\cis.bin  |
+-------------+----------+--------------------------------------+
| cis.bin     | 0x20000  | project\image\output\images\cis.bin  |
+-------------+----------+--------------------------------------+
| boot.bin    | 0x140000 | project\image\output\images\boot.bin |
+-------------+----------+--------------------------------------+

|  Burn the cis.bin mirroring (burn once at both 0x00000 and 0x20000) 

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/烧录手册05.png
   :alt: 烧录手册05.png
   :width: 60%

|  Burn the boot.bin mirroring 

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/烧录手册06.png
   :alt: 烧录手册06.png
   :width: 60%

TFTP Server Flashing
~~~~~~~~~~~~~~~~~~~~~~~

|  Open the TFTP server. The default path for the compiled mirroring is project/image/output/images. Copy the image to your computer, select Browse to set the path, as follows:

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/烧录手册07.png
   :alt: 烧录手册07.png
   :width: 60%

|  #The board needs to enter the startup mode: Startup DIP switch mode: 1: on, 2: on, 3: off, 4: off
|  #Insert the TYPEC cable, press and hold Enter while powering on to enter the Uboot Console, and set the IP as follows
|  setenv ipaddr 192.168.137.81; // Set the board-side IP, which is required to be able to ping with the PC side
|  setenv serverip 192.168.137.99; // Set the IP address of the PC side
|  setenv -f ethact sstar_emac; // Set to use Emac, which is used on this platform
|  setenv -f ethaddr 00:11:22:33:44:55; // Set the MAC address
|  setenv -f netmask 255.255.255.0; // Set the mask
|  setenv -f gatewayip 192.168.137.1; // Set gateway
|  estart // This command must be entered before using the network under uboot to initialize the network
|  estar
|  #Flashing successful, the board will automatically start
|  The difference from full flashing is that this method can execute the script in estar auto_update.txt to flash any individual partition
