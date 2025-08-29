Startup Manual
================

Development Board Connection
-------------------------------

Serial Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Use a Type-C cable to connect the "CON1" interface of the evaluation board to the USB port of the PC.
2. Refer to the :doc:`《XShell reference manual》</docs/COMMON/Terminal software XShell reference manual>` to create a new serial session and open the session.

Ethernet Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the Ethernet cable to "J15" or "J14", and the other end to the network port of the computer.

Download Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the double-headed USB cable to J6, and the other end to the rear USB port of the computer.

Power Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the power adapter to the "12V_IN" port of the development board, and the other end to a mains (220V AC) socket.

Starting the Development Board
---------------------------------

Interpretation of Development Board Startup Information
----------------------------------------------------------

|   After the development board is powered on, the startup information output by the development board can be viewed on the serial terminal software.

.. code-block:: shell

    U-Boot SPL board init
    U-Boot SPL 2017.09 (Jun 05 2025 - 15:47:49)
    sfc cmd=03H(6BH-x4)
    SPI Nand ID ef aa 22
    unrecognized JEDEC id bytes: ff, ef, aa
    Trying to boot from MTD1
    Trying fit image at 0x2000 sector
    Trying kernel at 0xba00 sector from 'boot' part
    Jumping to Kernel(0x01100000) via OP-TEE(0x00001000)
    Total: 278.672/343.84 ms

    I/TC: Status: cluster=0xc00, core=0xe100, bootcpu=0
    I/TC: Next entry point address: 0x01100000
    I/TC: OP-TEE version: 3.13.0-894-g0e7e5b3c7ff #chenjh (gcc version 10.2.1 20201103 (GNU Toolchain for the A-profile Architecture 10.2-2020.11 (arm-10.16))) #2 Tue Nov 12 09:21:23 CST 2024 arm, fwver: v1.25 
    I/TC: OP-TEE memory: TEEOS 0x5e000 TA 0x1000 SHM 0x1000
    I/TC: Primary CPU initializing
    I/TC: Primary CPU switching to normal world boot
    [    0.478757] Booting Linux on physical CPU 0xf00
    [    0.478780] Linux version 6.1.84 (huangyc@myzr-u2004-ec50) (arm-none-linux-gnueabihf-gcc (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 10.3.1 20210621, GNU ld (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 2.36.1.20210621) #1 SMP PREEMPT Thu Jun  5 15:50:39 CST 2025
    [    0.479080] Machine model: myzr-rk3506-ek200
  
U-Boot Information
~~~~~~~~~~~~~~~~~~~~

|   The line "U-Boot 2017.09 (Jun 05 2025 - 15:47:49)" in the startup information contains the following details:
|   [U-Boot Version]: 2017.09;
|   [Source Code Version Number]: g8372631b28;
|   [U-Boot File Compilation Time]: Jun 05 2025 - 15:47:49.

Kernel Information
~~~~~~~~~~~~~~~~~~~~

|   The line "Linux version 6.1.84 (huangyc@myzr-u2004-ec50) (aarch64-none-linux-gnu-gcc (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 10.3.1 20210621, GNU ld (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 2.36.1.20210621) #12 SMP Thu May 29 08:04:48 UTC 2025" in the startup information contains the following details:
|   [Kernel Version]: Linux-6.1.84;
|   [GCC Version for Kernel Compilation]: 10.3.1;
|   [Kernel File Compilation Time]: Thu May 29 08:04:48 UTC 2025.

Development Board Login
--------------------------

|   After the system starts up and the output shows "root@RK3506-MYZR:", you can log in with the following credentials:
|   [Username]: root
|   [Password]: None
|   Tip: After logging in, you can use the "passwd" command to set and modify the password.