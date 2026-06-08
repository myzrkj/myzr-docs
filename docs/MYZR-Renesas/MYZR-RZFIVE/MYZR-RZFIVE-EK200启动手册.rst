MYZR-RZFIVE-EK200启动手册
===========================

MYZR-RZFIVE-EK200 包装清单
----------------------------

**标准件**

|   【底板】：MYZR-RZFIVE-MB200，1片
|   【核心板】：MYZR-RZFIVE-CB200，1片
|   【电源适配器】：5V，1个
|   【网线】：1条
|   【串口线】：1条

**用户自备件**

|   【TF卡】：1个，下载时使用（常用的Android手机TF卡即可）
|   【USB 转串口线】：1条，调试时使用（如电脑没有DB9串口的情况下需要自备）

MYZR-RZFIVE-EK200 启动
------------------------

开发板连接
~~~~~~~~~~~

**检查电源开关**

|   把开发板的电源开关“SWITCH”的“o”按下，以确保开发板电源开关处于断开状态。

**串口线的连接**

|   把串口线的一端连接到开发板的“DEBUG”口，另一端连接到电脑的串口或USB口。
|   参考 :doc:`《终端软件XShell参考手册》 </docs/COMMON/Xshell.RM.参考手册>` 新建串口会话并打开会话。

**电源线的连接**

|   把电源适配器的一端连接到开发板的“5V_IN”，另一端插入到市电（220V的交流电）插座。

启动开发板
~~~~~~~~~~~

**检查拨码开关**

|   把开发板的SW1拨码开关拨到正常启动模式。
|   【启动模式】：1（OFF），2（OFF）, 3（ON），4（OFF）
|   【下载模式】：1（OFF），2（OFF）, 3（OFF），4（OFF）
|   注：拨码开关的ON是字母那一边，OFF是数字的那一边。

**为开发板上电**

|   把开发板的电源开关“SWITCH”的“-”按下，以使开发板电源开关打开。这时可以看到开发板LED灯有部分亮起来了。

开发板的启动信息解读
~~~~~~~~~~~~~~~~~~~~

|   开发板通电后在串口终端软件上可以看到开发板输出的启动信息。

.. code-block:: shell

   U-Boot SPL 2020.10 (Feb 15 2023 - 12:04:24 +0800)
   Trying to boot from MMC1
   þ

   U-Boot 2020.10 (Feb 15 2023 - 12:04:24 +0800)

   CPU:   rv64imafdc
   Model: myzr-rzfive
   DRAM:  1.9 GiB
   SW_ET0_EN: ON
   MMC:   sh-sdhi: 0, sh-sdhi: 1
   Loading Environment from MMC... OK
   In:    serial@1004b800
   Out:   serial@1004b800
   Err:   serial@1004b800
   Net:   
   Error: ethernet@11c30000 address not set.
   No ethernet found.

   Hit any key to stop autoboot:  0 

   .......

   Starting kernel ...
       0.000000] Linux version 5.10.145-cip17-riscv-renesas (linyn@u1804) (riscv64-oe-linux-gcc (GCC) 8.3.0, GNU ld (GNU Binutils) 2.31.1) #3 PREEMPT Fri Feb 17 11:31:39 CST 2023
   [    0.000000] OF: fdt: Ignoring memory range 0x48000000 - 0x48200000
   [    0.000000] efi: UEFI not found.

   .......

   OpenEmbedded nodistro.0 myzr-rzfive ttySC0

   myzr-rzfive login: root
   [   11.297976] audit: type=1006 audit(1671168594.911:2): pid=272 uid=0 old-auid=4294967295 auid=0 tty=(none) old-ses=4294967295 ses=1 res=1
   [   12.466686] FAT-fs (mmcblk0p1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.

**U-Boot 信息**

|   启动信息中“U-Boot 2020.10 (Feb 15 2023 - 12:04:24 +0800)”包含以下信息：
|   【u-boot版本】：2020.10；
|   【源码的版本号】：NC;
|   【u-boot文件的编译时间】：Feb 15 2023 - 12:04:24 +0800。

**内核信息**

|   启动信息中“Linux version 5.10.145-cip17-riscv-renesas (linyn@u1804) (riscv64-oe-linux-gcc (GCC) 8.3.0, GNU ld (GNU Binutils) 2.31.1) #3 PREEMPT Fri Feb 17 11:31:39 CST 2023”包含以下信息：
|   【内核版本】：Linux-5.10.145；
|   【内核的源码版本号】：cip17-riscv-renesas；
|   【编译内核的GCC版本】：8.3.0；
|   【内核文件的编译时间】：Fri Feb 17 11:31:39 CST 2023。

开发板登录
~~~~~~~~~~~~

|   启动系统完后输出“myzr-rzfive login: ”时，可以登录：
|   【用户名】：root
|   【密码】：无
|   注：登录后可以通过“passwd”命令来设置和修改密码。