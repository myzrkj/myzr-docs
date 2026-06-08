
MYZR-IMX6-EK200 L3035测试手册
===============================

测试前的准备
------------

1. 请按照《Linux快速启动手册》中的“Linux快速启动” -> “连接设备”进行连接。
2. 请按照《Linux快速启动手册》中的“Linux快速启动” -> “启动设备”进行启动。

测试项目
---------

网口测试
~~~~~~~~~~

|  MYZR-I.MX6 评估板支持双网口（2个百兆网口）。

**测试说明**

- 第1个以太网口位置底板正面“P4”，第2个以太网口位置底板正面“P5”。
- 系统启动后默认开启第1个以太网口，并且默认IP为192.168.3.104。

**测试方法**

1.  测试第1个以太网口

- 连接网线：用网络连接评估板“P4”与计算机网口
- 设置计算机IP：设置计算机网口IP为192.168.3.9

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.1.2.1.png
   :alt: MY-IMX6-EK200_L3035_2.1.2.1.png

- 为 eth0 配置IP：$ ifconfig eth0 192.168.3.104
- 执行测试命令：$ ping -I eth0 192.168.3.9 -c 2 -w 4
- 观察测试结果：系统会输出类似如下信息：

.. code-block:: shell

   --- 192.168.3.9 ping statistics ---
   2packets transmitted, 2 packets received, 0% packet loss

- 测试结果：“0% packet loss”表示测试通过

2.  测试第2个以太网口

- 连接网线：拔下第1个网口的网线接口插入到评估板“P5”，网线另一端保持与计算机网口相连。
- 设置计算机IP：设置计算机网口IP为192.168.3.9（如已经设置过可执行下一步骤）。
- 设置第2个网口IP：$ ifconfig eth1 192.168.3.18，设置后系统会输出第2个网口的工作状态信息，类似如下：

.. code-block:: shell

   smsc95xx 2-1.1:1.0: eth1: link up, 100Mbps, full-duplex, lpa 0xCDE1

- 执行测试命令：

.. code-block:: shell

   $ ping -I eth1 192.168.3.9 -c 2 -w 4

- 观察测试结果：系统会输出类似如下信息：

.. code-block:: shell

   --- 192.168.3.9 ping statistics ---
   2packets transmitted, 2 packets received, 0% packet loss

- 测试结果：“0% packet loss”表示测试通过

**附图**

|  说明：

 | 第1个红框为网口1的测试命令
 | 第2个红框为网口1的测试结果
 | 第3个红框为网口2的IP配置
 | 第4个红框为网口2的状态信息
 | 第5个红框为网口2的测试命令

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.1.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.1.3.1.png

USB测试
~~~~~~~~~

**测试说明**

|  MYZR-I.MX6 V2.5 评估板有2个USB HOST接口，位于底板正面“J8”。

**测试方法**

1.  开始测试

|  将USB设备插入底板USB接口，系统会输出类似如下信息：

.. code-block:: shell

   usb *-*.*: new high speed USB device number * using fsl-ehci
   ……

2.  测试结束

|  将USB设备从底板拔出，系统会输出类似如下信息：

.. code-block:: shell

   usb *-*.*: USB disconnect, device number *

**附图**

|  说明：

 | 图片上第1个红框为插入U盘时系统输出的信息；
 | 图片上第2个红框为拔出U盘时系统输出的信息；
 | 图片上第3个红框为插入USB鼠标时系统输出的信息；
 | 图片上第4个红框为拔出USB鼠标时系统输出的信息。

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.2.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.2.3.1.png

SD卡接口测试
~~~~~~~~~~~~~

**测试说明**

|  SD卡接口位于底板背面“J25”。

**开始测试**

1.  往SD卡槽插入设备

|  插入SD卡到底板SD卡接口。系统输出以下信息（见附图）即表示SD接口正常：

.. code-block:: shell

   mmc*: new high speed SD card at address ****
   mmcblk*: mmcx:xxxx SA**G *.**GiB
   mmcblk*: p*

2. 从SD卡槽弹出设备

|  再次住SD卡槽按下SD卡，底板会弹出SD卡。系统输出以下信息（见附图）表示SD卡接口弹出正常：

.. code-block:: shell

   mmc*: card **** removed

3.  结束测试

|  SD卡弹出后拨出SD卡即结束测试。

**附图**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.3.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.3.3.1.png

音视频测试
~~~~~~~~~~~

**测试说明**

|  这项测试是通过播放有声视频验证评估板的音频功能和视频功能。

**测试方法**

1. 准备测试

|  连接音频输出设备到底板正面的音频座子，音频座子在底板正面“J20”，丝印名称是“HP”。

2. 执行测试

|  使用gplay播放一个视频，示例命令如下：

.. code-block:: shell

   $ gplay /app_test/arm.flv

|  上面这条命令会使用gplay播放命令中指定的文件。

3. 测试结果

|  执行上面的测试命令后会在评估板显示屏上看到播放的视频，听到音频设备输出的声音。

**附图**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.4.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.4.3.1.png

LED（GPIO）测试
~~~~~~~~~~~~~~~~

**测试说明**

|  LED（GPIO）测试使用的CPU的管脚为“NANDF_CS0”，连接到底板上的“J4的4号管脚”，运行测试程序后GPIO会被测试程序控制输出高低电平。高低电平变化间隔为1秒。
|  提示：LED（GPIO）测试需要使用到万用表，没有万用表的用户可以使用跳过进行下一项测试。

**测试方法**

1. 执行测试程序

|  在终端下键入命令执行测试程序，示例如下：

.. code-block:: shell
   
   $ /app_test/led

|  这时测试程序会控制GPIO输出高低电平，并且输出类似以下信息

.. code-block:: shell

   Write=0
   Write=1
   ……

2. 检测测试结果

|  把万用表的地连接到开发板的地，万用表的另一条线连接到J4的4号管脚，会看到万用表的电压跳变。

3. 结束测试

|  按计算机上的“Ctrl”+“C”可结束按键测试程序。

**附图**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.3.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.3.3.1.png

按键测试
~~~~~~~~~

**测试说明**

|  MYZR-I.MX6底板有4个按键，其中3个为自定义功能按键（SW2：WAKE UP，SW3:V+，SW4:V-），以及1个复位按键（SW1：nRE）。测试程序key_test可以对3个功能按键进行测试。

**测试方法**

1. 执行测试程序

|  在终端下键入命令执行测试程序，示例如下：

.. code-block:: shell

   $ /app_test/key_test

2. 进行交互测试

|  分别按SW4、SW3、SW2，系统会输出相应的事件信息，如：

.. code-block:: shell

   key*** Pressed
   key*** Released

|  其中“key*** Pressed”信息是在按键被按下的时候被输出，“key*** Released”信息是在按键被松开的时候被输出。

3. 结束测试

|  按计算机上的“Ctrl”+“C”可结束按键测试程序。
|  注：按下SW1（系统会复位重启）。

**附图**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.6.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.6.3.1.png

串口测试
~~~~~~~~~

|  MYZR-I.MX6评估板有5个串口，其中4个为用户串口（位于底板正面“J1”位置，丝印名称为“TTL_UART”），1个为调试串口（位于底板正面“P2”位置）。

**测试说明**

|  系统设备文件说明：

- 调试串口的在系统中的设备文件是ttymxc0，用户串口的设备文件是ttymxc1、ttymxc2、ttymxc3、ttymxc4。

|  串口收发管脚及对应的设备文件说明：
|  UART2：发送 7，接收 9，ttymxc1。
|  UART3：发送 11，接收 13，ttymxc2。
|  UART4：发送 17，接收 15，ttymxc3。
|  UART5：发送 18，接收 16，ttymxc4。
|  提示：这里列出串口的收发管脚，串口所有管脚的定义请看原理图。

**测试方法**

|  采用串口自发自收的方式进行。
|  提示：这里以串口5为例，其它3个用户串口参照串口的测试方法进行测试

1. 准备测试

|  短接串口5的发送发接收管脚（J1的16和18号）。

2. 执行测试

.. code-block:: shell

   $ ~/my-demo/linux-3.0.35/uart_test.out /dev/ttymxc4 "www.myzr.com.cn"

3. 测试结果

|  如果串口正常，终端上会显示类似如下的信息：

.. code-block:: shell

   Read Test Data finished,Read Test Data is-------www.myzr.com.cn

**附图**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.7.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.7.3.1.png

RTC测试
~~~~~~~~

**测试说明**

|  受快递运输影响，MYZR-I.MX6 评估板发货时不带电池。测试RTC前请自备纽扣电池并安装到底板背面“BT1”上（在丝印“RTC”旁边）。

**测试方法**

1. 断电重启设备，查看当前系统时间和硬件时间。

|  查看当前系统时钟命令如下：

.. code-block:: shell

   $ date

|  系统输出信息如下：

.. code-block:: shell

   Thu Jan 1 00:00:59 UTC 1970

|  查看当前RTC芯片时钟命令如下：

.. code-block:: shell

   $ hwclock

|  系统输出信息如下：

.. code-block:: shell

   Tue Nov 30 00:00:00 1999 0.000000 seconds

2. 设置系统时钟，并同步到RTC芯片

|  设置系统时钟命令参考如下：

.. code-block:: shell

   $ date -s "2015-04-27 12:34:56"

|  将系统时钟写入硬件时钟命令如下：

.. code-block:: shell

   $ hwclock -w

3. 断电重启评估板，查看当前系统时钟和硬件时钟

|  请参考第1步

4. 测试结果

|  执行第3步以后看到的时钟为新设定的时钟。

**附图**

|  下图为测试方法中步骤1和2的截图

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.8.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.8.3.1.png

|  下图为测试方法中步骤3的截图

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.8.3.2.png
   :alt: MY-IMX6-EK200_L3035_2.8.3.2.png

WatchDog测试
~~~~~~~~~~~~~

**测试说明**

|  WatchDog测试包括2项：一项是复位测试，一项是喂狗测试。

**复位测试**

1. 测试说明

|  复位测试将启动WatchDog，但是并不喂狗，60秒后系统将会复位。

2. 执行测试

|  运行/app_test/watdogrestart，示例命令如下：

.. code-block:: shell

   $ /app_test/watdogrestart

3. 测试结果

|  运行测试命令后等待60秒后，WatchDog超时，系统被复位。将会在终端看到系统重新启动输出的信息。

**喂狗测试**

1. 测试说明

|  喂狗测试将启动WatchDog，并且每1秒钟进行1次喂狗，系统将不会因为WatchDog超时而复位。

2. 执行测试

|  运行/app_test/watdogtest &，示例命令如下：

.. code-block:: shell

   $ /app_test/watdogtest &

3. 测试结果

|  运行测试命令后，系统依然正常工作，并不会因为WatchDog超时而复位。

4. 附图

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.9.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.9.3.1.png

SPI测试
~~~~~~~~~

|  MYZR-I.MX6 V2.5底板上有一组SPI接口，在“J7”位置，丝印为“SPI”。

**测试说明**

|  测试需要用到SPI接口的MISO和MOSI管脚。SPI接口的 MISO管脚在底板“J7的8号”，MOSI管脚为“J7的10号”。

**测试方法**

|  采用SPI自发送（输出）自接收（输入）的方式。

1. 准备测试

|  短接SPI的MISO和MISO管脚，即短接底板上J7的8号和10号管脚。

2. 执行测试

.. code-block:: shell

   $ ~/my-demo/linux-3.0.35/spidev_test.out -D /dev/spidev1.0

3. 测试结果

|  如果SPI正常，在终端上会看到如下字符：

.. code-block:: shell

   FF FF FF FF FF FF
   40 00 00 00 00 95
   FF FF FF FF FF FF
   FF FF FF FF FF FF
   FF FF FF FF FF FF
   DE AD BE EF BA AD
   F0 0D

**附图**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.10.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.10.3.1.png

CAN接口测试
~~~~~~~~~~~~

**测试说明**

|  CAN测试需要用到示波器，没有示波器的客户请跳过CAN测试。

**测试方法**

1. 配置CAN0

|  示例命令如下：

.. code-block:: shell

   $ ip link set can0 up type can bitrate 250000

2. 配置连接示波器

|  将示波器的CH1和CH2连接到评估板的“R83”（在底板正面最上面的绿色座子）。
|  配置示波器（不会使用示波器的客户请找硬件工程师协助）。

3. 执行测试命令

.. code-block:: shell

   $ /app_test/client_test

|  4. 测试结果

|  执行测试命令的同时会在示波器上看到波形的变化。

**附图**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.11.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.11.3.1.png

PCIE接口测试
~~~~~~~~~~~~~

**测试说明**

|  系统已添加PCI接口的驱动，在启动过程中系统会检测PCI-E接口上的设备。

**测试方法**

|  复位系统，观察系统启动输出的信息

1. PCI-E驱动程序输出信息

|  在系统启动过程中输出如下信息表示PCI-E接口驱动加载没有问题：

.. code-block:: shell

   iMX6 PCIe PCIe RC mode imx_pcie_pltfm_probe entering.
   PCIE: imx_pcie_pltfm_probe start link up.

2. 不连接PCI-E设备时的输出信息

|  在系统启动过程中，如果PCI-E接口上没有连接有效的设备，系统会提示PCI-E端口“link down!”，类似如下：

.. code-block:: shell

   link up failed, DB_R0:0x00361900, DB_R1:0x08200000!
   IMX PCIe port: link down!

3. 连接有效PCI-E设备时的输出信息（这里以Intel 4965AGN为例）

|  在系统启动过程中，如果PCI-E接口上检测到有效的设备，并且设备模块正常，系统会提示PCI-E端口“link up”，如下：

.. code-block:: shell

   IMX PCIe port: link up.

4. Linux测试命令：$ lspci

|  如果在PCI-E接口上插入了有效的PCI-E设备，使用lspci将会得到该模块相关的信息，类似如下（这里连接的是Intel 4965AGN）：

.. code-block:: shell

   00:00.0 Class 0604: 16c3:abcd
   01:00.0 Class 0280: 8086:4229

|  如果PCI-E接口上没有连接设备，使用lspci系统将没有信息输出。

**附图**

|  下图为未连接PCI-E设备时系统输出的信息

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.12.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.12.3.1.png

|  下图为连接Intel 4965AGN时系统输出的信息

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.12.3.2.png
   :alt: MY-IMX6-EK200_L3035_2.12.3.2.png

|  下图为连接Intel 4965AGN后，进入系统使用lspci得到的信息

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.12.3.3.png
   :alt: MY-IMX6-EK200_L3035_2.12.3.3.png

WIFI测试
~~~~~~~~~~

**测试说明**

|  MYZR-I.MX6 评估板使用的WIFI芯片型号为RTL8188EUS。

**测试方法(test method)**

1. 加载WIFI模块驱动

|  示例命令如下：

.. code-block:: shell

   $ insmod /lib/modules/wifi/wlan.ko

2. 生成WIFI的config文件

|  参考命令如下：

.. code-block:: shell

   $ wpa_passphrase MYZR_TP-LINK myzrd2302 > /etc/wpa_supplicant.conf

|  这条命令指定的WIFI名称是和密码是“MYZR_TP-LINK myzrd2302”，需要替换成自己可连接的WIFI名称和密码。

3. 连接WIFI网络

|  示例命令如下：

.. code-block:: shell

   $ wpa_supplicant -B –c /etc/wpa_supplicant.conf -iwlan0

4. 自动获取IP

|  示例命令如下：

.. code-block:: shell

   $ udhcpc -i wlan0

|  注意：这里需要确认所在的WIFI网络已启用DHCP功能。

5. 测试WIFI网络连接

|  示例命令如下：

.. code-block:: shell

   $ ping -I wlan0 www.baidu.com -c 2

6. 测试结果

|  执行步骤5能ping通则表示WIFI模块工作正常。

**附图**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.13.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.13.3.1.png

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.13.3.2.png
   :alt: MY-IMX6-EK200_L3035_2.13.3.2.png

IPU测试
~~~~~~~~

**测试说明**

|  整个IPU测试过程完成需要十几分钟。

**测试方法**

1. 执行测试

|  进入测试程序所在目录（一定要进入测试程序所在目录才能正常执行测试脚本）

.. code-block:: shell

   $ cd /unit_tests/

|  执行测试脚本

.. code-block:: shell

   $ ./autorun-ipu.sh

2. 测试结果

|  在整个测试过程中，可以看到显示屏显示的内容在不停的变化。
|  测试完成后，在终端上可以看到类似如下信息：

.. code-block:: shell

   test stop at Thu Jan 1 00:33:38 UTC 1970

**附图**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.14.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.14.3.1.png

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.14.3.2.png
   :alt: MY-IMX6-EK200_L3035_2.14.3.2.png

GPU测试
~~~~~~~~

**测试说明**

|  测试具体内容请跟踪 /unit_tests/gpu.sh 文件。

**测试方法**

1. 执行测试

|  进入测试程序所在目录（一定要进入测试程序所在目录才能正常执行测试脚本）

.. code-block:: shell

   $ cd /unit_tests/

|  执行测试脚本

.. code-block:: shell

   $ ./gpu.sh

2. 测试过程

|  在整个测试过程中，可以看到显示屏显示的内容在不停的变化。

3. 退出测试

|  终端输出“press ESC to escape...”，按ESC可退出测试。

**附图**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.15.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.15.3.1.png

VPU测试
~~~~~~~~~

**测试说明**

|  测试过程将使用VPU解码视频文件并输出到显示设备。

**测试方法(test method)**

1. 执行测试

|  进入测试程序所在目录（一定要进入测试程序所在目录才能正常执行测试脚本）

.. code-block:: shell

   $ cd /unit_tests/

|  执行测试脚本

.. code-block:: shell

   $ ./autorun-vpu.sh

2. 测试过程

|  在整个测试过程中，从显示屏上可以看到VPU解码的视频。

背光测试
~~~~~~~~~

**测试说明**

|  测试过程通过设置背光亮度值验证评估板的背光功能。

**测试方法(test method)**

1. 查看最大亮度

.. code-block:: shell

   $ cat /sys/class/backlight/pwm-backlight.0/max_brightness

2. 设置亮度

.. code-block:: shell

   $ echo 200 >/sys/class/backlight/pwm-backlight.0/brightness

|  在整个测试过程中，执行上面的测试命令后会看到显示屏的亮度发生变化。

usb识别为U盘测试
~~~~~~~~~~~~~~~~~

**测试说明**

|  通过mini usb线在PC识别开发板为U盘。

**测试方法(test method)**

1. 创建一个10M大小的文件

.. code-block:: shell

   $ dd if=/dev/zero of=/dev/shm/disk bs=1024 count=10240

2. 载入模块

.. code-block:: shell

   $ modprobe g_file_storage stall=0 file=/dev/shm/disk removable=1

3. 识别U盘

|  此时PC“我的电脑”会出现U盘的驱动器，将其格式化后，便可对其读写

4. 挂载

.. code-block:: shell

   $ mount /dev/shm/disk /mnt

|  在/mnt/下看到在电脑写入的文件，在开发板写入文件，重新插拔MINI USB可在PC看到在开发板写入的新文件。

usb识别为网口测试
~~~~~~~~~~~~~~~~~

**测试说明**

|  通过mini usb线将usb识别为网口。

**测试方法(test method)**

1. 载入模块

.. code-block:: shell

   $ modprobe g_ether

2. 设置IP

.. code-block:: shell

   $ ifconfig usb0 192.168.7.2

|  将PC识别的rndis的本地连接IP设置为192.168.7.8

3. 测试网口

.. code-block:: shell

   $ ping 192.168.7.8 -c 2 -w 4

|  “0% packet loss”表示测试通过

|  注：若WIN10识别rndis为COM口，则需要下载驱动kindle_rndis.inf_amd64-v1.0.0.1.zip 解压后，以管理员权限执行5-runasadmin_register-CA-cer.cmd，然后在COM口处双击，在计算机中查找解压的驱动程序，这样就会有rndis网络了。

CPU温度测试
~~~~~~~~~~~~

**测试说明**

|  查看CPU的温度

**测试方法(test method)**

1. 执行测试

.. code-block:: shell

   $ cat /sys/class/thermal/thermal_zone0/temp

2. 测试结果

.. code-block:: shell

   44

tftp更新镜像
~~~~~~~~~~~~~~

**测试说明**

|  可更新zImage、u-boot、u-boot环境变量。

**测试方法(test method)**

|  电脑端打开软件 tftpd 地址设置为需更换的文件所在的目录。
|  把开发板的这个网口用网线跟电脑网口连接起来。
|  进入u-boot命令行。

1. 加载环境变量

.. code-block:: shell

   run load_scr; source;

2. 设置IP

|  设置开发板IP：

.. code-block:: shell

   setenv ipaddr 192.168.137.9

|  设置电脑IP：

.. code-block:: shell

   setenv serverip 192.168.137.99

|  设置MAC地址：

.. code-block:: shell

   setenv ethaddr 00:00:00:00:00:03

|  测试网络：

.. code-block:: shell

   ping 192.168.137.99

|  测试结果：“host 192.168.137.99 is alive”表示测试通过

3. 烧写zImage

.. code-block:: shell

   run update_kern

4. 烧写u-boot环境变量

.. code-block:: shell

   run update_scr

5. 烧写u-boot

.. code-block:: shell

   run update_ubot

复制更新镜像
~~~~~~~~~~~~

**测试说明**

|  可更新zImage、u-boot环境变量、内核模块。

**测试方法(test method)**

1. 复制相应文件到开发板当前目录，以tftp为例

|  电脑端打开软件 tftpd 地址设置为需更换的文件所在的目录。
|  把开发板的这个网口用网线跟电脑网口连接起来。

2. 测试连接

.. code-block:: shell

   $ ping 192.168.137.99 -c 2 -w 4

|  测试结果：“0% packet loss”表示测试通过

3. 传输文件

.. code-block:: shell

   $ tftp -g 192.168.137.99 -r zImage-myimx6a9
   $ tftp -g 192.168.137.99 -r my_environment.scr
   $ tftp -g 192.168.137.99 -r kernel-modules-myimx6a9.tar.bz2

4. 查看fat分区地址

.. code-block:: shell

   $ fdisk -l

|  输出信息：

.. code-block:: shell

   ......
   Device Boot Start End Blocks Id System
   /dev/mmcblk0p1 321 16320 512000 c Win95 FAT32 (LBA)
   /dev/mmcblk0p2 19201 480896 14774272 83 Linux
   ......

5. 手动挂载

.. code-block:: shell

   $ mount /dev/mmcblk0p1 /mnt/

6. 复制相应的文件到/mnt目录，将原文件替换

.. code-block:: shell

   $ cp zImage-myimx6a9 /mnt
   $ cp my_environment.scr /mnt

7. 解压更新内核模块

.. code-block:: shell

   $ tar xjvf kernel-modules-myimx6a9.tar.bz2 -C /

8. 保存并重启

.. code-block:: shell

   $ reboot

显示功能测试
~~~~~~~~~~~~~

- 特别说明：

.. code-block:: shell

    当U-Boot 版本u-boot-2016.03 svn315及以上    
        内核 版本  linux-3.0.35  svn31及以上
                 linux-3.14.52 svn369及以上
                 linux-3.14.52 svn368及以上
        烧录工具   MfgTool-MYIMX6A9-L* svn181及以上

|  请参考《MY-IMX6-A9系列：显示功能测试》进行测试


- 一般情况下则按照如下方法测试

|  说明：每项显示功能测试都需要重启系统进入到u-boot命令行，输入命令并按确认键。
|  示例如下：

单屏显示
~~~~~~~~~

|  说明：输入命令并按确定键，观察系统启动过程中显示屏的显示内容，即可看到Linux Logo。

**LVDS1**

|  将显示屏排线插入LVDS1（位于底板正面“J22”位置，丝印名称为“LVDS1”），启动系统，进入u-boot命令行，输入下面命令并按确定键：

`setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm`

**LVDS0**

|  将显示屏排线插入LVDS0（位于底板正面“J24”位置，丝印名称为“LVDS0”）,运行系统进入u-boot命令行，输入下面命令并按确定键：

`setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666 ldb=sin0; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm`

**HDMI**

`setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=hdmi,1920x1080M@60,if=RGB24; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm`

|  提示：HDMI显示在启动过程中屏幕无Linux Logo显示。进入系统后可以使用gplay命令播放视频，可以看到视频转出在显示屏上。
|  视频播放命令示例如下：

.. code-block:: shell

   $ gplay /unit_tests/akiyo.mp4

**RGB**

|  进入u-boot命令行，输入下面命令并按确定键：

`setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=lcd,SEIKO-WVGA,if=RGB24; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm`

双屏同步骤显示(dual screens synchronous display)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  说明：输入命令并按确定键，在内核启动过程中可以看到两个屏幕都显示Linux Logo，并且其它对显示屏的操作也会同样显示在两个屏幕上。

LVDS1+LVDS0同步显示(LVDS1+LVDS0 synchronous display)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666 ldb=dul0 video=mxcfb1:dev=ldb,LDB-1024X600,if=RGB666; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm`

双屏异步显示
~~~~~~~~~~~~~

**会用到的测试命令**

- 打开主显示屏的背光

.. code-block:: shell

   $ echo 0 > /sys/class/graphics/fb0/blank

- 打开第2显示屏的背光

.. code-block:: shell

   $ echo 0 > /sys/class/graphics/fb2/blank

- 播放指定的视频文件到视频设备（这里video17关联到主显示屏）

.. code-block:: shell

   $ gst-launch playbin2 uri=file:///unit_tests/akiyo.mp4 video-sink="mfw_v4lsink device=/dev/video17"

- 播放指定的视频文件到视频设备（这里video18关联到第2显示屏）

.. code-block:: shell

   $ gst-launch playbin2 uri=file:///unit_tests/akiyo.mp4 video-sink="mfw_v4lsink device=/dev/video18"

**测试方法说明**

1. 进入u-boot命令行输入命令并按确认键待系统启动完成。

|  示例如下：

2. 执行命令打开对应显示屏的背光。

|  示例如下：

3. 执行视频播放命令播放视频到显示屏。

|  示例如下：
|  说明：双屏异步显示模式下，系统启动后第2显示屏的背光默认是关闭的，所以需要执行步骤2）。

**LVDS1作为主屏**

- LVDS1+LVDS0双屏异步显示

`setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666 video=mxcfb1:dev=ldb,LDB-1024X600,if=RGB666; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm`

- LVDS1+RGB双屏异步显示

`setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666 video=mxcfb1:dev=lcd, SEIKO-WVGA,if=RGB24; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm`

- LVDS1+HDMI双屏异步显示

`setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666 video=mxcfb1:dev=hdmi,1920x1080M@60,if=RGB24; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm`

**LVDS0作为主屏**

- LVDS0+LVDS1双屏异步显示：

`setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666 ldb=sep0 video=mxcfb1:dev=ldb,LDB-1024X600,if=RGB666; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm`

- LVDS0+RGB双屏异步显示

`setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666 ldb=sin0 video=mxcfb1:dev=lcd,SEIKO-WVGA,if=RGB24; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm`

- LVDS0+HDMI双屏异步显示

`setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666 ldb=sin0 video=mxcfb1:dev=hdmi,1920x1080M@60,if=RGB24; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm`

**RGB作为主屏**

- RGB+LVDS1双屏异步显示：

`setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=lcd,SEIKO-WVGA,if=RGB24 video=mxcfb1:dev=ldb,LDB-1024X600,if=RGB666; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm`

- RGB+LVDS0双屏异步显示：

`setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=lcd,SEIKO-WVGA,if=RGB24 video=mxcfb1:dev=ldb,LDB-1024X600,if=RGB666 ldb=sin0; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm`

**HDMI作为主屏**

- HDMI+LVDS1双屏异步显示

`setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=hdmi,1920x1080M@60,if=RGB24 video=mxcfb1:dev=ldb,LDB-1024X600,if=RGB666; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm`

- HDMI+LVDS0双屏异步显示

`setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=hdmi,1920x1080M@60,if=RGB24 video=mxcfb1:dev=ldb,LDB-1024X600,if=RGB666 ldb=sin0; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm`

OV5642摄像头 测试
~~~~~~~~~~~~~~~~~~

1. 开发板断电，在"CAMARE"接上OV5642摄像头，接上摄像头后启动评估板。
2. 使用指令进行测试:

`/unit_tests/mxc_v4l2_overlay.out -iw 640 -ih 480 -it 0 -il 0 -ow 640 -oh 480 -ot 20 -ol 20 -r 0 -t 50 -do 0 -fg -fr 30`

4路视频采集模块（选配）测试
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. 开发板断电，接上tw6865四路摄像头模块，接上摄像头后启动评估板。
2. 使用指令进行测试

.. code-block:: shell

   EXEC_FILE=/my-demo/linux-3.0.35/MY_TW6865_DEMO_L3035_MYIMX6A9.out
   ${EXEC_FILE} -x 2 -ot 0 -ol 0 -ow 512 -oh 300 -m 2 &
   ${EXEC_FILE} -x 3 -ot 0 -ol 512 -ow 512 -oh 300 -m 2 &
   ${EXEC_FILE} -x 4 -ot 300 -ol 0 -ow 512 -oh 300 -m 2 &
   ${EXEC_FILE} -x 5 -ot 300 -ol 512 -ow 512 -oh 300 -m 2 &

关于环境变量的说明
------------------

MYZR-IMX6系列开发板环境变量的特点
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  MYZR-IMX6 系列开发板的环境变量具有以下特点：

1. 从引导内核的介质来区说，有：eMMC、网络（tftp）。
2. 从引导文件系统的介质来说，有：eMMC、网络（NFS）。
3. 从显示设备的配置来说，有 LVDS0、LVDS1、HDMI、RGB，以及双屏不同的组合。

|  这时候，如果环境变量把上面三种都组合，会有不少于60条的 bootcmd 环境变量，所以我们对环境变量进行了抽象分离及重组。
|  再由于 bootargs 环境变量里包括 console、video、ip、root 等其它参数，所以每一种 bootcmd 对 bootargs 有很强的依赖性，以及不同的 bootcmd 之间的差别较大。无疑，bootargs 是不能通用的。

bootcmd_xxx 环境变量的流程
~~~~~~~~~~~~~~~~~~~~~~~~~~

|  我们对 bootcmd 及 bootargs 按引导设备进行了抽象，抽象后 bootcmd_xxx 的流程是这样的：

1. 通过 bootargs_base 重设 bootargs，这样确保 bootargs 中不存在冲突；
2. 通过 bootargs_xxx 在 bootargs 后面添加与引导设备对应的参数；

|  再就 bootcmd_xxx 中“;”之后的内容就是大家很容易理解的了。

环境变量的正确设置方法
~~~~~~~~~~~~~~~~~~~~~~

|  关于对环境变量正确设置的方法：
|  首先需要注意的是，正常情况下直接对 bootargs 设置是会无效的，因为 bootargs_base 会重设 bootargs。
|  需要把 bootargs 的设置写到 bootargs_base 的命令当中。
|  bootargs_base 所包含的内容应当只是 console 和 video，再其它的参数应当写到 bootargs_mmc 或 bootcmd_tftp 或 bootargs_nfs 中。

环境变量的正确设置方法举例
~~~~~~~~~~~~~~~~~~~~~~~~~~

|  如需要设置“HDMI+LVDS1双屏异步显示”并保存环境变量，则：

1. `setenv bootargs_base 'setenv bootargs console=ttymxc0,115200 video=mxcfb0:dev=hdmi,1920x1080M@60,if=RGB24 video=mxcfb1:dev=ldb,LDB-1024X600,if=RGB666'`
2. `saveenv`

|  上面两条命令即可。

