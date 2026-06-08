Startup Manual
================

Development Board Connection
------------------------------

Check the Power Switch
~~~~~~~~~~~~~~~~~~~~~~~~

|   Toggle the power switch "SW1" of the development board to the side with letters to ensure the power switch of the development board is in the **off** state.

Serial Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Connect one end of the Type-C cable to the "CON5" port of the development board, and the other end to the serial port of the computer.
2. Refer to the *Xshell Reference Manual* to create a new serial session and open the session.

Ethernet Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the Ethernet cable to "CON15" or "CON16", and the other end to the Ethernet port of the computer.

Download Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the Type-C cable to CON12, and the other end to the rear USB port of the computer.

Power Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the power adapter to "CON3" of the development board, and the other end to a mains power (220V AC) socket.

HDMI Display Connection
~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the HDMI display cable to CON22 of the development board, and the other end to the HDMI display. Then power on the HDMI display.
|   **Note**: It is recommended that the HDMI display uses a resolution of 1080P and is a display with a native HDMI interface (not a display converted to an HDMI interface).


Power On the Development Board
---------------------------------

Power On the Development Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Toggle the power switch SW1 of the development board to the side with English letters to turn on the development board.

Interpretation of Development Board Startup Information
----------------------------------------------------------

|   After the development board is powered on, the startup information output by the development board can be viewed on the serial terminal software.

.. code-block:: shell

    U-Boot 2021.04-g245e65b5 (Jan 17 2023 - 17:01:28 +0800)
    CPU:   i.MX8MP[8] rev1.1 1800 MHz (running at 1200 MHz)
    CPU:   Commercial temperature grade (0C to 95C) at 28C
    Reset cause: POR
    Model: MYZR i.MX8MPlus EK314 board
    DRAM:  6 GiB
    MMC:   FSL_SDHC: 1, FSL_SDHC: 2
    Loading Environment from MMC... OK........
    Starting kernel ...
    [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd034]
    [    0.000000] Linux version 5.10.72-gdcb9071261a3 (tangbin@MYZR-230304) (aarch64-linux-gnu-gcc (Linaro GCC 7.5-2019.12) 7.5.0, GNU ld (Linaro_Binutils-2019.12) 2.28.2.20170706) #11 SMP PREEMPT Thu Mar 16 10:25:45 CST 2023
    [    0.000000] Machine model: MYZR i.MX8M Plus EK314 board
    [    0.000000] efi: UEFI not found.
    [    0.000000] Reserved memory: created CMA memory pool at 0x00000000c4000000, size 960 MiB
    [    0.000000] OF: reserved mem: initialized node linux,cma, compatible id shared-dma-pool
    [    0.000000] Reserved memory: created DMA memory pool at 0x0000000094300000, size 1 MiB
    [    0.000000] OF: reserved mem: ini............
    NXP i.MX Release Distro 5.10-hardknott imx8mp-ddr4-evk ttymxc1
    imx8mp-ddr4-evk login: [   33.759760] can1-stby: disabling


U-Boot Information
~~~~~~~~~~~~~~~~~~~~~

|   The startup information line **U-Boot SPL 2021.04-lf_v2021.04+g8372631b28 (Jun 10 2022 - 06:24:02 +0000)** contains the following details:

- [U-Boot Version]: 2021.04
- [Source Code Version]: g8372631b28
- [U-Boot File Compilation Time]: Jun 10 2022 - 06:24:02 +0000

Kernel Information
~~~~~~~~~~~~~~~~~~~~~
|   The startup information line **Linux version 5.10.72-gdcb9071261a3 (tangbin@MYZR-230304) (aarch64-linux-gnu-gcc (Linaro GCC 7.5-2019.12) 7.5.0, GNU ld (Linaro_Binutils-2019.12) 2.28.2.20170706) #11 SMP PREEMPT Thu Mar 16 10:25:45 CST 2023** contains the following details:

- [Kernel Version]: Linux 5.10.72
- [GCC Version for Kernel Compilation]: 7.5
- [Kernel File Compilation Time]: Thu Mar 16 10:25:45 CST 2023

Development Board Login
~~~~~~~~~~~~~~~~~~~~~~~~~~

|   After the system starts up, when the message **imx8mp-ddr4-evk login:** is displayed, you can log in with the following credentials:

- [Username]: root
- [Password]: None

|   **Tip**: After logging in, you can use the "passwd" command to set or modify the password.