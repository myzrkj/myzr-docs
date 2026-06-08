
MYZR-IMX8M-EK300 启动手册
==========================

MYZR-IMX8M-EK300 包装清单
--------------------------

**标准件**

|  【底板】：MYZR-IMX8M-MB300，1片
|  【核心板】：MYZR-IMX8M-CB300，1片
|  【电源适配器】：12V，1个
|  【网线】：1条
|  【串口线】：1条

**用户自备件**

|  【双头 USB线】：1条，下载时使用
|  【USB 转串口线】：1条，调试时使用（如电脑没有DB9串口的情况下需要自备）

MYZR-IMX8M-MB300 主要接口
---------------------------

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8M-EK300/1500px-IMX8M-EK300-front.png
   :alt: image-1500px-IMX8M-EK300-front.png

开发板连接
------------

**检查电源开关**

|  把开发板的电源开关“SWITCH”的“o”按下，以确保开发板电源开关处于断开状态。

**串口线的连接**

|  把串口线的一端连接到开发板的“DEBUG”口，另一端连接到电脑的串口或USB口。
|  参考 :doc:`《终端软件XShell参考手册》 </docs/COMMON/Xshell.RM.参考手册>` 新建串口会话并打开会话。

**网线的连接**

|  把网线的一端连接到“ETH1”，另一端连接到电脑的网口。

**USB下载线的连接**

|  把双头 USB线的一端连接J15，另一端连接到电脑的后置USB口。

**电源线的连接**

|  把电源适配器的一端连接到开发板的“12V_IN”，另一端插入到市电（220V的交流电）插座。

**HDMI显示屏连接**

|  将 HDMI 显示屏连接线的一端接到开发板，另一端接到 HDMI 显示屏，并为 HDMI 显示屏上电。
|  注意：HDMI 显示屏的分辨率建议使用 1080P，以及使用 HDMI 接口的显示屏，而不是转接为 HDMI 接口的。

启动开发板
-----------

**检查开发板的启动模式拨码**

|  把开发板的“BOOT MODE”拨码开关拨到正常启动模式。
|  【启动模式】：1（ON），2（OFF）
|  【下载模式】：1（OFF），2（ON）
|  注：拨码开关的ON是字母那一边，OFF是数字的那一边。

**为开发板上电**

|  把开发板的电源开关“SWITCH”的“-”按下，以使开发板电源开关打开。这时可以看到开发板LED灯有部分亮起来了。

**开发板的启动信息解读**

|  开发板通电后在串口终端软件上可以看到开发板输出的启动信息。

.. code-block:: shell

   U-Boot 2019.04-04784-g7666e4b (Dec 23 2019 - 10:15:13 +0800)

   CPU:   Freescale i.MX8MQ rev2.1 1500 MHz (running at 1000 MHz)
   CPU:   Commercial temperature grade (0C to 95C) at 26C
   Reset cause: POR
   Model: MYZR i.MX8M Evaluation Kit (300 pins)
   DRAM:  2 GiB
   MMC:   FSL_SDHC: 0, FSL_SDHC: 1
   Loading Environment from MMC... *** Warning - bad CRC, using default environment


   ......

   Starting kernel ...

   Booting Linux on physical CPU 0x0
   Linux version 4.14.98 (myzr@u14045) (gcc version 7.3.1 20180425 [linaro-7.3-2018.05 revision d29120a424ecfbc167ef90065c0eeb7f91977701] (Linaro GCC 7.3-2018.05)) #2 SMP PREEMPT Tue Jan 14 14:30:15 CST 2020
   Boot CPU: AArch64 Processor [410fd034]
   Machine model: MYZR i.MX8M Evaluation Kit (300 pins)

   ......

   [  OK  ] Reached target Multi-User System.
            Starting Update UTMP about System Runlevel Changes...
   [  OK  ] Started Session c1 of user root.
   [  OK  ] Started User Manager for UID 0.
   [  OK  ] Started Update UTMP about System Runlevel Changes.

   NXP i.MX Release Distro 4.14-sumo imx8mqek300 ttymxc0

**U-Boot 信息**

|  启动信息中“U-Boot 2019.04-04784-g7666e4b (Dec 23 2019 - 10:15:13 +0800)”包含以下信息：
|  【u-boot版本】：2019.04；
|  【源码的版本号】：g7666e4b；
|  【u-boot文件的编译时间】：Dec 23 2019 - 10:15:13 +0800。

**内核信息**

|  启动信息中“Linux version 4.14.98 (myzr@u14045) (gcc version 7.3.1 20180425 [linaro-7.3-2018.05 revision d29120a424ecfbc167ef90065c0eeb7f91977701] (Linaro GCC 7.3-2018.05)) #2 SMP PREEMPT Tue Jan 14 14:30:15 CST 2020”包含以下信息：
|  【内核版本】：Linux-4.14.98；
|  【编译内核的GCC版本】：7.3.1；
|  【内核文件的编译时间】：Tue Jan 14 14:30:15 CST 2020。

**开发板登录**

|  启动系统完后输出“imx8mqek300 login:: ”时，可以登录：
|  【用户名】：root
|  【密码】：无
|  注：登录后可以通过“passwd”命令来设置和修改密码。
