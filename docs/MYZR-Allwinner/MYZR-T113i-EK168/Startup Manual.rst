Startup Manual
================

Connecting the Development Board
----------------------------------

Checking the Power Switch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Toggle the power switch SW1 of the development board to the OFF position to ensure the development board's power switch is in the disconnected state.

Connecting the Serial Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Use a Type-C cable to connect the DEBUG (CON3) interface of the development board to the USB interface of the PC.
2. Open the Device Manager and confirm the COM port number corresponding to the DEBUG (CON3) interface debugging serial port of the development board.
3. Open Xshell, select the corresponding COM port number, set the baud rate to 115200, 8N1 (8 data bits, 1 stop bit), and no parity bit. Establish the serial connection.

Connecting the Power Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the 12V power adapter to the CON1 interface of the development board, and insert the other end into a mains (220V AC) socket.

Connecting the HDMI Display
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the HDMI display cable to the development board, and the other end to the HDMI display. Then power on the HDMI display.

Connecting the Network Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the network cable to the CON20 or CON21 interface of the development board, and the other end to the network port of the computer.

Starting the Development Board
--------------------------------

Powering On the Development Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Toggle the power switch SW1 of the development board to the ON position to turn on the development board.

Development Board Startup Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    U-Boot 2018.07 (May 28 2025 - 17:32:16 +0800) Allwinner Technology

    [00.384]CPU:   Allwinner Family
    [00.387]Model: sun8iw20
    I2C:   ready
    [00.408]DRAM:  256 MiB
    [00.411]Relocation Offset is: 0cebb000
    [00.439]secure enable bit: 0
    E/TC:0   fdt_getprop_u32:336 prop trace_level not found
    [00.453]CPU=1008 MHz,PLL6=600 Mhz,AHB=200 Mhz, APB1=100Mhz  MBus=300Mhz
    [00.459]gic: sec monitor mode
    SPI ALL:   ready
    [00.464]line:703 init_clocks
    [00.467]flash init start
    [00.469]workmode = 0,storage type = 2
    ...
    [04.236]Starting kernel ...

    [04.239][mmc]: mmc exit start
    [04.256][mmc]: mmc 2 exit ok
    [    0.000000] Booting Linux on physical CPU 0x0
    [    0.000000] Linux version 5.4.61 (root@myzr-u2004) (arm-linux-gnueabi-gcc (Linaro GCC 5.3-2016.05) 5.3.1 20160412, GNU ld (Linaro_Binutils-2016.05) 2.25.0 Linaro 2016_02) #11 SMP PREEMPT Thu May 29 14:04:27 CST 2025
    [    0.000000] CPU: ARMv7 Processor [410fc075] revision 5 (ARMv7), cr=10c5387d
    [    0.000000] CPU: div instructions available: patching division code
    [    0.000000] CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
    [    0.000000] OF: fdt: Machine model: MYZR-T113-EVB V1
    ...
    [    5.186111] FAT-fs (mmcblk0p8): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.
    /dev/by-name/UDISK already format
    [    5.201084] sunxi_set_cur_vol_work()422 WARN: get power supply failed
    [    5.240361] FAT-fs (mmcblk0p8): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.
    Starting dnsmasq: [    5.287866] android_work: sent uevent USB_STATE=CONNECTED
    [    5.325756] configfs-gadget gadget: high-speed config #1: c
    [    5.332294] android_work: sent uevent USB_STATE=CONFIGURED
    OK
    Trying to connect to SWUpdate...
    swu_param: ####
    swu_software: ####
    swu_mode: ####
    no swupdate_cmd to run, wait for next swupdate

U-Boot Information
~~~~~~~~~~~~~~~~~~~~

|   The startup information "U-Boot 2018.07 (May 28 2025 - 17:32:16 +0800) Allwinner Technology" contains the following information:
|   [U-Boot Version]: 2018.07;
|   [Chip Manufacturer]: Allwinner Technology;
|   [U-Boot File Compilation Time]: (May 28 2025 - 17:32:16 +0800).

Kernel Information
~~~~~~~~~~~~~~~~~~~~

|   The startup information "Linux version 5.4.61 (root@myzr-u2004) (arm-linux-gnueabi-gcc (Linaro GCC 5.3-2016.05) 5.3.1 20160412, GNU ld (Linaro_Binutils-2016.05) 2.25.0 Linaro 2016_02) #11 SMP PREEMPT Thu May 29 14:04:27 CST 2025" contains the following information:
|   [Kernel Version]: Linux-5.4.61;
|   [GCC Version for Kernel Compilation]: 5.3;
|   [Kernel File Compilation Time]: Thu May 29 14:04:27 CST 2025.

Logging In to the Development Board
--------------------------------------

.. code-block:: shell

    Trying to connect to SWUpdate...
    swu_param: ####
    swu_software: ####
    swu_mode: ####
    no swupdate_cmd to run, wait for next swupdate

|   When the above information is displayed during startup, press the Enter key to access the system.