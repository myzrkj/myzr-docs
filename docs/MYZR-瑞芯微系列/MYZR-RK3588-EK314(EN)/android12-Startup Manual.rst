Startup Manual
================

Development Board Connection
-------------------------------

Check the Power Switch
~~~~~~~~~~~~~~~~~~~~~~~~

|  Press the "o" position of the development board's power switch "SW1" to ensure the power switch of the development board is in the off state.

Connection of the Serial Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Connect one end of the serial cable to the "CON9" port of the development board, and the other end to the serial port or USB port of the computer.                                                                     
2. Refer to :doc:`《Xshell Reference Manual》 </docs/COMMON/Xshell.RM Reference Manual >` to create a new serial session and open the session.      

Connection of the Network Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Connect one end of the network cable to "J13" or "J14", and the other end to the network port of the computer.

Connection of the Download Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Connect one end of the double-headed USB-A cable to J2, and the other end to the rear USB port of the computer.

Connection of the Power Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Connect one end of the power adapter to the "JACK1" of the development board, and the other end to a mains (220V AC) socket.
         

Start the Development Board
------------------------------

|  Press the "-" position of the development board's power switch "SWITCH" to turn on the development board's power.

Interpretation of Development Board Startup Information
----------------------------------------------------------

|  After the development board is powered on, the startup information output by the development board can be viewed on the serial terminal software.

::

   U-Boot 2017.09 (Jan 10 2024 - 14:26:12 +0800)

   Model: MYZR RK3588 Evaluation Board
   PreSerial: 2, raw, 0xfeb50000
   DRAM:  3.7 GiB
   Sysmem: init
   Relocation Offset: eda39000
   Relocation fdt: eb9fa1f8 - eb9fecd8
   CR: M/C/I
   mmc@fe2c0000: 1, mmc@fe2e0000: 0
   Bootdev(atags): mmc 0
   MMC0: HS200, 200Mhz
   PartType: EFI
   DM: v2
   boot mode: recovery (misc)
   boot mode: None
   ........
   Starting kernel ...

   [    4.563675][    T0] Booting Linux on physical CPU 0x0000000000 [0x412fd050]
   [    4.563694][    T0] Linux version 5.10.110 (kuangwh@myzr-7a9b) (Android (7284624, based on r416183b)
   clang version 12.0.5 (https://android.googlesource.com/toolchain/llvm-project c935d99d7cf2016289302412d
   708641d52d2f7ee), LLD 12.0.5 (/buildbot/src/android/llvm-toolchain/out/llvm-project/lld c935d99d7cf20162
   89302412d708641d52d2f7ee)) #14 SMP PREEMPT Wed Jan 10 14:32:50 CST 2024
   ............

   console:/ $ 

U-Boot Information
~~~~~~~~~~~~~~~~~~~~~

|  The line ``U-Boot 2017.09 (Jan 10 2024 - 14:26:12 +0800)`` in the startup information contains the following details:
|  [U-Boot Version]: 2017.09;
|  [Compilation Time of U-Boot File]: Jan 10 2024 - 14:26:12 +0800.

Kernel Information
~~~~~~~~~~~~~~~~~~~~

|  The line ``Linux version 5.10.110 (kuangwh@myzr-7a9b) (Android (7284624, based on r416183b) clang version 12.0.5 (https://android.googlesource.com/toolchain/llvm-project c935d99d7cf2016289302412d708641d52d2f7ee), LLD 12.0.5 (/buildbot/src/android/llvm-toolchain/out/llvm-project/lld c935d99d7cf2016289302412d708641d52d2f7ee)) #14 SMP PREEMPT Wed Jan 10 14:32:50 CST 2024`` in the startup information contains the following details:
|  [Kernel Version]: Linux-5.10.110;
|  [Clang Version for Kernel Compilation]: clang version 12.0.5;
|  [Compilation Time of Kernel File]: Wed Jan 10 14:32:50 CST 2024.
 

Development Board Login
-------------------------

|  After the system starts up, you are logged in when ``console:/ $`` is displayed:
|  At this point, you can switch to the root user by entering the command "su".
