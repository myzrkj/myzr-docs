
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
| 　　2. 参考  :doc:`《Xshell 参考手册》 </docs/COMMON/Xshell.RM.参考手册>`  新建串口会话并打开会话。      

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

   U-Boot 2017.09 (Jan 10 2024 - 14:26:12 +0800)

   Model: MYZR RK3588 Evaluation Board
   PreSerial: 2, raw, 0xfeb50000
   DRAM:  3.7 GiB
   Sysmem: init
   Relocation Offset: eda39000
   Relocation fdt: eb9fa1f8 - eb9fecd8
   CR: M/C/I
   mmc@fe2c0000: 1, mmc@fe2e0000: 0
   Bootdev(atags): mmc 0
   MMC0: HS200, 200Mhz
   PartType: EFI
   DM: v2
   boot mode: recovery (misc)
   boot mode: None
   ........
   Starting kernel ...

   [    4.563675][    T0] Booting Linux on physical CPU 0x0000000000 [0x412fd050]
   [    4.563694][    T0] Linux version 5.10.110 (kuangwh@myzr-7a9b) (Android (7284624, based on r416183b)
   clang version 12.0.5 (https://android.googlesource.com/toolchain/llvm-project c935d99d7cf2016289302412d
   708641d52d2f7ee), LLD 12.0.5 (/buildbot/src/android/llvm-toolchain/out/llvm-project/lld c935d99d7cf20162
   89302412d708641d52d2f7ee)) #14 SMP PREEMPT Wed Jan 10 14:32:50 CST 2024
   ............

   console:/ $ 

U-Boot 信息
~~~~~~~~~~~

| 　　启动信息中 ``U-Boot 2017.09 (Jan 10 2024 - 14:26:12 +0800)`` 包含以下信息：
| 　　【u-boot版本】 ：2017.09；
| 　　【u-boot文件的编译时间】 ：Jan 10 2024 - 14:26:12 +0800。

内核信息
~~~~~~~~

| 　　启动信息中 ``Linux version 5.10.110 (kuangwh@myzr-7a9b) (Android (7284624, based on r416183b)
   clang version 12.0.5 (https://android.googlesource.com/toolchain/llvm-project c935d99d7cf2016289302412d
   708641d52d2f7ee), LLD 12.0.5 (/buildbot/src/android/llvm-toolchain/out/llvm-project/lld c935d99d7cf20162
   89302412d708641d52d2f7ee)) #14 SMP PREEMPT Wed Jan 10 14:32:50 CST 2024`` 包含以下信息：
| 　　【内核版本】 ：Linux- 5.10.110；
| 　　【编译内核的clang版本】 ： clang version 12.0.5；
| 　　【内核文件的编译时间】 ：Wed Jan 10 14:32:50 CST 2024。
 

开发板登录
----------

| 　　启动系统完后输出 ``console:/ $`` 时已登录：
| 　　这时可以切换root用户：输入命令su


--------------------------------------------------------------------------------

::

   --------------------------------------------------------------------------------
   * 珠海明远智睿科技有限公司  
   * ZhuHai MYZR Technology CO.,LTD.
   * Latest Update: 2024/1/10  
   * Supporter: kuangwh
   --------------------------------------------------------------------------------
