
MYZR-RK3288-EK314 Linux-3.10.79 测试手册
=========================================


测试前的准备
-------------

|   1）准备MYZR-RK3288-EK314开发板一套，5V直流稳压电源，USB转串口线。
|   2）接上串口线，给开发板供电，启动板子。


测试项目
--------

网口测试
~~~~~~~~~

|   MYZR-RK3288-EK314 评估板支持双网口，一个百兆，另一个千兆。

**接口属性**

+-------------------+----------+-----------------+----------+
|    评估板型号     | 接口位置 |  接口速率标准   | 系统接口 |
+===================+==========+=================+==========+
| MYZR-RK3288-EK314 | U13      | 10/100/1000Mbps | eth0     |
+                   +----------+-----------------+----------+
|                   | P1       | 10/100Mbps      | eth1     |
+-------------------+----------+-----------------+----------+


**测试方法**

|   1） 测试说明
|   设置计算机有线网卡IP为192.168.18.18

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.1.1.png
   :alt: My-rk32-ek314test_2.1.1.png


|   2） Eth0连接测试
|   连接网线：将评估板“eth0”对应的接口与计算机有线网卡的接口用网线相连接
|   设置评估板IP：

.. code:: shell

    ＃ ifconfig eth0 192.168.18.36      //configure the eth0

|   执行测试命令：

.. code:: shell

    ＃ ifconfig eth1 down      //eth1 to be shut down
    ＃ ping 192.168.18.18 -c 2 -w 4      //send ICMP to HOST


|   观察测试结果：系统会输出类似如下信息：

.. code:: shell

    --- 192.168.18.18 ping statistics ---
    2packets transmitted, 2 packets received, 0% packet loss

|   测试结果：“0% packet loss”表示测试通过
|   附图

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.1.2.png
   :alt: My-rk32-ek314test_2.1.2.png

|   3） Eth1连接测试
|   连接网线：将网线插入“eth1”对应的评估板接口，网线另一端保持与计算机有线网卡的接口连接。
|   设置第2个网口IP：

.. code:: shell

    ＃ ifconfig eth1 192.168.18.27      //configure the eth1

|   设置后系统会输出第2个网口的工作状态信息，类似如下：

.. code:: shell

    smsc95xx 1-1.1:1.0 eth1: link up, 100Mbps, full-duplex, lpa 0x4DE1

|   执行测试命令：

.. code:: shell

    ＃ ifconfig eth0 down      //eth0 to be shut down
    ＃ ping 192.168.18.18 -c 2 -w 4      //send ICMP to HOST

|   观察测试结果：系统会输出类似如下信息：

.. code:: shell

    --- 192.168.18.18 ping statistics ---
    2packets transmitted, 2 packets received, 0% packet loss

|   测试结果：“0% packet loss”表示测试通过
|   附图

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.1.3.png
   :alt: My-rk32-ek314test_2.1.3.png


USB测试
~~~~~~~~~

**接口属性**

+-------------------+----------+--------------+
|    评估板型号     | 接口位置 | 接口速率标准 |
+===================+==========+==============+
| MYZR-RK3288-EK314 | J10      | 480 Mbits/s  |
+-------------------+----------+--------------+

**测试方法**

|   1） 开始测试
|   将USB设备插入底板USB接口，输入以下命令：

.. code:: shell

    ＃ df

|   2） 测试结束
|   将USB设备从底板拔出，系统会输出类似如下信息：

.. code:: shell

    ＃ df

**附图**

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.2.1.png
   :alt: My-rk32-ek314test_2.2.1.png


SD卡测试
~~~~~~~~~~

**接口属性**

+-------------------+----------+----------+
|    评估板型号     | 接口位置 | 接口类型 |
+===================+==========+==========+
| MYZR-RK3288-EK314 | U22      | SD       |
+-------------------+----------+----------+

**开始测试**

|   1） 往SD卡槽插入设备
|   插入SD卡到底板SD卡接口，输入以下命令：

.. code:: shell

    ＃ df

|   2） 结束测试
|   SD卡弹出后拨出SD卡即结束测试。

**附图**

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.3.1.png
   :alt: My-rk32-ek314test_2.3.1.png


音频测试
~~~~~~~~~

**测试说明**

|   这项测试是通过播放音频文件验证评估板的音频功能。

**测试方法**

|   1）准备测试
|   连接音频输出设备到底板正面的音频座子，音频座子在底板正面“P15”。

|   2）执行测试
|   使用aplay播放一个视频，示例命令如下：

.. code:: shell

    ＃ aplay /usr/share/sounds/alsa/Rear_Left.wav

|   上面这条命令会使用aplay播放命令中指定的文件。

|   3）测试结果
|   执行上面的测试命令后会听到音频设备输出的声音。


**附图**

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.4.1.png
   :alt: My-rk32-ek314test_2.4.1.png


标准GPIO测试
~~~~~~~~~~~~~

**接口属性**

+-----------------+----------+----------+--------+
|   评估板型号    | LED标号  | GPIO属性 | IO序号 |
+=================+==========+==========+========+
| MY-RK3288-EK314 | D1       | GPIO0_B1 | 9      |
+-----------------+----------+----------+--------+
| D2              | GPIO0_C2 | 18       |        |
+-----------------+----------+----------+--------+
| D3              | GPIO0_B0 | 8        |        |
+-----------------+----------+----------+--------+
| D4              | GPIO0_A7 | 7        |        |
+-----------------+----------+----------+--------+

**测试方法**

|   1）GPIO输出测试
|   设置需要测试的GPIO的IO序号

.. code:: shell

    ＃ OUT_IO_NUMBER=9

导出GPIO

.. code:: shell

    ＃ echo ${OUT_IO_NUMBER} > /sys/class/gpio/export

设置GPIO方向

.. code:: shell

    ＃ echo out > /sys/class/gpio/gpio${OUT_IO_NUMBER}/direction

控制输出电平

.. code:: shell

    ＃ echo 0 > /sys/class/gpio/gpio${OUT_IO_NUMBER}/value
    ＃ echo 1 > /sys/class/gpio/gpio${OUT_IO_NUMBER}/value


.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.5.1.png
   :alt: My-rk32-ek314test_2.5.1.png


|   2）GPIO输入测试
|   设置需要测试的GPIO的IO序号

.. code:: shell

    ＃ IN_IO_NUMBER=18

|   导出GPIO

.. code:: shell

    ＃ echo ${IN_IO_NUMBER} > /sys/class/gpio/export

|   设置GPIO方向

.. code:: shell

    ＃ echo in > /sys/class/gpio/gpio${IN_IO_NUMBER}/direction

|   查看输入电平

.. code:: shell

    cat /sys/class/gpio/gpio${IN_IO_NUMBER}/value


GPIO-KEY测试
~~~~~~~~~~~~~~

**接口属性**

+-----------------+-----------+-------------+
| MY-RK3288-EK314                           |
+=================+===========+=============+
| 接口位置        | GPIO属性  | KEY属性     |
+-----------------+-----------+-------------+
| SW1             | gpio-keys | Volume Down |
+-----------------+-----------+-------------+
| SW2             | gpio-keys | Volume Up   |
+-----------------+-----------+-------------+
| SW3             | gpio-keys | Power       |
+-----------------+-----------+-------------+
| SW4             | gpio-keys | Reset       |
+-----------------+-----------+-------------+
| SW5             | gpio-keys | Recovery    |
+-----------------+-----------+-------------+

**测试方法**

|   1）执行测试程序
|   在终端下键入命令执行测试，示例如下：

.. code:: shell

    ＃ evtest

|   2）选择测试设备
|   Select the device event number [0-2]: 2
|   输入“gpio-keys”对应的序号，这里是2

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.6.1.png
   :alt: My-rk32-ek314test_2.6.1.png


|   3）进行交互测试
|   在终端会看到“Testing ... (interrupt to exit)”，这时我们按下或松开SW1、SW2。会看到如下类似信息：

.. code:: shell

    Event: time 1452590477.115958, type 1 (EV_KEY), code 114 (KEY_VOLUMEDOWN), value 0
    Event: time 1452590477.115958, -------------- SYN_REPORT ------------
    Event: time 1452590478.415953, type 1 (EV_KEY), code 115 (KEY_VOLUMEUP), value 1

|   其中“value 1”信息是在按键被按下的时候被输出，“value 0”信息是在按键被松开的时候被输出。


.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.6.2.png
   :alt: My-rk32-ek314test_2.6.2.png

|   4）结束测试
|   按计算机上的“Ctrl”+“C”可结束按键测试程序。


串口测试
~~~~~~~~~~

|   MYZR-RK3288-EK314共3个串口，其中1个调试串口，2个用户串口。

**用户串口属性**

+-------------------+-------+----------------+----------+
|    评估板型号     | UARTx |    硬件接口    | 系统接口 |
+===================+=======+================+==========+
| MYZR-RK3288-EK314 | UART0 | BT (Bluetooth) | ttyS0    |
+                   +-------+----------------+----------+
|                   | UART1 | P3             | ttyS1    |
+                   +-------+----------------+----------+
|                   | UART2 | P4 (DEBUG)     | ttyS2    |
+-------------------+-------+----------------+----------+

|   提示：这里列出串口的收发管脚，串口其它管脚的定义请看原理图。

**串口测试**

|   1）测试说明
|   测试方法说明：
|       串口线直接相连电脑和UART1,用ssh客户端登陆和测试。
|   测试结果说明：
|       通过ssh客户端向串口发送字符串，串口可以收到字符串。
|   2）安装ssh客户端

.. code:: shell

    ＃ apt-get install ssh

|   3）UART1测试
|   执行测试命令

.. code:: shell

    ＃ echo “myzr” > /dev/ttyS1 (UART1发送数据myzr)
    ＃ cat /dev/ttyS1 (UART1接收数据)

|   测试结果附图

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.7.1.png
   :alt: My-rk32-ek314test_2.7.1.png


RTC测试
~~~~~~~~~

**测试说明**

|   受快递运输影响，MYZR-RK3288-EK314 系列评估板发货时不带电池。测试RTC前请自备纽扣电池并安装到评估板上。
|   MYZR-RK3288-EK314的电池座在底板正面的“BT1”位置。

**测试方法(test method )**
|   1）断电重启设备，查看当前系统时间和硬件时间。
|   查看当前系统时钟命令如下：

.. code:: shell
    
    ＃ date

|   系统输出信息如下：

.. code:: shell

    Thu Aug 6 05:35:17 UTC 2012

2）查看当前RTC芯片时钟命令如下：

.. code:: shell

    ＃ hwclock

|   系统输出信息如下：

.. code:: shell

    Thu Aug 6 05:35:59 2012 0.000000 seconds

|   3）设置系统时钟，并同步到RTC芯片
|   设置系统时钟命令参考如下：

.. code:: shell

    ＃ date -s "2013-03-28 12:30:30"

|   将系统时钟写入硬件时钟命令如下：

.. code:: shell

    ＃ hwclok –w

|   4）断电重启评估板，查看当前系统时钟和硬件时钟
|   请参考第1步
|   5）测试结果
|   执行第3步以后看到的时钟为新设定的时钟。

**附图**

|   附图一：

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.8.1.png
   :alt: My-rk32-ek314test_2.8.1.png

|   附图二：

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.8.2.png
   :alt: My-rk32-ek314test_2.8.2.png


SPI测试
~~~~~~~~

|   MYZR-RK3288-EK314上有两组SPI接口。

**接口属性**

|   测试需要用到SPI接口的MISO和MOSI管脚，在下表中列出。

+-------------------+------+--------+--------+-----------+
|    评估板型号     | SPIx |  MISO  |  MOSI  | 系统接口  |
+===================+======+========+========+===========+
| MYZR-RK3288-EK314 | SPI1 | J11:33 | J11:35 | spidev0.0 |
+                   +------+--------+--------+-----------+
|                   | SPI2 | J11:38 | J13:34 | spidev2.0 |
+-------------------+------+--------+--------+-----------+


**测试说明**

|   1）采用SPI自发送（输出）自接收（输入）的方式。
|   ``注意：测试需要短接评估板的管脚，如果不确定自己能正确短接的请找硬件工程师支持，否则可能会损坏评估板。``
|   2）与SPI测试程序匹配的SPI接口是SPI2，所以我们的SPI测试是测试SPI2。

**测试方法**

|   1）准备测试
|   短接SPI0的MISO和MOSI管脚。

|   2）执行测试

.. code:: shell

    ＃ ./spi_test -D /dev/spidev0.0

|   3）测试结果
|   如果SPI正常，在终端上会看到如下字符：

.. code:: shell

    FF FF FF FF FF FF
    40 00 00 00 00 95
    FF FF FF FF FF FF
    FF FF FF FF FF FF
    FF FF FF FF FF FF
    DE AD BE EF BA AD
    F0 0D


**附图**

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.9.1.png
   :alt: My-rk32-ek314test_2.9.1.png

WIFI测试
~~~~~~~~

|   MYZR-RK3288-EK314 评估板使用的WIFI芯片型号为AP6335
|   1）步骤一
|   选择SSID，如：Honor V9

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.10.1.png
   :alt: My-rk32-ek314test_2.10.1.png

|   2）步骤二
|   输入WIFI密码,并连接成功

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.10.2.png
   :alt: My-rk32-ek314test_2.10.2.png


蓝牙测试
~~~~~~~~

|   MYZR-RK3288-EK314 评估板使用的Bluetooth芯片型号为AP6335
|   1）步骤一
|   打开蓝牙,点击“Prefrences”->“Bluetooth Manager”

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.11.1.png
   :alt: My-rk32-ek314test_2.11.1.png

|   2）步骤二
|   搜索蓝牙，点击"Search"


.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.11.2.png
   :alt: My-rk32-ek314test_2.11.2.png

4G测试
~~~~~~~~

**测试说明**

|   测试上网4G模块，如L506。

**测试方法**

- 安装wvdial

.. code:: shell

    ＃ sudo apt-get install wvdial

- 修改配置文件/etc/wvdial.conf

.. code:: shell

    ＃ vim /etc/wvdial.conf

|   增加以下内容：

.. code:: shell

    [Dialer Defaults]
    Modem = /dev/ttyUSB2
    Baud = 115200
    Init1 = ATZ
    Init2 = AT+CGDCONT=1,"IP","CMNET"
    Init3 = AT+CGEQREQ=1,2,128,384,,,0,,,,,,
    Phone = *99*1#
    Username = cmnet
    Password = cmnet
    New PPPD = yes

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.12.1.png
   :alt: My-rk32-ek314test_2.12.1.png

- 拨号

.. code:: shell
    
    ＃ wvdial &

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.12.2.png
   :alt: My-rk32-ek314test_2.12.2.png


HDMI测试
~~~~~~~~~~

**测试说明**

|   接上HDMI显示屏。

**测试方法**

- 烧写linux-boot_hdmi.img

|   用AndroidTool_Release_v2.35烧写。

- 测试

|   开机，HDMI有显示图像

- 修改分辨率

|   想修改分辨率，可以修改arch/arm/boot/dts/lcd-box.dtsi。


EDP测试
~~~~~~~~

**测试说明**

|   接上EDP显示屏。

**测试方法**

- 烧写linux-boot_edp.img

|   用AndroidTool_Release_v2.35烧写。

- 测试

|   开机，EDP有显示图像

- 修改分辨率

|   想修改分辨率，可以修改arch/arm/boot/dts/lcd-EDP1080p.dtsi。
|   To modify the resolution, modify arch/arm/boot/dts/lcd-EDP1080p.dtsi.