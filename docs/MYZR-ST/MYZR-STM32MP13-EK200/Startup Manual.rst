Startup Manual
================

Development Board Connection
------------------------------

Checking the Power Switch
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Press the "o" position of the development board's power switch "J2" to ensure the power switch of the development board is in the **off** state.

Connecting the Serial Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Connect one end of the serial cable to the "P2" port of the development board, and the other end to the serial port or USB port of the computer.                                                                     
2. Refer to the :doc:`《Xshell Reference Manual》 </docs/COMMON/Xshell.RM Reference Manual >` to create a new serial session and open the session.      

Connecting the Ethernet Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Connect one end of the Ethernet cable to "ETH1" or "ETH2", and the other end to the network port of the computer.

Connecting the Download Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Connect one end of the Type-C cable to J5, and the other end to the rear USB port of the computer.

Connecting the Power Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Connect one end of the power adapter to "J1" of the development board, and the other end to a mains power (220V AC) socket.
         

Starting the Development Board
--------------------------------

Checking the Boot Mode DIP Switch of the Development Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Set the "SW3" DIP switch of the development board to the *boot mode*.

+------------+------------+------------+------------+---------------+
| BOOT_MODE3 | BOOT_MODE2 | BOOT_MODE1 | BOOT_MODE0 | Description   |
+============+============+============+============+===============+
| 0          | 0          | 0          | 0          | Flashing Mode |
+------------+------------+------------+------------+---------------+
| 0          | 0          | 1          | 0          | Boot Mode     |
+------------+------------+------------+------------+---------------+

|  Note: The ON (1) position of the DIP switch is on the side with letters, and the OFF (0) position is on the side with numbers.


Powering On the Development Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Press the "-" position of the development board's power switch "SWITCH" to turn on the development board's power.

Interpreting the Development Board's Boot Information
-------------------------------------------------------

|  After the development board is powered on, the boot information output by the development board can be viewed through the serial port.

::

   U-Boot 2021.10-stm32mp-r2 (Aug 24 2023 - 18:17:43 +0800)

   CPU: STM32MP135D Rev.Y
   Model: MYZR STM32MP13 Discovery Board
   Board: stm32mp1 in trusted mode (myzr,myzr-stm32mp13)
   DRAM:  512 MiB
   optee optee: OP-TEE: revision 3.16
   Clocks:
   - MPU : 1000 MHz
   - AXI : 266.500 MHz
   - PER : 24 MHz
   - DDR : 533 MHz
   ........
   Starting kernel ...
   [    0.000000] Booting Linux on physical CPU 0x0
   [    0.000000] Linux version 5.15.67 (kuangwh@myzr-7a9b) (arm-ostl-linux-gnueabi-gcc (GCC) 11.3.0, GNU ld (GNU Binutils) 2.38.20220708) #4 PREEMPT Fri Aug 25 10:55:19 CST 2023
   [    0.000000] CPU: ARMv7 Processor [410fc075] revision 5 (ARMv7), cr=10c5387d
   [    0.000000] CPU: div instructions available: patching division code
   [    0.000000] CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
   [    0.000000] OF: fdt: Machine model: MYZR STM32MP13 Discovery Board
   ............
   ST OpenSTLinux - Weston - (A Yocto Project Based Distro) 4.0.4-openstlinux-5.15-yocto-kirkstone-mp1-v22.11.23 stm32mp1 ttySTM0

   stm32mp1 login: root (automatic login)

   root@stm32mp1:~# 

U-Boot Information
~~~~~~~~~~~~~~~~~~~~

|  The line ``U-Boot 2021.10-stm32mp-r2 (Aug 24 2023 - 18:17:43 +0800)`` in the boot information contains the following details:
|  [U-Boot Version] : 2021.10;
|  [Source Code Version] : stm32mp-r2;
|  [U-Boot File Compilation Time] : Aug 24 2023 - 18:17:43 +0800.

Kernel Information
~~~~~~~~~~~~~~~~~~~~

|  The line ``Linux version 5.15.67 (kuangwh@myzr-7a9b) (arm-ostl-linux-gnueabi-gcc (GCC) 11.3.0, GNU ld (GNU Binutils) 2.38.20220708) #4 PREEMPT Fri Aug 25 10:55:19 CST 2023`` in the boot information contains the following details:
|  [Kernel Version] : Linux- 5.15.67;
|  [GCC Version for Kernel Compilation] : 11.3;
|  [Kernel File Compilation Time] : Fri Aug 25 10:55:19 CST 2023.
 

Logging In to the Development Board
--------------------------------------

|  After the system starts up and displays ``stm32mp1 login:``, you can log in with the following credentials:
|  [Username] : root
|  [Password] : None
|  ``Note: The factory system enables automatic login; no need to enter a username or password``
|  **Tip**: After logging in, you can use the "passwd" command to set or modify the password.
