MYZR-IMX6-EK140P 启动手册
===========================

MYZR-IMX6-EK140P 包装清单
---------------------------

**标准件**

|  【底板】：MYZR-IMX6-MB140P，1片
|  【核心板】：MYZR-IMX6-CB140，1片（已贴在底板上）
|  【电源适配器】：5V，1个
|  【网线】：1条
|  【串口线】：1条

**用户自备件**

|  【Micro USB线】：1条，下载时使用（常用的Android手机数据线即可）
|  【USB 转串口线】：1条，调试时使用（如电脑没有DB9串口的情况下需要自备）

**其它选配件**

|  【显示屏电路板】
|  【液晶显示屏】
|  【触摸屏】

MYZR-IMX6-EK140P 主要接口
---------------------------

.. figure:: /image/MYZR-iMX6系列/MYZR-IMX6-EK140P/1425px-MYIMX6A7-MB140P-Port-F.png
   :alt: 1425px-MYIMX6A7-MB140P-Port-F.png

开发板连接
-----------

**检查电源开关**

|   把开发板的电源开关“SWITCH”的“o”按下，以确保开发板电源开关处于断开状态。

**串口线的连接**

|   把串口线的一端连接到开发板的“DEBUG”口，另一端连接到电脑的串口或USB口。
|   参考 :doc:`《终端软件XShell参考手册》 </docs/COMMON/Xshell.RM.参考手册>` 新建串口会话并打开会话。

**网线的连接**

|   把网线的一端连接到“ETH1”，另一端连接到电脑的网口。

**USB下载线的连接**

|   把Micro USB线的一端连接到开发板的“USB OTG”口，另一端连接到电脑的后置USB口。

**电源线的连接**

|   把电源适配器的一端连接到开发板的“5V_IN”，另一端插入到市电（220V的交流电）插座。

启动开发板
-----------

**检查开发板的启动模式拨码**

|   把开发板的“BOOT MODE”拨码开关拨到正常启动模式。
|   【启动模式】：1（OFF），2（ON）
|   【下载模式】：1（ON），2（OFF）
|   注：拨码开关的ON是字母那一边，OFF是数字的那一边。

**检查开发板的启动介质拨码**

|   根据自己的开发板选择对应的启动介质。
|   【eMMC 启动】：1（ON），2（ON），3（ON），4（OFF）
|   【Nand 启动】：1（OFF），2（OFF），3（OFF），4（ON）

**为开发板上电**

|   把开发板的电源开关“SWITCH”的“-”按下，以使开发板电源开关打开。这时可以看到开发板LED灯有部分亮起来了。

开发板的启动信息解读
---------------------

|   开发板通电后在串口终端软件上可以看到开发板输出的启动信息。

.. code-block:: shell

   U-Boot 2016.03-svn315 (Nov 21 2018 - 15:03:14 +0800)

   CPU:   Freescale i.MX6ULL rev1.0 528 MHz (running at 396 MHz)
   CPU:   Industrial temperature grade (-40C to 105C) at 35C
   Reset cause: POR
   Board: MYIMX6EK140P-6Y
   I2C:   ready
   DRAM:  512 MiB

   ......

   Starting kernel ...

   Booting Linux on physical CPU 0x0
   Linux version 4.9.88-myimx6a7-svn392 (myzr@u14045) (gcc version 5.3.0 (GCC) ) #25 SMP PREEMPT Tue Nov 20 15:28:40 CST 2018
   CPU: ARMv7 Processor [410fc075] revision 5 (ARMv7), cr=10c53c7d
   ......

   *** Welcome to i.MX6 *************************************** 
       Rootfs File: L4115-fsl-image-gui-myimx6a7.tar.bz2 
       Build Time:  20180919143629 
       Config Time: 2018-08-16 14:41:29.098557900 +0800 
       IP Address:  192.168.137.81   

       SITE: www.myzr.com.cn 
       WIKI: wiki.myzr.com.cn 
       BBS:  bbs.myzr.com.cn 
   *************************************************************

**U-Boot 信息**

|   启动信息中“U-Boot 2016.03-svn315 (Nov 21 2018 - 15:03:14 +0800)”包含以下信息：
|   【u-boot版本】：2016.03；
|   【源码的版本号】：svn315；
|   【u-boot文件的编译时间】：Nov 21 2018 - 15:03:14 +0800。

**内核信息**

|   启动信息中“Linux version 4.9.88-myimx6a7-svn392 (myzr@u14045) (gcc version 5.3.0 (GCC) ) #25 SMP PREEMPT Tue Nov 20 15:28:40 CST 2018”包含以下信息：
|   【内核版本】：Linux-4.9.88；
|   【内核的编译的基础配置文件】：myimx6a7_defconfig；
|   【内核的源码版本号】：svn392；
|   【编译内核的GCC版本】：5.3.0；
|   【内核文件的编译时间】：Tue Nov 20 15:28:40 CST 2018。

**文件系统信息**

|   启动信息中两行“**********”之间的内容有文件系统的信息：
|   【Rootfs File】表示文件系统的基础包；
|   【Build Time】表示文件系统的编译时间；
|   【Config Time】表示文件系统的配置包的信息；
|   【IP Address】表示开发板第一个网口的IP地址；

开发板登录
-----------

|   启动系统完后输出“myimx6ek140p login:”时，可以登录：
|   【用户名】：root
|   【密码】：无
|   `注：登录后可以通过“passwd”命令来设置和修改密码。`