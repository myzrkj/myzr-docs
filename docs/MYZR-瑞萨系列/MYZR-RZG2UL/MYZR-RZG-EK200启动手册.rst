
MYZR-RZG2L
=============

MYZR-RZG-EK200 包装清单
-------------------------

**标准件**

|  【底板】：MYZR-RZG2L-MB200 / MYZR-RZG2UL-MB200-LCD / MYZR-RZG2UL-MB200-ETH，1片
|  【核心板】：MYZR-G2L-CB200 / MYZR-G2UL-CB200，1片
|  【电源适配器】：5V，1个
|  【DEBUG串口接头】：1个
|  【网线】：1条

**用户自备件**

|  【TF卡/U盘】
|  【USB 转串口线】：1条，调试时使用

**其它选配件**

|  【显示屏电路板】
|  【液晶显示屏】
|  【触摸屏】

MYZR-STM32-EK152 主要接口
---------------------------

**MYZR-RZG2L-MB200**

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2UL/1425px-Myzr_rzg2l_zheng.jpg
   :alt: 1425px-Myzr_rzg2l_zheng.jpg

**MYZR-RZG2UL-MB200-ETH**

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2UL/1425px-Myzr_rzg2ul-eth_zheng.jpg
   :alt: 1425px-Myzr_rzg2ul-eth_zheng.jpg

**MYZR-RZG2UL-MB200-LCD**

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2UL/1425px-Myzr_rzg2ul-lcd_zheng.jpg
   :alt: 1425px-Myzr_rzg2ul-lcd_zheng.jpg

开发板连接
-----------

**电源连接**

|  电源线连接到DC：5v-3A的接口上。

**串口线的连接**

|  Debug串口接头连上Debug_232接口上，然后使用USB转串口线连接电脑串口和Debug串口接头。
|  参考 :doc:`《终端软件XShell参考手册》 </docs/COMMON/Xshell.RM.参考手册>` 新建串口会话并打开会话。

**网线的连接**

|  网线一端接ETH10/100/1000M，另一段接电脑网口。

启动开发板
-----------

**检查开发板拨码开关**

|  把开发板的拨码开发板SW：BOOT拨到正常的启动模式，拨码的模式如下：
|  【EMMC启动】：1（off），2（off），3（on），4（off）
|  【烧录模式】：1（on），2（off），3（on），4（off） 　　注：拨码开关的ON是字母那一边，OFF是数字的那一边。

**为开发板上电**

|  直接接上电源适配器给开发板上电，打开电源开关

开发板的启动信息解读
---------------------

|  开发板通电后在串口终端软件上可以看到开发板输出的启动信息。

.. code:: shell

   U-Boot 2021.10 (Feb 07 2023 - 11:36:41 +0800)

   CPU:   Renesas Electronics K rev 16.15
   Model: myzr-rzg2l
   DRAM:  1.9 GiB
   MMC:   sd@11c00000: 0, sd@11c10000: 1
   Loading Environment from MMC... OK
   In:    serial@1004b800
   Out:   serial@1004b800
   Err:   serial@1004b800
   Net:   
   Error: ethernet@11c20000 address not set.
   No ethernet found.

   Hit any key to stop autoboot:  0 
   20951552 bytes read in 666 ms (30 MiB/s)
   38404 bytes read in 3 ms (12.2 MiB/s)
   Moving Image from 0x48080000 to 0x48200000, end=49670000
   ## Flattened Device Tree blob at 48000000
      Booting using the fdt blob at 0x48000000
      Loading Device Tree to 0000000057ff3000, end 0000000057fff603 ... OK

   Starting kernel ...

   [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x412fd050]
   [    0.000000] Linux version 5.10.131-cip13-yocto-standard (kuangwh@myzr-7a9b) (aarch64-poky-linux-gcc (GCC) 8.3.0, GNU ld (GNU Binutils) 2.31.1) #1 SMP PREEMPT Tue Feb 7 11:45:39 CST 2023
   [    0.000000] Machine model: Renesas MYZR EK200 based on r9a07g044l2
   ......

   Welcome to Poky (Yocto Project Reference Distro) 3.1.17 (dunfell)!

   [    4.514423] systemd[1]: Set hostname to <myzr-rzg2l>.
   。。。
   Poky (Yocto Project Reference Distro) 3.1.17 myzr-rzg2l ttySC0

   BSP: RZG2L/MYZR-RZG2L-EK200/3.0.1
   LSI: RZG2L
   Version: 3.0.1
   myzr-rzg2l login: 

**U-Boot 信息**

|  “U-Boot 2021.10 (Feb 07 2023 - 11:36:41 +0800)”：为UBOOT的版本号和编译时间
|  “CPU: STM32MP157AAC Rev.Z”：为CPU信息
|  “Model: myzr-rzg2l”：为我们开发板的软件名称。
|  “DRAM: 1.9 GiB”：表示使用的是1.9 G的DDR
|  “Hit any key to stop autoboot: 0”：为uboot倒数时间，在倒数时间结束内按下回车键可进行uboot命令行模式

**内核信息**

|  启动信息中“Linux version 5.10.131-cip13-yocto-standard (kuangwh@myzr-7a9b) (aarch64-poky-linux-gcc (GCC) 8.3.0, GNU ld (GNU Binutils) 2.31.1) #1 SMP PREEMPT Tue Feb 7 11:45:39 CST 2023”包含以下信息：
|  【内核版本】：5.10.131；
|  【主机名称】：(kuangwh@myzr-7a9b)
|  【编译器版本】：gcc version 8.3.0
|  【内核文件的编译时间】：Tue Feb 7 11:45:39 CST 2023。

**文件系统信息**

|  “Welcome to Poky (Yocto Project Reference Distro) 3.1.17 (dunfell)!”：表示从这里开始进入到文件系统
|  【ttySC0】表示文件系统的debug串口设备；
|  【myzr-rzg2l login:】登录信息，输入root即可登录成功。