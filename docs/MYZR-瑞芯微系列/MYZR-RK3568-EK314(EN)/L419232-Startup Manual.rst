Startup Manual
================

Development Board Connection
------------------------------

Check the Power Switch
~~~~~~~~~~~~~~~~~~~~~~~~

Press the "o" on the development board's power switch "SW1" to ensure the power switch is in the off state.

Serial Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Connect one end of the serial cable to the "CON9" port of the development board, and the other end to the serial port or USB port of the computer.
2. Refer to the :doc:`《Xshell Reference Manual》 </docs/COMMON/Terminal software XShell reference manual>` to create a new serial session and open it.

Ethernet Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connect one end of the Ethernet cable to "J13" or "J14", and the other end to the network port of the computer.

Download Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connect one end of the double-headed USB-A cable to J2, and the other end to the rear USB port of the computer.

Power Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~

Connect one end of the power adapter to the "JACK1" of the development board, and the other end to a mains (220V AC) socket.


Starting the Development Board
--------------------------------

Press the "-" on the development board's power switch "SWITCH" to turn on the power.

Interpretation of Development Board Startup Information
---------------------------------------------------------

After the development board is powered on, you can see the startup information output by the development board on the serial terminal software.

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
   [    0.000000] Linux version 4.19.232 (kuangwh@myzr-7a9b) (gcc version 10.3.1 20210621 (GNU Toolchain 
   for the A-profile Architecture 10.3-2021.07 (arm-10.29)), GNU ld (GNU Toolchain for the A-profile Architecture 
   10.3-2021.07 (arm-10.29)) 2.36.1.20210621) #16 SMP Mon Sep 18 15:33:57 CST 2023
   ............

   root@RK356X:/# 

U-Boot Information
~~~~~~~~~~~~~~~~~~~~

| The ``U-Boot 2017.09 (Sep 19 2023 - 14:06:08 +0800)`` in the startup information includes the following:

- [U-Boot version]: 2017.09
- [U-Boot file compilation time]: Sep 19 2023 - 14:06:08 +0800

Kernel Information
~~~~~~~~~~~~~~~~~~~~

| The ``Linux version 4.19.232 (kuangwh@myzr-7a9b) (gcc version 10.3.1 20210621 (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)), GNU ld (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 2.36.1.20210621) #16 SMP Mon Sep 18 15:33:57 CST 2023`` in the startup information includes the following:

- [Kernel version]: Linux-4.19.232
- [GCC version for compiling the kernel]: 10.3.1
- [Kernel file compilation time]: Mon Sep 18 15:33:57 CST 2023


Development Board Login
-------------------------

| After the system starts and outputs ``root@RK356X:/#``, you can log in:

- [Username]: root
- [Password]: None

``Note: The factory system logs in automatically; no need to enter a username and password.``

- **Tip**: After logging in, you can set and modify the password using the "passwd" command.
