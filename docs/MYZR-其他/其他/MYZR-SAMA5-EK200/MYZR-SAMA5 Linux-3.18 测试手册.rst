MYZR-SAMA5 Linux-3.18 测试手册
===============================

测试前的准备
-------------

|   1）请按照《Linux快速启动手册》中的“Linux快速启动” -> “连接设备”进行连接。
|   2）请按照《Linux快速启动手册》中的“Linux快速启动” -> “启动设备”进行启动。

测试项目
---------

网口测试
~~~~~~~~~

|   MYZR-SAMA5-EK200支持双网口（1个百兆网口，一个千兆网口）。

**测试说明**

|   第1个以太网口位置底板正面“J3”，第2个以太网口位置底板正面“J2”。

**测试方法**

|   1） 测试第1个以太网口（百兆网口）

- 连接网线：用网络连接评估板“J3”与计算机网口
- 设置计算机IP：设置计算机网口IP为192.168.18.18

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5-MB200_back_2.2.0.1.jpg
   :alt: MY-SAMA5-MB200_back_2.2.0.1.jpg

- 设置评估板IP：

.. code-block:: shell

    ifconfig eth0 192.168.18.81 # configure the eth0
    ifconfig eth1 down

- 执行测试命令：

.. code-block:: shell

    ping 192.168.18.18 -c 2 -w 4 # send ICMP to HOST

- 观察测试结果：系统会输出类似如下信息：

.. code-block:: shell

    --- 192.168.18.18 ping statistics ---

    2packets transmitted, 2 packets received, 0% packet loss

- 测试结果：“0% packet loss”表示测试通过

**附图**

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_2.1.2.2.png
   :alt: MY-SAMA5_Linux-3.18_2.1.2.2.png

|   2） 测试第2个以太网口（千兆网口）

- 连接网线：拔下第1个网口的网线接口插入到评估板“J2”，网线另一端保持与计算机网口相连。
- 设置计算机IP：设置计算机网口IP为192.168.18.18（如已经设置过可执行下一步骤）。
- 设置第2个网口IP：

.. code-block:: shell

    ifconfig eth1 192.168.18.82 ＃ configure the eth1
    ifconfig eth0 down

|   设置后系统会输出第2个网口的工作状态信息，类似如下：

.. code-block:: shell

    macb f0028000.ethernet eth1: link up (1000/Full)

|   执行测试命令：

.. code-block:: shell

    ping 192.168.18.18 -c 2 -w 4 # send ICMP to HOST

- 观察测试结果：系统会输出类似如下信息：

.. code-block:: shell

    --- 192.168.18.18 ping statistics ---

    2packets transmitted, 2 packets received, 0% packet loss

|   测试结果：“0% packet loss”表示测试通过
|   附图

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_2.1.2.3.png
   :alt: MY-SAMA5_Linux-3.18_2.1.2.3.png

USB测试
~~~~~~~~~

**测试说明**

|   MYZR-IMX6-EK200有2个USB HOST接口，位于底板正面“J8”。

**测试方法**

|   1） 开始测试
|   将USB设备插入底板USB接口，系统会输出类似如下信息：

.. code-block:: shell

    usb *-*.*: new high-speed USB device number * using atmel-ehci
    ……

|   2） 测试结束
|   将USB设备从底板拔出，系统会输出类似如下信息：

.. code-block:: shell

    usb *-*.*: USB disconnect, device number *

**附图**

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_2.2.3.1.png
   :alt: MY-SAMA5_Linux-3.18_2.2.3.1.png

SD卡接口测试
~~~~~~~~~~~~~

**测试说明**

|   SD卡接口位于底板背面“J29”。

**开始测试**

|   1） 往SD卡槽插入设备
|   插入SD卡到底板SD卡接口。系统输出以下信息（见附图）即表示SD接口正常：

.. code-block:: shell

    mmc*: new high speed SD card at address ****
    ……

|   2）从SD卡槽弹出设备
|   再次住SD卡槽按下SD卡，底板会弹出SD卡。系统输出以下信息（见附图）表示SD卡接口弹出正常：

.. code-block:: shell

    mmc*: card **** removed

|   3） 结束测试
|   SD卡弹出后拨出SD卡即结束测试。

**附图**

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_2.3.3.1.png
   :alt: MY-SAMA5_Linux-3.18_2.3.3.1.png

LED（GPIO）测试
~~~~~~~~~~~~~~~~

**LED（GPIO）定义**

|   在MYZR-SAMA5-EK200底板正面有4个LED，详细如下：

+------+---------+-----------+----------------+
| 丝印 | CPU引脚 | LED属性   | 用途           |
+------+---------+-----------+----------------+
| D12  | PE1     | default   | 内核启动后点亮 |
+------+---------+-----------+----------------+
| D13  | PE2     | heartbeat | CPU工作时闪烁  |
+------+---------+-----------+----------------+
| D14  | PE3     | gpio      | 用户控制输出   |
+------+---------+-----------+----------------+
| D15  | PE4     | timer     | Timer演示      |
+------+---------+-----------+----------------+

**led-default测试**

|   led-default对应D12。系统启动完成后，该LED默认被点亮，通常可用作供电指示。就是说在用户没有控制该指示灯的情况下，亮表示设备通电（即电源工作正常）。当然，用户也可以控制该指示灯的亮灭，但这时候灯灭与电源是否工作不存在关联。
|   控制命令如下：

.. code-block:: shell

    echo 0 > /sys/class/leds/default/brightness
    echo 1 > /sys/class/leds/default/brightness

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_2.4.2.1.png
   :alt: MY-SAMA5_Linux-3.18_2.4.2.1.png

**led-heartbeat**

|   led-heartbeat对应D13。系统启动后，该LED闪烁，该LED的状态可表示CPU的工作状态。闪烁表示CPU工作正常。常亮或常灭表示CPU工作不正常（即可能是CPU不工作了）。

**led-gpio测试**

|   led-gpio对应D14。系统启动后，该LED默认保持常灭的状态。进入系统后，我们可通过指令来控制该LED的亮灭。
|   该LED使用的CPU引脚为PE3，在系统中表现由/sys/class/leds/gpioE3/目录下相关的文件表示它的属性。
|   控制指令如下：

.. code-block:: shell

    echo 1 > /sys/class/leds/gpioE3/brightness
    echo 0 > /sys/class/leds/gpioE3/brightness

**led-timer测试**

|   led-timer对应D15。这主要演示GPIO作为timer信号。
|   在系统中由/sys/class/leds/timer/目录下相关的文件表示它的属性。
|   我们可能通过设置delay来控制该GPIO高低电平保持的时间。
|   控制指令如下：

.. code-block:: shell

    echo 1000 > /sys/class/leds/timer/delay_off

|   通过delay_off控制低电平保持的时间，1000即1000ms

.. code-block:: shell

    echo 2000 > /sys/class/leds/timer/delay_on

|   通过delay_on控制低电平保持的时间，2000即2000ms
|   执行上面两条指令后，我们看到的效果是：D15灭1秒后，亮2秒，如此循环。

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_2.4.5.1.png
   :alt: MY-SAMA5_Linux-3.18_2.4.5.1.png

串口测试
~~~~~~~~~

MYZR-SAMA5-EK200评估板有6个串口，其中5个为用户串口，1个为调试串口（位于底板正面“P1”位置）。

+---------+-------------+---------------+------------------+
| MPU定义 | 功能实现    | Linux设备文件 | 连接位置         |
+=========+=============+===============+==================+
| DBGU    | 调试串口    | /dev/ttyS0    | P1               |
+---------+-------------+---------------+------------------+
| USART0  | RS232       | /dev/ttyS1    | J27:5,6(RX,TX)   |
+---------+-------------+---------------+------------------+
| USART1  | RS232,RS485 | /dev/ttyS2    | J26:14,11(RX,TX) |
+---------+-------------+---------------+------------------+
| USART2  | RS232,RS485 | /dev/ttyS3    | J26:10,7(RX,TX)  |
+---------+-------------+---------------+------------------+
| USART3  | RS232       | /dev/ttyS4    | J27:1,2(RX,TX)   |
+---------+-------------+---------------+------------------+
| UART0   | RS232       | /dev/ttyS5    | J27:3,4(RX,TX)   |
+---------+-------------+---------------+------------------+

|   在串口测试中我们测试5个用户串口。

**测试说明**

- 测试方法说明：

|   采用串口自发自收的方式进行。

- 测试结果说明：

|   通过测试程序向串口发送字符串，并输出串口接收到的字符串。

**测试方法**

|   1）短接串口的收发引脚
|   这一步请根据需要测试的串口找到对应的引脚，并仔细检查，确保无误。如不确定请在硬件工程师的支持下进行。错误的短接可能会对评估板造成损坏。
|   2）准备测试程序

- 下载测试应用程序

|   将uart_test.out下载到评估板，参考命令如下：

.. code-block:: shell

    tftp –gr uart_test.out 192.168.18.18

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_2.5.2.1.png
   :alt: MY-SAMA5_Linux-3.18_2.5.2.1.png

- 为测试程序添加可执行权限

.. code-block:: shell

    chmod +x uart_test.out

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_2.5.2.2.png
   :alt: MY-SAMA5_Linux-3.18_2.5.2.2.png

|   3）测试USART0（ttyS1）

- 指定需要测试的串口

|   指定USART0为被测试设备，根据前面的表格，UASRT0对应ttyS1

.. code-block:: shell

    USART_DEV="/dev/ttyS1"

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_2.5.2.3.png
   :alt: MY-SAMA5_Linux-3.18_2.5.2.3.png

- 执行测试命令

.. code-block:: shell

    ./uart_test.out $USART_DEV "www.myzr.com.cn"

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_2.5.2.4.png
   :alt: MY-SAMA5_Linux-3.18_2.5.2.4.png

|   3）其它串口测试
|   测试其它串口同样需要指定对应的设备文件，并执行测试命令，参考如下：

.. code-block:: shell

    USART_DEV="/dev/ttyS2"
    ./uart_test.out $USART_DEV "www.myzr.com.cn"

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_2.5.2.5.png
   :alt: MY-SAMA5_Linux-3.18_2.5.2.5.png

.. code-block:: shell

    USART_DEV="/dev/ttyS3"
    ./uart_test.out $USART_DEV "www.myzr.com.cn"

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_2.5.2.6.png
   :alt: MY-SAMA5_Linux-3.18_2.5.2.6.png

.. code-block:: shell

    USART_DEV="/dev/ttyS4"
    ./uart_test.out $USART_DEV "www.myzr.com.cn"

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_2.5.2.7.png
   :alt: MY-SAMA5_Linux-3.18_2.5.2.7.png

.. code-block:: shell

    USART_DEV="/dev/ttyS5"
    ./uart_test.out $USART_DEV "www.myzr.com.cn"

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_2.5.2.8.png
   :alt: MY-SAMA5_Linux-3.18_2.5.2.8.png

RTC测试
~~~~~~~~~

**测试说明**

|   受快递运输影响，MYZR-SAMA5-EK200 评估板发货时不带电池。测试RTC前请自备纽扣电池并安装到底板背面“BT1”上（在丝印“RTC”旁边）。

**测试方法**

|   1）断电重启设备，查看当前系统时间和硬件时间。

- 查看当前系统时钟命令如下：

.. code-block:: shell

    date

|   系统输出信息如下：

.. code-block:: shell

    Tue Nov 17 06:07:13 UTC 2015

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_2.6.2.1.png
   :alt: MY-SAMA5_Linux-3.18_2.6.2.1.png

|   2）查看当前RTC芯片时钟命令如下：

.. code-block:: shell

    hwclock

|   系统输出信息如下：

.. code-block:: shell

    Tue Nov 17 06:08:14 2015 0.000000 seconds

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_2.6.2.2.png
   :alt: MY-SAMA5_Linux-3.18_2.6.2.2.png

|   3）设置系统时钟，并同步到RTC芯片

- 设置系统时钟命令参考如下：

|   command to set system clock as below：

.. code-block:: shell

    date -s "2015-11-23 12:34:56"

|   将系统时钟写入硬件时钟命令如下：

.. code-block:: shell

    hwclock -w

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_2.6.2.3.png
   :alt: MY-SAMA5_Linux-3.18_2.6.2.3.png

|   4）断电重启评估板，查看当前系统时钟和硬件时钟
|   请参考第1步
|   5）测试结果
|   执行第3步以后看到的时钟为新设定的时钟。

SPI测试
~~~~~~~~~

|   MYZR-SAMA5-EK200上有一组SPI接口，在“J22”位置上。

**测试说明**

|   SPI测试采用自发送（输出）自接收（输入）的方式。
|   测试需要用到SPI接口的MISO和MOSI管脚。SPI接口的 MISO管脚在底板“J22的5号”，MOSI管脚为“J22的1号”。

**测试方法**

|   1）短接SPI的收发引脚
|   短接J22的1号和5号管脚，并仔细检查，确保无误。如不确定请在硬件工程师的支持下进行。错误的短接可能会对评估板造成损坏。
|   2）准备测试程序

- 下载测试应用程序

|   将spi_test.out下载到评估板，参考命令如下：

.. code-block:: shell

    tftp -gr spidev_test.out 192.168.18.18

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_2.7.2.1.png
   :alt: MY-SAMA5_Linux-3.18_2.7.2.1.png

- 为测试程序添加可执行权限

.. code-block:: shell

    chmod +x spidev_test.out

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_2.7.2.2.png
   :alt: MY-SAMA5_Linux-3.18_2.7.2.2.png

|   3）执行测试

.. code-block:: shell

    ./spidev_test.out -D /dev/spidev32765.0

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_2.7.2.3.png
   :alt: MY-SAMA5_Linux-3.18_2.7.2.3.png

|   4）测试结果
|   如果SPI正常，在终端上会看到如下字符：

.. code-block:: shell

    FF FF FF FF FF FF
    40 00 00 00 00 95
    FF FF FF FF FF FF
    FF FF FF FF FF FF
    FF FF FF FF FF FF
    DE AD BE EF BA AD
    F0 0D

CAN接口测试
~~~~~~~~~~~~

**测试说明**

|   CAN测试需要用到示波器，没有示波器的客户请跳过CAN测试。
|   这里演示CAN0的测试，CAN1测试类似。

**测试方法**

|   1）配置CAN0
|   示例命令如下：

.. code-block:: shell

    ip link set can0 up type can bitrate 125000

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_2.8.2.1.png
   :alt: MY-SAMA5_Linux-3.18_2.8.2.1.png

|   2）配置连接示波器
|   将示波器的CH1和CH2连接到评估板的“J12”（在底板正面最上面的蓝色座子）。
|   配置示波器（不会使用示波器的客户请找硬件工程师协助）。
|   3）执行测试命令

.. code-block:: shell

    cansend can0 5A1 #11.2233.44556677.88

|   4）测试结果
|   执行测试命令的同时会在示波器上看到波形的变化。

WIFI测试
~~~~~~~~~

|   1）在网盘“4_烧录支持/mysama5ek200_image”下载编译好的 WIFI 驱动模块“8188eu.ko”。
|   2）把 8188eu.ko 传输到开发板的 “~/my-demo/linux-3.18/” 目录。
|   3）测试

.. code-block:: shell

    insmod ~/my-demo/linux-3.18/8188eu.ko
    wpa_passphrase WIFI名称 WIFI密码 > /etc/wpa_supplicant.conf
    wpa_supplicant -Dwext -iwlan0 -c/etc/wpa_supplicant.conf -B
    udhcpc -i wlan0

