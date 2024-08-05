
启动手册
========

开发板连接
----------

检查电源开关
~~~~~~~~~~~~

| 　　把开发板的电源开关“SW1”的“o”按下，以确保开发板电源开关处于断开状态。

串口线的连接
~~~~~~~~~~~~

| 　　1. 把串口线的一端连接到开发板的“CON9”口，另一端连接到电脑的串口或USB口。                                                                     
| 　　2. 参考  :doc:`《Xshell 参考手册》 <../../COMMON/Xshell.RM.参考手册>`  新建串口会话并打开会话。      

网线的连接
~~~~~~~~~~

| 　　把网线的一端连接到“J13”或“J14”，另一端连接到电脑的网口。

下载线的连接
~~~~~~~~~~~~

| 　　把双头USB-A线的一端连接J2，另一端连接到电脑的后置USB口。

电源线的连接
~~~~~~~~~~~~

| 　　把电源适配器的一端连接到开发板的“JACK1”，另一端插入到市电（220V的交流电）插座。
         

启动开发板
----------

| 　　把开发板的电源开关“SWITCH”的“-”按下，以使开发板电源开关打开。

开发板的启动信息解读
--------------------

| 　　开发板通电后在串口终端软件上可以看到开发板输出的启动信息。

::

   U-Boot 2017.09 (Sep 19 2023 - 14:06:08 +0800)

   Model: MYZR RK3568 Evaluation Board
   PreSerial: 2, raw, 0xfe660000
   DRAM:  4 GiB
   Sysmem: init
   Relocation Offset: ed349000
   Relocation fdt: eb9f9260 - eb9fecd0
   CR: M/C/I
   dwmmc@fe2b0000: 1, dwmmc@fe2c0000: 2, sdhci@fe310000: 0
   Bootdev(atags): mmc 0
   MMC0: HS200, 200Mhz
   PartType: EFI
   DM: v1
   boot mode: None
   ........
   Starting kernel ...

   [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x412fd050]
   [    0.000000] Linux version 4.19.232 (kuangwh@myzr-7a9b) (Android (6573524 based on r383902b) 
   clang version 11.0.2 (https://android.googlesource.com/toolchain/llvm-project b397f81060ce6d701042b782172ed13bee898b79),
   LLD 11.0.2 (/buildbot/tmp/tmpF3FjA8 b397f81060ce6d701042b782172ed13bee898b79)) #28 SMP PREEMPT Fri Jan 5 09:39:22 CST 2024
   ............

   console:/ $ 

U-Boot 信息
~~~~~~~~~~~

| 　　启动信息中 ``U-Boot 2017.09 (Sep 19 2023 - 14:06:08 +0800)`` 包含以下信息：
| 　　【u-boot版本】 ：2017.09；
| 　　【u-boot文件的编译时间】 ：Sep 19 2023 - 14:06:08 +0800。

内核信息
~~~~~~~~

| 　　启动信息中 ``Linux version 4.19.232 (kuangwh@myzr-7a9b) (Android (6573524 based on r383902b) 
                  clang version 11.0.2 (https://android.googlesource.com/toolchain/llvm-project b397f81060ce6d701042b782172ed13bee898b79),
                  LLD 11.0.2 (/buildbot/tmp/tmpF3FjA8 b397f81060ce6d701042b782172ed13bee898b79)) #28 SMP PREEMPT Fri Jan 5 09:39:22 CST 2024`` 包含以下信息：
| 　　【内核版本】 ：Linux- 4.19.232；
| 　　【编译内核的clang版本】 ： clang version 11.0.2；
| 　　【内核文件的编译时间】 ：Fri Jan 5 09:39:22 CST 2024。
 

开发板登录
----------

| 　　启动系统完后输出 ``console:/ $`` 时已登录：
| 　　这时可以切换root用户：输入命令su


--------------------------------------------------------------------------------

::

   --------------------------------------------------------------------------------
   * 珠海明远智睿科技有限公司  
   * ZhuHai MYZR Technology CO.,LTD.
   * Latest Update: 2024/1/9  
   * Supporter: kuangwh
   --------------------------------------------------------------------------------
