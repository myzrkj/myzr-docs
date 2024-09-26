MYZR-LS1012A-EK200 启动手册
=============================

MYZR-LS1012A-EK200 包装清单
-----------------------------

**标准件**

|   【底板】：MYZR-LS1012A-MB200，1片
|   【核心板】：MYZR-LS1012A-CB200，1片
|   【电源适配器】：5V，1个
|   【网线】：1条
|   【串口线】：1条

**用户自备件**

|   【Mini USB线】：1条，下载时使用（常用的Android手机数据线即可）
|   【USB 转串口线】：1条，调试时使用（如电脑没有DB9串口的情况下需要自备）

MYZR-LS1012A-EK200 主要接口
-----------------------------

开发板连接
~~~~~~~~~~~~

**检查电源开关**

|   把开发板的电源开关“SWITCH”的“o”按下，以确保开发板电源开关处于断开状态。

**串口线的连接**

|   把串口线的一端连接到开发板的“DEBUG”口，另一端连接到电脑的串口或USB口。
|   参考 :doc:`《终端软件XShell参考手册》 </docs/COMMON/Xshell.RM.参考手册>` 新建串口会话并打开会话。

**网线的连接**

|   把网线的一端连接到“ETH1”，另一端连接到电脑的网口。

**USB下载线的连接**

|   把Mini USB线的一端连接K20-JTAG模块，另一端连接到电脑的后置USB口。

**电源线的连接**

|   把电源适配器的一端连接到开发板的“5V_IN”，另一端插入到市电（220V的交流电）插座。

**K20-JTAG模块的连接**

|   把K20-JTAG模块连接开发板的J8接口，另一端连接miniUSB线

启动开发板
~~~~~~~~~~~

**检查开发板的启动模式拨码**

|   把开发板的“BOOT MODE”拨码开关拨到正常启动模式。
|   【启动模式】：1（OFF），2（ON）
|   【下载模式】：1（ON），2（OFF）
|   注：拨码开关的ON是字母那一边，OFF是数字的那一边。

**为开发板上电**

|   把开发板的电源开关“SWITCH”的“-”按下，以使开发板电源开关打开。这时可以看到开发板LED灯有部分亮起来了。

开发板的启动信息解读
~~~~~~~~~~~~~~~~~~~~~

|   开发板通电后在串口终端软件上可以看到开发板输出的启动信息。

.. code:: shell

   U-Boot 2016.092.0+ga06b20925c (Nov 01 2019 - 18:45:12 +0800)

   SoC:  LS1012A Rev1.0 (0x87040110)
   Clock Configuration:
          CPU0(A53):800  MHz  
          Bus:      250  MHz  DDR:      1000 MT/s
   Reset Configuration Word (RCW):
          00000000: 08000008 00000000 00000000 00000000
          00000010: 33050000 c000000c 40000000 00001800
          00000020: 00000000 00000000 00000000 00004570
          00000030: 00000000 00c28120 00000096 00000000
   I2C:   ready
   DRAM:  510 MiB


   ......

   Starting kernel ...

   [    0.000000] Booting Linux on physical CPU 0x0
   [    0.000000] Initializing cgroup subsys cpu
   [    0.000000] Linux version 4.1.35-rt41 (linyn@u12045) (gcc version 4.9.3 20150311 (prerelease) (Linaro GCC 4.9-2015.03) ) #1 SMP Mon Nov 4 19:59:14 CST 2019
   [    0.000000] CPU: AArch64 Processor [410fd034] revision 4

   ......

   Starting system log daemon...0
   Starting kernel log daemon...0
   Starting internet superserver: xinetd.

   QorIQ SDK (FSL Reference Distro) 2.0 ls1012a-ek200 /dev/ttyS0

**U-Boot 信息**

|   启动信息中“U-Boot 2016.092.0+ga06b20925c (Nov 01 2019 - 18:45:12 +0800)”包含以下信息：
|   【u-boot版本】：2016.09；
|   【源码的版本号】：ga06b20925c；
|   【u-boot文件的编译时间】：Nov 01 2019 - 18:45:12 +0800。

**内核信息**

|   启动信息中“Linux version 4.1.35-rt41 (linyn@u12045) (gcc version 4.9.3 20150311 (prerelease) (Linaro GCC 4.9-2015.03) ) #1 SMP Mon Nov 4 19:59:14 CST 2019”包含以下信息：
|   【内核版本】：Linux-4.1.35；
|   【内核的源码版本号】：rt41；
|   【编译内核的GCC版本】：4.9.3；
|   【内核文件的编译时间】：Mon Nov 4 19:59:14 CST 2019。

开发板登录
~~~~~~~~~~~~

|   启动系统完后输出“ls1012a-ek200 login: ”时，可以登录：
|   【用户名】：root
|   【密码】：无

`注：登录后可以通过“passwd”命令来设置和修改密码。`