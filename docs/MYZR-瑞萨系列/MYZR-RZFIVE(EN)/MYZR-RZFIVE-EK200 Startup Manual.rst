MYZR-RZFIVE-EK200 Startup Manual
==================================

MYZR-RZFIVE-EK200 Package List
--------------------------------

**Standard Components**

|   [Base Board]: MYZR-RZFIVE-MB200, 1 piece
|   [Core Board]: MYZR-RZFIVE-CB200, 1 piece
|   [Power Adapter]: 5V, 1 piece
|   [Ethernet Cable]: 1 piece
|   [Serial Cable]: 1 piece

**User-Prepared Components**

|   [TF Card]: 1 piece, used for downloading (a common TF card for Android phones is sufficient)
|   [USB-to-Serial Cable]: 1 piece, used for debugging (required if the computer does not have a DB9 serial port)

MYZR-RZFIVE-EK200 Startup
---------------------------

Development Board Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Check the Power Switch**

|   Press the "o" position of the development board's power switch "SWITCH" to ensure the power switch of the development board is in the off state.

**Serial Cable Connection**

|   Connect one end of the serial cable to the "DEBUG" port of the development board, and the other end to the serial port or USB port of the computer.
|   Refer to the :doc:`《Xshell.RM Reference Manual 》 </docs/COMMON/Xshell.RM.Reference Manual>` to create a new serial session and open the session.

**Power Cable Connection**

|   Connect one end of the power adapter to the "5V_IN" port of the development board, and the other end to a mains power (220V AC) socket.

Start the Development Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Check the DIP Switch**

|   Set the SW1 DIP switch of the development board to the normal startup mode.
|   [Startup Mode]: 1 (OFF), 2 (OFF), 3 (ON), 4 (OFF)
|   [Download Mode]: 1 (OFF), 2 (OFF), 3 (OFF), 4 (OFF)
|   Note: The "ON" position of the DIP switch is on the side with letters, and the "OFF" position is on the side with numbers.

**Power On the Development Board**

|   Press the "-" position of the development board's power switch "SWITCH" to turn on the power switch of the development board. At this point, you can see some of the LEDs on the development board light up.

Interpretation of Development Board Startup Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   After the development board is powered on, you can view the startup information output by the development board in the serial terminal software.

.. code-block:: shell

   U-Boot SPL 2020.10 (Feb 15 2023 - 12:04:24 +0800)
   Trying to boot from MMC1
   þ

   U-Boot 2020.10 (Feb 15 2023 - 12:04:24 +0800)

   CPU:   rv64imafdc
   Model: myzr-rzfive
   DRAM:  1.9 GiB
   SW_ET0_EN: ON
   MMC:   sh-sdhi: 0, sh-sdhi: 1
   Loading Environment from MMC... OK
   In:    serial@1004b800
   Out:   serial@1004b800
   Err:   serial@1004b800
   Net:   
   Error: ethernet@11c30000 address not set.
   No ethernet found.

   Hit any key to stop autoboot:  0 

   .......

   Starting kernel ...
       0.000000] Linux version 5.10.145-cip17-riscv-renesas (linyn@u1804) (riscv64-oe-linux-gcc (GCC) 8.3.0, GNU ld (GNU Binutils) 2.31.1) #3 PREEMPT Fri Feb 17 11:31:39 CST 2023
   [    0.000000] OF: fdt: Ignoring memory range 0x48000000 - 0x48200000
   [    0.000000] efi: UEFI not found.

   .......

   OpenEmbedded nodistro.0 myzr-rzfive ttySC0

   myzr-rzfive login: root
   [   11.297976] audit: type=1006 audit(1671168594.911:2): pid=272 uid=0 old-auid=4294967295 auid=0 tty=(none) old-ses=4294967295 ses=1 res=1
   [   12.466686] FAT-fs (mmcblk0p1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.

**U-Boot Information**

|   The startup information "U-Boot 2020.10 (Feb 15 2023 - 12:04:24 +0800)" includes the following details:
|   [U-Boot Version]: 2020.10;
|   [Source Code Version Number]: NC;
|   [U-Boot File Compilation Time]: Feb 15 2023 - 12:04:24 +0800.

**Kernel Information**

|   The startup information "Linux version 5.10.145-cip17-riscv-renesas (linyn@u1804) (riscv64-oe-linux-gcc (GCC) 8.3.0, GNU ld (GNU Binutils) 2.31.1) #3 PREEMPT Fri Feb 17 11:31:39 CST 2023" includes the following details:
|   [Kernel Version]: Linux-5.10.145;
|   [Kernel Source Code Version Number]: cip17-riscv-renesas;
|   [GCC Version for Kernel Compilation]: 8.3.0;
|   [Kernel File Compilation Time]: Fri Feb 17 11:31:39 CST 2023.

Development Board Login
~~~~~~~~~~~~~~~~~~~~~~~~~

|   After the system starts up and outputs "myzr-rzfive login: ", you can log in:
|   [Username]: root
|   [Password]: None
|   Note: After logging in, you can use the "passwd" command to set and modify the password.