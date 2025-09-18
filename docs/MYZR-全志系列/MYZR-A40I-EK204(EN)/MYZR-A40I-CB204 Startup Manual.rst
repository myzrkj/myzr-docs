MYZR-A40I-CB204 Startup Manual
================================

Powering On the Development Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Press the "-" of the "SWITCH" on the development board to turn on the power.

Interpreting the Startup Information of the Development Board
----------------------------------------------------------------

| After the development board is powered on, you can view the startup information output by the board on the serial terminal software.

.. code-block:: shell

   U-Boot 2014.07 (Jun 03 2021 - 15:42:22) Allwinner Technology 

   uboot commit : 8 
   i2c_init: by cpux
   i2c_init ok
   [0.533]pmbus:   ready
   [0.554]PMU: AXP221
   [0.554]PMU: AXP22x found
   [0.555]PMU: dcdc2 1160
   [0.555]PMU: cpux 1008 Mhz,AXI=336 Mhz
   PLL6=600 Mhz,AHB1=200 Mhz, APB1=100Mhz  MBus=400Mhz
   DRAM:  1 GiB


   ......

   Starting kernel ...

   [    0.000000] Booting Linux on physical CPU 0x0
   [    0.000000] Initializing cgroup subsys cpu
   [    0.000000] Linux version 3.10.65 (liangyh@FS12) (gcc version 6.4.1 (OpenWrt/Linaro GCC 6.4-2017.11 2017-11) ) #142 SMP Thu Jun 24 07:43:32 UTC 2021
   [    0.000000] CPU: ARMv7 Processor [410fc075] revision 5 (ARMv7), cr=10c53c7d
   [    0.000000] CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
   [    0.000000] Machine: sun8iw11p1, model: sun8iw11p1
   [    0.000000] cma: CMA: reserved 256 MiB at 5f800000
   [    0.000000] Memory policy: ECC disabled, Data cache writealloc
   [    0.000000] On node 0 totalpages: 262144
   [    0.000000] free_area_init_node: node 0, pgdat c06b2880, node_mem_map c06fa000
   [    0.000000]   Normal zone: 1520 pages used for memmap
   [    0.000000]   Normal zone: 0 pages reserved
   [    0.000000]   Normal zone: 194560 pages, LIFO batch:31
   [    0.000000]   HighMem zone: 528 pages used for memmap
   [    0.000000]   HighMem zone: 67584 pages, LIFO batch:15

   ......

U-Boot Information
~~~~~~~~~~~~~~~~~~~~~

| The startup information "U-Boot 2014.07 (Jun 03 2021 - 15:42:22) Allwinner Technology " contains the following details:
| [U-Boot Version]: 2014.07;
| [Compilation Time of U-Boot File]: Jun 03 2021 - 15:42:22 +0800.

Kernel Information
~~~~~~~~~~~~~~~~~~~~~

| The startup information "Linux version 3.10.65 (liangyh@FS12) (gcc version 6.4.1 (OpenWrt/Linaro GCC 6.4-2017.11 2017-11) ) #142 SMP Thu Jun 24 07:43:32 UTC 2021" includes the following information:
| [Kernel Version]: Linux-3.10.65;
| [GCC Version for Kernel Compilation]: 6.4.1;
| [Compilation Time of Kernel File]: Thu Jun 24 07:43:32 UTC 2021. (Note: The original text has a typo "202", which is corrected to "2021" here for accuracy.)


Logging In to the Development Board
--------------------------------------

| After the system starts up, press the Enter key to log in.

要不要我帮你检查这份英文手册中是否存在术语翻译不一致的情况，或者生成一份**中英文术语对照表**方便后续查阅？