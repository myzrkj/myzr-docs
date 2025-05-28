
MYZR-A40I-CB204 启动手册
=========================

启动开发板
------------

为开发板上电
~~~~~~~~~~~~~

|  把开发板的电源开关“SWITCH”的“-”按下，以使开发板电源开关打开。

开发板的启动信息解读
--------------------

|  开发板通电后在串口终端软件上可以看到开发板输出的启动信息。

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

U-Boot 信息
~~~~~~~~~~~~

|  启动信息中“U-Boot 2014.07 (Jun 03 2021 - 15:42:22) Allwinner Technology ”包含以下信息：
|  【u-boot版本】：2014.07 ；
|  【u-boot文件的编译时间】：Jun 03 2021 - 15:42:22 +0800。

内核信息
~~~~~~~~~

|  启动信息中“Linux version 3.10.65 (liangyh@FS12) (gcc version 6.4.1 (OpenWrt/Linaro GCC 6.4-2017.11 2017-11) ) #142 SMP Thu Jun 24 07:43:32 UTC 2021”包含以下信息：
|  【内核版本】：Linux- 3.10.65；
|  【编译内核的GCC版本】：6.4.1；
|  【内核文件的编译时间】：Thu Jun 24 07:43:32 UTC 202。


开发板登录
-----------

|  启动系统完后按回车，可以登录
