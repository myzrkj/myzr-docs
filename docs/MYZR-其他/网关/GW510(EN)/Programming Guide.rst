
.. raw:: html

   <style>
   h1 {
       color: #4CAF50;  /* Level 1 heading font color */
   }
   </style>


Programming Guide
=================

USB Interface Download (Recommended)
------------------------------------

-  Programming mode DIP switch setting: 1: on, 2: off, 3: off, 4: off
-  Programming tool: UsbFactoryTool_1.0.0.19.tar.gz
-  Image file: SstarUsbImage_202503050415.bin

**Extract Programming Tool**

Right-click to extract to the current directory. Since my computer is 64-bit, select USB_Factory_Tool_64_1.0.0.19.exe.

**Set Programming Mode**

Programming mode DIP switch setting: 1: on, 2: off, 3: off, 4: off

**Download**

Connect power and USB cable. The computer will detect a "USB Mass Storage Device".

.. image:: ../../../../image/MYZR-SigmaStar系列/MYZR-SSD2351/烧录手册01.png
   :alt: Programming Guide 01
   :width: 100%

Double-click the programming tool USB_Factory_Tool_64_1.0.0.19.exe:

1. You can see the detected device
2. Select the firmware to program
3. Click the green button to start programming

.. image:: ../../../../image/MYZR-SigmaStar系列/MYZR-SSD2351/烧录手册02.png
   :alt: Programming Guide 02
   :width: 100%

4. When progress reaches 100%, click the red stop button to finish

Flash_Tool Programming
----------------------

1. Programming tool: FlashTool_5.0.52.tar.gz
2. This method is suitable for blank chip programming or when the board cannot enter Uboot console.
3. For non-blank chips or boards that can boot normally, to use Flash Tool for programming, you need to disable Debug Uart first as follows:

- In uboot console, directly type "debug" and close the serial terminal

.. image:: ../../../../image/MYZR-SigmaStar系列/MYZR-SSD2351/烧录手册03.png
   :alt: Programming Guide 03
   :width: 100%

- Under kernel, type "11111" and close the serial terminal

.. image:: ../../../../image/MYZR-SigmaStar系列/MYZR-SSD2351/烧录手册04.png
   :alt: Programming Guide 04
   :width: 100%

1. Power on and ensure the serial log cannot reach the uboot console (if it can boot normally, enter "debug" command in uboot console first to disable serial debug)
2. Close the serial debug terminal
3. Required partitions and partition start addresses for booting to Uboot

Nand Flash:

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
   }
   th {
       background-color: #4CAF50;
       color: white;
       text-align: center;  /* Center header text */
   }
     td {
       border: 1px solid #ddd;
       padding: 8px;
       text-align: center;  /* Center first row content */
   }

   }
   </style>

.. raw:: html

   <style>
   table {
       width: 100%;  /* Uniform width */
       border-collapse: collapse;
       table-layout: auto;  /* Auto column width */
   }
   td {
       word-wrap: break-word;  /* Auto wrap long content */
   }
   </style>

=============  =========  ===========================================
Binary file    offset     Binary File Path
=============  =========  ===========================================
cis.bin        0x00000    project/image/output/images/cis.bin
cis.bin        0x20000    project/image/output/images/cis.bin
boot.bin       0x140000   project/image/output/images/boot.bin
=============  =========  ===========================================

Program cis.bin image (Program both at 0x00000 and 0x20000)

.. image:: ../../../../image/MYZR-SigmaStar系列/MYZR-SSD2351/烧录手册05.png
   :alt: Programming Guide 05
   :width: 100%

Program boot.bin image

.. image:: ../../../../image/MYZR-SigmaStar系列/MYZR-SSD2351/烧录手册06.png
   :alt: Programming Guide 06
   :width: 100%

TFTP Server Programming
-----------------------

Open TFTP server. The default compiled image path is project/image/output/images. Copy the image to your computer and click Browse to set the path:

.. image:: ../../../../image/MYZR-SigmaStar系列/MYZR-SSD2351/烧录手册07.png
   :alt: Programming Guide 07
   :width: 100%

.. code-block:: shell

    #Enter boot mode on the board: Boot DIP switch setting: 1: on, 2: on, 3: off, 4: off
    #Connect TYPEC cable, press and hold Enter during boot to enter Uboot console, then set IP as follows:
    setenv ipaddr 192.168.137.81; //Set board IP, must be pingable from PC
    setenv serverip 192.168.137.99; //Set PC IP
    setenv -f ethact sstar_emac; //Set to use Emac, this platform uses Emac
    setenv -f ethaddr 00:11:22:33:44:55; //Set MAC address
    setenv -f netmask 255.255.255.0; //Set subnet mask
    setenv -f gatewayip 192.168.137.1; //Set gateway
    estart //Initialize network, required before using network in uboot
    estar
    #After successful programming, the board will boot automatically
    #Unlike full programming, this method can execute scripts in auto_update.txt to program any individual partition