Startup Manual
================

Development Board Connection
------------------------------

Check the Power Switch
~~~~~~~~~~~~~~~~~~~~~~~~

|  Press the "o" position of the development board's power switch "J2" to ensure the power switch is in the **off** state.

Connect the Serial Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Connect one end of the serial cable to the "P2" port on the development board, and the other end to the computer's serial port or USB port.
2. Refer to the :doc:`《Xshell Reference Manual》 </docs/COMMON/Terminal software XShell reference manual>` to create a new serial session and open it.

Connect the Ethernet Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Connect one end of the Ethernet cable to "U10" and the other end to the computer's Ethernet port.

Connect the Download Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Connect one end of the double-headed USB cable to J14, and the other end to the **rear USB port** of the computer.

Connect the Power Cable
~~~~~~~~~~~~~~~~~~~~~~~~~

|  Connect one end of the power adapter to "J1" on the development board, and the other end to a mains power (220V AC) outlet.


Power On the Development Board
--------------------------------

Check the Boot Mode DIP Switch of the Development Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Set the "SW1" DIP switch on the development board to the *boot mode*.

+------------+------------+------------+------------+---------------+
| BOOT_MODE0 | BOOT_MODE1 | BOOT_MODE2 | BOOT_MODE3 | Description   |
+------------+------------+------------+------------+---------------+
| 1          | 0          | 1          | 0          | Flashing Mode |
+------------+------------+------------+------------+---------------+
| 0          | 1          | 1          | 0          | Boot Mode     |
+------------+------------+------------+------------+---------------+

|  Note: The ON (1) position of the DIP switch is on the side with letters, and the OFF (0) position is on the side with numbers.


Power On the Development Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Press the "-" position of the development board's power switch "SWITCH" to turn on the power. At this point, you will see some of the LEDs on the development board light up.


Interpretation of Development Board Boot Information
------------------------------------------------------

|  After the development board is powered on, you can view the boot information output by the board in the serial terminal software.

::

   U-Boot 2021.04-gf0666134 (May 04 2023 - 15:53:36 +0800)

   CPU:   i.MX8MMQ rev1.0 1800 MHz (running at 1200 MHz)
   CPU:   Commercial temperature grade (0C to 95C) at 41C
   Reset cause: POR
   Model: MYZR i.MX8MMini EK200 board
   DRAM:  2 GiB
   tcpc_init: Can't find device id=0x52
   setup_typec: tcpc port2 init failed, err=-19
   tcpc_init: Can't find device id=0x50
   setup_typec: tcpc port1 init failed, err=-19
   MMC:   FSL_SDHC: 1, FSL_SDHC: 2
   Loading Environment from MMC... *** Warning - bad CRC, using default environment

   ........
   Moving Image from 0x40480000 to 0x40600000, end=42240000
   ## Flattened Device Tree blob at 43000000
     Booting using the fdt blob at 0x43000000
     Using Device Tree in place at 0000000043000000, end 000000004300e306
   adv7535_mipi2hdmi adv7535@3d: Can't find cec device id=0x3c
   fail to probe panel device adv7535@3d
   mxs_video lcdif@32e00000: failed to get any video link display timings
   probe video device failed, ret -22

   Starting kernel ...

   [0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd034]
   [0.000000] Linux version 5.10.72-g492a823d1cf5-dirty (zhongjy@myzr-8a09) (aarch64-linux-gnu-gcc (Linaro GCC 7.5-2019.12) 7.5.0, GNU ld (Linaro_Binutils-2019.12) 2.28.2.20170706) #1 SMP PREEMPT Mon May 8 08:25:31 UTC 2023

   ............
   NXP i.MX Release Distro 5.10-hardknott imx8mm-ddr4-evk ttymxc1

U-Boot Information
~~~~~~~~~~~~~~~~~~~~

|  The line ``U-Boot 2021.04-gf0666134 (May 04 2023 - 15:53:36 +0800)`` in the boot information contains the following details:
|  [U-Boot Version]: U-Boot 2021.04;
|  [Source Code Version]: gf0666134;
|  [U-Boot File Compilation Time]: May 04 2023 - 15:53:36 +0800.

Kernel Information
~~~~~~~~~~~~~~~~~~~~

|  The line ``Linux version 5.10.72-g492a823d1cf5-dirty (zhongjy@myzr-8a09) (aarch64-linux-gnu-gcc (Linaro GCC 7.5-2019.12) 7.5.0, GNU ld (Linaro_Binutils-2019.12) 2.28.2.20170706) #1 SMP PREEMPT Mon May 8 08:25:31 UTC 2023`` in the boot information contains the following details:
|  [Kernel Version]: 5.10.72-g492a823d1cf5-dirty;
|  [GCC Version for Kernel Compilation]: 7.5;
|  [Kernel File Compilation Time]: Mon May 8 08:25:31 UTC 2023.

Development Board Login
-------------------------

|  After the system starts up and displays ``imx8mm-ddr4-evk login:``, you can log in with the following credentials:
|  [Username]: root
|  [Password]: None
|  **Tip**: After logging in, you can use the "passwd" command to set or modify the password.
