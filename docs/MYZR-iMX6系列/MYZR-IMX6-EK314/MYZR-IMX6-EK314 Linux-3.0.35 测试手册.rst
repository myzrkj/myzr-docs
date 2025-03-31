
Linux-3.0.35 测试手册
=======================

测试前的准备
------------

|   1）请按照《MYZR-IMX6-EK314启动手册》中的“评估板与计算机的连接”进行连接。
|   2）请按照《MYZR-IMX6-EK314启动手册》中的“评估板的启动”进行启动。

测试项目
---------

网口测试
~~~~~~~~~

|   MYZR-IMX6-EK314 评估板支持双网口（1个百兆网口，1个千兆网口）。

**测试说明**

- 第1个以太网口位置底板正面“U12”，第2个以太网口位置底板正面“P1”。

**测试方法**

|   1） 测试第1个以太网口

- 连接网线：用网络连接评估板“U12”与计算机网口
- 设置计算机IP：设置计算机网口IP为192.168.18.18

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY-IMX6-EK314_L3035_2.1.2.1.png
   :alt: MY-IMX6-EK314_L3035_2.1.2.1.png

- 设置评估板IP：

.. code-block:: shell

    $ ifconfig eth0 192.168.18.36　　　　 　 ＃ configure the eth0

- 执行测试命令：

.. code-block:: shell

    $ ifconfig eth1 down 　　　　 　 ＃ eth1 to be shut down
    $ ping 192.168.18.18 -c 2 -w 4 　　　　 　＃ send ICMP to HOST

- 观察测试结果：系统会输出类似如下信息：

.. code-block:: shell

    --- 192.168.18.18 ping statistics ---
    2packets transmitted, 2 packets received, 0% packet loss

- 测试结果：“0% packet loss”表示测试通过
- 附图

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY-IMX6-EK314_L3035_2.1.2.2.png
   :alt: MY-IMX6-EK314_L3035_2.1.2.2.png

|   2） 测试第2个以太网口

- 连接网线：拔下第1个网口的网线接口插入到评估板“P1”，网线另一端保持与计算机网口相连。
- 设置计算机IP：设置计算机网口IP为192.168.18.18（如已经设置过可执行下一步骤）。
- 设置第2个网口IP：

.. code-block:: shell

    $ ifconfig eth1 192.168.18.27 　　　　 　＃ configure the eth1

|   设置后系统会输出第2个网口的工作状态信息，类似如下：

.. code-block:: shell

    smsc95xx 1-1.1:1.0 eth1: link up, 100Mbps, full-duplex, lpa 0x4DE1

|   执行测试命令：

.. code-block:: shell

    $ ifconfig eth0 down 　　　　 　＃ eth0 to be shut down
    $ ping 192.168.18.18 -c 2 -w 4 　　　　　＃ send ICMP to HOST

- 观察测试结果：系统会输出类似如下信息：

.. code-block:: shell

    --- 192.168.18.18 ping statistics ---

    2packets transmitted, 2 packets received, 0% packet loss

- 测试结果：“0% packet loss”表示测试通过
- 附图

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY-IMX6-EK314_L3035_2.1.2.3.png
   :alt: MY-IMX6-EK314_L3035_2.1.2.3.png

USB测试
~~~~~~~~

**测试说明**

|   MYZR-IMX6-EK314评估板有2个USB HOST接口，位于底板正面“J2”。

**测试方法**

|   1） 开始测试
|   将USB设备插入底板USB接口，系统会输出类似如下信息：

.. code-block:: shell

    usb *-*.*: new high speed USB device number * using fsl-ehci
    ……

|   2） 测试结束
|   将USB设备从底板拔出，系统会输出类似如下信息：

.. code-block:: shell

    usb *-*.*: USB disconnect, device number *

**附图**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY-IMX6-EK314_L3035_2.2.3.1.png
   :alt: MY-IMX6-EK314_L3035_2.2.3.1.png

SD卡接口测试
~~~~~~~~~~~~~

**测试说明**

|   SD卡接口位于底板背面“SD3”。

**开始测试**

|   1） 往SD卡槽插入设备
|   插入SD卡到底板SD卡接口。系统输出以下信息（见附图）即表示SD接口正常：

.. code-block:: shell

    mmc*: new high speed SD card at address ****
    mmcblk*: mmcx:xxxx SA**G *.**GiB
    　mmcblk*: p*
    
|   2）从SD卡槽弹出设备
|   再次住SD卡槽按下SD卡，底板会弹出SD卡。系统输出以下信息（见附图）表示SD卡接口弹出正常：

.. code-block:: shell

    mmc*: card **** removed

|   3） 结束测试
|   SD卡弹出后拨出SD卡即结束测试。

**附图**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY-IMX6-EK314_L3035_2.3.3.1.png
   :alt: MY-IMX6-EK314_L3035_2.3.3.1.png

音频测试
~~~~~~~~~

**测试说明**

|   这项测试是通过播放音频文件验证评估板的音频功能。

**测试方法**

|   1）准备测试
|   连接音频输出设备到底板正面的音频座子，音频座子在底板正面“J20”，丝印名称是“HP”。
|   2）执行测试
|   使用aplay播放一个视频，示例命令如下：

.. code-block:: shell

    ＃ aplay /unit_tests/audio8k16S.wav

|   上面这条命令会使用aplay播放命令中指定的文件。
|   3）测试结果
|   执行上面的测试命令后会听到音频设备输出的声音。

**附图**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY-IMX6-EK314_L3035_2.4.3.1.png
   :alt: MY-IMX6-EK314_L3035_2.4.3.1.png

视频测试
~~~~~~~~~

**测试说明**

|   这项测试是通过播放视频验证评估板的音频视频功能。

**测试方法**

|   使用gplay播放一个视频，示例命令如下：

.. code-block:: shell
    
    ＃ gplay /unit_tests/akiyo.mp4

|   上面这条命令会使用gplay播放命令中指定的文件。

- 测试结果

|   执行上面的测试命令后会在评估板显示屏上看到大约1秒钟的视频图像。

**附图**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY-IMX6-EK314_L3035_2.5.3.1.png
   :alt: MY-IMX6-EK314_L3035_2.5.3.1.png

GPIO测试
~~~~~~~~~

**测试说明**

|   在MYZR-IMX6-EK314底板正面的U14上，有33个GPIO，其中一个用作GPIO-LED。
|   GPIO-LED使用的CPU的管脚为“EIM_D22”，连接到底板上的“U14:30管脚”。
|   提示：GPIO-LED测试需要使用到万用表，没有万用表的用户可以使用跳过进行下一项测试。

GPIO-LED（GPIO）测试
~~~~~~~~~~~~~~~~~~~~~

|   GPIO的测试方法如下：

.. code-block:: shell

    $ echo 1 > /sys/class/leds/user_led/brightness

|   使用万用表测试U14:30引脚，可以看到该引脚是高电平。

.. code-block:: shell

    $ echo 0 > /sys/class/leds/user_led/brightness

|   使用万用表测试U14:30引脚，可以看到该引脚是低电平。

**通用GPIO测试**

|   这里我们以EIM_D21为例，通过原理图我们可以看到EIM_D21最终连接到U14:29。
|   1）计算GPIO的序号
|   根据芯片手册，我们可以找到EIM_D21 PAD可以配置为GPIO3_IO21。
|   IMX6 GPIO序号的计算方法为：（所在的组 - 1） * 32 + 序号，所以PIO3_IO21的管脚值为 （3 – 1） * 32 + 21 = 85。
|   2）设置需要测试的GPIO的IO Number

.. code-block:: shell

    $ IO_NUMBER=85

|   3）导出GPIO

.. code-block:: shell

    $ echo ${IO_NUMBER} > /sys/class/gpio/export

|   4）设置GPIO方向

.. code-block:: shell

    $ echo out > /sys/class/gpio/gpio${IO_NUMBER}/direction

|   5）控制输出值

.. code-block:: shell

    $ echo 1 > /sys/class/gpio/gpio${IO_NUMBER}/value

|   使用万用表测试IO_NUMBER对应的引脚，可以看到该引脚是高电平。

.. code-block:: shell
    
    $ echo 0 > /sys/class/gpio/gpio${IO_NUMBER}/value

|   使用万用表测试IO_NUMBER对应的引脚，可以看到该引脚是低电平。

按键测试
~~~~~~~~~~@

**测试说明**

|   MYZR-IMX6-EK314评估板有4个按键，其中3个为自定义功能按键（SW2：VOL-，SW3: VOL+，SW4: Sleep Wake），以及1个复位按键（SW5：nRE）。测试程序key_test可以对3个功能按键进行测试。

**测试方法**

|   1）执行测试程序
|   在终端下键入命令执行测试程序，示例如下：

.. code-block:: shell

    $ /app_test/key_test

|   2）进行交互测试
|   分别按SW2、SW3、SW4，系统会输出相应的事件信息，如：

.. code-block:: shell

    key*** Pressed
    key*** Released

|   其中“key*** Pressed”信息是在按键被按下的时候被输出，“key*** Released”信息是在按键被松开的时候被输出。
|   3）结束测试
|   按计算机上的“Ctrl”+“C”可结束按键测试程序。
|   注：按下SW1（系统会复位重启）。

**附图**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY-IMX6-EK314_L3035_2.7.3.1.png
   :alt: MY-IMX6-EK314_L3035_2.7.3.1.png

串口测试
~~~~~~~~~

|   MYZR-IMX6-EK314评估板有5个串口，其中4个为用户串口（位于底板正面“J12”位置，丝印名称为“UART”），1个为调试串口（位于底板正面“P3”位置，丝印为DEBUG）。

**测试说明**

|   系统设备文件说明：

- 调试串口的在系统中的设备文件是ttymxc0，用户串口的设备文件是ttymxc1、ttymxc2、ttymxc3、ttymxc4。

|   串口收发管脚及对应的设备文件说明：

- UART2：发送 9，接收 10，ttymxc1。
- UART3：发送 13，接收 14，ttymxc2。
- UART4：发送 15，接收 17，ttymxc3。
- UART5：发送 16，接收 18，ttymxc4。

|   提示：这里列出串口的收发管脚，串口所有管脚的定义请看原理图。

串口测试
~~~~~~~~~

|   1）测试说明

- 测试方法说明：

|   采用串口自发自收的方式进行。

- 测试结果说明：

|   通过测试程序向串口发送字符串，并输出串口接收到的字符串。
|   2）进入测试程序目录

.. code-block:: shell

    $ cd /app_test

|   3）UART2测试

- 准备测试

|   短接串口2的发送发接收管脚（J12的9和10号）。

- 执行测试命令

.. code-block:: shell

    $ ./uart_test /dev/ttymxc1 "www.myzr.com.cn"

- 测试结果附图

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY-IMX6-EK314_L3035_2.8.2.1.png
   :alt: MY-IMX6-EK314_L3035_2.8.2.1.png

|   4）UART3测试

- 准备测试

|   短接串口3的发送发接收管脚（J12的12和13号）。

- 执行测试命令

.. code-block:: shell

    $ ./uart_test /dev/ttymxc2 "www.myzr.com.cn"

|   5）UART4测试

- 准备测试

|   短接串口4的发送发接收管脚（J1的15和17号）。

- 执行测试命令

.. code-block:: shell

    $ ./uart_test /dev/ttymxc3 "www.myzr.com.cn"

- 测试结果附图


.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY-IMX6-EK314_L3035_2.8.2.2.png
   :alt: MY-IMX6-EK314_L3035_2.8.2.2.png

|   6）UART5测试

- 准备测试

|   短接串口5的发送发接收管脚（J1的16和18号）。

- 执行测试命令

.. code-block:: shell

    $ ./uart_test /dev/ttymxc4 "www.myzr.com.cn"

- 测试结果附图

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY-IMX6-EK314_L3035_2.8.2.3.png
   :alt: MY-IMX6-EK314_L3035_2.8.2.3.png

RS232串口测试
~~~~~~~~~~~~~~~

**测试说明**

|   MYZR-IMX6-EK314评估板通过串口4引出一个RS232接口，位于底板正面“P2”位置（DB9座子）。

**测试方法**

|   1）准备测试
|   短接RS232的发送发接收管脚（P2的2和3号引脚）。
|   2）执行测试命令

.. code-block:: shell

    $ ./uart_test /dev/ttymxc3 "www.myzr.com.cn"

|   说明：由于RS232是通过UART4引出的，测试同样可以按照UART4的方法。
|   3）测试结果附图

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY-IMX6-EK314_L3035_2.9.2.1.png
   :alt: MY-IMX6-EK314_L3035_2.9.2.1.png

RTC测试
~~~~~~~~~

**测试说明**

|   受快递运输影响，MYZR-IMX6-EK314评估板发货时不带电池。测试RTC前请自备纽扣电池并安装到底板正面“BT1”上。

**测试方法**

|   1）断电重启设备，查看当前系统时间和硬件时间。

|   查看当前系统时钟命令如下：

.. code-block:: shell

    $ date

|   系统输出信息如下：

.. code-block:: shell

    Thu Jan 1 00:00:12 UTC 1970

|   查看当前RTC芯片时钟命令如下：

.. code-block:: shell

    $ hwclock

|   系统输出信息如下：

.. code-block:: shell

    Tue Nov 30 00:00:00 1999 0.000000 seconds

|   2）设置系统时钟，并同步到RTC芯片
|   设置系统时钟命令参考如下：

.. code-block:: shell

    $ date -s "2015-09-02 12:34:56"

|   将系统时钟写入硬件时钟命令如下：

.. code-block:: shell

    $ hwclock –w

|   3）断电重启评估板，查看当前系统时钟和硬件时钟
|   请参考第1步

|   4）测试结果
|   执行第3步以后看到的时钟为新设定的时钟。

**附图**

|   下图为测试方法中步骤1和2的截图

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY-IMX6-EK314_L3035_2.10.3.1.png
   :alt: MY-IMX6-EK314_L3035_2.10.3.1.png

|   下图为测试方法中步骤3的截图

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY-IMX6-EK314_L3035_2.10.3.2.png
   :alt: MY-IMX6-EK314_L3035_2.10.3.2.png

WatchDog测试
~~~~~~~~~~~~~~

**测试说明**

|   WatchDog测试包括2项：一项是复位测试，一项是喂狗测试。

**复位测试**

|   1）测试说明
|   复位测试将启动WatchDog，但是并不喂狗，超时后系统将会复位。
|   2）执行测试

.. code-block:: shell

    $ /unit_tests/wdt_driver_test.out 10 15 1

|   3）测试结果
|   运行测试命令后等待10秒后，WatchDog超时，系统被复位。将会在终端看到系统重新启动输出的信息。

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY-IMX6-EK314_L3035_2.11.2.1.png
   :alt: MY-IMX6-EK314_L3035_2.11.2.1.png

喂狗测试
~~~~~~~~~

|   1）测试说明
|   喂狗测试将启动WatchDog，并且每2秒钟进行1次喂狗，系统将不会因为WatchDog超时而复位。
|   2）执行测试

- 启动WatchDog

.. code-block:: shell

    $ /unit_tests/wdt_driver_test.out 4 2 1 &

- 查看当前时间

.. code-block:: shell

    $ date

|   3）验证

- 查看当前时间

|   经过几分钟之后，系统依然没有复位。我们再查看当前时间。

.. code-block:: shell

    $ date

- 停止喂狗

|   这时我们终止Watchdog测试程序，这样就没有程序进行喂狗了，系统将会在超时时间（这里是4秒）内复位。

.. code-block:: shell

    $ ps | grep "/unit_tests/wdt_driver_test.out"
    3195root 　　 1464 S 　　 /unit_tests/wdt_driver_test.out 4 2 1

|   可以看到wdt_driver_test.out的pid为3195，下面我们终止3195的进程：

.. code-block:: shell

    $ kill 3195

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY-IMX6-EK314_L3035_2.11.3.1.png
   :alt: MY-IMX6-EK314_L3035_2.11.3.1.png

SPI测试
~~~~~~~~~

|   MYZR-IMX6-EK314评估板底板上有一组SPI接口，在“J13”位置，丝印为“SPI”。

**测试说明**

|   SPI1用作SPI Nor Flash。这里我们测试SPI2。
|   测试需要用到SPI接口的MISO和MOSI管脚。SPI接口的  MISO管脚在底板“J13的7号”，MOSI管脚为“J13的11号”。

**测试方法**

|   采用SPI自发送（输出）自接收（输入）的方式。
|   1）准备测试
|   短接SPI的MISO和MISO管脚，即短接底板上J13的7号和11号管脚。
|   2）执行测试

.. code-block:: shell

    $ /app_test/spi_test -D /dev/spidev1.0

|   3）测试结果
|   如果SPI正常，在终端上会看到如下字符：

.. code-block:: shell

    FF FF FF FF FF FF
    40 00 00 00 00 95
    FF FF FF FF FF FF
    FF FF FF FF FF FF
    FF FF FF FF FF FF
    DE AD BE EF BA AD
    F0 0D

**附图**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY-IMX6-EK314_L3035_2.12.3.1.png
   :alt: MY-IMX6-EK314_L3035_2.12.3.1.png

CAN接口测试
~~~~~~~~~~~~

**测试说明**

|   CAN测试需要用到示波器，没有示波器的客户请跳过CAN测试。

**测试方法**

|   1）配置CAN0
|   示例命令如下：

.. code-block:: shell

    $ ip link set can0 up type can bitrate 250000

|   2）配置连接示波器
|   将示波器的CH1和CH2连接到评估板的“R83”（在底板正面最上面的绿色座子）。
|   配置示波器（不会使用示波器的客户请找硬件工程师协助）。
|   3）执行测试命令

.. code-block:: shell

    $ /app_test/client_test

|   4）测试结果
|   执行测试命令的同时会在示波器上看到波形的变化。

**附图**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY-IMX6-EK314_L3035_2.13.3.1.png
   :alt: MY-IMX6-EK314_L3035_2.13.3.1.png

PCIE接口测试
~~~~~~~~~~~~~

**测试说明**

|   系统已添加PCI接口的驱动，在启动过程中系统会检测PCI-E接口上的设备。

**测试方法**

|   复位系统，观察系统启动输出的信息
|   1）PCI-E驱动程序输出信息
|   在系统启动过程中输出如下信息表示PCI-E接口驱动加载没有问题：

.. code-block:: shell

    iMX6 PCIe PCIe RC mode imx_pcie_pltfm_probe entering.
    PCIE: imx_pcie_pltfm_probe start link up.

|   2）不连接PCI-E设备时的输出信息
|   在系统启动过程中，如果PCI-E接口上没有连接有效的设备，系统会提示PCI-E端口“link down!”，类似如下：

.. code-block:: shell

    link up failed, DB_R0:0x00801600, DB_R1:0x08200000!
    IMX PCIe port: link down!

|   3）连接有效PCI-E设备时的输出信息（这里以Intel 4965AGN为例）
|   在系统启动过程中，如果PCI-E接口上检测到有效的设备，并且设备模块正常，系统会提示PCI-E端口“link up”，如下：

.. code-block:: shell

    IMX PCIe port: link up.

4）Linux测试命令：

.. code-block:: shell

    $ lspci

|   如果在PCI-E接口上插入了有效的PCI-E设备，使用lspci将会得到该模块相关的信息，类似如下（这里连接的是Intel 4965AGN）：

.. code-block:: shell

    00:00.0 Class 0604: 16c3:abcd
    01:00.0 Class 0280: 8086:4229

|   如果PCI-E接口上没有连接设备，使用lspci系统将没有信息输出。

**附图**

|   下图为未连接PCI-E设备时系统输出的信息

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY-IMX6-EK314_L3035_2.14.3.1.png
   :alt: MY-IMX6-EK314_L3035_2.14.3.1.png

|   下图为连接Intel 4965AGN时系统输出的信息

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY-IMX6-EK314_L3035_2.14.3.2.png
   :alt: MY-IMX6-EK314_L3035_2.14.3.2.png

|   下图为连接Intel 4965AGN后，进入系统使用lspci得到的信息

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY-IMX6-EK314_L3035_2.14.3.3.png
   :alt: MY-IMX6-EK314_L3035_2.14.3.3.png

WIFI测试
~~~~~~~~~~

**测试说明**

|   MYZR-I.MX6 评估板使用的WIFI芯片型号为RTL8188EUS。

**测试方法**

|   1）加载WIFI模块驱动
|   示例命令如下：

.. code-block:: shell

    $ insmod /lib/modules/wifi/wlan.ko

|   2）生成WIFI的config文件
|   参考命令如下：

.. code-block:: shell

    $ wpa_passphrase MYZR_TP-LINK myzrd2302 > /etc/wpa_supplicant.conf

|   这条命令指定的WIFI名称是和密码是“MYZR_TP-LINK myzrd2302”，需要替换成自己可连接的WIFI名称和密码。
|   3）连接WIFI网络
|   示例命令如下：

.. code-block:: shell

    $ wpa_supplicant -B –c /etc/wpa_supplicant.conf -iwlan0

|   4）自动获取IP
|   示例命令如下：

.. code-block:: shell

    $ udhcpc -i wlan0

|   注意：这里需要确认所在的WIFI网络已启用DHCP功能。
|   5）测试WIFI网络连接
|   示例命令如下：

.. code-block:: shell

    $ ping -I wlan0 www.baidu.com -c 2

|   6）测试结果
|   执行步骤5能ping通则表示WIFI模块工作正常。

IPU测试
~~~~~~~~

**测试说明**

|   整个IPU测试过程完成需要十几分钟。

**测试方法**

|   1）执行测试
|   进入测试程序所在目录（一定要进入测试程序所在目录才能正常执行测试脚本）

.. code-block:: shell

    $ cd /unit_tests/

|   执行测试脚本

.. code-block:: shell

    $ ./autorun-ipu.sh

|   2）测试结果
|   在整个测试过程中，可以看到显示屏显示的内容在不停的变化。
|   测试完成后，在终端上可以看到类似如下信息：

.. code-block:: shell
    
    autorun-ipu.sh: Exiting PASS

    ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝test stop at Wed Sep 2 16:08:55 UTC 2015 ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

**附图**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY-IMX6-EK314_L3035_2.16.3.1.png
   :alt: MY-IMX6-EK314_L3035_2.16.3.1.png

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY-IMX6-EK314_L3035_2.16.3.2.png
   :alt: MY-IMX6-EK314_L3035_2.16.3.2.png

GPU测试
~~~~~~~~~

**测试说明**

|   验证GPU功能。

**测试方法**

- 执行测试命令

.. code-block:: shell

    $ cd /opt/viv_samples/vdk/ && ./tutorial3 -f 100
    $ cd /opt/viv_samples/vdk/ && ./tutorial4_es20 -f 100
    $ cd /opt/viv_samples/tiger/ &&./tiger

**测试过程**

|   执行测试命令时，可以看到显示屏显示的内容在变化。更多请参照/unit_test/gpu.sh

**附图**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY-IMX6-EK314_L3035_2.17.3.1.png
   :alt: MY-IMX6-EK314_L3035_2.17.3.1.png

VPU测试
~~~~~~~~

**测试说明**

|   测试过程将使用VPU解码视频文件并输出到显示设备。

**测试方法**

- 执行测试

|   进入测试程序所在目录（一定要进入测试程序所在目录才能正常执行测试脚本）

.. code-block:: shell

    $ cd /unit_tests/

- 执行测试脚本

.. code-block:: shell

    $ ./autorun-vpu.sh

- 测试现象

|   在整个测试过程中，从显示屏上可以看到VPU解码的视频。

**附图**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY-IMX6-EK314_L3035_2.18.3.1.png
   :alt: MY-IMX6-EK314_L3035_2.18.3.1.png

背光测试
~~~~~~~~~

**测试说明**

|   测试过程通过设置背光亮度值验证评估板的背光功能。

**测试方法(test method)**

|   1）查看最大亮度

.. code-block:: shell

    $ cat /sys/class/backlight/pwm-backlight.0/max_brightness

|   2）设置亮度

.. code-block:: shell

    $ echo 200 >/sys/class/backlight/pwm-backlight.0/brightness

|   在整个测试过程中，执行上面的测试命令后会看到显示屏的亮度发生变化。

usb识别为U盘测试
~~~~~~~~~~~~~~~~~

**测试说明**

|   通过mini usb线在PC识别开发板为U盘。

**测试方法(test method)**

|   1）创建一个10M大小的文件

.. code-block:: shell

    $ dd if=/dev/zero of=/dev/shm/disk bs=1024 count=10240

|   2）载入模块

.. code-block:: shell

    $ modprobe g_file_storage stall=0 file=/dev/shm/disk removable=1

|   3）识别U盘
|   此时PC“我的电脑”会出现U盘的驱动器，将其格式化后，便可对其读写
|   4）挂载

.. code-block:: shell

    $ mount /dev/shm/disk /mnt

|   在/mnt/下看到在电脑写入的文件，在开发板写入文件，重新插拔MINI USB可在PC看到在开发板写入的新文件。

usb识别为网口测试
~~~~~~~~~~~~~~~~~

**测试说明**

|   通过mini usb线将usb识别为网口。

**测试方法(test method)**

|   1）载入模块

.. code-block:: shell

    $ modprobe g_ether

|   2）设置IP

.. code-block:: shell

    $ ifconfig usb0 192.168.7.2

|   将PC识别的rndis的本地连接IP设置为192.168.7.8
|   3）测试网口

.. code-block:: shell

    $ ping 192.168.7.8 -c 2 -w 4

|   “0% packet loss”表示测试通过
|   注：若WIN10识别rndis为COM口，则需要下载驱动kindle_rndis.inf_amd64-v1.0.0.1.zip 解压后，以管理员权限执行5-runasadmin_register-CA-cer.cmd，然后在COM口处双击，在计算机中查找解压的驱动程序，这样就会有rndis网络了。

CPU温度测试
~~~~~~~~~~~~

**测试说明**

|   查看CPU的温度

**测试方法(test method)**

|   1）执行测试

.. code-block:: shell

    $ cat /sys/class/thermal/thermal_zone0/temp

|   2）测试结果

.. code-block:: shell

    44

tftp更新镜像
~~~~~~~~~~~~~

**测试说明**

|   可更新zImage、u-boot、u-boot环境变量。

**测试方法(test method)**

|   电脑端打开软件 tftpd 地址设置为需更换的文件所在的目录。
|   把开发板的这个网口用网线跟电脑网口连接起来。
|   进入u-boot命令行。
|   1)加载环境变量

.. code-block:: shell

    run load_scr; source;

|   2）设置IP
|   设置开发板IP：

.. code-block:: shell

    setenv ipaddr 192.168.137.9

|   设置电脑IP：

.. code-block:: shell

    setenv serverip 192.168.137.99

|   设置MAC地址：

.. code-block:: shell

    setenv ethaddr 00:00:00:00:00:03

|   测试网络：

.. code-block:: shell

    ping 192.168.137.99

|   测试结果：“host 192.168.137.99 is alive”表示测试通过

|   3）烧写zImage

.. code-block:: shell

    run update_kern

|   4)烧写u-boot环境变量

.. code-block:: shell

    run update_scr

|   5)烧写u-boot

.. code-block:: shell

    run update_ubot

复制更新镜像
~~~~~~~~~~~~

**测试说明**

|   可更新zImage、u-boot环境变量、内核模块。

**测试方法(test method)**

|   1)复制相应文件到开发板当前目录，以tftp为例
|   电脑端打开软件 tftpd 地址设置为需更换的文件所在的目录。
|   把开发板的这个网口用网线跟电脑网口连接起来。
|   2）测试连接

.. code-block:: shell

    $ ping 192.168.137.99 -c 2 -w 4

|   测试结果：“0% packet loss”表示测试通过
|   3）传输文件

.. code-block:: shell

    $ tftp -g 192.168.137.99 -r zImage-myimx6a9
    $ tftp -g 192.168.137.99 -r my_environment.scr
    $ tftp -g 192.168.137.99 -r kernel-modules-myimx6a9.tar.bz2

|   4)查看fat分区地址

.. code-block:: shell

    $ fdisk -l

|   输出信息：

.. code-block:: shell

    ......
    Device Boot Start End Blocks Id System
    /dev/mmcblk0p1 321 16320 512000 c Win95 FAT32 (LBA)
    /dev/mmcblk0p2 19201 480896 14774272 83 Linux
    ......

|   5)手动挂载

.. code-block:: shell

    $ mount /dev/mmcblk0p1 /mnt/

|   6)复制相应的文件到/mnt目录，将原文件替换

.. code-block:: shell

    $ cp zImage-myimx6a9 /mnt
    $ cp my_environment.scr /mnt

|   7)解压更新内核模块

.. code-block:: shell

    $ tar xjvf kernel-modules-myimx6a9.tar.bz2 -C /

|   8)保存并重启

.. code-block:: shell

    $ reboot

显示功能测试
-------------

- 特别说明：

|   当U-Boot 版本u-boot-2016.03 svn315及以上    
|   内核 版本  linux-3.0.35  svn31及以上
|   linux-3.14.52 svn369及以上
|   linux-3.14.52 svn368及以上
|   烧录工具   MfgTool-MYIMX6A9-L* svn181及以上    
|   请参考《MYZR-IMX6-A9系列：显示功能测试》进行测试


- 一般情况下则按照如下方法测试

|   说明：每项显示功能测试都需要重启系统进入到u-boot命令行，输入命令并按确认键。
|   示例如下：

单屏显示
~~~~~~~~~

|   说明：输入命令并按确定键，观察系统启动过程中显示屏的显示内容，即可看到Linux Logo。

**LVDS1**

|   setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

**LVDS0**

|   进入u-boot命令行，输入下面命令并按确定键：

.. code-block:: shell

    setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666 ldb=sin0; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

**HDMI**

.. code-block:: shell

    setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=hdmi,1920x1080M@60,if=RGB24; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

|   提示：HDMI显示在启动过程中屏幕无Linux Logo显示。进入系统后可以使用gplay命令播放视频，可以看到视频转出在显示屏上。
|   视频播放命令示例如下：

.. code-block:: shell

    $ gplay /unit_tests/akiyo.mp4

**RGB**

.. code-block:: shell

    setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=lcd,SEIKO-WVGA,if=RGB24; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

双屏同步骤显示
~~~~~~~~~~~~~~~

|   说明：输入命令并按确定键，在内核启动过程中可以看到两个屏幕都显示Linux Logo，并且其它对显示屏的操作也会同样显示在两个屏幕上。

LVDS1+LVDS0同步显示
~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666 ldb=dul0 video=mxcfb1:dev=ldb,LDB-1024X600,if=RGB666; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

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

    $ gst-launch playbin2 uri=file:///unit_tests/akiyo.mp4 \ 
    video-sink="mfw_v4lsink device=/dev/video17"

- 播放指定的视频文件到视频设备（这里video18关联到第2显示屏）

.. code-block:: shell

    $ gst-launch playbin2 uri=file:///unit_tests/akiyo.mp4 \ 
    video-sink="mfw_v4lsink device=/dev/video18"

**测试方法说明**

|   1）进入u-boot命令行输入命令并按确认键待系统启动完成。
|   示例如下：
|   2）执行命令打开对应显示屏的背光。
|   示例如下：
|   3）执行视频播放命令播放视频到显示屏。
|   示例如下：
|   说明：双屏异步显示模式下，系统启动后第2显示屏的背光默认是关闭的，所以需要执行步骤2）。

**LVDS1作为主屏**

- LVDS1+LVDS0双屏异步显示

.. code-block:: shell

    setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666 video=mxcfb1:dev=ldb,LDB-1024X600,if=RGB666; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

- LVDS1+RGB双屏异步显示

.. code-block:: shell

    setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666 video=mxcfb1:dev=lcd, SEIKO-WVGA,if=RGB24; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

- LVDS1+HDMI双屏异步显示

.. code-block:: shell

    setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666 video=mxcfb1:dev=hdmi,1920x1080M@60,if=RGB24; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

**LVDS0作为主屏**

- LVDS0+LVDS1双屏异步显示：

.. code-block:: shell
    
    setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666 ldb=sep0 video=mxcfb1:dev=ldb,LDB-1024X600,if=RGB666; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

- LVDS0+RGB双屏异步显示

.. code-block:: shell

    setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666 ldb=sin0 video=mxcfb1:dev=lcd,SEIKO-WVGA,if=RGB24; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

- LVDS0+HDMI双屏异步显示

.. code-block:: shell

    setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666 ldb=sin0 video=mxcfb1:dev=hdmi,1920x1080M@60,if=RGB24; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

**RGB作为主屏**

- RGB+LVDS1双屏异步显示：

.. code-block:: shell

    setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=lcd,SEIKO-WVGA,if=RGB24 video=mxcfb1:dev=ldb,LDB-1024X600,if=RGB666; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

- RGB+LVDS0双屏异步显示：

.. code-block:: shell

    setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=lcd,SEIKO-WVGA,if=RGB24 video=mxcfb1:dev=ldb,LDB-1024X600,if=RGB666 ldb=sin0; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

**HDMI作为主屏**

- HDMI+LVDS1双屏异步显示

.. code-block:: shell

    setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=hdmi,1920x1080M@60,if=RGB24 video=mxcfb1:dev=ldb,LDB-1024X600,if=RGB666; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

- HDMI+LVDS0双屏异步显示

.. code-block:: shell

    setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=hdmi,1920x1080M@60,if=RGB24 video=mxcfb1:dev=ldb,LDB-1024X600,if=RGB666 ldb=sin0; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

OV5642摄像头 测试
~~~~~~~~~~~~~~~~~~

1. 开发板断电，在"CAMERA"接上OV5642摄像头，接上摄像头后启动评估板。
2. 使用指令进行测试:

.. code-block:: shell

    /unit_tests/mxc_v4l2_overlay.out -iw 640 -ih 480 -it 0 -il 0 -ow 640 -oh 480 -ot 20 -ol 20 -r 0 -t 50 -do 0 -fg -fr 30

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
