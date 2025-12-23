Startup Manual
================

Development Board Connection
------------------------------

Serial Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Use a Type-C cable to connect the "CON4" interface of the evaluation board to the USB interface of the PC.
2. Refer to the :doc:`《Xshell Reference Manual》</docs/COMMON/Terminal software XShell reference manual>` to create a new serial session and open the session.

Ethernet Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the Ethernet cable to "J14" or "J15", and the other end to the Ethernet port of the PC.

Download Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the male-to-male double-head USB cable to "OTG2.0 (J6)", and the other end to the rear USB port of the PC.

Power Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the power adapter to the "12V_IN" of the development board (the development board is powered by 12V), and the other end to a mains power (220V AC) socket.

Development Board Startup
---------------------------

Power On the Development Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the power adapter to the "12V_IN" of the development board to turn on the power of the development board.

Interpretation of Development Board Startup Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   After the development board is powered on, the startup information output by the development board can be viewed on the serial terminal software.

.. code-block:: shell

    U-Boot SPL 2017.09 (Jun 05 2025 - 15:47:49)

    Model: myzr-rk3506-ek200
    MPIDR: 0x0
    PreSerial: 0, raw, 0xff210000

    DDR3, 750MHz
    Sysmem: init
    Relocation Offset: 7da3b000
    Relocation fdt: 7b7fa590 - 7b7fecf0
    CR: M/C/I
    DM: v2
  
U-Boot Information
~~~~~~~~~~~~~~~~~~~~~

|   The startup information **U-Boot 2017.09 (Jun 05 2025 - 15:47:49)** includes the following details:
|   【U-Boot Version】: 2017.09;
|   【U-Boot File Compilation Time】: Jun 05 2025 - 15:47:49.

Kernel Information
~~~~~~~~~~~~~~~~~~~~

|   In the startup information:

|   [   0.478780] Linux version 6.1.84 (huangyc@myzr-u2004-ec50) (aarch64-none-linux-gnu-gcc (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 10.3.1 20210621, GNU ld (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 2.36.1.20210621) #12 SMP Thu May 29 08:04:48 UTC 2025
|   [   0.479080] Machine model: myzr-rk3506-ek200

|   The following information is included:

|   【Kernel Version】: Linux-6.1.84;
|   【GCC Version for Kernel Compilation】: 10.3.1;
|   【Kernel File Compilation Time】: Thu May 29 08:04:48 UTC 2025

Development Board Login
-------------------------

|   After the system starts, press the Enter key to display **root@RK3506-MYZR:~#**
|   【Username】: root
|   【Password】: None
|   Tip: After logging in, you can use the "passwd" command to set and modify the password.
