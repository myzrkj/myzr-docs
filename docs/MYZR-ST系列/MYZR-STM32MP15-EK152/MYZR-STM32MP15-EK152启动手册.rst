
MYZR-STM32MP15-EK152启动手册
=============================

MYZR-STM32MP15-EK152 包装清单
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

标准件
""""""""

|  【底板】：MYZR-STM32-MB152，1片
|  【核心板】：MYZR-STM32-CB152，1片（已贴在底板上）
|  【电源适配器】：5V，1个
|  【DEBUG串口接头】：1个
|  【Micro USB线】：1条

用户自备件
""""""""""""

|  【网线】：1条
|  【USB 转串口线】：1条，调试时使用（如电脑没有DB9串口的情况下需要自备）

其它选配件
""""""""""""

|  【显示屏电路板】
|  【液晶显示屏】
|  【触摸屏】

MYZR-STM32MP15-EK152 主要接口
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/1425px-MYZR-STM32MP15-EK152-Front.png
   :alt: 1425px-MYZR-STM32MP15-EK152-Front.png
   
开发板连接
~~~~~~~~~~~

电源连接
""""""""""

|  开发板没有电源开关，所以在连接电源线时需确保使用正确的电源适配器，电源线连接到 **DC：5v-3A** 的接口上。

串口线的连接
""""""""""""""

|  Debug串口接头连上 **Debug_232** 接口上，然后使用USB转串口线连接电脑串口和Debug串口接头。
|  参考 :doc:`《终端软件参考手册》 </docs/COMMON/Xshell.RM.参考手册>` 新建串口会话并打开会话。

网线的连接
""""""""""""

|  网线一端接 **ETH10/100/1000M** ，另一段接电脑网口。

USB下载线的连接
""""""""""""""""

|  把Micro USB线的一端连接到开发板的 **BootLoader** 口，另一端连接到电脑的后置USB口。

启动开发板
~~~~~~~~~~~

检查开发板拨码开关
""""""""""""""""""

|  把开发板的拨码开发板 **SW：BOOT** 拨到正常的启动模式，拨码的模式如下：
|  【EMMC启动】：1（off），2（on），3（off），4（off）
|  【TF卡启动】：1（on），2（off），3（on），4（off）
|  【下载模式】：1（off），2（off），3（off），4（off）
|  注：拨码开关的ON是字母那一边，OFF是数字的那一边。

检查开发板的启动介质拨码
""""""""""""""""""""""""

|  根据自己的开发板选择对应的启动介质。
|  【eMMC 启动】：1（ON），2（ON），3（ON），4（OFF）
|  【Nand 启动】：1（OFF），2（OFF），3（OFF），4（ON）

为开发板上电
""""""""""""""

|  直接接上电源适配器给开发板上电。

开发板的启动信息解读
~~~~~~~~~~~~~~~~~~~~

|  开发板通电后在串口终端软件上可以看到开发板输出的启动信息。

.. code-block:: shell
   
   NOTICE:  CPU: STM32MP157AAC Rev.Z
   NOTICE:  Model: MYZR STM32MP15 Discovery Board
   INFO:    Reset reason (0x10):
   INFO:      Reset due to a failure of VDD_CORE
   INFO:    PMIC version = 0x10
   INFO:    Using EMMC
   INFO:      Instance 2
   INFO:    Boot used partition fsbl1
   NOTICE:  BL2: v2.2-r1.0(debug):2e4f8b4-dirty
   NOTICE:  BL2: Built : 06:17:37, Apr  7 2021
   INFO:    Using crypto library 'stm32_crypto_lib'
   INFO:    BL2: Doing platform setup
   INFO:    RAM: DDR3-DDR3L 16bits 533000Khz
   INFO:    Memory size = 0x10000000 (256 MB)
   ...
   NOTICE:  SP_MIN: Built : 06:17:46, Apr  7 2021

   ......

   U-Boot 2020.01-stm32mp-r1 (Apr 07 2021 - 19:15:56 +0800)

   CPU: STM32MP157AAC Rev.Z
   Model: MYZR STM32MP15 Discovery Board
   Board: stm32mp1 in trusted mode (myzr,myzr-stm32mp15)
   DRAM:  256 MiB
   Clocks:
   - MPU : 650 MHz
   - MCU : 208.878 MHz
   - AXI : 266.500 MHz
   - PER : 24 MHz
   - DDR : 533 MHz

   ......

   Starting kernel ...

   [    0.000000] Booting Linux on physical CPU 0x0
   [    0.000000] Linux version 5.4.31 (myzr@u14045) (gcc version 9.3.0 (GCC)) #20 SMP PREEMPT Tue Apr 6 19:11:34 CST 2021
   [    0.000000] CPU: ARMv7 Processor [410fc075] revision 5 (ARMv7), cr=10c5387d
   ......

   ST OpenSTLinux - Weston - (A Yocto Project Based Distro) 3.1-openstlinux-5.4-dunfell-mp1-20-06-24 stm32mp1 ttySTM0

   stm32mp1 login: root (automatic login)

TF-A 信息
""""""""""

.. code-block:: shell

   "NOTICE: CPU: STM32MP157AAC Rev.Z"：表示使用的CPU型号为STM32MP157AAC，版本为Z。对于153和151的CPU则为"CPU: STM32MP153AAC Rev.Z"，"CPU: STM32MP151AAC Rev.Z"。
   "NOTICE: Model: MYZR STM32MP15 Discovery Board"为我们开发板的软件名称。
   "Reset reason (0x10)"：表示开发板复位的原因。
   "Using EMMC"：表示使用emmc启动，使用TF启动则是"Using SDMMC"。
   "INFO: RAM: DDR3-DDR3L 16bits 533000Khz"，"INFO: Memory size = 0x10000000 (256 MB)"表示DDR的信息。
   "SP_MIN: Built : 06:17:46, Apr 7 2021"：表示TF-A镜像编译时间，调试时可根据此来判断是否更新成功。

U-Boot 信息
""""""""""""

.. code-block:: shell

   "U-Boot 2020.01-stm32mp-r1 (Apr 07 2021 - 19:15:56 +0800)"：为UBOOT的版本号和编译时间
   "CPU: STM32MP157AAC Rev.Z"：为CPU信息
   "Model: MYZR STM32MP15 Discovery Board"：为我们开发板的软件名称
   "DRAM:256 MiB"：表示使用的是256m的DDR
   "Clocks"：是各种时钟的配置

内核信息
""""""""""

.. code-block:: shell

   启动信息中"Linux version 5.4.31 (myzr@u14045) (gcc version 9.3.0 (GCC)) #20 SMP PREEMPT Tue Apr 6 19:11:34 CST 2021"包含以下信息：
   【内核版本】：Linux-5.4.31；
   【主机名称】：(myzr@u14045)
   【编译器版本】：gcc version 9.3.0
   【内核文件的编译时间】：Tue Apr 6 19:11:34 CST 2021。

文件系统信息
""""""""""""""

.. code-block:: shell

   启动信息中两行"ST OpenSTLinux - Weston - (A Yocto Project Based Distro) 3.1-openstlinux-5.4-dunfell-mp1-20-06-24 stm32mp1 ttySTM0"包含以下信息：
   【ST OpenSTLinux - Weston】表示文件系统的基础包；
   【20-06-24】表示文件系统的编译时间；
   【ttySTM0】表示文件系统的debug串口设备；
   【automatic login】表示此系统自动登录；
