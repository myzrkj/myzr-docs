Startup Manual
================

Development Board Connection
-------------------------------

Check the Power Switch
~~~~~~~~~~~~~~~~~~~~~~~~~

|   Press the "o" position of the development board's power switch "SW1" to ensure the power switch of the development board is in the **off** state.

Connection of the Serial Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Use a TTL serial module. Connect one end of the serial cable to the "J22" port of the development board, and the other end to the serial port of the computer.

|   J22 Connector: (The pin indicated by the triangular mark is GND; the power pin does not need to be connected)

+-----+-----+-----+-----+------+
| No. | 1   | 2   | 3   | 4    |
+-----+-----+-----+-----+------+
| Pin | GND | RX  | TX  | 3.3V |
+-----+-----+-----+-----+------+

2. Refer to the :doc:`"Xshell Reference Manual" </docs/COMMON/Xshell.RM Reference Manual >` to create a new serial session and open the session.

Connection of the Network Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the network cable to "J13" or "J14", and the other end to the network port of the computer.

Connection of the Download Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the Type-C cable to J5, and the other end to the rear USB port of the computer.

Connection of the Power Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the power adapter to "J1" of the development board (the development board is powered by 12V), and insert the other end into a mains (220V AC) socket.

Connection of the HDMI Display
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the HDMI display cable to J8 or J9 of the development board, and the other end to the HDMI display. Then power on the HDMI display.
|   Note: It is recommended that the resolution of the HDMI display be 1080P, and use a display with a native HDMI interface instead of one converted to an HDMI interface.

Start the Development Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Power On the Development Board
""""""""""""""""""""""""""""""""

|   Press the "-" position of the development board's power switch SW1 to turn on the development board's power.

Interpretation of the Development Board's Startup Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   After the development board is powered on, the startup information output by the development board can be viewed on the serial terminal software.

.. code-block:: shell

    U-Boot 2017.09 (May 12 2025 - 15:23:24 +0000)

    Model: MYZR RK3588 EK360 Board
    MPIDR: 0x81000000
    PreSerial: 2, raw, 0xfeb50000
    DRAM:  4 GiB
    Sysmem: init
    Relocation Offset: eda1b000
    Relocation fdt: eb9fa200 - eb9fece0
    CR: M/C/I
    DM: v2

U-Boot Information
""""""""""""""""""""

|   The line "U-Boot 2017.09 (May 12 2025 - 15:23:24 +0000)" in the startup information contains the following details:

- [U-Boot Version]: 2017.09;
- [Compilation Time of the U-Boot File]: May 12 2025 - 15:23:24 +0000.

Kernel Information
""""""""""""""""""""

|   The following lines in the startup information:

.. code-block:: shell

    [    1.903539] Linux version 5.10.198 (root@myzr-u2004) (aarch64-none-linux-gnu-gcc (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 10.3.1 20210621, GNU ld (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 2.36.1.20210621) #1 SMP Mon May 12 15:25:06 UTC 2025
    [    1.914167] Machine model: MYZR RK3588 EK360 Board

|   contain the following details:

 - [Kernel Version]: Linux 5.10.198;
 - [GCC Version for Kernel Compilation]: 10.3.1;
 - [Compilation Time of the Kernel File]: Mon May 12 15:25:06 UTC 2025


Log In to the Development Board
""""""""""""""""""""""""""""""""""

|   After the system starts up completely, press the **Enter** key. The prompt "root@root:/#" will be displayed.

- [Username]: root
- [Password]: None

|   Tip: After logging in, you can use the "passwd" command to set and change the password.