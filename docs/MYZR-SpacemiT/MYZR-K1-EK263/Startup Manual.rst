Startup Manual
================

Development Board Connection
------------------------------

Check Power Switch
~~~~~~~~~~~~~~~~~~~~

|   Slide the development board power switch POW_KEY to the OFF side to ensure the power switch is disconnected.

Serial Port Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Connect one end of the Type-C cable to the Debug port of the development board, and the other end to the serial port of the computer.
2. Refer to the *Xshell Reference Manual* to create and open a new serial session.

Network Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the network cable to ETH1 or ETH0, and the other end to the computer network port.

Download Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the Type-C cable to U18, and the other end to the rear USB port of the computer.

Power Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the 12V power adapter to CON1 on the development board, and plug the other end into a 220V AC mains socket.

HDMI Display Connection

|   Connect one end of the HDMI display cable to the HDMI interface of the development board, connect the other end to the HDMI display, and power on the HDMI display.

Power On the Development Board
--------------------------------

Board Power-on
~~~~~~~~~~~~~~~~

1. Connect one end of the Type-C cable to Debug and the other end to the computer USB port; connect 12V power to CON1, toggle the SW2 DIP switch of the development board to boot mode; switch POW_KEY to ON to power on the board.

+------------+------------+------------+------------+-------------+
| QSPI_DATA0 | QSPI_DATA1 | QSPI_DATA2 | QSPI_DATA3 | Description |
+------------+------------+------------+------------+-------------+
| 0          | 0          | 0          | 1          | Flash Mode  |
+------------+------------+------------+------------+-------------+
| 0          | 0          | 0          | 0          | Boot Mode   |
+------------+------------+------------+------------+-------------+

|   Note: The ON (1) side of the DIP switch is the letter side, and OFF (0) is the number side

Analysis of Development Board Boot Logs
-----------------------------------------

|   After the development board is powered on, boot information output by the board can be viewed in the serial terminal software.

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
~~~~~~~~~~~~~~~~~~~~

|   The boot log entry U-Boot SPL 2022.10spacemit (Dec 01 2025 - 04:34:31 +0000) includes the following details:
|   [U-Boot Version] : 2022.10;
|   [U-Boot Compile Time] : Dec 01 2025 - 04:34:31 +0000.

Kernel Information
~~~~~~~~~~~~~~~~~~~~

|   The boot log entry Linux version 6.6.63 (chensz@myzr-u2004) (riscv64-unknown-linux-gnu-gcc (g09b62c20e09) 13.2.1 20240423, GNU ld (GNU Binutils) 2.42) #3 SMP PREEMPT Tue Dec  2 09:07:38 UTC 2025 contains the following information:
|   [Kernel Version] : Linux version 6.6.63;
|   [Kernel Build GCC Version] : 13.2.1;
|   [Kernel Compile Time] : Tue Dec  2 09:07:38 UTC 2025.

Development Board Login
~~~~~~~~~~~~~~~~~~~~~~~~~

|   Automatic login will be completed after system startup. Press any key and enter the credentials below:
|   [Username] : root
|   [Password] : bianbu
|   Tip: Use the "passwd" command after login to set and modify the password.