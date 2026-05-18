Startup Manual
================

Development Board Connection
------------------------------

Check the Power Switch
~~~~~~~~~~~~~~~~~~~~~~~~

|  Press the "o" on the development board's power switch "SW1" to ensure the development board's power switch is in the off state.

Connection of Serial Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  1. Connect one end of the serial cable to the "CON9" port of the development board, and the other end to the serial port or USB port of the computer.                                                                     
|  2. Refer to :doc:`《Xshell Reference Manual》 </docs/COMMON/Xshell.RM Reference Manual >` to create a new serial session and open the session.      

Connection of Network Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Connect one end of the network cable to "J13" or "J14", and the other end to the network port of the computer.

Connection of Download Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Connect one end of the double-headed USB-A cable to J2, and the other end to the rear USB port of the computer.

Connection of Power Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Connect one end of the power adapter to the "JACK1" of the development board, and the other end to the mains (220V AC) socket.
         

Start the Development Board
-----------------------------

|  Press the "-" on the development board's power switch "SWITCH" to turn on the development board's power.

Interpretation of Development Board Startup Information
----------------------------------------------------------

|  After the development board is powered on, the startup information output by the development board can be seen on the serial terminal software.

::

   U-Boot 2017.09 (Sep 19 2023 - 14:06:08 +0800)

   Model: MYZR RK3568 Evaluation Board
   PreSerial: 2, raw, 0xfe660000
   DRAM:  4 GiB
   Sysmem: init
   Relocation Offset: ed349000
   Relocation fdt: eb9f9260 - eb9fecd0
   CR: M/C/I
   dwmmc@fe2b0000: 1, dwmmc@fe2c0000: 2, sdhci@fe310000: 0
   Bootdev(atags): mmc 0
   MMC0: HS200, 200Mhz
   PartType: EFI
   DM: v1
   boot mode: None
   ........
   Starting kernel ...

   [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x412fd050]
   [    0.000000] Linux version 4.19.232 (kuangwh@myzr-7a9b) (Android (6573524 based on r383902b) 
   clang version 11.0.2 (https://android.googlesource.com/toolchain/llvm-project b397f81060ce6d701042b782172ed13bee898b79),
   LLD 11.0.2 (/buildbot/tmp/tmpF3FjA8 b397f81060ce6d701042b782172ed13bee898b79)) #28 SMP PREEMPT Fri Jan 5 09:39:22 CST 2024
   ............

   console:/ $ 

U-Boot Information
~~~~~~~~~~~~~~~~~~~~

|  The ``U-Boot 2017.09 (Sep 19 2023 - 14:06:08 +0800)`` in the startup information contains the following information:
|  【u-boot version】: 2017.09;
|  【u-boot file compilation time】: Sep 19 2023 - 14:06:08 +0800.

Kernel Information
~~~~~~~~~~~~~~~~~~~~

|  The ``Linux version 4.19.232 (kuangwh@myzr-7a9b) (Android (6573524 based on r383902b) 
                  clang version 11.0.2 (https://android.googlesource.com/toolchain/llvm-project b397f81060ce6d701042b782172ed13bee898b79),
                  LLD 11.0.2 (/buildbot/tmp/tmpF3FjA8 b397f81060ce6d701042b782172ed13bee898b79)) #28 SMP PREEMPT Fri Jan 5 09:39:22 CST 2024`` in the startup information contains the following information:
|  【Kernel version】: Linux-4.19.232;
|  【clang version for compiling the kernel】: clang version 11.0.2;
|  【Kernel file compilation time】: Fri Jan 5 09:39:22 CST 2024.
 

Development Board Login
-------------------------

|  After the system starts up, you are logged in when ``console:/ $`` is output:
|  At this time, you can switch to the root user by entering the command "su".