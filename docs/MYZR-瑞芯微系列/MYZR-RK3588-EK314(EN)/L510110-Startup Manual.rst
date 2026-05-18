Startup Manual
================

Development Board Connection
------------------------------

Check the Power Switch
~~~~~~~~~~~~~~~~~~~~~~~~~

| Press the "o" position of the development board's power switch "SW1" to ensure the power switch of the development board is in the **off** state.

Connection of the Serial Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| 　　1. Connect one end of the serial cable to the "J22" port of the development board, and the other end to the serial port or USB port of the computer.                                                                     
| 　　2. Refer to the :doc:`Xshell Reference Manual </docs/COMMON/Xshell.RM Reference Manual >` to create a new serial session and open the session.      

Connection of the Network Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Connect one end of the network cable to "J14" or "J15", and the other end to the network port of the computer.

Connection of the Download Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Connect one end of the Type-C cable to J4, and the other end to the rear USB port of the computer.

Connection of the Power Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Connect one end of the power adapter to the "J1" port of the development board, and the other end to a mains (220V AC) socket.
         

Start the Development Board
------------------------------

| Press the "-" position of the development board's power switch "SWITCH" to turn on the development board.

Interpretation of Development Board Startup Information
----------------------------------------------------------

| After the development board is powered on, the startup information output by the development board can be viewed on the serial terminal software.

::

   U-Boot 2017.09-g32640b0ada-230713-dirty #kuangwh (Dec 21 2023 - 11:52:41 +0800)

   Model: MYZR RK3588 Evaluation Board
   MPIDR: 0x81000000
   PreSerial: 2, raw, 0xfeb50000
   DRAM:  4 GiB
   Sysmem: init
   Relocation Offset: eda1d000
   Relocation fdt: eb9fa280 - eb9fecc8
   CR: M/C/I
   Using default environment

   DM: v2
   mmc@fe2c0000: 1, mmc@fe2e0000: 0
   Bootdev(atags): mmc 0
   MMC0: HS400 Enhanced Strobe, 200Mhz
   PartType: EFI
   boot mode: None
   ........
   Starting kernel ...

   [    2.175016] Booting Linux on physical CPU 0x0000000000 [0x412fd050]
   [    2.175034] Linux version 5.10.110 (kuangwh@myzr-7a9b) (aarch64-none-linux-gnu-gcc 
   (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 10.3.1 20210621,
    GNU ld (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 2.36.1.20210621) 
    #17 SMP Fri Jan 5 10:22:17 CST 2024
   ............

   root@rk3588:/# 

U-Boot Information
~~~~~~~~~~~~~~~~~~~~~

| The line ``U-Boot 2017.09-g32640b0ada-230713-dirty #kuangwh (Dec 21 2023 - 11:52:41 +0800)`` in the startup information contains the following details:
| 　　[U-Boot Version]: 2017.09；
| 　　[U-Boot File Compilation Time]: Dec 21 2023 - 11:52:41 +0800.

Kernel Information
~~~~~~~~~~~~~~~~~~~~

| The line ``Linux version 5.10.110 (kuangwh@myzr-7a9b) (aarch64-none-linux-gnu-gcc 
   (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 10.3.1 20210621,
    GNU ld (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 2.36.1.20210621) 
    #17 SMP Fri Jan 5 10:22:17 CST 2024`` in the startup information contains the following details:
| 　　[Kernel Version]: Linux-5.10.110；
| 　　[GCC Version for Kernel Compilation]: 10.3.1；
| 　　[Kernel File Compilation Time]: Fri Jan 5 10:22:17 CST 2024.
 

Development Board Login
-------------------------

| After the system starts up and ``root@rk3588:/#`` is displayed, you can log in with the following credentials:
| 　　[Username]: root
| 　　[Password]: None
|     ``Note: The factory system logs in automatically; no need to enter a username or password``
| 　　**Tip**: After logging in, you can use the "passwd" command to set and change the password.
