Startup Manual
================

Development Board Connection
------------------------------

Check the Power Switch
~~~~~~~~~~~~~~~~~~~~~~~~

|  Press the "o" position of the development board's power switch "J2" to ensure the power switch is in the **off** state.

Connect the Serial Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~

|  1. Connect one end of the serial cable to the "P2" port on the development board, and the other end to the serial port or USB port of the computer.                                                                     
|  2. Refer to the :doc:`《Xshell Reference Manual》 </docs/COMMON/Xshell.RM Reference Manual >` to create a new serial session and open it.      

Connect the Network Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Connect one end of the network cable to "U9" or "U12", and the other end to the network port of the computer.

Connect the Download Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Connect one end of the double-headed USB cable to J3, and the other end to the **rear USB port** of the computer.

Connect the Power Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Connect one end of the power adapter to the "J1" port of the development board, and the other end to a mains power (220V AC) socket.

Connect the HDMI Display 
~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Connect one end of the HDMI display cable to the development board, the other end to the HDMI display, and power on the HDMI display. 

|  **Note:** It is recommended to use an HDMI display with a resolution of **1080P** and a native HDMI interface (not an adapter-converted HDMI interface).                         

Start the Development Board
------------------------------

Check the Boot Mode DIP Switch of the Development Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Set the "SW3" DIP switch of the development board to the *boot mode*.

==========  ==========  ==========  ==========  ===========  ====
BOOT_MODE3  BOOT_MODE2  BOOT_MODE1  BOOT_MODE0  Description
==========  ==========  ==========  ==========  ===========  ====
0           0           0           1           Flashing     Mode
0           0           1           0           Boot         Mode
==========  ==========  ==========  ==========  ===========  ====

|  Note: The ON (1) position of the DIP switch is on the side with letters, and the OFF (0) position is on the side with numbers.

Power On the Development Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Press the "-" position of the development board's power switch "SWITCH" to turn on the power.

Interpretation of Development Board Boot Information
-------------------------------------------------------

|  After the development board is powered on, you can view the boot information output by the development board in the serial terminal software.

::

   U-Boot 2021.04-g245e65b5 (Jan 17 2023 - 17:01:28 +0800)
   CPU:   i.MX8MP[8] rev1.1 1800 MHz (running at 1200 MHz)
   CPU:   Commercial temperature grade (0C to 95C) at 28C
   Reset cause: POR
   Model: MYZR i.MX8MPlus EK314 board
   DRAM:  6 GiB
   MMC:   FSL_SDHC: 1, FSL_SDHC: 2
   Loading Environment from MMC... OK
   ........
   Starting kernel ...
   [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd034]
   [    0.000000] Linux version 5.10.72-gdcb9071261a3 (tangbin@MYZR-230304) (aarch64-linux-gnu-gcc (Linaro GCC 7.5-2019.12) 7.5.0, GNU ld (Linaro_Binutils-2019.12) 2.28.2.20170706) #11 SMP PREEMPT Thu Mar 16 10:25:45 CST 2023
   [    0.000000] Machine model: MYZR i.MX8M Plus EK314 board
   [    0.000000] efi: UEFI not found.
   [    0.000000] Reserved memory: created CMA memory pool at 0x00000000c4000000, size 960 MiB
   [    0.000000] OF: reserved mem: initialized node linux,cma, compatible id shared-dma-pool
   [    0.000000] Reserved memory: created DMA memory pool at 0x0000000094300000, size 1 MiB
   [    0.000000] OF: reserved mem: ini
   ............
   NXP i.MX Release Distro 5.10-hardknott imx8mp-ddr4-evk ttymxc1
   imx8mp-ddr4-evk login: [   33.759760] can1-stby: disabling

U-Boot Information
~~~~~~~~~~~~~~~~~~~~~

|  The line ``U-Boot SPL 2021.04-lf_v2021.04+g8372631b28 (Jun 10 2022- 06:24:02 +0000)`` in the boot information contains the following details:
| 　　[U-Boot Version]: 2021.04;
| 　　[Source Code Version]: g8372631b28;
| 　　[U-Boot File Compilation Time]: Jun 10 2022 - 06:24:02 +0000.

Kernel Information
~~~~~~~~~~~~~~~~~~~~

|  The line ``Linux version 5.10.72-gdcb9071261a3(tangbin@MYZR-230304) |(aarch64-linux-gnu-gcc (Linaro GCC 7.5-2019.12)7.5.0, GNU ld (Linaro_Binutils-2019.12) 2.28.2.20170706) #11 SMPPREEMPT Thu Mar 16 10:25:45 CST 202`` in the boot information contains the following details:
| 　　[Kernel Version]: Linux- 5.10.72;
| 　　[GCC Version for Kernel Compilation]: 7.5;
| 　　[Kernel File Compilation Time]: Thu Mar 16 10:25:45 CST 2023.
 

Development Board Login
--------------------------

|  After the system starts up and outputs ``imx8mp-ddr4-evk login:``, you can log in with the following credentials:
| 　　[Username]: root
| 　　[Password]: None
| 　　**Tip**: After logging in, you can use the "passwd" command to set or modify the password.
