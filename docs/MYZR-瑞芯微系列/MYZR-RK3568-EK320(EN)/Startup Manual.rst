Startup Manual
================

Development Board Connection
------------------------------

Connection of Serial Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Connect one end of the serial cable to the "J9" port of the development board, and the other end to the serial port of the computer.
2. Refer to :doc:`《Xshell Reference Manual》</docs/COMMON/Xshell.RM.参考手册>` to create a new serial session and open the session.

Connection of Network Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the network cable to "U9" and the other end to the network port of the computer.

Connection of Download Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the double-headed USB cable to U9, and the other end to the rear USB port of the computer.

Connection of Power Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the power adapter to the "J15" of the development board, and the other end to the mains (220V AC) socket.

HDMI Display Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the HDMI display cable to J2 of the development board, the other end to the HDMI display, and power on the HDMI display.
|   Note: It is recommended that the resolution of the HDMI display is 1080P, and use a display with an HDMI interface instead of one converted to an HDMI interface.

Start the Development Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Power on the Development Board
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|   Insert the power adapter into the J15 socket of the development board to supply power to the board.

Interpretation of Development Board Startup Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   After the development board is powered on, the startup information output by the development board can be seen on the serial terminal software.

.. code:: shell

    U-Boot SPL 2017.09-gaaca6ffec1-211203 #zzz (Dec 03 2021 - 18:42:16)
    Linux version 4.19.232 (zhengc@myzr-92aa) (gcc version 10.3.1 20210621 (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)), GNU ld (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 2.36.1.20210621) #4 SMP Tue Apr 15 17:28:04 CST 2025
    vcc3v3_pcie: disabling

U-Boot Information
^^^^^^^^^^^^^^^^^^^^

|   The startup information U-Boot SPL 2017.09-gaaca6ffec1-211203 #zzz (Dec 03 2021 - 18:42:16) contains the following information:
|   【u-boot version】: 2017.09;
|   【source code version number】: gaaca6ffec1;
|   【compilation time of u-boot file】: Dec 03 2021 - 18:42:16.

Kernel Information
^^^^^^^^^^^^^^^^^^^^

|   The startup information Linux version 4.19.232 (zhengc@myzr-92aa) (gcc version 10.3.1 20210621 (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)), GNU ld (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 2.36.1.20210621) #4 SMP Tue Apr 15 17:28:04 CST 2025 contains the following information:
|   【kernel version】: Linux-4.19.232;
|   【GCC version for compiling the kernel】: 10.3.1;
|   【compilation time of the kernel file】: Tue Apr 15 17:28:04 CST 2025.

Development Board Login
~~~~~~~~~~~~~~~~~~~~~~~~~

|   After the system is started, press the Enter key to log in;