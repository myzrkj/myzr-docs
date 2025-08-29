Startup Manual
================

Development Board Connection
------------------------------

Serial Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Connect one end of the Type-C cable to the "CON4" port on the development board, and the other end to the rear USB port of the computer.
2. Refer to the :doc:`《XShell reference manual》</docs/COMMON/Terminal software XShell reference manual>` to create a new serial session and open the session.

Ethernet Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Connect one end of the Ethernet cable to "CON8" or "CON9", and the other end to the network port of the computer.

Download Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Connect one end of the Type-C cable to "USB3.0 OTG (CON6)", and the other end to the rear USB port of the computer.

Power Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~

| Connect one end of the power adapter to the "Power IN (J15)" of the development board, and the other end to a mains (220V AC) socket.


HDMI Display Connection
~~~~~~~~~~~~~~~~~~~~~~~~~

| Connect one end of the HDMI display cable to CON14 on the development board, and the other end to the HDMI display. Then power on the HDMI display.
| **Note:** It is recommended that the HDMI display uses a resolution of 1080P and is a display with a native HDMI interface, rather than one converted to an HDMI interface.


Starting the Development Board
--------------------------------

Powering On the Development Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Connect one end of the power adapter to "J15" on the development board to turn on the power of the development board.


Interpretation of Development Board Startup Information
----------------------------------------------------------

| After the development board is powered on, the startup information output by the development board can be viewed on the serial terminal software.

.. code-block:: shell

    U-Boot 2017.09 (May 12 2025 - 15:29:05 +0000)
    
    Model: MYZR RK3562 EK200 Board
    MPIDR: 0x0
    PreSerial: 0, raw, 0xff210000
    DRAM:  2 GiB
    Sysmem: init
    Relocation Offset: 7da3b000
    Relocation fdt: 7b7fa590 - 7b7fecf0
    CR: M/C/I
    DM: v2

U-Boot Information
~~~~~~~~~~~~~~~~~~~~

| The startup information "U-Boot 2017.09 (May 12 2025 - 15:29:05 +0000)" includes the following information:
| [U-Boot Version]: 2017.09;
| [Source Code Version Number]: g8372631b28;
| [U-Boot File Compilation Time]: May 12 2025 - 15:29:05 +0000.


Kernel Information
~~~~~~~~~~~~~~~~~~~~~

| The following content in the startup information:
| [    1.903539] Linux version 5.10.209-rt89 (root@RK3562-MYZR) (aarch64-none-linux-gnu-gcc (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 10.3.1 20210621, GNU ld (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 2.36.1.20210621) ##6 SMP Mon May 26 09:06:41 UTC 2025
| [    1.914167] Machine model: MYZR RK3562 EK200 Board

| Contains the following information:
| [Kernel Version]: Linux-5.10.72;
| [GCC Version for Kernel Compilation]: 10.3.1;
| [Kernel File Compilation Time]: Mon May 26 09:06:41 UTC 2025.


Development Board Login
--------------------------

| After the system starts, press the Enter key to display "root@RK3562-MYZR:~#".
| [Username]: root
| [Password]: None
| **Tip:** After logging in, you can use the "passwd" command to set and change the password.