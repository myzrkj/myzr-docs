Startup Manual
================

Development Board Connection
-------------------------------

Check the Power Switch
~~~~~~~~~~~~~~~~~~~~~~~~

|   Press the "o" on the development board's power switch "SW1" to ensure the power switch of the development board is in the off state.

Connection of Serial Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Connect one end of the Type-C cable to the "Debug" port of the development board, and the other end to the serial port of the computer.
2. Refer to :doc:`《Xshell Reference Manual》</docs/COMMON/Xshell.RM.参考手册>` to create a new serial session and open it.

Connection of Network Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the network cable to "J11" or "J12", and the other end to the network port of the computer.

Connection of Download Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the Type-C cable to J2, and the other end to the rear USB port of the computer.

Connection of Power Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the 12V-5A power adapter to "J1" of the development board, and the other end to a mains (220V AC) socket.

HDMI Display Connection
~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the HDMI display cable to J10 of the development board, the other end to the HDMI display, and power on the HDMI display.


Start the Development Board
------------------------------

Check the Boot Mode DIP Switch of the Development Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Set the "SW1" DIP switch of the development board to the boot mode.
|   Note: The ON side of the DIP switch is the I side, and the OFF (0) side is the O side.

Power on the Development Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Press the "I" on the development board's power switch SW1 to turn on the power of the development board.

Interpretation of Development Board Startup Information
---------------------------------------------------------

|   After the development board is powered on, the startup information output by the development board can be seen on the serial terminal software.


.. code-block:: shell

    U-Boot 2017.09-gbe3408d-dirty #root (Jun 05 2025 - 01:17:48 +0000)

    Model: MYZR-RK3576 board
    MPIDR: 0x0
    PreSerial: 0, raw, 0x2ad40000
    DRAM:  4 GiB
    Sysmem: init
    Relocation Offset: bda1b000
    Relocation fdt: fb9f9c10 - fb9fecd8
    CR: M/C/I
    Using default environment

    optee api revision: 2.0
    mmc@2a310000: 1, mmc@2a330000: 0
    Bootdev(atags): mmc 0
    MMC0: HS400 Enhanced Strobe, 200Mhz
    PartType: EFI
    TEEC: Waring: Could not find security partition
    DM: v2
    boot mode: None
  
U-Boot Information
~~~~~~~~~~~~~~~~~~~~~

|   The startup information U-Boot 2017.09-gbe3408d-dirty #root (Jun 05 2025 - 01:17:48 +0000) contains the following information:
|   【u-boot version】: 2017.09;
|   【source code version number】: gbe3408d;
|   【compilation time of u-boot file】: Jun 05 2025 - 01:17:48 +0000.

Kernel Information
~~~~~~~~~~~~~~~~~~~~~

|   The startup information Linux version 6.1.75 (tangbin@myzr-u2004) (aarch64-none-linux-gnu-gcc (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 10.3.1 20210621, GNU ld (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 2.36.1.20210621) #1 SMP Thu Jun  5 01:44:23 UTC 2025 contains the following information:
|   【kernel version】: Linux- 6.1.75;
|   【GCC version for compiling the kernel】: 10.3.1;
|   【compilation time of the kernel file】: Thu Jun  5 01:44:23 UTC 2025.

Development Board Login
~~~~~~~~~~~~~~~~~~~~~~~~~


|   After the system starts, it logs in automatically. Press any key and enter:
|   【username】: root
|   【password】: none
|   Tip: After logging in, you can set and modify the password through the "passwd" command.